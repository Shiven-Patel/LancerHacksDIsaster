import time
import sys
from dictionary import disasters
from termcolor import colored
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import os
import numpy
import matplotlib.pyplot as plt


tor_xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=np.float64)
tor_ys = np.array([16, 11, 138, 80, 259, 106, 126, 151, 27, 146, 20, 222],
                  dtype=np.float64)

fir_xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=np.float64)
fir_ys = np.array(
    [1600, 1386, 7532, 7075, 7242, 5791, 7024, 5239, 3202, 2275, 5984, 4383],
    dtype=np.float64)

cyc_xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=np.float64)
cyc_ys = np.array([14, 11, 9, 9, 9, 10, 7, 18, 19, 10, 11, 9],
                  dtype=np.float64)

hur_xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=np.float64)
hur_ys = np.array([0, 0, 0, 7, 8, 7, 9, 8, 0, 0, 0, 0], dtype=np.float64)

ear_xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], dtype=np.float64)
ear_ys = np.array([13, 16, 20, 18, 12, 4, 11, 17, 10, 11, 13, 14],
                  dtype=np.float64)


def best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
         ((mean(xs) * mean(xs)) - mean(xs * xs)))
    b = mean(ys) - m * mean(xs)
    return m, b


def slow_print(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)
    print()


def graph(xs, ys):
  mymodel = numpy.poly1d(numpy.polyfit(xs, ys, 3))
  myline = numpy.linspace(1, 12, 100)
  plt.scatter(xs, ys)
  plt.plot(myline, mymodel(myline))
  plt.show()

def main():
    slow_print("Welcome to our natural disaster service.")
    print()
    user = input("Which natural disaster do you need assistance with? ")
    letters = user[0:3].lstrip()
    text = colored(disasters[letters], "red")
    print()
    slow_print(text)
    time.sleep(2)
    print()
    if letters.lower() == "tor":
        slow_print("Look at the graph above for information^^")
        slow_print(
            "X axis: Months in terms of numbers, Y axis: Number of Occurences // to continue click x on the top right corner of the graph")
        graph(tor_xs, tor_ys)
    elif letters.lower() == "fir":
        slow_print("Look at the graph above for information^^")
        slow_print(
            "X axis: Months in terms of numbers, Y axis: Number of Occurences // to continue click x on the top right corner of the graph")
        graph(fir_xs, fir_ys)
    elif letters.lower() == "cyc":
        slow_print("Look at the graph above for information^^")
        slow_print(
            "X axis: Months in terms of numbers, Y axis: Number of Occurences // to continue click x on the top right corner of the graph")
        graph(cyc_xs, cyc_ys)
    elif letters.lower() == "hur":
        slow_print("Look at the graph above for information^^")
        slow_print(
            "X axis: Months in terms of numbers, Y axis: Number of Occurences // to continue click x on the top right corner of the graph")
        graph(hur_xs, hur_ys)
        addition()
    elif letters.lower() == "ear":
        slow_print("Look at the graph above for information^^")
        slow_print(
            "X axis: Months in terms of numbers, Y axis: Number of Occurences // to continue click x on the top right corner of the graph")
        graph(ear_xs, ear_ys)
    elif letters.lower() not in "jf":
      slow_print("Sorry, we don't have that disaster in our database.")
      c = input("Would you like to add a new disaster to the database? ")
      if c[0]=="y":
        name = input("What is the name of the disaster? ")
        content = input("What should people do in this situation? ")
        disasters[name] = content
        slow_print("Your disaster has been added to the database.")
        time.sleep(5)
        os.system("clear")
    b = input("Do you need assistance on another natural disaster? ")
    if (b[0] == "y"):
      os.system("clear")
      main()
    if b[0] == "n":
      slow_print("Thank you for using our service. Always thrive to stay safe.")
      time.sleep(5)
      os.system("clear")
    else:
      slow_print("Sorry, that wasn't a valid input. Try again.")
      time.sleep(5)
      os.system("clear")
      main()

main()