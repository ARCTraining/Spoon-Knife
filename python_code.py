import numpy
import obspy

print("you need more python in your life")
print("also seismology")

st = obspy.read('*SAC')

for i,tr in enumerate st:
	print(tr)