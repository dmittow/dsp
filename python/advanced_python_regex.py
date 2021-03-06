import csv
import re

with open('faculty.csv','r') as f: 
    f_reader = csv.reader(f)
    next(f_reader)
    
    degrees = []
    titles = []
    emails = []
    domains = []
    
    for line in f_reader:
        deg_std = str.split(str.replace(line[1], '.','').lower(),' ')
        degrees = degrees + [d.upper() for d in deg_std if d != '' and d.isalpha()]
        titles = titles + [str.replace(str.replace(line[2], ' of Biostatistics', ''), ' is Biostatistics','')]
        emails = emails + [e for e in line if re.match(r'.*@.*',e)]
        domains = domains + [d[d.index('@') + 1:] for d in line if re.match(r'.*@.*',d)]
        
    deg_count_dict = {d:degrees.count(d) for d in degrees}
    title_count_dict = {t:titles.count(t) for t in titles}
    unique_domains = set(domains)
    
print(deg_count_dict)
print(title_count_dict)
print(emails)
print(unique_domains)

