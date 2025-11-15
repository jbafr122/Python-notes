#   1.  Write an assert statement that triggers an AssertionError if the variable spam is an integer less than 10.

# spam = 1
# assert spam >= 10

#   2.  Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different. (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)

#bacon = "hello"
#eggs = "Hello"
#assert bacon.lower() != eggs.lower()

#   3.  Write an assert statement that always triggers an AssertionError.

#assert False

#   4.  What two lines must your program have to be able to call logging.debug()?

#import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

#   5.  What two lines must your program have to make logging.debug() send a logging message to a file named programLog.txt?

#import logging
#logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,format=' %(asctime)s -  %(levelname)s -  %(message)s')

#   6.  What are the five logging levels?

#CRITICAL, ERROR, WARNING, INFO, DEBUG

#   7.  What line of code can you add to disable all logging messages in your program?

#logging.disable()

#   8.  Why is using logging messages better than using print() to display the same message?

#Because when you are done logging with print statements you will have to remove each one individually. Opposed to using logging which can remove each logging message with one command (logging.disable()).

#   9.  What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?

#Step Over - if the code in the next line is a function call, the debugger will rush through the code in the function
#Step In - Execute each line one by one even if the next line is a function call
#Step Out - Will execute lines at full speed until it returns from the current function

# 10.  After you click Continue, when will the debugger stop?

#Until the debugger reaches a breakpoint

# 11.  What is a breakpoint?

#A stopping point manually set up in the debugger to halt the code




