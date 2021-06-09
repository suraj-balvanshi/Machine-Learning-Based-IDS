import os
import glob
import csv
#set working directory
os.chdir("datasets/")

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
print(all_filenames)

for i in all_filenames:
	with open(i) as f:
		data=[row for row in csv.reader(f)]
		print(data)
	with open('/root/Downloads/Python-Packet-Sniffer/attack1hulk.csv', 'a+') as f:
		w=csv.writer(f)
		for row in data:
			w.writerow(row)
			
		
