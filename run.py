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
        self.box_3 =menuPanel.addTextField("0",row = 2, column = 1)
        self.box_4 =menuPanel.addTextField("", row=2, column = 0)
        self.inputText = menuPanel.addLabel(text="class document or letter grade", row = 3, column = 0, background = "light green")
        self.credits = menuPanel.addLabel(text="Credits", row =3, column = 1, background = "light green")
        self.box_5 = menuPanel.addTextField("0",row = 3, column = 1)
        self.box_6 =menuPanel.addTextField("", row=3, column = 0)
        self.inputText = menuPanel.addLabel(text="class document or letter grade", row = 4, column = 0, background = "light green")
        self.credits = menuPanel.addLabel(text="Credits", row =4, column = 1, background = "light green")
        self.box_7 =menuPanel.addTextField("0",row = 4, column = 1)
        self.box_8 =menuPanel.addTextField("", row=4, column = 0)
        self.GPAButton = self.addButton("Check GPA", row = 5, column = 0, command = self.checkGPA)
        self.save = self.addButton("  Save GPA", row = 6, columnspan = 2, column = 0, command = self.writeFile)
        self.listForFile=[]
        self.listforCredit=[]

    def getText(self):
        print("works")
        self.box_1Credit= self.box_1.getText()
        self.box_2Input = self.box_2.getText()
        self.box_3Credit = self.box_3.getText()
        self.box_4Input = self.box_4.getText()
        self.box_5Credit = self.box_5.getText()
        self.box_6Input = self.box_6.getText()
        self.box_7Credit = self.box_7.getText()
        self.box_8Input = self.box_8.getText()
        print(self.box_2Input)
        print(self.box_4Input)
        print(self.box_6Input)
        print(self.box_8Input)


        
        
    def checkGPA(self):
        print("GPA works")
        #Gets text from text box 
        self.getText()

        #Input one 
        if self.box_2Input=="":

            self.newPoints1 = 0

        elif self.box_2Input!="":

            self.avg_1 = 0
            if self.box_2Input == "A":
                self.avg_1+= 90
                g = Grade_Calculator(self.avg_1)
                self.newPoints1 = g.points_conversion()
            elif self.box_2Input == "B":
                self.avg_1+= 80
                g = Grade_Calculator(self.avg_1)
                self.newPoints1 = g.points_conversion()
            elif self.box_2Input == "C":
                self.avg_1+= 70
                g = Grade_Calculator(self.avg_1)
                self.newPoints1 = g.points_conversion()
            elif self.box_2Input == "D":
                self.avg_1+= 65
                g = Grade_Calculator(self.avg_1)
                self.newPoints1 = g.points_conversion()
            elif self.box_2Input == "F":
                self.avg_1+= 55
                g = Grade_Calculator(self.avg_1)
                self.newPoints1 = g.points_conversion()
            
            else:                
                

                run = Main(self.box_2Input)
                self.changeInput1 = run.findGrade()
                self.box_2.setText(self.changeInput1)
                self.newPoints1 = run.findPoints()
                print("Credits = ",self.box_1Credit)
                print("this is what we want = ",self.newPoints1)

        #Input two 
        if self.box_4Input=="":
            
            self.newPoints2 = 0

        elif self.box_4Input!="":

            self.avg_2 = 0
            if self.box_4Input == "A":
                self.avg_2+= 90
                g = Grade_Calculator(self.avg_2)
                self.newPoints2 = g.points_conversion()
                
            elif self.box_4Input == "B":
                self.avg_2+= 80
                g = Grade_Calculator(self.avg_2)
                self.newPoints2 = g.points_conversion()
                
            elif self.box_4Input == "C":
                self.avg_2+= 70
                g = Grade_Calculator(self.avg_2)
                self.newPoints2 = g.points_conversion()
                
            elif self.box_4Input == "D":
                self.avg_2+= 65
                g = Grade_Calculator(self.avg_2)
                self.newPoints2 = g.points_conversion()
                
            elif self.box_4Input == "F":
                self.avg_2+= 55
                g = Grade_Calculator(self.avg_2)
                self.newPoints2 = g.points_conversion()

 
            
            else:
                run = Main(self.box_4Input)
                self.changeInput2 = run.findGrade()
                self.box_4.setText(self.changeInput2)
                self.newPoints2 = run.findPoints()
                print("Credits = ",self.box_3Credit)
                print("this is what we want = ",self.newPoints2)

        #Input three 
        if self.box_6Input=="":
            self.newPoints3 = 0

        elif self.box_6Input!="":

            self.avg_3 = 0
            if self.box_6Input == "A":
                self.avg_3+= 90
                g = Grade_Calculator(self.avg_3)
                self.newPoints3 = g.points_conversion()
                
            elif self.box_6Input == "B":
                self.avg_3+= 80
                g = Grade_Calculator(self.avg_3)
                self.newPoints3 = g.points_conversion()
                
            elif self.box_6Input == "C":
                self.avg_3+= 70
                g = Grade_Calculator(self.avg_3)
                self.newPoints3 = g.points_conversion()
                
            elif self.box_6Input == "D":
                self.avg_3+= 65
                g = Grade_Calculator(self.avg_3)
                self.newPoints3 = g.points_conversion()
                
            elif self.box_6Input == "F":
                self.avg_3+= 55    
                g = Grade_Calculator(self.avg_3)
                self.newPoints3 = g.points_conversion()
                
            
            
            else:
                run = Main(self.box_6Input)
                self.changeInput3 = run.findGrade()
                self.box_6.setText(self.changeInput3)
                self.newPoints3 =run.findPoints()
                print("Credits = ",self.box_5Credit)
                print("this is what we want = ", self.newPoints3)

        #Input four
        if self.box_8Input=="":
            self.newPoints4 = 0
            
        elif self.box_8Input!="":

                self.avg_4 = 0
                if self.box_8Input == "A":
                    self.avg_4+= 90
                    g = Grade_Calculator(self.avg_4)
                    self.newPoints4 = g.points_conversion()
                elif self.box_8Input == "B":
                    self.avg_4+= 80
                    g = Grade_Calculator(self.avg_4)
                    self.newPoints4 = g.points_conversion()
                elif self.box_8Input == "C":
                    self.avg_4+= 70
                    g = Grade_Calculator(self.avg_4)
                    self.newPoints4 = g.points_conversion()
                elif self.box_8Input == "D":
                    self.avg_4+= 65
                    g = Grade_Calculator(self.avg_4)
                    self.newPoints4 = g.points_conversion()
                elif self.box_8Input == "F":
                    self.avg_4+= 55
                    g = Grade_Calculator(self.avg_4)
                    self.newPoints4 = g.points_conversion()
                    
            
                else:
                    run = Main(self.box_8Input)
                    self.changeInput4 = run.findGrade()
                    self.box_8.setText(self.changeInput4)
                    self.newPoints4 = run.findPoints()
                    print("Credits = ", self.box_7Credit)
                    print("this is what we want =",self.newPoints4)

        
        G = GPA_Calculator(self.box_1Credit,self.newPoints1, self.box_3Credit, self.newPoints2, self.box_5Credit, self.newPoints3, self.box_7Credit, self.newPoints4)
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
    
