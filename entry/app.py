#!flask/bin/python
from flask import Flask
from flask import request
from flask import Response
from flask import jsonify 
import uuid


app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    videoFile = request.files['file'];
    theID = uuid.uuid4()
    videoFile.save(str(theID) + ".mp4")
    resp = Response()
    resp.headers['Location'] = '/' + str(theID)
    return resp,201

@app.route('/<uuid>/status')
def status(uuid):
    res = { 'status' : 'QUEUED' , 'progress' : 0 }
    return jsonify(res)


@app.route('/<uuid>/download')
def download(uuid):
    resp = Response()
    resp.headers['Content-disposition'] = 'attachment; filename=' + uuid + '.mp4'
    theFile = open(uuid + '.mp4','rb')
    resp.data = theFile.read()
    return resp

if __name__ == '__main__':
    app.run(debug=True)
