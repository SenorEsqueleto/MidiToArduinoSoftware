import midi
import os
import time
import glob

notes = {
	50: 294,
	53: 349,
	55: 391,
	56: 415,
	57: 440,
	62: 587
}

print(notes)

debug = True;

# Takes the midi and generates beep() functions
def generateBeeps(track):
	# beepstring is the final string that will be returned
	beepstring = "";
	tracknum = 1

	# If should debug, print track
	print(track[tracknum])

	# For each event in the 1st track of the midi, do tis function
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
