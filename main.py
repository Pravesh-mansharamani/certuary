from flask import Flask, request
from datetime import date

from generateQR import generateQR
from pasteQR import pasteQR
from pinToIPFS import pinToIPFS
from flask_cors import CORS, cross_origin


from createCertificate import createCertificate
from verify_cid import verify_cid

app = Flask(__name__)
CORS(app, support_credentials=True)



@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# TODO: Deta Link, Front and Backend Integration


@app.route('/createCertificate',methods = ["POST"])
@cross_origin(supports_credentials=True)
def create_invoice():

    name = request.json['name']
    desc = request.json['description']
    company = request.json['company']
    sign = request.json['oname']
    role = request.json['role']
    date_issued = date.today().strftime("%B %d, %Y")

    res = createCertificate(name,sign,desc,company,role)
    print(res)
    new = (pasteQR(res['cid']))


    return new['cid']

@app.route('/verify/<CID>', methods=["GET"])
@cross_origin(supports_credentials=True)
def verify(CID):
    return verify_cid(CID)


@app.route('/mint',methods=['GET'])
@cross_origin(supports_credentials=True)
def mint():
    response = pinToIPFS()
    return response




if __name__ == '__main__':
    app.run(debug=True)
