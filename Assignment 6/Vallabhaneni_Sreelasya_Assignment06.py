#Name: VallabhaneniSreelasya.Assignment06.py
#ID: Assignment 05
#Question: Automatically collect from memphis.edu 10,000 files
#Name: Sree Lasya Vallabhaneni
#Due Date: November 8, 2016

from collections import deque
from bs4 import BeautifulSoup
#from urllib.parse import urljoin
import re
import urllib
import time
from nltk import PorterStemmer
#seed Url 
url = "http://www.memphis.edu/lambuth/studentservices/"
print ("Page to be crawled:", url)
print ("===================")
# Create queue
queue = deque([])
# Maintains list of visited pages
visited_list = []
urlcollection=[]
stop = "stop.txt" #stopword file path 
stopwords_file = open(stop, 'r') #opening stopword file 
line = stopwords_file.read()
line = line.replace('\n',' ')
stopword=line.split(" ") #splitting the words like a list
stopwords=set(stopword)

# Crawl the page and populate the queue with newly found URLs
def crawl(url):
   try:
       if not url.endswith(".pdf"):
#            visited_list.append(url)         
#            if len(visited_list) > 1000:
#                return
            urlf = urllib.request.urlopen(url)
            soup = BeautifulSoup(urlf.read().decode('utf-8'))
            text = soup.get_text()
            if len(text) > 50:
                outputname= str(url.split("//")[1].replace('/',''))
        #                print(outputname)
                #        print(outputname)
                file=open("output/"+outputname+".txt",'w' )
                print("Start reading", url)         
                file.write(url)
                words_in_file = re.findall('[a-z]+',text.lower()) #extract only words from file removes digits punctuations symbols
                #print(words_in_file)
                for w in sorted(words_in_file):
                    stemmed_word = PorterStemmer().stem(w)
                    if stemmed_word not in stopwords: #if any stopwords then it will filter
#                final_words.append(stemmed_word)            
    #            print(len(text))
        #        print(text)                  
                   #outputname= "Doc-" + str(len(visited_list))                        
                        file.write('\n')
                        file.write(stemmed_word)
                file.close()
                print("Completed writing", url) #print the visited urls
                print("Completed till now:",len(visited_list))
                print("--------------")        
            #write to file and give name
            
            a_tags = soup.findAll("a", href=True) #take only links
        #    print(urls)
            if '#' in a_tags:
                a_tags = a_tags.split('#')[0]
            if '?' in a_tags:
                a_tags = a_tags.split('?')[0]
            if (('.ppt' in a_tags) or ('mailto:' in a_tags)):
                print("ppt or other files")
            tempurl=[]
            for listurl in a_tags:
                eachurl = listurl["href"]
    #            print(eachurl)               
        #            print(eachurl)
                #checking conditions of visited and taking only memphis.edu domain links
                if eachurl.startswith("http:"):   
    #                print(eachurl)
                    if eachurl not in visited_list:
                        if "memphis.edu" in eachurl:
                            tempurl.append(eachurl)
                            
                            
            tempurl=list(set(tempurl))
            for x in tempurl:
                urlcollection.append(x)   
            for url in urlcollection:
                if url not in visited_list and len(visited_list)<1100: #checking 10000 limit
                    visited_list.append(url)
                    urlcollection.remove(url)
                    crawl(url)
                    time.sleep(2) #sleep for 1 second                  
             #crawl(eachurl)                        
   except Exception as e:
        print("error in page",url,"  " ,str(e))

crawl(url) #crawl main seed url
    
