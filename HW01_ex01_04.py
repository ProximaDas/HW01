# HW01_ex01_04
# Start the Python interpreter and use it as a calculator. 
# Python's syntax for math operations is almost the same as 
# standard mathematical notation. For example, the symbols 
# +, - and / denote addition, subtraction and division, as you would expect. 
# The symbol for multiplication is *.

# If you run a 10 kilometer race in 43 minutes 30 seconds, what is your 
# average time per mile? What is your average speed in miles per hour? 
# (Hint: there are 1.61 kilometers in a mile).
# Average Speed in MPH: 8.56714499893

miles = 10/1.61
print miles
time = 43.0/60 + 30.0/3600
print time
tpm = time/miles
print 'Time per mile: ' + str(tpm)
mph = miles/time
print 'Miles per hour: ' + str(mph)