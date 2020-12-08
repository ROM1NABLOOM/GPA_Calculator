# GPA_Calculator
Final Project for Intro to Programming. 

This program is a GPA Grading Calculator. In my GPA Calculator the user can put in their letter grade for the class, or if they don’t know their letter grade, they can import a file that has the percentage for each assignment. For each class they also need to put in the credit ammount. 

After the user has put in all the information they want, they can click the "Check GPA" button. Once they have clicked this button, two things happen. One, the file name they entered changes to a letter grade and two, a popup window shows them their GPA. 

If the user wants to save this GPA to check back on later, they are able to do so by clicking the "save GPA" button. Once they click this button they enter what they want to call the file where the GPA will be saved. These files will be saved in a folder, called "GPA Past Semester". 

HOW THIS PROJECT MEETS REQUIREMENTS:
- I have defined and customized both a GUI enviornment and classes
- I have written and defined MORE than 3 methods and funtions, some of these include 
    - loadFile(self)  (File class)
    - stripFile(self) (File class)
    - average(self)   (File class)
    - combine(self)   (File class) 
    - letterGrade(self) (Grade_Calculator class)
    - points_conversion(self) (Grade_Calculator class) 
    - total (self) (GPA_Calculator class)
    (these are just the ones in the classes, they don't include the ones in run and main)
- I have used multiple lists mainly in the File class and in the GPA_Calculator class
- I used four modules which include, datetime, math, breezypythongui, and os
- I read files in the File class and I write a file to save the GPA in run 
- I use exception handeling in the GPA_Calculator class 
- I use if, else, elif, and data verification multiple places in my program including in the Grade_Calculator class and in run 
- I haven't yet met the requirement of applying a python concept not learned in class, but I still have a week to figure out what I want to do to meet it

