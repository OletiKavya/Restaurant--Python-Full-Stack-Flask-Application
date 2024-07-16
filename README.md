# 🍽️ Restaurant Full-Stack Application 🚀

Welcome to our vibrant restaurant full-stack web application! Customize your plates, enjoy delicious options, and explore the flavors with our interactive menu.

## 🌟 Features

- 🔒 User authentication with JWT (JSON Web Token)
- 🍲 Customizable menu options for vegetarian and non-vegetarian plates
- 🛠️ Database setup and seeding commands
- 📱 Responsive design with Bootstrap

## 🛠️ Technologies Used

- Flask
- Flask-SQLAlchemy
- Flask-JWT-Extended
- HTML
- CSS
- Bootstrap
- SQLite

## 🔧 Setup Instructions

### Prerequisites

- Python 3.x
- Virtual Environment (`venv`)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/restaurant-full-stack.git
    cd restaurant-full-stack
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    flask db_create
    flask db_seed
    ```

5. Run the application:
    ```bash
    flask run
    ```

## 🚀 Usage

### Home Page

- 🏠 Navigate to the home page to choose between registering as a new user or logging in as an existing user.

### Registration

- 📝 New users can register by providing a username, password, and role (admin or user).

### Login

- 🔑 Existing users can log in with their credentials to access the customization options.

### Menu Customization

- 🍽️ After logging in, users can customize their vegetarian or non-vegetarian plates by selecting different options for fry and curry.

## 🎯 Endpoints

- `/` : Home page
- `/login` : User login
- `/register` : User registration
- `/page.html` : Menu page
- `/vegOptions.html` : Vegetarian customization page
- `/NonvegOptions.html` : Non-vegetarian customization page
- `/protected` : Protected route (requires JWT)
- `/admin` : Admin-only route (requires JWT with admin role)
