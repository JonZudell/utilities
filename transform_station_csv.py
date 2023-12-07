#!/usr/bin/env python3
import csv
import json
import sys

def convert_field(field):
    if field == "9999" or field == "":
        return None
    else:
        return int(field)

def parse_true_false(field):
    if field.strip() == "1":
        return True
    else:
        return False
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {}
     
    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        # Convert each row into a dictionary 
        # and add it to data
        for rows in csvReader:
             
            # Assuming a column named 'No' to
            # be the primary key
            key = rows['DATE']
            del rows['STATION']
            del rows['DATE']
            del rows['LATITUDE']
            del rows['LONGITUDE']
            del rows['ELEVATION']
            del rows['NAME']
            rows['PRCP'] = convert_field(rows['PRCP'])
            rows['SNOW'] = convert_field(rows['SNOW'])
            rows['SNWD'] = convert_field(rows['SNWD'])
            rows['TMAX'] = convert_field(rows['TMAX'])
            rows['TMIN'] = convert_field(rows['TMIN'])
            rows['WT03'] = parse_true_false(rows['WT03'])
            rows['WT08'] = parse_true_false(rows['WT08'])
            rows['WT16'] = parse_true_false(rows['WT16'])
            data[key] = rows
 
    # Open a json writer, and use the json.dumps() 
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

if __name__ == "__main__":
    station_path = sys.argv[1]
    output_path = sys.argv[2]
    make_json(station_path, output_path)