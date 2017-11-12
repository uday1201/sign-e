from django.http import HttpResponse
from django.shortcuts import render
from .ml.do import predict
import serial

# Create your views here.

def index(request):
	return render(request, "index.html", {})
def getWord(request):
	ser = serial.Serial("/dev/cu.usbmodem1411", 9600, timeout = 1)
	read = ser.readline()
	print(read)
	feats = [ int(x) for x in read.strip().split(b' ') if int(x) < 1000 ]
	while len(feats) < 10:
		read = ser.readline()
		feats = [ int(x) for x in read.strip().split(b' ') if int(x) < 1000 ]
	word = predict("a.p", feats)
	serial.close()
	return HttpResponse("{word:" + word + "}")