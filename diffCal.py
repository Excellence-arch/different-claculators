from tkinter import *
import math
import tkinter.ttk as ttk

class main():
    def __init__(self):
        self.root = Tk()
        self.root.config(bg='black')
        self.root.title('Calculator')
        self.root.geometry('400x450')
        self.root.iconbitmap('icons8_Calculator.ico')
        self.mainFrame = Frame(self.root, bg='black')
        self.mainFrame.pack(pady=5)
        self.menubar = Menu(self.root, tearoff=0)
        self.menu = Menu(self.menubar, tearoff=0)
        self.menu.add_command(label='Simple Calculator', command=self.simple)
        self.menu.add_command(label='Scientific Calculator', command=self.scientific, accelerator='Ctrl + s')
        self.menu.add_command(label='temperature Calculator', command=self.temperature)
        self.menubar.add_cascade(label='Menu', menu=self.menu)
        self.root.config(menu=self.menubar)
        self.simple()
        self.root.mainloop()
    
    
    def simple(self):
        self.mainFrame.destroy()
        self.mainFrame= Frame(self.root, bg='black')
        self.mainFrame.pack()
        self.frame1 = Frame(self.mainFrame, bg='black')
        self.frame1.pack()
        self.screen = Entry(self.frame1, width=57, borderwidth=0.6, bg='black', fg='white', font=("Courier", 40))
        self.screen.insert(0, '')
        # self.screen.config(font=("Courier", 30))
        self.screen.pack(side='left', pady=7)
        
        self.frame2 = Frame(self.mainFrame, bg='black')
        self.frame2.pack(pady=5)
        Button(self.frame2, width=11, bg='spring green', text="7", command=lambda: self.write("7")).pack(side='left', padx=5, ipady=17)
        Button(self.frame2, width=11, bg='spring green', text="8", command=lambda: self.write("8")).pack(side='left', padx=5, ipady=17)
        Button(self.frame2, width=11, bg='spring green', text="9", command=lambda: self.write("9")).pack(side='left', padx=5, ipady=17)
        Button(self.frame2, width=11, bg='spring green', text="+", command=lambda: self.write('+')).pack(side='left', padx=5, ipady=17)
        
        self.frame3 = Frame(self.mainFrame, bg='black')
        self.frame3.pack(pady=3)
        Button(self.frame3, bg='spring green', width=11, text="4", command=lambda: self.write("4")).pack(side='left', padx=5, ipady=17)
        Button(self.frame3, bg='spring green', width=11, text="5", command=lambda: self.write("5")).pack(side='left', padx=5, ipady=17)
        Button(self.frame3, bg='spring green', width=11, text="6", command=lambda: self.write("6")).pack(side='left', padx=5, ipady=17)
        Button(self.frame3, bg='spring green', width=11, text="-", command=lambda:self.write('-')).pack(side='left', padx=5, ipady=17)
        
        self.frame4 = Frame(self.mainFrame, bg='black')
        self.frame4.pack(pady=5)
        Button(self.frame4, bg='spring green', width=11, text="1", command=lambda: self.write("1")).pack(side='left', padx=5, ipady=17)
        Button(self.frame4, bg='spring green', width=11, text="2", command=lambda: self.write("2")).pack(side='left', padx=5, ipady=17)
        Button(self.frame4, bg='spring green', width=11, text="3", command=lambda: self.write("3")).pack(side='left', padx=5, ipady=17)
        Button(self.frame4, bg='spring green', width=11, text="x", command=lambda:self.write('*')).pack(side='left', padx=5, ipady=17)
        
        self.frame5 = Frame(self.mainFrame, bg='black')
        self.frame5.pack(pady=5)
        Button(self.frame5, bg='orange red', width=11, text="C", command=self.clear).pack(side='left', padx=5, ipady=17)
        Button(self.frame5, bg='spring green', width=11, text="0", command=lambda: self.write("0")).pack(side='left', padx=5, ipady=17)
        Button(self.frame5, bg='spring green', width=11, text=".", command=lambda: self.write(".")).pack(side='left', padx=5, ipady=17)
        Button(self.frame5, bg='spring green', width=11, text="/", command=lambda:self.write('/')).pack(side='left', padx=5, ipady=17)
        
        self.frame6 = Frame(self.mainFrame, bg='black')
        self.frame6.pack(pady=5)
        self.state = False
        self.one = False
        Button(self.frame6, width=35, bg='grey50', fg='snow', text="=", command=self.equal).pack(side='left', padx=5, ipady=13)
        self.onOff = Button(self.frame6, width=11, bg='red', fg='white', text="On", command=self.changeState)
        self.onOff.pack(padx=5, ipady=13)
    
    def write(self, num):
        if not self.state:
            return
        else:
            if not self.one:
                self.screen.delete(0, 1)
                self.screen.insert(0, num)
                self.one = True
            else:
                self.nums = self.screen.get()
                self.screen.delete(0, len(self.nums))
                self.screen.insert(0, self.nums+num)
    
    def equal(self):
        if not self.state:
            return
        else:
            self.var = self.screen.get()
            self.screen.delete(0, len(self.var))
            try:
                self.screen.insert(0, eval(self.var))
            except:
                self.screen.insert(0, 'Maths Error')
    
    def clear(self):
        if not self.state:
            return
        else:
            self.var = self.screen.get()
            self.screen.delete(0, len(self.var))
            self.screen.insert(0, 0)
            self.one = False
    
    def changeState(self):
        if not self.state:
            self.onOff.config(text='Off')
            self.state = True
            self.var = self.screen.get()
            self.screen.delete(0, len(self.var))
            self.screen.insert(0, 0)
            self.one = False
        else:
            self.onOff.config(text='On')
            self.state =False
            self.var = self.screen.get()
            self.screen.delete(0, len(self.var))
            self.screen.insert(0, '')
    
    def scientific(self):
        self.mainFrame.destroy()
        self.mainFrame = Frame(self.root, bg='black')
        self.mainFrame.pack()
        
        self.newFrame011 = Frame(self.mainFrame, bg='black')
        self.newFrame011.pack()
        
        self.new_screen = Entry(self.newFrame011, width=65, font=('Courier', 20))
        self.new_screen.insert(0, '')
        self.new_screen.pack(pady=1)
        
        self.newFrame012 = Frame(self.mainFrame, bg='black')
        self.newFrame012.pack(pady=1)
        Button(self.newFrame012, width=10,pady=15, text='x^2', command=lambda: self.sciAdd('**2')).grid(row=0, column=0)
        Button(self.newFrame012, width=10,pady=15, text='x^y', command=lambda: self.sciAdd('**')).grid(row=0, column=1)
        Button(self.newFrame012, width=10,pady=15, text='sin', command=lambda: self.angles('sin')).grid(row=0, column=2)
        Button(self.newFrame012, width=10,pady=15, text='cos', command=lambda: self.angles('cos')).grid(row=0, column=3)
        Button(self.newFrame012, width=10,pady=15, text='tan', command=lambda: self.angles('tan')).grid(row=0, column=4)
        
        
        
        self.newFrame013 = Frame(self.mainFrame, bg='black')
        self.newFrame013.pack(pady=1)
        Button(self.newFrame013, width=10,pady=15, text='sqrt', command=self.sqrt).grid(row=0, column=0)
        Button(self.newFrame013, width=10,pady=15, text='10^x', command=self.ten).grid(row=0, column=1)
        Button(self.newFrame013, width=10,pady=15, text='log', command=self.log).grid(row=0, column=2)
        Button(self.newFrame013, width=10,pady=15, text='Exp', command=lambda: self.sciAdd('-')).grid(row=0, column=3)
        Button(self.newFrame013, width=10,pady=15, text='Mod', command=lambda: self.sciAdd('%')).grid(row=0, column=4)
        
        
        self.newFrame014 = Frame(self.mainFrame, bg='black')
        self.newFrame014.pack(pady=1)
        Button(self.newFrame014, width=10,pady=15, text='~', command=self.change).grid(row=0, column=0)
        Button(self.newFrame014, width=10,pady=15, text='CE', command=self.clean).grid(row=0, column=1)
        Button(self.newFrame014, width=10,pady=15, text='C', command=self.clean).grid(row=0, column=2)
        Button(self.newFrame014, width=10,pady=15, text='Del', command=self.deletes).grid(row=0, column=3)
        Button(self.newFrame014, width=10,pady=15, text='/', command=lambda: self.sciAdd('/')).grid(row=0, column=4)
        
        self.newFrame015 = Frame(self.mainFrame, bg='black')
        self.newFrame015.pack(pady=1)
        Button(self.newFrame015, width=10,pady=15, text='Pi', command=self.pi).grid(row=0, column=0)
        Button(self.newFrame015, width=10,pady=15, text='7', command=lambda: self.sciAdd('7')).grid(row=0, column=1)
        Button(self.newFrame015, width=10,pady=15, text='8', command=lambda: self.sciAdd('8')).grid(row=0, column=2)
        Button(self.newFrame015, width=10,pady=15, text='9', command=lambda: self.sciAdd('9')).grid(row=0, column=3)
        Button(self.newFrame015, width=10,pady=15, text='x', command=lambda: self.sciAdd('*')).grid(row=0, column=4)
        
        self.newFrame016 = Frame(self.mainFrame, bg='black')
        self.newFrame016.pack(pady=1)
        Button(self.newFrame016, width=10,pady=15, text='n!', command=self.permut).grid(row=0, column=0)
        Button(self.newFrame016, width=10,pady=15, text='4', command=lambda: self.sciAdd('4')).grid(row=0, column=1)
        Button(self.newFrame016, width=10,pady=15, text='5', command=lambda: self.sciAdd('5')).grid(row=0, column=2)
        Button(self.newFrame016, width=10,pady=15, text='6', command=lambda: self.sciAdd('6')).grid(row=0, column=3)
        Button(self.newFrame016, width=10,pady=15, text='-', command=lambda: self.sciAdd('-')).grid(row=0, column=4)
        
        self.newFrame017 = Frame(self.mainFrame, bg='black')
        self.newFrame017.pack(pady=1)
        Button(self.newFrame017, width=10,pady=15, text='+-', command=lambda: self.sciAdd('-')).grid(row=0, column=0)
        Button(self.newFrame017, width=10,pady=15, text='1', command=lambda: self.sciAdd('1')).grid(row=0, column=1)
        Button(self.newFrame017, width=10,pady=15, text='2', command=lambda: self.sciAdd('2')).grid(row=0, column=2)
        Button(self.newFrame017, width=10,pady=15, text='3', command=lambda: self.sciAdd('3')).grid(row=0, column=3)
        Button(self.newFrame017, width=10,pady=15, text='+', command=lambda: self.sciAdd('+')).grid(row=0, column=4)
        
        self.newFrame018 = Frame(self.mainFrame, bg='black')
        self.newFrame018.pack(pady=1)
        Button(self.newFrame018, width=10,pady=15, text='(', command=lambda: self.sciAdd('(')).grid(row=0, column=0)
        Button(self.newFrame018, width=10,pady=15, text=')', command=lambda: self.sciAdd(')')).grid(row=0, column=1)
        Button(self.newFrame018, width=10,pady=15, text='0', command=lambda: self.sciAdd('0')).grid(row=0, column=2)
        Button(self.newFrame018, width=10,pady=15, text='.', command=lambda: self.sciAdd('.')).grid(row=0, column=3)
        Button(self.newFrame018, width=10,pady=15, text='=', command=self.simpleNums).grid(row=0, column=4)
    
    
    
    def deletes(self):
        self.onScreen = self.new_screen.get()
        self.new_screen.delete(0, len(self.new_screen.get()))
        self.new_screen.insert(0, self.onScreen[:-1])
    
    def log(self):
        self.onScreen = int(self.new_screen.get())
        self.new_screen.delete(0, len(self.new_screen.get()))
        self.new_screen.insert(0, math.log(self.onScreen))
    
    def ten(self):
        self.onScreen = int(self.new_screen.get())
        self.new_screen.delete(0, len(self.new_screen.get()))
        self.new_screen.insert(0, 10**int(self.onScreen))
    
    def sqrt(self):
        self.onScreen = int(self.new_screen.get())
        self.new_screen.delete(0, len(self.new_screen.get()))
        self.new_screen.insert(0, math.sqrt(self.onScreen))
    
    def permut(self):
        self.onScreen = int(self.new_screen.get())
        i = 1
        b = 1
        while i <= self.onScreen:
            b *= i
            i += 1
        self.new_screen.delete(0, self.onScreen)
        self.new_screen.insert(0, b)
    
    def clean(self):
        self.new_screen.delete(0, len(self.new_screen.get()))
    
    def angles(self, ang):
        self.ang = ang
        self.onScreen = self.new_screen.get()
        self.new_screen.delete(0, len(self.onScreen))
        if self.ang == 'sin':
            self.new_screen.insert(0, math.sin(float(self.onScreen)))
        elif self.ang == 'cos':
            self.new_screen.insert(0, math.cos(float(self.onScreen)))
        elif self.ang == 'tan':
            self.new_screen.insert(0, math.tan(float(self.onScreen)))
    
    def change(self):
        return
    
    def pi(self):
        self.onScreen = self.new_screen.get()
        if self.onScreen != '':
            self.new_screen.delete(0, len(self.onScreen))
            self.new_screen.insert(0, self.onScreen + str(math.pi))
        else:
            self.new_screen.insert(0, math.pi)
    
    
    def sciAdd(self, user):
        self.user = user
        self.onScreen = self.new_screen.get()
        if self.onScreen != '':
            self.new_screen.delete(0, len(self.onScreen))
            self.new_screen.insert(0, self.onScreen + self.user)
        else:
            self.new_screen.insert(0, self.user)
    
    def simpleNums(self):
        self.onScreen = self.new_screen.get()
        self.new_screen.delete(0, len(self.onScreen))
        self.new_screen.insert(0, eval(self.onScreen))
    
    def temperature(self):
        self.mainFrame.destroy()
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()
        self.val = StringVar()
        
        self.screen1 = Entry(self.mainFrame)
        self.screen1.pack()
        self.newFrame021 = Frame(self.mainFrame)
        self.newFrame021.pack()
        self.main = ttk.Combobox(self.newFrame021, value=('Kelvin', 'Celcius', 'Farenheit'), textvariable=self.val)
        self.main.set('Celcius')
        self.main.pack()
        
        self.newFrame022 = Frame(self.mainFrame)
        self.newFrame022.pack()
        Button(self.newFrame022, text='9', command=lambda: self.keys('9')).pack(side='left')
        Button(self.newFrame022, text='8', command=lambda: self.keys('8')).pack(side='left')
        Button(self.newFrame022, text='7', command=lambda: self.keys('7')).pack(side='left')

        self.newFrame024 = Frame(self.mainFrame)
        self.newFrame024.pack()
        Button(self.newFrame024, text='6', command=lambda: self.keys('6')).pack(side='left')
        Button(self.newFrame024, text='5', command=lambda: self.keys('5')).pack(side='left')
        Button(self.newFrame024, text='4', command=lambda: self.keys('4')).pack(side='left')


        self.newFrame025 = Frame(self.mainFrame)
        self.newFrame025.pack()
        Button(self.newFrame025, text='3', command=lambda: self.keys('3')).pack(side='left')
        Button(self.newFrame025, text='2', command=lambda: self.keys('2')).pack(side='left')
        Button(self.newFrame025, text='1', command=lambda: self.keys('1')).pack(side='left')

        self.newFrame026 = Frame(self.mainFrame)
        self.newFrame026.pack()
        Button(self.newFrame026, text='0', command=lambda: self.keys('0')).pack(side='left')
        Button(self.newFrame026, text='Clear', command=self.clear).pack()


        self.screen2 = Entry(self.mainFrame)
        self.screen2.pack()
        self.newFrame023 = Frame(self.mainFrame)
        self.newFrame023.pack()
        items = ['Kelvin', 'Celcius', 'Farenheit']
        self.main1 = ttk.Combobox(self.newFrame023, value=items)
        self.main1.set('Kelvin')
        self.main1.pack()

    def clear(self):
    	self.screen1.delete(0, END)
    	self.screen2.delete(0, END)
    
    def keys(self, num):
    	self.onScreen = self.screen1.get()
    	self.screen1.delete(0, len(self.onScreen))
    	self.screen1.insert(0, self.onScreen + num)
    	if self.main.get() == 'Kelvin' and self.main1.get() == 'Celcius':
    		self.newVal = self.screen1.get()
    		self.celcius(self.newVal)
    	elif self.main.get() == 'Celcius' and self.main1.get() == 'Kelvin':
    		self.newVal = self.screen1.get()
    		self.kel(self.newVal)
    	elif self.main.get() == 'Farenheit' and self.main1.get() == 'Celcius':
    		self.newVal = self.screen1.get()
    		self.far(self.newVal)
    	elif self.main.get() == 'Farenheit' and self.main1.get() == 'Kelvin':
    		self.newVal = self.screen1.get()
    		self.farKel(self.newVal)
    	elif self.main.get() == 'Celcius' and self.main1.get() == 'Farenheit':
    		self.newVal = self.screen1.get()
    		self.celFar(self.newVal)
    	elif self.main.get() == 'Kelvin' and self.main1.get() == 'Farenheit':
    		self.newVal = self.screen1.get()
    		self.kelFar(self.newVal)
    	else:
    		print('Try Again')

    def kelFar(self, kel):
        self.screen2.delete(0, END)
        self.screen2.insert(0, (float(kel - 273.15) * 9/5) + 32)

    def celFar(self, far):
        self.screen2.delete(0, END)
        self.screen2.insert(0, (float(cels) * 9/5) + 32.0)

    def farKel(self, kel):
    	self.screen2.delete(0, END)
    	self.screen2.insert(0, (float(kel) - 32) * (5/9) + 273.15)

    def far(self, cel):
    	self.screen2.delete(0, END)
    	self.screen2.insert(0, (float(cel)-32)*(5/9))

    def kel(self, cel):
    	self.screen2.delete(0, END)
    	self.screen2.insert(0, (float(cel)-273))

    def celcius(self, kel):
    	self.screen2.delete(0, END)
    	self.screen2.insert(0, (float(kel)-273))

me = main()