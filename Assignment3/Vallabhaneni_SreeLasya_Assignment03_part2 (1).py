import urllib.request
import re
from bs4 import BeautifulSoup
from collections import Counter
import urllib.parse
# Website that needs to be scrapped
#urls = ["http://www.cs.memphis.edu/~vrus/teaching/ir-websearch/assignments/assignment-03.txt",
 #       "http://www.cs.memphis.edu/~vrus/teaching/ir-websearch/assignments/assignment-01.txt"]
#f = open("/Users/lasyavallabhaneni/Documents/Courses/IR/Assignments/Assignment3/input.txt", "w")
soup = BeautifulSoup
def get_text(url):
    # Crawl the site to get html
    site = urllib.request.urlopen(url).read().decode('utf-8')
    html = BeautifulSoup(site, "html.parser") # Get the html from the site
    # Remove all script and style tags
    for script in html(["script", "style"]):
            script.extract() # Remove these two elements from the BS4 object
    # Get the plain text from html
    text = html.get_text()
    lines = (line.strip() for line in text.splitlines()) # break into lines
    chunks = (phrase.strip() for line in lines for phrase in line.split("  ")) # break multi-headlines into a line each
    def chunk_space(chunk):
        chunk_out = chunk + ' ' # Need to fix spacing issue
        return chunk_out  
    text = ''.join(chunk_space(chunk) for chunk in chunks if chunk).encode('utf-8') # Get rid of all blank lines and ends of line
    # Now clean out all of the unicode junk (this line works great!!!)
    text = text.decode('unicode_escape').encode('ascii', 'ignore') # Need this as some websites aren't formatted
    text = text.decode('utf-8') # Bytecode like text to string probably wierd with python 3
    text = re.sub("[^a-zA-Z.+3]"," ", text)  # Now get rid of any terms that aren't words
    text = text.lower().split()  # Go to lower case and split them apart
    
    return text

def get_word_counts(text):
    only  = {}
    for i in text: 
        if i not in only: #variable w parses each word to check if it is repeating and counting
            only[i] = 1
        else:
            only[i] += 1
#    with open(str(file )+ ".txt", "w") as text_file:
#        for w1 in sorted(only.keys()):
#            text_file.write('\n' + str(w1) + " " + str(only[w1]))
#        text_file.write('\n\n\n')
            
    return only
urls =[]    
mainurl = 'http://www.cs.memphis.edu/~vrus/teaching/ir-websearch/'
htmlfile = urllib.request.urlopen(mainurl).read().decode('utf-8')
soup = BeautifulSoup(htmlfile)
pagelink = re.findall(r'"http://.*?"',htmlfile)
for pagelinks in pagelink:  
    urls.append(pagelinks)
print(urls)     
#repeat( "http://www.cs.memphis.edu/~vrus/teaching/ir-websearch/assignments/assignment-03.txt", "http://www.cs.memphis.edu/~vrus/teaching/ir-websearch/assignments/assignment-01.txt")
#urls = ["http://www.cs.memphis.edu/~vrus/teaching/ir-websearch/","http://www.cs.memphis.edu/~vrus/teaching/ir-websearch/assignments/assignment-03.txt", 
#          "http://www.cs.memphis.edu/~vrus/teaching/ir-websearch/assignments/assignment-01.txt",
#          "http://www.cs.memphis.edu/~vrus/",
#          "http://venturebeat.com/2016/09/07/the-200-billion-chatbot-disruption-part-two/?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A%20venturebeat/SZYF%20%28VentureBeat%29"]
all_words = {}
occurances ={}
for i in range(len(urls)):
    previous = Counter(all_words) 
    next = Counter(get_word_counts(get_text(urls[i])))
    if (i==0):
        for word in next.keys():
            occurances[word] = 1
    else:
        for word in next.keys():
            if word in occurances:
                occurances[word] += 1            
                
    all_words = previous + next
    
all_words = Counter(all_words)
print(len(occurances))

with open("occurrances.txt", "w") as text_file:
    for word in sorted(occurances.keys()):
        text_file.write('\n' + str(word) + " " + str(occurances[word]))
        
with open("test.txt", "w") as text_file:
    for w1 in sorted(all_words.keys()):
        text_file.write('\n' + str(w1) + " " + str(all_words[w1]))