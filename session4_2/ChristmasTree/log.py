'''
Write your own version of Filelog here!

The Filelog Class opens up a file and add log within. The
previous log, if any, should not be removed. Also, there
can be only one Filelog object at any time of this
program - that is, a second Filelog object will lead to
exact the same instance in the memory as the first one. 

At least three methods are required:
info(msg), warning(msg), and error(msg).
'''
#class FileLog():

'''
The following function serves as a simple test to check
whether the id of multiple instances of Filelog remain
the same.
'''

def FileLogTest(filelogInstance = None):
    if filelogInstance == None:
        raise ValueError('Filelog Instance doesn\'t exist')

    log = filelogInstance()
    log.warning('One CS162 Filelog instance found with id ' + str(id(log)))
    log2 = filelogInstance()
    log2.warning('Another CS162 Filelog instance Found with id ' + str(id(log2)))

#FileLogTest(filelogInstance = FileLog)
