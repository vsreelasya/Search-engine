

#Name: VallabhaneniSreelasya.Assignment02.py
#ID: Assignment 02
#Question: script that copies, line by line, a text file into a destination file. The source and destination file paths are given as input parameters.
#Name: Sree Lasya Vallabhaneni
#Due Date: Sept 13, 2016

import os.path
def copyFile(sourceFile, destinationFile): #Function to declare parameters source and destination files
    f = open(sourceFile)
    f1 = open(destinationFile, "w") #Opening output funtion in write mode
    if(os.path.exists("/Users/lasyavallabhaneni/Documents/Courses/IR/Assignments/Assignment2/Part1/input.txt")): #if loop to checks whether file is present or not
        if(os.path.exists("/Users/lasyavallabhaneni/Documents/Courses/IR/Assignments/Assignment2/Part1/output.txt")): #if loop to checks whether file is present or not
            for line in f: 
                    line = line.strip()  #Remove extra white space in file f i.e source file
                    print(line)
                    f1.write(line) #copying from source file to destination file
            f.close()
            f1.close()
        else:
            print("Destination file not found")
    else:
        print("Source file not file found")
#calling function to pass parameters
copyFile("/Users/lasyavallabhaneni/Documents/Courses/IR/Assignments/Assignment2/Part1/input.txt","/Users/lasyavallabhaneni/Documents/Courses/IR/Assignments/Assignment2/Part1/output.txt")