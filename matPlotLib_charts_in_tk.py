'''MatPlotLib Charts in tkinter'''

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title("Matplotlib and Numpy Module: Charts in tkinter")
root.geometry("400x200")

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

button = Button(root, text="Graph it", command=graph).pack()

root.mainloop()
