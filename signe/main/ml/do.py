import pickle
import serial
from sklearn.tree import DecisionTreeClassifier

prev_word = ' '

def predict_from_serial(file_name):
	cl = pickle.load(open(file_name, "rb"))

	# print(cl.predict([603, 555, 463, 499]))
	ser = serial.Serial("/dev/cu.HC-05-DevB", 9600)
	while True:
		res = ser.readline()
		res = [ int(x) for x in res.split(b' ') ]
		if len(res) == 10:
			yield cl.predict([res[:4]])[0]
def predict(file_name, feats):
	cl = pickle.load(open(file_name, "rb"))
	return cl.predict(feats)[0]

def say(text):
	from gtts import gTTS
	obj = gTTS(text = text, lang = "en", slow = False)
	obj.save("temp.mp3")
	import os
	os.system("afplay temp.mp3")

if __name__ == "__main__":	
	for word in predict_from_serial("model.p"):
		if len(prev_word) > 0 and (word == prev_word[-1] or (word == "blank" and prev_word == " ")):
			pass
		else:
			if word == 'blank':
				print(prev_word + " ")
				say(prev_word.strip())
				prev_word = " "
			else:
				prev_word += word
				print(word)