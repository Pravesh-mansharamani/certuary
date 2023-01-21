from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/createCertificate',methods = ["POST"])
def createInvoice():
    invoice = request.json['name']
    return invoice

if __name__ == '__main__':
    app.run(debug=True)
