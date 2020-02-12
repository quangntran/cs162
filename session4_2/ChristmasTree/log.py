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
"""
Ensure a class only has one instance, and provide a global point of
access to it.
"""
import logging
class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class YourClass(metaclass=Singleton)
class FileLog(metaclass=Singleton):
    NAME = 'ANY'
    def __init__(self):
        # Create a custom logger
        self.logger = logging.getLogger(self.NAME)
        # Create handler
        f_handler = logging.FileHandler('file.log', mode='a')
        # Add handlers to the logger
        self.logger.addHandler(f_handler)
        # configure level
        self.logger.setLevel(logging.DEBUG)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)




#
# def main():
#     m1 = MyClass()
#     m2 = MyClass()
#     assert m1 is m2
#
#
# if __name__ == "__main__":
#     main()


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

# FileLogTest(filelogInstance = FileLog)
