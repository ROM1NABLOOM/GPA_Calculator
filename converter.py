"""
Program: Converter class for final project
Author: Landon Dahl

Objective: Helps the user convert their scores into a text document.

- Creates a GUI window
- Takes input, number you got on the assignment and total number of points for assignment
- Divides the first input by the second input
- Multipys that number by 100
- puts a percentage sign at the end
"""

from breezypythongui import EasyFrame

class converter(EasyFrame):
    def __init__(self):
         EasyFrame.__init__(self, width=400, height=200, title = "Grade converter", background="pink")
         self.titletext = self.addLabel(text = "This converts your scores to percentages", row=0, sticky = "NSEW", column=0)
         mainPanel = self.addPanel(row=1, column=0, background = "pink")
         self.direction1 = mainPanel.addLabel(text = "points you got on the assignment", row=1, column=0)
         self.Input1 = mainPanel.addTextField("", row=1, column =2)
         self.direction2 = mainPanel.addLabel(text = "total number of points for the assignment", row=2, column=0)
         self.Input2 = mainPanel.addTextField("", row=2, column=2)
         self.saveas = self.addButton("Save As", row=3, column = 0, command = self.save_as)
         self.save = self.addButton("Save", row=4, column=0, command = self.convert)


    def save_as(self):
        self.keep = self.prompterBox(title = "Save as", promptString = "What do you want to call your file?")

        
        
        
    def convert(self):
        try:
            self.numerator = float(self.Input1.getText())
            self.denominator = float(self.Input2.getText())
            self.total = round((self.numerator/self.denominator)*100)
            print(self.total)
            self.written = str(self.total)
            f = open(self.keep + ".txt", 'a')
            #'a' is a new concept that I used when writing this program, the purpose is to update rather than rewrite. 
            print("File opened")
            f.writelines(self.written + "%\n")
            f.close()
            print("File clossed")
            self.Input1.setText("")
            self.Input2.setText("")
        except:
            self.messageBox(title = "ERROR",
                            message = "You need to name the file before you can save it, click on the save as button first.")
        
    
def main():
    converter().mainloop()

if __name__== "__main__":
    main()
