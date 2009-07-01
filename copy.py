#!/usr/bin/python
import os, time, glob,shutil

date_file_list = []

def to_gigs(bytes):
	return bytes / 1024 / 1024 / 1024

for file in glob.glob("/mnt/gig/movies/*.*"):
	stats = os.stat(file)
	size = os.path.getsize(file)
	lastmod_date = time.localtime(stats[8])
	date_file_tuple = lastmod_date, file, size
	date_file_list.append(date_file_tuple)

date_file_list.sort()
date_file_list.reverse()

total_size=0

copypath="/home/ted/porsche/"
s = os.statvfs(copypath)
space = s.f_bsize * s.f_bavail
print "Space free: " + str(to_gigs(space))

for f in date_file_list:
	file_date = time.strftime("%m/%d/%y %H:%M:%S", f[0])
	folder, file_name = os.path.split(f[1])

	if ((total_size + f[2]) < space):
		total_size += f[2]
		print file_date + ": " + file_name + ": " + str(f[2]) + \
			": " + str(to_gigs(total_size))
		#copy the file
		shutil.copyfile(file_name,copypath + "/" + file_name)