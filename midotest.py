import mido
from mido import MidiFile

mid = MidiFile('MegalovaniaNoChords.mid')

for i, track in enumerate(mid.tracks):
	print('Track {}: {}'.format(i, track.name))
	for msg in track:
		if msg.is_meta:
			print("Meta: " + str(msg))
		elif msg.type == 'note_on':
			print("Note On " + str(msg))
		elif msg.type == 'note_off':
			print("Note Off " + str(msg))
			print(mido.tick2second(msg.time, mid.ticks_per_beat, 200))