import serial

ser = serial.Serial("/dev/cu.HC-05-DevB", 9600)

import sys
label = sys.argv[1]
file_name = sys.argv[2]

feats = list()
labels = list()

try:
	while True:
		res = ser.readline()
		print(res)
		res = [ int(x) for x in res.split(b' ') if int(x) < 1000]
		if len(res) == 10:
			feats.append(res[:4])
			labels.append(label)
finally:
	import pickle
	with open(file_name, "rb") as f:
		prev_feats, prev_labels = pickle.load(f)
	prev_feats = prev_feats + feats
	prev_labels = prev_labels + labels

	with open(file_name, "wb") as f:
		pickle.dump([prev_feats, prev_labels], f)