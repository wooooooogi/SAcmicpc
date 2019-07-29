# -*- coding: utf-8 -*-

#   Coded by Sungwook Kim
#   2019-07-29
#   IDE: Spyder 3

#   Use "map" function to get input value

#   gather two input values
print("Write two variables to sum.(variables are seperate from space")
input1, input2 = map(int, input().split())
#   map function: map(arg1, arg2)
#   arg1: function or type of variable
#   arg2: input I want to map
#   input function: get input from console window (or command window)
#   split function: split string (if nothing in "()", split by space)

#   print +sum
print("Result: {sum}".format(sum=(input1 + input2)))
#   formatting: use variable in "strings"

#   similar to 1001.py