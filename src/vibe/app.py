from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Change this in production

# In-memory storage (replace with a database in production)
users = {}
articles = [
    {"id": 1, "name": "Laptop", "description": "A high-performance laptop", "price": 1200},
    {"id": 2, "name": "Smartphone", "description": "Latest model smartphone", "price": 800},
    {"id": 3, "name": "Headphones", "description": "Noise-canceling headphones", "price": 200},
]
carts = {}


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        shipping_address = request.form.get('shipping_address', '')
        payment_details = request.form.get('payment_details', '')

        if username in users:
            return "Username already taken!"

        users[username] = {
            'password': generate_password_hash(password),
            'shipping_address': shipping_address,
            'payment_details': payment_details
        }
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('articles_page'))
        return "Invalid credentials!"
    return render_template('login.html')


@app.route('/articles')
def articles_page():
    query = request.args.get('query', '')
    filtered_articles = [a for a in articles if query.lower() in a['name'].lower()]
    return render_template('articles.html', articles=filtered_articles)


@app.route('/cart/add/<int:article_id>')
def add_to_cart(article_id):
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    if username not in carts:
        carts[username] = []

    carts[username].append(article_id)
    return redirect(url_for('cart'))


@app.route('/cart')
def cart():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    user_cart = [a for a in articles if a['id'] in carts.get(username, [])]
    return render_template('cart.html', cart=user_cart)


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    user = users.get(username)

    if request.method == 'POST':
        shipping_address = request.form['shipping_address']
        payment_details = request.form['payment_details']
        return "Order placed successfully!"

    return render_template('checkout.html', shipping_address=user.get('shipping_address', ''),
                           payment_details=user.get('payment_details', ''))


if __name__ == '__main__':
    app.run(debug=True)
