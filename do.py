import pickle
feats, labels = pickle.load(open("a.p", "rb"))

from sklearn import naive_bayes

print(feats)

print(labels)

cl = naive_bayes.GaussianNB()
# print( [ len(x) for x in feats ] )
cl.fit(feats, labels)

import serial
ser = serial.Serial("/dev/cu.usbmodem1411", 9600)
i = 1
while True:
	res = ser.readline()
	res = [ int(x) for x in res.split(b' ') ]
	if len(res) == 10:
		print(cl.predict([res[:4]]))
		print(i)
		i = i+1