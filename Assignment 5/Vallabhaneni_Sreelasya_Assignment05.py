#Name: VallabhaneniSreelasya.Assignment02.py
#ID: Assignment 05
#Question:Write a  program that generates the inverted index of a set of already preprocessed files. The files are stored in a 
#directory which is given as an input parameter to the program. Use the files preprocessed in the previous assignment(s) as test data. Use raw term frequency (tf) in the document without normalizing it.
#Name: Sree Lasya Vallabhaneni
#Due Date: oct 27, 2016
import os
#import math
#import shutil
#count = {}
#count_dict = {}
#total_dict_frequency = {}
from collections import defaultdict
count = {} #dictionary that stores the count
#N = 0
#metrics = defaultdict(dict)
documents = defaultdict(dict) #dictionary of dictionary
#idfs = defaultdict(dict)
#tfidfs = defaultdict(dict)

for i in os.listdir("inputfiles"): #reading input files
    
    if i.endswith(".txt"):
       # N += 1
        count = {}
        stop = "inputfiles/"+i 
        reading_file = open(stop, 'r') #opening stopword file 
        line = reading_file.read()
        line = line.replace('\n',' ')
        stopword=line.split(" ")
        for w in stopword: 
            if w not in count: #variable w parses each word to check if it is repeating and counting
                count[w] = 1
            else:
                count[w] += 1 #counting term frequency
        for w in count:
           documents[w][i] = count[w]               
#        for w2 in sorted(count.keys()):
#            output.write ('\n' + str(i) + " " + str(w2) + " " + str(count[w2]))
#print(documents.keys())
finename = ("output/output") #creating output
output =open(finename, "w") # Opening in write mode      
for word in sorted(documents.keys()): 
    n = len(documents[word].keys()) #n is length of dictionary of dictionary i.e a word present in how many documents
    output.write("\n" + word +':' + str(n)) #word and df
    #idf = math.log10(N/n)
    #idfs[w] = idf     
    output.write("\n")
    output.write(str(documents[word])) #document name and term frequency
    
    #for doc in (documents[w].keys()):
        
    #tfidfs[w]
#    formula  = tf * idf
#            
#