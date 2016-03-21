import urllib2
import re
import os
import time
 
while 1:
 
    html_content = urllib2.urlopen('http://results.vtu.ac.in/').read() 
 
    matches = re.findall('B.E/B.Tech', html_content);  
 
 
    if len(matches) == 0: 
       os.system("msg * 'Yes!, Result is not declared yet'")
       time.sleep(900)
 
    else:
       os.system("msg * 'Oops!, Result Declared'")
       quit()