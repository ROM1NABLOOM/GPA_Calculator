"""
Title: GPA Calculator for final project
Author: Landon

Objective: Take the previous values and output the GPA through the GPA formula

How the GPA Claculator will calculate:

Take the points associated with the letter
A = 4
B = 3
C = 2
D = 1
F = 0

and mulitiply them by the credits earned for that class

A in a class of 3 credits = 12

Add those numbers for each class

ex:
A in a class of 3 credits = 12
B in a class o 1 credit = 3
C in a class of 4 credits = 8
12+8+3 = 23
23/total number of credits

3+4+1 = 8

23/8 = 2.875 (2.88)

*********
Methods to create:

Just __init__
and total
**********
Input = Credits, points
Output = GPA
"""
#Uses the math method for presision in GPA calculation
import math

class GPA_Calculator(object):

    #Take all the input of GUI in credits and point form 
    def __init__(self, credit1, points1, credit2, points2, credit3, points3, credit4, points4, credit5, points5, credit6, points6):
        self.error = False 

        #Converts the string into a float
        try:
            
            self.credit1 = float(credit1)
            self.points1 = float(points1)

            
            self.credit2 = float(credit2)
            self.points2 = float(points2)
            
            
            self.credit3 = float(credit3)
            self.points3 = float(points3)
            
            self.credit4 = float(credit4)
            self.points4 = float(points4)

            self.credit5 = float(credit5)
            self.points5 = float(points5)

            self.credit6 = float(credit6)
            self.points6 = float(points6)
        except:
            self.error = True
            return
            
        #Creates a list for addition and adds all the credit to that list 
        self.creditList =[]
        self.creditList.append(self.credit1)
        self.creditList.append(self.credit2)
        self.creditList.append(self.credit3)
        self.creditList.append(self.credit4)
        self.creditList.append(self.credit5)
        self.creditList.append(self.credit6)
        #Create a variable for the sum of all credit (will use this later)
        self.Total_Credits = math.fsum(self.creditList)
        
        #Creates a list for each row of input or each class (meaning class taken in school, not the class in python)
        self.class1 = []
        self.class1.append(self.credit1)
        self.class1.append(self.points1)
        self.class2 = []
        self.class2.append(self.credit2)
        self.class2.append(self.points2)
        self.class3 = []
        self.class3.append(self.credit3)
        self.class3.append(self.points3)
        self.class4 = []
        self.class4.append(self.credit4)
        self.class4.append(self.points4)
        self.class5 = []
        self.class5.append(self.credit5)
        self.class5.append(self.points5)
        self.class6 = []
        self.class6.append(self.credit6)
        self.class6.append(self.points6)

        #Uses math.prod to find the product for each of those classes
        self.product_class1 = math.prod(self.class1)
        self.product_class2 = math.prod(self.class2)
        self.product_class3 = math.prod(self.class3)
        self.product_class4 = math.prod(self.class4)
        self.product_class5 = math.prod(self.class5)
        self.product_class6 = math.prod(self.class6)
        
        #Creates another list for addition
        self.productList = []
        self.productList.append(self.product_class1)
        self.productList.append(self.product_class2)
        self.productList.append(self.product_class3)
        self.productList.append(self.product_class4)
        self.productList.append(self.product_class5)
        self.productList.append(self.product_class6)
        

    def total(self):
        #Finds the total for the classes added up
        
        self.Total = math.fsum(self.productList)
        #Divides this by the Total_Credits variable created earlier
        
        self.GPA = self.Total/self.Total_Credits

        #Returns the float of the number, rounded to 2 decimal places. 
        return("%.2f"%self.GPA)

##"""This was just to test the program before I plugged it in"""
##if __name__== "__main__":
##    g = GPA_Calculator("3.00","4.00","4.00","3.00","2.00","2.00","0","0", "3.00","3.00", "3.00","3.00")
##    okay = g.total()
##    print(okay)
    

    
               
    





































