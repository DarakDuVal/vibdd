# Flask Webshop

This is a simple Flask-based webshop application that allows users to browse articles, register/login, add items to a shopping cart, and complete a checkout process.

## Features
- User registration and login
- Browsing articles for sale
- Adding items to a shopping cart
- Filtering articles by name
- Checkout process with shipping and payment details

## Installation

### Prerequisites
- Python 3.x
- Flask
- Werkzeug

### Clone the Repository
```sh
git clone https://github.com/yourusername/flask-webshop.git
cd flask-webshop
```

### Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

## Running the Application
```sh
python app.py
```

The application will be available at `http://127.0.0.1:5000/`

## Directory Structure
```
flask-webshop/
│-- app.py
│-- requirements.txt
│-- templates/
│   │-- index.html
│   │-- register.html
│   │-- login.html
│   │-- articles.html
│   │-- cart.html
│   │-- checkout.html
│-- static/
```

## Future Improvements
- Use a database instead of in-memory storage
- Add authentication using Flask-Login
- Implement order history

## License
This project is licensed under the MIT License.
