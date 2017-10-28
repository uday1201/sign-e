import pickle
import serial
from sklearn.naive_bayes import GaussianNB

prev_word = ' '

def predict_from_serial(file_name):
	feats, labels = pickle.load(open(file_name, "rb"))
	# cl = naive_bayes.GaussianNB()
	cl = GaussianNB()
	# print( [ len(x) for x in feats ] )
	cl.fit(feats, labels)

	# print(cl.predict([603, 555, 463, 499]))
	ser = serial.Serial("/dev/cu.usbmodem1411", 9600)
	while True:
		res = ser.readline()
		res = [ int(x) for x in res.split(b' ') ]
		if len(res) == 10:
			yield cl.predict([res[:4]])[0]

if __name__ == "__main__":	
	for word in predict_from_serial("a.p"):
		if len(prev_word) > 0 and (word == prev_word[-1] or (word == "blank" and prev_word == " ")):
			pass
		else:
			if word == 'blank':
				print(prev_word + " ")
				prev_word = " "
			else:
				prev_word += word
				print(word)