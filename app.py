from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/about')
def about():
    return "About"

@app.route('/contact')
def contact():
    return "Contact Page"  

@app.route('/test/<data>')
def test(data):
    return f"{data} is a test"

@app.route('/number/<n1>/<n2>')
def number(n1,n2):
    n1 = int(n1)
    n2 = int(n2)
    return f"{n1} + {n2} = {n1+n2}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)