import csv
import tkinter as tk
from tkinter import *


def enterData():
  first = int(input1.get())
  second = int(input2.get())

  label1 = tk.Label(root, text=int(first + second))
  canvas.create_window(200, 230, window=label1)

# Read data from CSV file
with open('csv.csv', 'r') as file:
    reader = csv.reader(file)
    labels = next(reader) # only use the first row as labels

root = tk.Tk()
root.title("AI")

canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

for i, label in enumerate(labels):
    canvas.create_text(200,80+i*40,text=label)

#label1 = tk.Label(root, text='Input 1:')
#label1.config(font=('helvetica', 10))
#canvas.create_window(200, 80, window=label1)
#
#label2 = tk.Label(root, text='Input 2:')
#label2.config(font=('helvetica', 10))
#canvas.create_window(200, 120, window=label2)

input1 = tk.Entry(root)
canvas.create_window(200, 100, window=input1)

input2 = tk.Entry(root)
canvas.create_window(200, 140, window=input2)

button1 = tk.Button(text='Add', command=enterData)
canvas.create_window(200, 180, window=button1)

root.mainloop()