#Name: VallabhaneniSreelasya.Assignment02.py
#ID: Assignment 04
#Question: program that preprocesses a collection of documents The input to the program will be a directory containing a list of text files. Use the files from assignment test data as well as 10 documents (manually) collected from news.yahoo.com . 
#The yahoo documents must be converted to text before using them.Remove the following : digits, punctuation ,stop words,urls and other html-like strings,uppercases,morphological variations
#Name: Sree Lasya Vallabhaneni
#Due Date: oct 13, 2016

#import fileinput
import re
import os
from nltk import PorterStemmer #import nltk 
import shutil
#output =open("output.txt", "w") #opening output file to write all the outputs
stop = "stop.txt" #stopword file path 
stopwords_file = open(stop, 'r') #opening stopword file 
line = stopwords_file.read()
line = line.replace('\n',' ')
stopword=line.split(" ") #splitting the words like a list
stopwords=set(stopword) #appending to the set stopword
#print(stopwords)
dir = 'output'
if os.path.exists(dir):
    shutil.rmtree(dir) #check duplicates and delete folders
os.makedirs(dir)

for i in os.listdir("input"):
    if i.endswith(".txt"):
            final_words = []
            stop = "input/"+i 
            cont = open(stop, 'r') #opening stopword file 
            content = cont.read()
            cont.close()
            finename = ("output/out-"+i) 
            output =open(finename, "w") 
            lines = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', content) #Removing links from the input files
            #print(lines)
            #lines= re.sub(r'[^\w\s]','',lines) #can use this regular expression to remove punctuations
            words_in_file = re.findall('[a-z]+',lines.lower()) #extract only words from file removes digits punctuations symbols
            #print(words_in_file)
            for w in sorted(words_in_file):
                stemmed_word = PorterStemmer().stem(w)
                if stemmed_word not in stopwords: #if any stopwords then it will filter
                    final_words.append(stemmed_word) #morphological corrections are made by potter stemmer
            
            final_words = sorted(list(final_words))
            for word in final_words:
                output.write(word) # writing to output file
                output.write("\n")
               
            
        