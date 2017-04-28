from flask import Flask, render_template, request

import os
import math
import re
from nltk import PorterStemmer
from collections import defaultdict

def get_search_results(query):
    count = {} #dictionary that stores the count
    N = 0 #Number of Documents
    documents = defaultdict(dict) #dictionary of dictionary
    idfs = defaultdict(dict) #idf dictionary #tfidf dictionary i.e weights
    files = defaultdict(dict) #all the files 
    for i in os.listdir("inputfiles"):
    #    print(i)#reading input files  
        if i.endswith(".txt"):
            N += 1
            count = {}
            stop = "inputfiles/"+i 
            reading_file = open(stop, 'r') #opening stopword file 
            line = reading_file.read()
            line = line.replace('\n',' ')
            split=line.split(" ")
            for w in split: 
                if w not in count: #variable w parses each word to check if it is repeating and counting
                    count[w] = 1
                else:
                    count[w] += 1 #counting term frequency
            for w in count:
               documents[w][i] = count[w]  
               files[i][w] = len(documents[w].keys())     
    for word in sorted(documents.keys()): 
        n = len(documents[word].keys()) #n is length of dictionary of dictionary i.e a word present in how many documents
    #    output.write("\n" + word +':' + str(n)) #word and df
        idf = math.log10(N/n)
        
        idfs[word] = idf      
    #    output.write("\n")
    #    output.write(str(documents[word])) #document n and term frequency
    #for word in document:
    weights = defaultdict(dict)
    lengths = defaultdict(dict)
    #Caluclating thw document and weights of the word in document
    for document in files.keys():
        for word in files[document]:
            weights[document][word] = files[document][word] * idfs[word]
    for document in weights.keys():
        lengths[document] = 0
        for word in weights[document].keys():
            lengths[document] += (weights[document][word]) * (weights[document][word])  
        lengths[document] = math.sqrt(lengths[document])
    #query of the user
    #preprocessing the query
    stop = "stop.txt" #stopword file path 
    stopwords_file = open(stop, 'r') #opening stopword file 
    line = stopwords_file.read()
    line = line.replace('\n',' ')
    stopword=line.split(" ") #splitting the words like a list
    stopwords=set(stopword) #appending to the set stopword
    words_in_query= []
    raw_words_in_query = []
    raw_words_in_query = re.findall('[a-z]+',query.lower()) #extract only words from file removes digits punctuations symbols
                #print(words_in_fi
    #tf values for the query and finding the weights of the query words
    query_tfs = defaultdict(dict)
    for w in sorted(raw_words_in_query):
        stemmed_word = PorterStemmer().stem(w)
        if stemmed_word not in stopwords: #if any stopwords then it will filter
            words_in_query.append(stemmed_word) #morphological corrections are made by potter stemmer
            
            if stemmed_word not in query_tfs:
                query_tfs[stemmed_word] = 1
            else:
                query_tfs[stemmed_word] += 1
    query_weights = {}
    query_length = 0
    for word in query_tfs.keys():
        if word in documents:
    
            query_weights[word] = (query_tfs[word]) * (idfs[word])
            query_length += (query_weights[word]) * (query_weights[word])
    query_length = math.sqrt(query_length)
    list_of_documents = defaultdict(dict)
    scored_documents = {}
    retriveddocument={}
    #find the lenghts of documents and finding the scores 
    for word in query_tfs.keys():
         if word in documents:
             retriveddocument=documents[word]
             for document in retriveddocument.keys():
                 if document not in list_of_documents:
                     list_of_documents[document]['score'] = query_weights[word] * weights[document][word]
                 else:
                     list_of_documents[document]['score'] =+ query_weights[word] * weights[document][word]
                 if(query_length==0 or lengths[document]==0):
                     scored_documents[document] = 0
                 else:
                     scored_documents[document] = (list_of_documents[document]['score']) / (query_length * lengths[document])
    #ranking the retrieved documents 
    results = []
    for w in sorted(scored_documents, key=scored_documents.get, reverse=True):
        
        result = {
            'file': w,
            'score': scored_documents[w] 
        }
        with open("inputfiles/"+w, 'r') as f:
          first_line = f.readline()
          result['link'] = first_line
          results.append(result)
    return results

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def data():
    return render_template('index.html')

@app.route('/search', methods = ['POST'])
def search():
   if request.method == 'POST':
      query = request.form['query']
      results = get_search_results(query)
      
      return render_template('results.html', results=results, query=query)


if __name__ == "__main__":
    app.run(debug=True)