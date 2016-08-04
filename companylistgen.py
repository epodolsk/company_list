#Name: Eric Podolsky
#Date: 3 August 2016
#Description: Retrieves a list of companies from the Ohio State career fair website
#			  and generates a text file containing the name of each company with a 
#			  Wikipedia summary.

import urllib
import re
import wikipedia

ufile = urllib.urlopen("https://expo.engineering.osu.edu/stub-0")
source = ufile.read()
source = re.sub("&amp;", "&", source)
#find all lines containing company names
companies = re.findall("(?:<p>)?\t?(.+)(?:<br />)|(?:</p>)", source)

f=open('companies.txt', 'w')
for c in companies:
    f.write(c.encode('utf-8') + '\n')
    if(c != ""):
        try:
            summary=wikipedia.summary(c).encode("utf-8")
        except wikipedia.exceptions.PageError as e:
            print "None found"
        except wikipedia.exceptions.DisambiguationError as e:
            print "Disambiguation error"
        f.write(summary + '\n')
f.close()
