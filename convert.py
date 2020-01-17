import os
import glob
from pydub import AudioSegment as convert

# find all files that end with m4a
songs = glob.glob("*.m4a")

# print names of files being converted
print("----------------------------------------\nFiles being converted:\n")

for song in songs:
	print(song)

print("----------------------------------------\n")

# loop converting files and showing progress of each
for song in songs:

	song_name = song[:-4]
	print("Converting",song_name)

	destination = song_name+".mp3"

	song = convert.from_file(song, format="m4a")
	song.export(destination, format="mp3")

	print("Done\n")

# display completion and where files are located
working_dir = os.getcwd()
print("All files have been converted and can be found in",working_dir)