# Change all pictures filenames from Google Nexus 5 to dropbox style in a directory
# An example of source file name: 
# 	IMG_20141224_204028 (1).jpg
# Destination file name: 
# 	2014-12-24 20.40.28 (1).jpg
# Developed in Python 3

import os, datetime
import re # For regular expression

# Working directory
directory = './'

# Get a list of files in the directory
filelist = os.listdir( directory )

# count the number of files that are renamed
count = 0

# regular string pattern 
pattern = re.compile('IMG_\d{8,8}_\d{6,6}[ (0-9)]*.jpg')

for file in filelist:
	newFile = 'Not Renamed'

	# if file name matches the defined pattern
	if ( pattern.match( file ) ):
		str_year   = file[4:8]
		str_month  = file[8:10]
		str_day    = file[10:12]
		str_hour   = file[13:15]
		str_minute = file[15:17]
		str_second = file[17:19]

		# Contruct the new name
		newFile  = str_year + '-' + str_month + '-' + str_day + ' ';
		newFile += str_hour + '.' + str_minute + '.' + str_second;
		newFile += file[19:]

		# rename the file
		os.rename( file, newFile );
		
		count = count + 1

	# printing log
	print( file.rjust(35) + '    =>    ' + newFile )


print( 'All done. ' + str(count) + ' files are renamed. ')