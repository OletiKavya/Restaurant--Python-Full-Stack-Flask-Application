from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'auth.db')
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Change this to a secure key

db = SQLAlchemy(app)
jwt = JWTManager(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(80), nullable=False)

@app.cli.command('db_create')
def db_create():
    db.create_all()
    print("Database created.")

@app.cli.command('db_seed')
def db_seed():
    user1 = User(username='admin', password='admin', role='admin')
    user2 = User(username='user', password='user', role='user')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print("Database seeded.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/page.html')
def page():
    return render_template('page.html')

@app.route('/vegOptions.html')
def veg():
    return render_template('vegOptions.html')

@app.route('/NonvegOptions.html')
def nonveg():
    return render_template('NonvegOptions.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/register',methods=['POST'])
def register():
    data = request.get_json()
    a = data.get('username')
    b = data.get('password')
    c = data.get('role')
    print(a,b,c)
    user = User(username=a, password=b,role=c)
    if user:
        db.session.add(user)
        db.session.commit()
        return jsonify(), 200

    
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"msg": "Admins only!"}), 403
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True)
