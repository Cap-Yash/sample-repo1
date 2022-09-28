# import pywin
# import pywinauto
# import os

def number(num1):
    try:
        for i in range(num1):
            print (i)
    except Exception as e:
        print (f"This is exception {e}")

number("harry")