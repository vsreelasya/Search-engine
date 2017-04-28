##Name: VallabhaneniSreelasya.Assignment02
##ID: Assignment 02
##Question:  script that counts how many words are in the main page of the course website. 
##Also, display the vocabularyof the page in alphabetical order showing for each word its frequency in the page.
##Name: Sree Lasya Vallabhaneni
##Due Date: Sept 13, 2016
##
import re #package for regular expression
count = {} #Creation of Dictionary 
input = "/Users/lasyavallabhaneni/Documents/Courses/IR/Assignments/Assignment2/Part2/ex1.txt"
try:  #Checking whether file is present or not
   with open(input) as f:  
       for line in f:
           words = re.findall('\w+',line.lower()) #Regular expression that takes only words and convert to lower case
           for w in words: 
               if w not in count: #variable w parses each word to check if it is repeating and counting
                   count[w] = 1
               else:
                   count[w] += 1
except IOError as e:
   print(" Error: File not found") #exception handler
print("Frequency of words is displayed below:") 
for w1 in sorted(count.keys()):  #Sorting alphabetically
   print(w1, " ", str(count[w1])) 
   
print("Number of words with repetetion in course website", sum(count.values())) #sum function is to add the frequency
print("Number of words in the course website ", len(count.keys())) 

