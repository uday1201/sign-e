from flask import stream_with_context, Flask, render_template, Response
from signe.main.ml.do import predict_from_serial
import serial

app = Flask(__name__)

ser = serial.Serial("/dev/cu.usbmodem1411", 9600)

@app.route('/')
def index():
	return render_template('index.html')	

@app.route('/text_stream')
def streamed_response():
	return Response(stream_with_context(predict_from_serial(ser, "ml/model.p")))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)