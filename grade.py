"""
Title: Grade Calculator class for Final Project
Author: Landon Dahl

Objective: Take in the average and find the letter grade and points 

*******
Different methods needed
- letterGrade method (takes in the average and outputs the letter grade)
- points_conversion method (uses the dictionary to convert to points)
A = 4
A- =3.70
B+=3.33
B= 3.00
B- =2.70
C+ =2.30
C =2.00
C-=1.70
D+=1.30
D=1.00
D-=0.70
F=0
*******
Input = Average
Output = Letter Grade, Points 
"""
from file import File

class Grade_Calculator (object):

    #Input is average
    def __init__(self, average):
        #Converts the average to a float
        self.avg = float(average)

        #Dicitionary to connect letter grade to the points needed for the GPA Calculator
        self.points = {"A":"4.00","B":"3.00", "C":"2.00", "D":"1.00", "F":"0.00"}

    def letterGrade(self):
        """Shows the letter grade for the average"""
        """Purpose is to use this to change what is in the input box of GUI"""
        if  (self.avg)>=90:
             return ("A")
        elif(self.avg)>=80 and self.avg<90:
             return ("B")
        elif(self.avg)>=70 and self.avg <80:
             return ("C")
        elif (self.avg)>=60 and self.avg <70:
            return("D")
        elif (self.avg)<=60:
            return("F")
        
    def points_conversion(self):
        """Takes the dictionary and uses is to convert average to letter grade points"""
        """Purpose, the GPA Calculator will need these points for the calculation"""
        if (self.avg)>=90:
            return (self.points["A"])
        elif (self.avg)>=80 and self.avg<90:
            return (self.points["B"])
        elif (self.avg)>=70 and self.avg <80:
            return (self.points["C"])
        elif (self.avg)>=60 and self.avg <70:
            return (self.points["D"])
        elif (self.avg)<=60:
            return (self.points["F"])
    



