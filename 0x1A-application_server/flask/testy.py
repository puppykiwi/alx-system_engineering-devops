from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Sample Webpage', heading='Welcome to My Sample Webpage', message='This is a simple webpage served using Flask.')

if __name__ == '__main__':
    app.run(debug=True)
