from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sample Webpage</title>
    </head>
    <body>
        <h1>Welcome to My Sample Webpage</h1>
        <p>This is a simple webpage served using Flask.</p>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run()
