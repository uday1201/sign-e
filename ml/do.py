import pickle
import serial


prev_word = ' '
prev_alpha = 'blank'
word = ''

def predict_from_serial(ser, file_name):
	global prev_alpha
	cl = pickle.load(open(file_name, "rb"))


	# print(cl.predict([603, 555, 463, 499]))
	#ser = serial.Serial("/dev/cu.HC-05-DevB", 9600)
	while True:
		res = ser.readline()
		res = [ int(x) for x in res.split(b' ') ]
		if len(res) == 4:
			value = cl.predict([res])[0]
			if prev_alpha == value:
				yield ""
			else:
				prev_alpha = value
				if value == "blank":
					temp = word
					word = ''
					yield "<br>"
				else:
					word += value
					yield value
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
	ser = serial.Serial("/dev/cu.HC-05-DevB", 9600)
	for word in predict_from_serial(ser, "model.p"):
		if len(prev_word) > 0 and (word == prev_word[-1] or (word == "blank" and prev_word == " ")):
			pass
		else:
			if word == 'blank':
				print(prev_word + " ")
				# say(prev_word.strip())
				prev_word = " "
			else:
				prev_word += word
				print(word)