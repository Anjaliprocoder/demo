#try block,except block,else block and finally blocks for handling error
#try block for testing
#except block for handle it
#else block works when there is no error find in try block
#finally block works when error is present or not
#print(x)
try:
    print("x")
except TypeError:
    print("check the variable")
except:
    print("anjali")
else:
    print("no error")
finally:
    print("completed")

#exception raise
x=-24
if x<0:
    raise Exception("negative numbers are not allowed")