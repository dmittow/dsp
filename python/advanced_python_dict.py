import csv
import re

with open('faculty.csv','r') as f: 
    f_reader = csv.reader(f)
    next(f_reader)
    
    faculty_dict = {}
    faculty_dict_fnm = {}
    
    for line in f_reader:
        last_name = str.split(line[0], ' ')[-1]
        first_name = str.split(line[0], ' ')[0]
        name_tup = (last_name, first_name)
        degree = str.split(str.replace(line[1], '.','').lstrip(),' ')[0]
        title = str.replace(line[2], ' of Biostatistics', '')
        email = line[3]
        val = [degree, title, email]
        faculty_dict.setdefault(last_name, []).append(val)
        faculty_dict_fnm.setdefault(name_tup,[]).append(val)
        
       
    
#print 3 random values from faculty dictionary keyed by last name
print({k: faculty_dict[k] for k in list(faculty_dict.keys())[:3]})

#print 3 random values from faculty dictionary keyed by (last name, first name)
print({k: faculty_dict_fnm[k] for k in list(faculty_dict_fnm.keys())[:3]})

#print first 3 key value pairs from faculty dict sorted by last name
print({k: faculty_dict_fnm[k] for k in sorted(list(faculty_dict_fnm.keys()), key=lambda name:name[0])[:3]})
