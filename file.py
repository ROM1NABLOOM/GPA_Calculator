"""
Title: File class for Final Project
Author: Landon Dahl

Objective: Take in a file with number grades

ex: 90%

and find the average

********
Different methods needed
- importFile method (takes in the file and reads it)
- stripFile method (takes the contents of the file, stips it to a list, and creates a numberator and denominator list)
- calculate method(Takes the numberator list and divides it by the numerator list, creates an average list)
- average methods(Finds the summ of the average list and divides it by its length

********
Input = File
Output = Average of that file
********

"""


class File (object):

    #Takes the file as input
    def __init__(self, file):
        self.file = file


    def combine(self):
        """Combines all the methods for this class"""
        self.loadFile()
        self.stripFile()
        self.average()

        #Output is the average    
        return (self.avg)
    
            
            
            

    def loadFile(self):
        """Inputs file."""
        
        self.f = open(self.file,'r')
        
        #Gets ride of /n
        self.text= ""
        for line in self.f:
            self.stripped_line=line.rstrip()
            self.text+=self.stripped_line
        self.f.close()
        return(self.text)
        
            
        
    def stripFile(self):
    
        """Splits up the file into a list"""

        #Splits is by the percent symbol
        self.splitList = self.text.split("%")
        self.f.close()
        #returns the list 
        return (self.splitList)
 
    def average(self):
        """Takes the list, adds it up and divides it by the length."""
        #Create a variable set to 0 for later
        sUm = 0

        #Creates a for loop to convert the list to intiger form 
        for i in self.splitList:
            if i != "":
                sUm+=int(i)
                
        #Formula to find the average        
        self.avg = sUm/len(self.splitList)
        return (self.avg)
            
