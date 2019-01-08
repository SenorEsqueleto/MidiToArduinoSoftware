import midi
import os
import time
import glob
from mido import Message, MidiFile, MidiTrack

# This list contains the note read by python3-midi, then the real frequency that the arduino should read
notes = {
	11: 31,
	12: 33,
	13: 35,
	14: 37,
	15: 39,
	16: 41,
	17: 44,
	18: 46,
	19: 49,
	20: 52,
	21: 55,
	22: 58,
	23: 62,
	24: 65,
	25: 69,
	26: 73,
	27: 78,
	28: 82,
	29: 87,
	30: 93,
	31: 98,
	32: 104,
	33: 110,
	34: 117,
	35: 123,
	36: 131,
	37: 139,
	38: 147,
	39: 156,
	40: 165,
	41: 175,
	42: 185,
	43: 196,
	44: 208,
	45: 220,
	46: 233,
	47: 247,
	48: 262,
	49: 277,
	50: 294,
	51: 311,
	52: 330,
	53: 349,
	54: 370,
	55: 391,
	56: 415,
	57: 440,
	58: 466,
	59: 494,
	60: 523,
	61: 554,
	62: 587,
	63: 622,
	64: 659,
	65: 698,
	66: 740,
	67: 784,
	68: 831,
	69: 880,
	70: 932,
	71: 988,
	72: 1047,
	73: 1109,
	74: 1175,
	75: 1245,
	76: 1319,
	77: 1397,
	78: 1480,
	79: 1568,
	80: 1661,
	81: 1760,
	82: 1865,
	83: 1976,
	84: 2093,
	85: 2217,
	86: 2349,
	87: 2489,
	88: 2637,
	89: 2794,
	90: 2960,
	91: 3136,
	92: 3322,
	93: 3520,
	94: 3729,
	95: 3951,
	96: 4186,
	97: 4435,
	98: 4699,
	99: 4978
}

print(notes)

debug = False;

# Takes the midi and generates beep() functions
def generateBeeps(track):
	# beepstring is the final string that will be returned
	beepstring = "";
	tracknum = 1

	# If should debug, print track
	#print(track[tracknum])
	if debug is True:
		print(track)

	for event in track[0]:
		if isinstance(event, midi.SetTempoEvent):
			print(event.bpm)

	# For each event in the 1st track of the midi, do this function
	for event in track[tracknum]:

		# If its the start of a note, do...
		if isinstance(event, midi.NoteOnEvent):
			# Delay the code by the NoteOnEvent tick (which is equal to the amount of time since the last note)
			beepstring += "delay(" + str(event.tick) + ");\n";
			# Make a beep with the note (incorrect as of now) and the duration is the tick of the next event (hopefully the NoteOffEvent, should probably make sure of that)

			note = 0;

			if event.data[0] in notes:
				note = notes[event.data[0]]
			else:
				note = event.data[0]

			beepstring += "beep(" + str(note) + "," + str(track[tracknum][track[tracknum].index(event) + 1].tick) + ");\n";
	# Give the code the final string
	return beepstring

# Creates a list of all .mid files in the current directory
midlist = glob.glob('*.mid');
s = 1;

# Asks the user which mid to run the code on
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

# Puts all the functions together and creates the final string
def MakeCode(midname):
	# header.txt contains all of the beginning code that doesn't need to be dynamic
	headerfile = open('header.txt', 'r')
	headertext = headerfile.read().strip()
	headerfile.close()
	# Read midi track
	track = midi.read_midifile(midname);

	# Generate beepstring
	generateBeeps(track);
	# footer.txt contains anything after loop(), which in this case is just a curly brace
	footerfile = open('footer.txt', 'r')
	footertext = footerfile.read().strip()
	footerfile.close()

	# Assemble the strings
	finalcode = (headertext + "\n" + generateBeeps(track) + "\n" + footertext).strip();

	# Writes the final string to a file so we don't have to output it in the terminal
	if os.path.exists("result.txt"): 
		os.remove("result.txt")
		time.sleep(1) 
	else: 
		print("No result.txt")
	text_file = open("result.txt", "w")
	text_file.write(finalcode)
	text_file.close()
	print("Written to result.txt")

# Prints all the midi files and runs the functions
for file in midlist:
  print(str(midlist.index(file) + 1) + ": " + file)
MakeCode(getMidName(len(midlist)))
