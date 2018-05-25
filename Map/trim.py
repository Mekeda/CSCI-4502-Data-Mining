#Python CSV Trimming script

import csv
import json

file = open('drop_locations.csv', 'w')

with open("yellow_tripdata_2017-02.csv") as csvfile:
	reader = csv.DictReader(csvfile)

	for row in reader:
		file.write('{'+ 'lat: '+ row['dropoff_latitude'] + ', ' + 'lng: ' + row['dropoff_longitude'] + '}' + ',' + '\n')



file.close()



