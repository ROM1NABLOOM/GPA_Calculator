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
import re
import os, os.path


class File (object):
    def __init__(self, file):
        self.file = file
        
    def detangle(self):
        self.loadFile()
        self.stripFile()
        self.average()
            
        return (self.avg)
    
            
            
            

    def loadFile(self):
        """Inputs file.
        * I need to figure out how
        to import files with just the text name using os.path,
        this method should take the input, convert it into file,
        find that file, and open that file.""
        self.f = open(self.file, 'r')
        self.text="""
        
        self.f = open(self.file,'r')
        self.text= ""
        for line in self.f:
            self.stripped_line=line.rstrip()
            self.text+=self.stripped_line
        self.f.close()
        return(self.text)
        
            
        
    def stripFile(self):
    
        """Splits up the file into a list using "/",
        *I need to releran how to split up the list
        by an indicator in text"""
        
        self.splitList = self.text.split("%")
        self.f.close()
        return (self.splitList)
 
    def average(self):
        """Takes the list, adds it up and divides it by the length."""
        sUm = 0
        for i in self.splitList:
            if i != "":
                sUm+=int(i)
                
        self.avg = sUm/len(self.splitList)
        return (self.avg)
            
