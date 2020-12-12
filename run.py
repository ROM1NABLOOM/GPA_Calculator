from breezypythongui import EasyFrame
from grade import Grade_Calculator
from main import Main
from GPA import GPA_Calculator
import os
import datetime

class GUI(EasyFrame):
    
    def __init__(self):
        EasyFrame.__init__(self, width=600, height = 400, title = "GPA CALCULATOR", background = "light grey")
        self.GPAtext = self.addLabel(text="College GPA Calculator", row=0, column = 0, sticky ="NSEW")
        menuPanel = self.addPanel(row=1, column = 0, background = "light green")
        self.inputText = menuPanel.addLabel(text="class document or letter grade", row = 1, column = 0, background = "light green")
        self.credits = menuPanel.addLabel(text="Credits", row =1, column = 1, background = "light green")
        optionPanel= self.addPanel(row = 2, column = 0, background = "light green")
        self.box_1 = menuPanel.addTextField("0",row = 1, column = 1)
        self.box_2 = menuPanel.addTextField("", row=1, column = 0)
        self.inputText = menuPanel.addLabel(text="class document or letter grade", row = 2, column = 0, background = "light green")
        self.credits = menuPanel.addLabel(text="Credits", row =2, column = 1,background = "light green")
        self.box_3 = menuPanel.addTextField("0",row = 2, column = 1)
        self.box_4 = menuPanel.addTextField("", row=2, column = 0)
        self.inputText = menuPanel.addLabel(text="class document or letter grade", row = 3, column = 0, background = "light green")
        self.credits = menuPanel.addLabel(text="Credits", row =3, column = 1, background = "light green")
        self.box_5 = menuPanel.addTextField("0",row = 3, column = 1)
        self.box_6 =menuPanel.addTextField("", row=3, column = 0)
        self.inputText = menuPanel.addLabel(text="class document or letter grade", row = 4, column = 0, background = "light green")
        self.credits = menuPanel.addLabel(text="Credits", row =4, column = 1, background = "light green")
        self.box_7 = menuPanel.addTextField("0",row = 4, column = 1)
        self.box_8 = menuPanel.addTextField("", row=4, column = 0)
        self.inputText = menuPanel.addLabel(text="class document or letter grade", row = 5, column = 0, background = "light green")
        self.credits = menuPanel.addLabel(text="Credits", row =5, column = 1, background = "light green")
        self.box_9 = menuPanel.addTextField("0",row = 5, column = 1)
        self.box_10 = menuPanel.addTextField("", row=5, column = 0)
        self.inputText = menuPanel.addLabel(text="class document or letter grade", row = 6, column = 0, background = "light green")
        self.credits = menuPanel.addLabel(text="Credits", row =6, column = 1, background = "light green")
        self.box_11 = menuPanel.addTextField("0",row = 6, column = 1)
        self.box_12 = menuPanel.addTextField("", row=6, column = 0)
        self.GPAButton = self.addButton("Check GPA", row = 7, column = 0, command = self.checkGPA)
        
        self.save = self.addButton("  Save GPA", row = 8, columnspan = 2, column = 0, command = self.writeFile)
        self.listForFile=[]
        self.listforCredit=[]

    def getText(self):
        print("works")
        self.box_1Credit = self.box_1.getText()
        self.Input_one = self.box_2.getText()
        self.box_3Credit = self.box_3.getText()
        self.Input_two = self.box_4.getText()
        self.box_5Credit = self.box_5.getText()
        self.Input_three = self.box_6.getText()
        self.box_7Credit = self.box_7.getText()
        self.Input_four = self.box_8.getText()
        self.box_9Credit = self.box_9.getText()
        self.Input_five = self.box_10.getText()
        self.box_11Credit = self.box_11.getText()
        self.Input_six = self.box_12.getText()


        
        
    def checkGPA(self):
        print("GPA works")
        #Gets text from text box 
        self.getText()

        #Input one 
        if self.Input_one=="":

            self.newPoints1 = 0

        elif self.Input_one!="":

            self.avg_1 = 0
            if self.Input_one == "A":
                self.avg_1+= 90
                g = Grade_Calculator(self.avg_1)
                self.newPoints1 = g.points_conversion()
            elif self.Input_one == "B":
                self.avg_1+= 80
                g = Grade_Calculator(self.avg_1)
                self.newPoints1 = g.points_conversion()
            elif self.Input_one == "C":
                self.avg_1+= 70
                g = Grade_Calculator(self.avg_1)
                self.newPoints1 = g.points_conversion()
            elif self.Input_one == "D":
                self.avg_1+= 65
                g = Grade_Calculator(self.avg_1)
                self.newPoints1 = g.points_conversion()
            elif self.Input_one == "F":
                self.avg_1+= 55
                g = Grade_Calculator(self.avg_1)
                self.newPoints1 = g.points_conversion()
            
            else:                
                

                run = Main(self.Input_one)
                self.changeInput1 = run.findGrade()
                self.box_2.setText(self.changeInput1)
                self.newPoints1 = run.findPoints()

        #Input two 
        if self.Input_two=="":
            
            self.newPoints2 = 0

        elif self.Input_two!="":

            self.avg_2 = 0
            if self.Input_two == "A":
                self.avg_2+= 90
                g = Grade_Calculator(self.avg_2)
                self.newPoints2 = g.points_conversion()
                
            elif self.Input_two == "B":
                self.avg_2+= 80
                g = Grade_Calculator(self.avg_2)
                self.newPoints2 = g.points_conversion()
                
            elif self.Input_two == "C":
                self.avg_2+= 70
                g = Grade_Calculator(self.avg_2)
                self.newPoints2 = g.points_conversion()
                
            elif self.Input_two == "D":
                self.avg_2+= 65
                g = Grade_Calculator(self.avg_2)
                self.newPoints2 = g.points_conversion()
                
            elif self.Input_two == "F":
                self.avg_2+= 55
                g = Grade_Calculator(self.avg_2)
                self.newPoints2 = g.points_conversion()

 
            
            else:
                run = Main(self.Input_two)
                self.changeInput2 = run.findGrade()
                self.box_4.setText(self.changeInput2)
                self.newPoints2 = run.findPoints()

        #Input three 
        if self.Input_three=="":
            self.newPoints3 = 0

        elif self.Input_three!="":

            self.avg_3 = 0
            if self.Input_three == "A":
                self.avg_3+= 90
                g = Grade_Calculator(self.avg_3)
                self.newPoints3 = g.points_conversion()
                
            elif self.Input_three == "B":
                self.avg_3+= 80
                g = Grade_Calculator(self.avg_3)
                self.newPoints3 = g.points_conversion()
                
            elif self.Input_three == "C":
                self.avg_3+= 70
                g = Grade_Calculator(self.avg_3)
                self.newPoints3 = g.points_conversion()
                
            elif self.Input_three == "D":
                self.avg_3+= 65
                g = Grade_Calculator(self.avg_3)
                self.newPoints3 = g.points_conversion()
                
            elif self.Input_three == "F":
                self.avg_3+= 55    
                g = Grade_Calculator(self.avg_3)
                self.newPoints3 = g.points_conversion()
                
            
            
            else:
                run = Main(self.Input_three)
                self.changeInput3 = run.findGrade()
                self.box_6.setText(self.changeInput3)
                self.newPoints3 =run.findPoints()
                print("Credits = ",self.box_5Credit)
                print("this is what we want = ", self.newPoints3)

        #Input four
        if self.Input_four=="":
            self.newPoints4 = 0
            
        elif self.Input_four!="":

                self.avg_4 = 0
                if self.Input_four == "A":
                    self.avg_4+= 90
                    g = Grade_Calculator(self.avg_4)
                    self.newPoints4 = g.points_conversion()
                elif self.Input_four == "B":
                    self.avg_4+= 80
                    g = Grade_Calculator(self.avg_4)
                    self.newPoints4 = g.points_conversion()
                elif self.Input_four == "C":
                    self.avg_4+= 70
                    g = Grade_Calculator(self.avg_4)
                    self.newPoints4 = g.points_conversion()
                elif self.Input_four == "D":
                    self.avg_4+= 65
                    g = Grade_Calculator(self.avg_4)
                    self.newPoints4 = g.points_conversion()
                elif self.Input_four == "F":
                    self.avg_4+= 55
                    g = Grade_Calculator(self.avg_4)
                    self.newPoints4 = g.points_conversion()
                    
            
                else:
                    run = Main(self.Input_four)
                    self.changeInput4 = run.findGrade()
                    self.box_8.setText(self.changeInput4)
                    self.newPoints4 = run.findPoints()
                    print("Credits = ", self.box_7Credit)
                    print("this is what we want =",self.newPoints4)
        #Input five
        if self.Input_five=="":
            self.newPoints5 = 0
        elif self.Input_five!="":

            self.avg_5 = 0
            if self.Input_five == "A":
                self.avg_5+= 90
                g = Grade_Calculator(self.avg_5)
                self.newPoints5 = g.points_conversion()
            elif self.Input_five == "B":
                self.avg_5+= 80
                g = Grade_Calculator(self.avg_5)
                self.newPoints5 = g.points_conversion()
            elif self.Input_five == "C":
                self.avg_5+= 70
                g = Grade_Calculator(self.avg_5)
                self.newPoints5 = g.points_conversion()
                print(self.newPoints5)
            elif self.Input_five == "D":
                self.avg_5+= 65
                g = Grade_Calculator(self.avg_5)
                self.newPoints5 = g.points_conversion()
            elif self.Input_five == "F":
                self.avg_5+= 55
                g = Grade_Calculator(self.avg_5)
                self.newPoints5 = g.points_conversion()
                
        
            else:
                run = Main(self.Input_five)
                self.changeInput5 = run.findGrade()
                self.box_10.setText(self.changeInput5)
                self.newPoints5 = run.findPoints()
                print("Credits = ", self.box_9Credit)
                print("this is what we want =",self.newPoints5)
        #Input six
        if self.Input_six=="":
            self.newPoints6 = 0
        elif self.Input_six!="":
            self.avg_6 = 0
            
            if self.Input_six == "A":
                self.avg_6+= 90
                g = Grade_Calculator(self.avg_6)
                self.newPoints6 = g.points_conversion()
            elif self.Input_six == "B":
                self.avg_6+= 80
                g = Grade_Calculator(self.avg_6)
                self.newPoints6 = g.points_conversion()
            elif self.Input_six == "C":
                self.avg_6+= 70
                g = Grade_Calculator(self.avg_6)
                self.newPoints6 = g.points_conversion()
            elif self.Input_six == "D":
                self.avg_6+= 65
                g = Grade_Calculator(self.avg_6)
                self.newPoints6 = g.points_conversion()
            elif self.Input_six == "F":
                self.avg_6+= 55
                g = Grade_Calculator(self.avg_6)
                self.newPoints6 = g.points_conversion()
                
        
            else:
                run = Main(self.Input_six)
                self.changeInput6 = run.findGrade()
                self.box_12.setText(self.changeInput6)
                self.newPoints6 = run.findPoints()
                print("Credits = ", self.box_11Credit)
                print("this is what we want =",self.newPoints6)
            

        
        G = GPA_Calculator(self.box_1Credit,self.newPoints1, self.box_3Credit,
                           self.newPoints2, self.box_5Credit, self.newPoints3,
                           self.box_7Credit, self.newPoints4, self.box_9Credit,
                           self.newPoints5, self.box_11Credit, self.newPoints6)
        
        if G.error == False:
            self.GPA = G.total()
            print("this is the GPA = ",self.GPA)
            popup_window = self.messageBox(title = "GPA", message = "Your GPA is = " + self.GPA)
        elif G.error == True:
            error_popup_window = self.messageBox(title = "error", message = "Please enter number for credit ammount.")

    def writeFile(self):
        os.chdir("GPA Past Semester")
        self.output = self.prompterBox(title = "Save File", promptString = "Enter the name for the is file")
        self.date = datetime.date.today().strftime("%m/%d/%Y")
        
        f = open(self.output + ".txt", 'w')
        f.write(self.date +"\n" + "This semester's GPA " + self.GPA)
        






def main():
    GUI().mainloop()

if __name__== "__main__":
    main()
    
