import urllib.request
import re
from bs4 import BeautifulSoup, SoupStrainer
from collections import Counter
from urllib.parse import urljoin
# Website that needs to be scrapped
def get_text(url):
    # Crawl the site to get html   
    # What if the link doesnot exist?
        try:
            site = urllib.request.urlopen(url).read().decode('utf-8')
        except urllib.error.URLError as e:
            return ''
        else:
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
mainurl = 'http://www.memphis.edu/'
htmlfile = urllib.request.urlopen(mainurl).read()

# Query webpage to get all links only
for link in BeautifulSoup(htmlfile, "html.parser", parse_only=SoupStrainer('a')):
    if 'href' in getattr(link, 'attrs', {}):
        href = link['href']
        # Remove any whitespace
        href = href.strip()
        
        # Cleaning hashed urls and url params
        if '#' in href:
            href = href.split('#')[0]
        if '?' in href:
            href = href.split('?')[0]
        
        # Ignore PPT file, main url, email links
        if (('.ppt' in href) or('.pdf' in href) or (href == mainurl) or ('mailto:' in href)):
            continue
        
        # Uh! Check for relative URL if so fix it by appending the current url
        if re.match('^[a-zA-Z]{2,}:', href) == None:
            abs_href = urljoin(mainurl, href)
            #print("Converting relative URL to absolute: %s -> %s" % (href, abs_href))
            href = abs_href
        
        if (href not in urls):
            # Finally! push it to urls list
            urls.append(href)
                              
all_words = {}
occurances ={}
for i in range(len(urls)):
    print(urls[i]);
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