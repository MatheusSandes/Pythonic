""" This code is not pythonic """

try:
    print("This is a large try")
    print ("This code is horrible!!")
    d = 10/0 # Raise ZeroDivisionError
    print ('two: ' + 2)  # Raise TypeError
    print (d)
except Exception as e:
    print (e)

finally:
    print ("I'm in finally")
