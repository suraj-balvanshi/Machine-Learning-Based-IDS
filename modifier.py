import glob
import csv
def modify():
	i="current.csv"
	with open(i) as f:
		data=[row for row in csv.reader(f)]
		l = len(data)
		for j in range(l):
			for k in range(14):
				if data[j][k] == '':
					data[j][k] = '0'
		with open(i, 'w') as f:
			w=csv.writer(f)
			for row in data:
				w.writerow(row)
				
