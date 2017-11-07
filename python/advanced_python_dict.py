import csv
import re

with open('faculty.csv','r') as f: 
    f_reader = csv.reader(f)
    next(f_reader)
    
    degrees = []
    titles = []
    emails = []
    last_names = []
    values = []
    faculty_dict = {}
    
    for line in f_reader:
        last_name = str.split(line[0], ' ')[-1]
        deg_std = str.split(str.replace(line[1], '.','').lstrip(),' ')
        degree = deg_std[0]
        #[d.upper() for d in deg_std if d != '' and d.isalpha()]
        title = str.replace(line[2], ' of Biostatistics', '')
        email = line[3]
        val = [degree, title, email]
        faculty_dict.setdefault(last_name, []).append(val)
        
