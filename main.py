"""
Title: Main class for final project
Author: Landon Dahl

Objective: Combine all the classes so that code is shorter in run

Note: Takes just the File and Grade_Calculator classes because
the GPA_Calculator requires all the input and this is doing the calculation
for each row of input

"""

from file import File
from grade import Grade_Calculator

class Main(object):

    #Input is file 
    def __init__(self, file):
        self.file = file


    def findGrade(self):
        #Takes the file and runs it through the File Class 
        avg = File(self.file)
        
        #self.runFile is the same as average 
        self.runFile = avg.combine()
        
        #Takes the average and runs it through the Grade_Calculator class
        self.grade = Grade_Calculator(self.runFile)
        #runs it through the letterGrade method which converts it to a letter Grade
        self.newInput = self.grade.letterGrade()
        #Returns that letter grade 
        return(self.newInput)

    def findPoints(self):
        #Takes the average and finds the points 
        self.newPoints = self.grade.points_conversion()
        #Returns those points 
        return(self.newPoints)
        
        
    
