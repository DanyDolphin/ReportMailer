# Utils
import csv


def read_csv_file(file_name):
    '''Read csv file'''
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data
