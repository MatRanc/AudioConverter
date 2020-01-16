import os
import glob
from pydub import AudioSegment as convert

songs = glob.glob("*.m4a")

print("--------------------------------------------")
print("\nFiles being converted:\n")

for song in songs:
	print(song)

print("--------------------------------------------\n")

for song in songs:

	song_name = song[:-4]
	print("Converting ",song_name)

	destination = song_name+".mp3"

	song = convert.from_file(song, format="m4a")
	song.export(destination, format="mp3")

	print("Done\n")

working_dir = os.getcwd()
print("All files have been converted and can be found in",working_dir)