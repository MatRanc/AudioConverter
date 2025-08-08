import os
import glob
from pydub import AudioSegment

INPUT_FORMAT = 'm4a'
OUTPUT_FORMAT = 'mp3'

# find all files that end with m4a
file_list = glob.glob('*.'+INPUT_FORMAT)

# print names of files being converted
print('----------------------------------------\nFiles being converted:\n')

for file in file_list:
	print(file)

print('----------------------------------------\n')

# loop converting files and showing progress of each
for file in file_list:
	file_name = file.strip('.'+INPUT_FORMAT)
	print('Converting', file_name)

	destination = file_name+'.'+OUTPUT_FORMAT

	output = AudioSegment.from_file(file, format=INPUT_FORMAT)
	output.export(destination, format=OUTPUT_FORMAT)

	print('Done\n')

# display completion and where files are located
working_dir = os.getcwd()
print('All files have been converted and can be found in', working_dir)