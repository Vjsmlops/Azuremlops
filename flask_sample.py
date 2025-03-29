from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    """
    Displays a welcome message for the Azure Cloud Workshop.
    """
    return "<h1>Welcome to the Azure Cloud Workshop!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
