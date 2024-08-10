from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get('https://api.npoint.io/db6f0c7b544ff0881771')
posts = response.json()
print(posts)


@app.route('/')
def home():
    return render_template('index.html', all_posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post')
def post():
    return render_template('post.html')


if __name__ == "__main__":
    app.run(debug=True)
