from flask import Flask, request
from datetime import date
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# TODO: QR Code, API for Verification
@app.route('/createCertificate',methods = ["POST"])
def create_invoice():
    # name = request.json['name']
    # description = request.json['description']
    # company_name = request.json['company']
    date_issued = date.today().strftime("%B %d, %Y")
    return date_issued

@app.route('/verify/<CID>', methods=["POST"])
def verify(CID):

    return f'CID is {CID}'



if __name__ == '__main__':
    app.run(debug=True)
