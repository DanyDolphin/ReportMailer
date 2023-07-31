# Utils
import os
import csv


def read_csv_file(file_name):
    '''Read csv file'''
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)
    return data


def read_file(file_name):
    '''Read file using main directory as base'''
    path = os.path.join(os.getcwd(), file_name)
    with open(path, 'r') as file:
        data = file.read()
    return data
