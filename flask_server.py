from flask import stream_with_context, request, Flask, render_template, Response
from ml.do import predict_from_serial
import serial

app = Flask(__name__, static_url_path='/static')

ser = serial.Serial("/dev/cu.HC-05-DevB", 9600)

@app.route('/')
def index():
	return render_template('index.html')	

@app.route('/text_stream')
def streamed_response():
	return Response(stream_with_context(predict_from_serial(ser, "ml/model.p")))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)