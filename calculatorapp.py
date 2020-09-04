import tkinter as tk

root = tk.Tk()
root.title("simple calculator")

e = tk.Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "Enter the number: ")

def button_click(number):
    #e.delete(0, tk.END)
    current= e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, tk.END)

def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, tk.END)

def button_sub():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, tk.END)


def button_mul():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, tk.END)


def button_div():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, tk.END)


def button_equal():
	second_number = e.get()
	e.delete(0, tk.END)

	if math == "addition" :
		e.insert(0, f_num + int(second_number))

	if math == "subtraction" :
		e.insert(0, f_num - int(second_number))

	if math == "multiplication" :
		e.insert(0, f_num * int(second_number))

	if math == "division" :
		e.insert(0, f_num / int(second_number))



    
 #define the buttons
 #put the buttons on the screen

button_1 = tk.Button(root, text = "1", padx = 40, pady = 20, command=lambda: button_click(1)).grid(row=3, column=0)
button_2 = tk.Button(root, text = "2", padx = 40, pady = 20, command=lambda: button_click(2)).grid(row=3, column=1)
button_3 = tk.Button(root, text = "3", padx = 40, pady = 20, command=lambda: button_click(3)).grid(row=3, column=2)
button_4 = tk.Button(root, text = "4", padx = 40, pady = 20, command=lambda: button_click(4)).grid(row=2, column=0)
button_5 = tk.Button(root, text = "5", padx = 40, pady = 20, command=lambda: button_click(5)).grid(row=2, column=1)
button_6 = tk.Button(root, text = "6", padx = 40, pady = 20, command=lambda: button_click(6)).grid(row=2, column=2)
button_7 = tk.Button(root, text = "7", padx = 40, pady = 20, command=lambda: button_click(7)).grid(row=1, column=0)
button_8 = tk.Button(root, text = "8", padx = 40, pady = 20, command=lambda: button_click(8)).grid(row=1, column=1)
button_9 = tk.Button(root, text = "9", padx = 40, pady = 20, command=lambda: button_click(9)).grid(row=1, column=2)
button_0 = tk.Button(root, text = "0", padx = 40, pady = 20, command=lambda: button_click(0)).grid(row=4, column=0)
button_add = tk.Button(root, text = "+", padx = 40, pady = 20, command=button_add).grid(row=5, column=0) 
button_sub = tk.Button(root, text = "-", padx = 40, pady = 20, command=button_sub).grid(row=6, column=1) 
button_mul = tk.Button(root, text = "*", padx = 41, pady = 20, command=button_mul).grid(row=6, column=0) 
button_div = tk.Button(root, text = "/", padx = 41, pady = 20, command=button_div).grid(row=6, column=2) 
button_equal = tk.Button(root, text = "=", padx = 90, pady = 20, command=button_equal).grid(row=5, column=1,columnspan=2)
button_clear = tk.Button(root, text = "clear", padx = 79 , pady = 20, command=button_clear).grid(row=4, column=1,columnspan=2)

root.mainloop()
