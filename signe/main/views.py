from django.http import HttpResponse
from django.shortcuts import render
from ml.do import predict

# Create your views here.

def index(request):
	return render(request, "index.html", {})

def getWord(request):
	import serial
	ser = serial.Serial("", 9600)
	read = ser.readline()
	feats = [ int(x) for x in read.strip().split(' ') if int(x) < 1000 ]
	while len(feats) < 10:
		ser = serial.Serial("", 9600)
		read = ser.readline()
		feats = [ int(x) for x in read.strip().split(' ') if int(x) < 1000 ]
	word = predict("a.p", feats)
	return HttpResponse("{word:" + word + "}")