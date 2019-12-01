from flask import Flask, render_template, request
from flask_cors import CORS

import reader

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/home')
def home():
    author, title, url, upvote_ratio, body = reader.get_content()
    return render_template("index.html", author=author, title=title, url=url, upvote_ratio=upvote_ratio, body=body)


if __name__ == '__main__':
    app.run(debug=True)