import midi
import os
import glob

def generateBeeps(track):
	beepstring = "";
	tracknum = 1
	for event in track[tracknum]:
		if isinstance(event, midi.NoteOnEvent):
			beepstring += "delay(" + str(event.tick) + ");\n";
			beepstring += "beep(" + str(event.data[0]) + "," + str(track[tracknum][track[tracknum].index(event) + 1].tick) + ");\n";
		#print(event)
	#print(beepstring)
	return beepstring

midlist = glob.glob('*.mid');
s = 1;

def getMidName(listlength):
	s = input()
	try:
		int(s)
	except ValueError:
		try:
			float(s)
		except ValueError:
			print("This is not a number")
			s = 0
	s = int(s)
	if s is 0:
		getMidName(listlength)
	elif s > listlength:
		print("Not an option")
		getMidName(listlength)
	else:
		print('You typed ' + str(s))
		return midlist[s - 1]

def MakeCode(midname):
	headerfile = open('header.txt', 'r')
	headertext = headerfile.read().strip()
	headerfile.close()
	track = midi.read_midifile(midname);
	generateBeeps(track);
	footerfile = open('footer.txt', 'r')
	footertext = footerfile.read().strip()
	footerfile.close()

	finalcode = (headertext + "\n" + generateBeeps(track) + "\n" + footertext).strip();

	text_file = open("result.txt", "w")
	text_file.write(finalcode)
	text_file.close()
	print("written to result.txt")

for file in midlist:
  print(str(midlist.index(file) + 1) + ": " + file)
MakeCode(getMidName(len(midlist)))