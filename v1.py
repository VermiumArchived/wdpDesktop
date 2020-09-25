import os, datetime

# Working directory
directory = './'

# extensions for files that we want rename
extensions = (['.jpg', '.jpeg']);

# Get a list of files in the directory
filelist = os.listdir( directory )

# New file dictionary
newfilesDictionary = {}

# count the number of files that are renamed
count = 0

for file in filelist:
	# split the file into filename and extension
	filename, extension = os.path.splitext(file)
	# if the extension is a valid extension
	if ( extension in extensions ):
		# Get the create time of the file
		create_time = os.path.getctime( file )
		# get the readable timestamp format 
		format_time = datetime.datetime.fromtimestamp( create_time )
		# convert time into string
		format_time_string = format_time.strftime("%Y-%m-%d %H.%M.%S") # e.g. 2015-01-01 09.00.00.jpg
		# Contruct the new name of the file
		newfile = format_time_string + extension; 

		# If there is other files created at the same timestamp
		if ( newfile in newfilesDictionary.keys() ):
			index = newfilesDictionary[newfile] + 1;
			newfilesDictionary[newfile] = index; 
			newfile = format_time_string + '-' + str(index) + extension; # e.g. 2015-01-01 09.00.00-1.jpg
		else:
			newfilesDictionary[newfile] = 0; 

		# rename the file
		os.rename( file, newfile );
		# count the number of files that are renamed
		count = count + 1
		# printing log
		print( file.rjust(35) + '    =>    ' + newfile.ljust(35) )


print( 'All done. ' + str(count) + ' files are renamed. ')