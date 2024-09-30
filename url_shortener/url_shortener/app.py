from flask import Flask, render_template, request, redirect, url_for
from models import db, URL
import string, random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def generate_short_id(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_id = generate_short_id()

        # Create a new URL entry
        new_url = URL(original_url=original_url, short_id=short_id)
        db.session.add(new_url)
        db.session.commit()

        short_url = request.host_url + short_id
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<short_id>')
def redirect_to_url(short_id):
    # Fetch the original URL using the short ID
    url = URL.query.filter_by(short_id=short_id).first_or_404()
    return redirect(url.original_url)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        print("Database tables created.")
    app.run(debug=True)


