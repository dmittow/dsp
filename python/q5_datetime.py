# Hint:  use Google to find python function

import numpy
import pandas
from datetime import datetime as dt
from dateutil.parser import parse

####a) 
date_start_0 = '01-02-2013'    
date_stop_0 = '07-28-2015'

diff_0 = dt.date(dt.strptime(date_stop_0, '%m-%d-%Y')) - dt.date(dt.strptime(date_start_0, '%m-%d-%Y'))
print(diff)

####b)  
date_start_1 = '12312013'  
date_stop_1 = '05282015' 

diff_1 = dt.date(dt.strptime(date_stop_1, '%m%d%Y')) - dt.date(dt.strptime(date_start_1, '%m%d%Y'))
print(diff_1)

####c)  
date_start_2 = '15-Jan-1994'      
date_stop_2 = '14-Jul-2015' 

diff_2 = dt.date(dt.strptime(date_stop_2, '%d-%b-%Y')) - dt.date(dt.strptime(date_start_2, '%d-%b-%Y'))
print(diff_2)
