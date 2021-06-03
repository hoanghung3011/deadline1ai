import tkinter as tk
import tkinter.messagebox
import tkinter.font

class Example():
    def __init__(self):
        self.root = tk.Tk(className='Start Up')
        self.fontStyle = tkinter.font.Font(self.root, family='Helvetica', size=12)

        self.button = tk.Button(self.root, text='Start', command=self.get_start)
        self.button.grid(row=5, column=3, columnspan=2, ipadx=30)

        self.SPLabel1 = tk.Label(self.root, text='No. Task', font=self.fontStyle)
        self.setTrow = tk.Spinbox(self.root, font=self.fontStyle, from_=1,to=20)
        self.SPLabel1.grid(row=2, column=3, ipadx=5)
        self.setTrow.grid(row=2, column=4, ipadx=5)

        self.SPLabel2 = tk.Label(self.root, text='No. Machine', font=self.fontStyle)
        self.setMachine = tk.Spinbox(self.root, font=self.fontStyle, from_=1,to=5)
        self.SPLabel2.grid(row=3, column=3,ipadx=5)
        self.setMachine.grid(row=3, column=4,ipadx=5)
    
        self.data = {}
        self.ouputCell = []

    def get_start(self):
        self.machine = int(self.setMachine.get())
        for m in range(self.machine):
            self.ouputCell.append(tk.StringVar())

        self.newWindow = tk.Toplevel(self.root)
        self.newWindow.title('Division of Labour')
        self.Label1 = tk.Label(self.newWindow, text='Task', font=self.fontStyle)
        self.Label2 = tk.Label(self.newWindow, text='Time', font=self.fontStyle)

        self.Label1.grid(row=0, column=0, ipadx=30)
        self.Label2.grid(row=0, column=1, ipadx=30)

        self.table = []
        self.table.append([])
        self.table.append([])
        self.tcolumn = 2
        self.trow = int(self.setTrow.get())
        for x in range(self.trow):
            for y in range(self.tcolumn):
                self.table[y].append(tk.Entry(self.newWindow, width=30, font=self.fontStyle))
                self.table[y][-1].grid(row=x+1, column=y)
                self.table[y][-1].bind("<Return>", self.handleEnter)
                self.table[y][-1].bind("<Down>", self.handleDown)
                self.table[y][-1].bind("<Left>", self.handleLeft)
                self.table[y][-1].bind("<Right>", self.handleRight)
                self.table[y][-1].bind("<Up>", self.handleUp)
                #self.table[y][-1].bind('<Button-1>',self.MouseDown)

        self.button1 = tk.Button(self.newWindow,text='Divide', command=self.divide)
        self.button1.grid(row=self.trow+1, column=0, columnspan=2, rowspan=2, ipadx=50)   

        for m in range(self.machine):
            currentLabel = tk.Label(self.newWindow, width=20, font=self.fontStyle, text='Machine No. '+str(m+1))
            currentLabel.grid(row=m, column=2)
            currentEntry = tk.Entry(self.newWindow, width=30, font=self.fontStyle, textvariable=self.ouputCell[m])
            self.ouputCell.append(currentEntry)
            self.ouputCell[-1].grid(row=m, column=3)

    def divide(self):
        for i in range(self.trow):
            if self.table[0][i].get() == '' or self.table[1][i].get() == '':
                #self.error = tk.Toplevel(self.newWindow)
                ##self.error.title('Error')
                #self.LabelError = tk.Label(self.error,text='Missing value at row '+ str(i+1))
                #self.LabelError.grid(row=0,column=0, ipadx=50,ipady=20)
                tkinter.messagebox.showerror(self.newWindow, message='Missing value at row ' + str(i+1)+'!')
                self.data.clear()
                return
            if self.table[0][i].get() in self.data:
                #self.error = tk.Toplevel(self.newWindow)
                #self.error.title('Error')
                #self.LabelError = tk.Label(self.error,text='Duplicate name at row '+ str(i+1))
                #self.LabelError.grid(row=0,column=0, ipadx=50,ipady=20)
                tkinter.messagebox.showerror(self.newWindow, message='Duplicate name at row ' + str(i+1)+'!')
                self.data.clear()
                return
            if self.isDigit(self.table[1][i].get().strip()) == False:
                #self.error = tk.Toplevel(self.newWindow)
                #self.error.title('Error')
                #self.LabelError = tk.Label(self.error,text='Invalid value at row '+ str(i+1) + '.Time must be int')
                #self.LabelError.grid(row=0,column=0, ipadx=50,ipady=20)
                message = tkinter.messagebox.showerror(self.newWindow, message='Invalid value at row ' + str(i+1)+'. Time must be digit!')
                self.data.clear()
                return
            self.data[self.table[0][i].get()] = float(self.table[1][i].get())
        self.sortedData = {k: v for k,v in sorted(self.data.items(), key = lambda item: item[1]) }
        self.data.clear()
        self.getResult()
        #print (self.sortedData)

    def getResult(self):
        self.final = []
        for x in range(self.machine):
            self.final.append([])
        tmpList = list(self.sortedData)
        currentMachine = 0
        for m in range(self.trow):
            self.final[currentMachine].append(tmpList[m])
            currentMachine = (currentMachine+1)%self.machine
        
        #self.resultWindow = tk.Toplevel(self.newWindow)
        #self.resultWindow.title('Result')

        for x in range(self.machine):
            #tk.Label(self.resultWindow, text='Machine No.'+str(x+1)+":", font=self.fontStyle).grid(row=x, column=0, ipadx=30, ipady=3)
            #print(self.final[x])
            current = ', '.join(self.final[x])
            #tk.Label(self.resultWindow, text=current, font=self.fontStyle).grid(row=x, column=1, ipadx=30, ipady=3)
            #self.ouputCell[x].set('')
            self.ouputCell[x].set(current)
        
        #print(self.final)
    
    @staticmethod
    def isDigit(x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    def handleEnter(self, event):
        current = event.widget
        row = int(current.grid_info()['row'])
        column = int(current.grid_info()['column'])
        index = row-1
        index = index+1 if index+1 < self.trow else 0

        current = self.table[column][index]
        current.focus_set()
    
    def handleDown(self, event):
        current = event.widget
        row = int(current.grid_info()['row'])
        column = int(current.grid_info()['column'])
        row = row-1
        row = row+1 if row+1 < self.trow else 0

        current = self.table[column][row]
        current.focus_set()
    def handleLeft(self, event):
        current = event.widget
        row = int(current.grid_info()['row'])
        column = int(current.grid_info()['column'])
        row = row-1
        column = column-1 if column-1 >= 0 else 1

        current = self.table[column][row]
        current.focus_set()
    
    def handleUp(self, event):
        current = event.widget
        row = int(current.grid_info()['row'])
        column = int(current.grid_info()['column'])
        row = row-1
        row = row-1 if row-1 >=0  else self.trow-1

        current = self.table[column][row]
        current.focus_set()

    def handleRight(self, event):
        current = event.widget
        row = int(current.grid_info()['row'])
        column = int(current.grid_info()['column'])
        row = row-1
        column = column+1 if column+1 < self.tcolumn else 0

        current = self.table[column][row]
        current.focus_set()      

if __name__.endswith('__main__'):
    EXAMPLE = Example()
    #example.get_table()
    tk.mainloop()


#dt = pd.read_csv('data.csv')
 
#print(dt['Task name'][1])
