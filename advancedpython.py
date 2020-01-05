from string import Template
import itertools
import collections
from collections import defaultdict
from collections import Counter
from enum import Enum, unique, auto
import logging
def stringsandbytes():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s= 'This is a string'
    print(s)
#   Cannot add a byte and a string
    # print(b+s) #not possible
    # Decode the byte to ascii using decode
    s2 = b.decode('utf-8')
    print(s2)
    # Now you can combine the s1 with s2    
    print(s+s2)
    # similary you can encode string
    b2 = s.encode('utf-8')
    print(b+b2)
    """  Inshort you need to properly encode and decode bytes and string
    before playing around with them """

    b3 = s.encode('utf-32')
    print(b3)
def stringformating():
    # using format() function to format a string
    str = "you are testing formating {0} {1}".format("Jerrin", "Francis")
    print(str)
    # using template string
    templ = Template("You are learning template string technique ${FirstName} ${LastName}")
    str2 = templ.substitute(FirstName="Jerrin", LastName="Francis")
    print(str2)
    # Using dictionary with substitute
    data = {
        "FirstName" : "Jerrin",
        "LastName" : "Francis"
    }
    str3 = templ.substitute(data)
    print(str3)
    # Reasons to use templates over foramt 
    # Format is ofcourse very powerful hence potential security concerns
    # and for  simple substitution it is better to use substitute.
    # Again for simple substitute it is more readable
def anyallminmaxsum():
    # Advantages save time and performance
    # any() and all()
    list1 = [1, 2, 3, 0, 5, 6]
    # any will return true if any of the sequence values are true
    print(any(list1))
    # all will return true only if all values are true
    print(all(list1))
    # min and max will return minimum and maximum values in a sequence
    print(f"min: {min(list1)}")
    print(f"max: {max(list1)}")
    # Use sum() to sum up all of the values in a sequence
    print(f"sum: {sum(list1)}")
def iterationtesting():
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    # iterate using a function and a sentinel
    with open("learniteration.txt") as fp:
        for line in iter(fp.readline, ''):
            print(line)
    # using regular iteration over the days
    for m in range(len(days)):
        print(m+1, days[m])
    # usage of enumerate : reduces code and gives a counter
    for i,m in enumerate(days, start=1):
        print(i, m)
    # use zip to combine sequences
    for i,m in enumerate(zip(days, daysFr), start=1):
        print(i, m[0], "=", m[1], "in French")
    # incase if seqeunce length is different, the zip function terminates
    # at the shortest sequence is exhausted
    daysFr1 = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven"]
    for i,m in enumerate(zip(days, daysFr1), start=1):
        print(i, m[0], "=", m[1], "in French")
def filterEven(x):
    if x % 2 == 0:
        return False
    else:
        return True
def filterLower(x):
    if x.isupper(): 
        return False
    else:
        return True
def squareFunc(x):
    return x ** 2
def toGrade(x):
    if (x >= 90 ):
        return "A"
    elif(x>=80 and x<=90):
        return "B"
    elif(x>=70 and x<=80):
        return "C"
    elif(x>=65 and x<=70):
        return "D"
    else:
        return "F"
def transformation():
    # sample sequence to operate on 
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)
    # filter 
    odds = tuple(filter(filterEven, nums))
    print(odds)
    # filetr on charcters
    lowers = list(filter(filterLower, chars))
    print(lowers)
    #use map function to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(squares)
    # use sorted and map to change numbers to grade
    print(grades)
    grades = sorted(grades)
    print(grades)
    letters = list(map(toGrade, grades))
    print(letters)
def testFunction(x):
    return x < 40
def itertoolLearn():
    # Do not use list, tuple etc with infinite iterator
    # cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    # count iterator ( start and skip)
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    # Accumulate: creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals)
    # here accumulate is not an infinite iterator hence list can be used
    print(list(acc))
    # we can custom function for accumulation
    acc1 = itertools.accumulate(vals, max)
    print(list(acc1))
    # chain can be used to connect sequence together
    x = itertools.chain("ABCD", "1234")
    print(list(x))
    # dropwhile and takewhile will return values until certain
    # condition is met that stops them 
    # dropwhile will drop values while the testFunction returns true
    # and then it will start returning every value after that
    # takewhile returns value while testFunction return true
    print(list(itertools.dropwhile(testFunction, vals))) 
    print(list(itertools.takewhile(testFunction, vals))) 
def documentation(arg1, arg2=None):
    """documentation(arg1, arg2=None) --> testing documentations
    Parameters
    arg1 : the first arg
    arg2 : second arg
    It is always good to write documentation strings for
    functions classes and modules. To get documentation print(map.__doc__)
    it works for classes and modules for eg import collections
    print(collections.__doc__)
    Best Practices
    ---------------
    Always enclose docstrings in triple quotes
    even if it is only one line

    First line should be summary sentence of functionality

    Modules:List important classes, functions, exceptions

    classes: List important methods

    Functions: List parameters and explain each, one per line
    if there is a return value, then list it otherwise omit it
    if function raises exceptions list it

    For more best practice check out PEP 257
    """

    print(arg1, arg2)
def variablearguments(*args):
    """variablearguments(*numbers)--> learning variable arguments 
    the variable arguments must be the last of parameters
    like def log_message(messageType, msg, *params)

    Downside: if you want to add a new positional parameter
    all the callers need to adjust f
    for eg if i change addition(base, *numbers)
    """
    result = 0
    for arg in args:
        result += arg
    return result
def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9

def learnLambdaFunc():
    """learnLambdaFunc() --> learn about lambda functions
    small anonymous functions
    Can be passed as arguments where you need a function
    Typically used in place just when needed
    Defined as :
    lambda (parameters) : (expression)
    """
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]
    print(list(map(FahrenheitToCelsisus, ftemps)))
    print(list(map(CelsisusToFahrenheit, ctemps)))
    # acheive same using lambda
    print(list(map(lambda t: (t-32) * 5/9, ftemps)))
    print(list(map(lambda t: (t * 9/5) + 32 , ctemps)))
# use keyword-only arguments to help ensure code clarity
def myKeyWordOnly(arg1, arg2, *, suppressExceptions=False):
    print(arg1, arg2, suppressExceptions)
def keywordArgumentsOnly():
    """keywordArguments() --> learn about keyword only arguments
    def myFunction(arg1, arg2, arg3="foo")
    myFunction(1, 2, arg3="bar")
    sometimes we require the caller specify the keyword arguments
    using keyword only, so the significance of parameter is 
    understood
    then define seperate your positional arguments from keyword only by *
    def criticalFunc(arg1, suppressExec=False)
    def criticalFunc(arg1, *, suppressExec=False)
    """
    # try to call the function without the keyword
    # myKeyWordOnly(1, 2, True)
    # myKeyWordOnly() takes 2 positional arguments but 3 were given
    myKeyWordOnly(1, 2, suppressExceptions=True)
def namedTuple():
    """
    learn namedTuples
    import collections module
    it becomes easy to access the columns by names

    """
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(20, 30)
    print(p1, p2)
    print(p1.x, p2.x)
    # use replace
    p1 = p1._replace(x=100)
    print(p1)
def learndefdict():
    """
    from collections import defaultdict
    Downsides:
    Any key that you have not explicitly added to the dictionary
    will be assigned a default value by the factory function
    so it might not be probably right collections to use in case you want to check 
    not added keys
    """
    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']
    # use a dictionary to count each element
    # fruitCounter = {}
    # use in default dict
    # the int is called factory function so that it initialized
    # to that object
    # you can have custom factory
    # fruitCounter = defaultdict(int)
    fruitCounter = defaultdict(lambda : 100)

    for fruit in fruits:
        # fruitCounter[fruit] += 1 # just this statement alone will result in error as it does not exist
        # if fruit in fruitCounter.keys():
        #     fruitCounter[fruit] += 1
        # else: 
        #     fruitCounter[fruit] = 1
        # with default dict we can just have below line
        fruitCounter[fruit] += 1 

    
    for (k, v) in fruitCounter.items():
        print(f'{k} : {str(v)}')

def learnCounter():
    """
    learn counter 
    from collections import counter

    """
     # list of students in class 1
    class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah"
              "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]
    # Create a Counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)
    # How many students in class 1 named James?
    print(c1['James'])
    # How many students are in class 1?
    print(sum(c1.values()))
    # Combine the two classes
    c1.update(c2)
    print(sum(c1.values()), "students in class 1 and 2")
    #find most common name in two classes
    # top 3 names
    print(c1.most_common(3))
    # Seperate classes
    c1.subtract(c2)
    print(c1.most_common(3))
    # find common between 2 classes
    print(c1 & c2)
@unique
class Fruit(Enum):
    """
    from enum import Enum is done to get enumeration class
    cannot have duplicate names for eg APPLE = 6 along with 1
    error: Attempted to reuse key
    But can have duplicate values.
    To prevent unique values you can have unique decorators
    from enum import unique

    If you dont care what the value is you can auto assign using
    auto code
    from enum import auto
    """
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()
    # APPLE = 6 this will be duplicate key error
    # CHERRY = 1 #again error if unique decorator is used

def learnEnum():
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))
    # enums have both name and value
    print(Fruit.APPLE.name, Fruit.APPLE.value)
    # from auto
    print(Fruit.PEAR.value)
    # enums are hashable and can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "Testing Enum as hashable keys"
    print(myFruits[Fruit.BANANA])

class Person():
    def __init__(self):
        self.fname = 'Jerrin'
        self.lname = 'Francis'
        self.age = 10
    def __repr__(self):
        return f'<Person Class fname:{self.fname} lname: {self.lname} age: {self.age}'
    def __str__(self):
        return f'Person ({self.fname} {self.lname} is {self.age})'
    def __bytes__(self):
        val = "Person:{0}:{1}:{2}".format(self.fname,
        self.lname, self.age)
        return bytes(val.encode('utf-8'))
def learnStringReprOfObjects():
    cls1 = Person()
    # without overridding the string repr
    print(str(cls1))
    print(repr(cls1))
    print(f'Formatted: {cls1}')
    print(bytes(cls1))
class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100
    def __getattr__(self, attr):
        if attr == "rgbcolor":
            return (self.red, self.green, self.blue)
        elif attr == "hexcolor":
            return "#{0:02x}{1:02x}{2:02x}".format(
                self.red, self.green,self.blue
                )
        else:
            raise AttributeError
    def __setattr__(self, attr, val):
        if attr == "rgbcolor":
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            # make sure to have this 
            super().__setattr__(attr, val)
    # use dir to list the available properties
    def __dir__(self):
        return ("red","green", "blue","rgbolor", "hexcolor")

def learnComputedAttr():
    cls1 = myColor()
    # print a computed attribute
    print(cls1.rgbcolor)
    print(cls1.hexcolor)
    # set attribute
    cls1.rgbcolor = (20, 40, 100)
    print(cls1.rgbcolor)
    print(cls1.hexcolor)
    # regular attribute
    print(cls1.red)
    # check dir functionality
    print(dir(cls1))
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'<Point x:{self.x}, y:{self.y}>'
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
def learnObjectOps():
    p1 = Point(10, 20)
    p2 = Point(20, 30)
    print(p1, p2)
    # Add two points
    # this will result in error of __add__ is not implemented

    p3 = p1 + p2
    print(p3)

    p4 = p3 - p2
    print(p4)

    p1 += p2
    print(p1)
class Employee():
    def __init__(self, fname, lname, level, yrsService):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrsService
    def __ge__(self, other):
        return self.level >= other.level
    def __gt__(self, other):
        return self.level > other.level
    def __lt__(self, other):
        return self.level < other.level
    def __le__(self, other):
        return self.level <= other.level


def learnComparisonOps():
    # define some employees
    dept = []
    dept.append(Employee("Tim", "Sims", 5, 9))
    dept.append(Employee("John", "Doe", 4, 12))
    dept.append(Employee("Jane", "Smith", 6, 6))
    dept.append(Employee("Rebecca", "Robinson", 5, 13))
    dept.append(Employee("Tyler", "Durden", 5, 12))
    # who is more senior
    print(dept[0]>dept[1])
    print(dept[4]<dept[3])

    # sorted uses these methods to sor
    emps = sorted(dept)
    for emp in emps:
        print(emp.lname)


def learnBasicLogging():
    """
    import logging
    by default logging will happen only for level 
    Warning and above this changed  by basicConfig()
    basicConfig() will be called only once
    and any subsequent call will not have any effect
    By default log output is appended to the recent output content of file

    This can be controlled by filemode argument. if we do not specify
    it will be append mode
    """
    # use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG,
                        filename="output.log", filemode="w")
     # Try out each of the log levels
    logging.debug("This is a debug-level log message")
    logging.info("This is an info-level log message")
    logging.warning("This is a warning-level message")
    logging.error("This is an error-level message")
    logging.critical("This is a critical-level message")

    # Output formatted string to the log
    logging.info("Here's a {} variable and an int: {}".format("string", 10))

extData = {'user': 'joem@example.com'}
def anotherFunction():
    logging.debug("This is a debug-level log message", extra=extData)
def learnCustomLogging():
    # set the output file and debug level, and
    # use a custom formatting specification
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    dateStr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunction()

def learnListComprehensions():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    # perform a mapping and filter 
    # evenSquared = list(
    #     map(lambda e: e**2, filter(lambda e: e>4 and e<16,evens)))
    # print(evenSquared)
    #  using comprehensions
    evenSquared = [ e**2 for e in evens]
    print(evenSquared)

    oddsSquared = [ e**2 for e in odds if e>3 and e<17]
    print(oddsSquared)

def learnDictComprehensions():
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]
    # use comprehension to build a dictionary
    tempDict = {t: (t * 9/5) + 32 for t in ctemps if t <100}
    print(tempDict)
    print(tempDict[12])
    # Merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}

    newTeam = {k : v for team in (team1, team2) for k, v in team.items()}
    print(newTeam)




    



if __name__ == "__main__":
    # stringsandbytes()
    # stringformating()
    # anyallminmaxsum()
    # iterationtesting()
    # transformation()
    # itertoolLearn()
    # print(documentation.__doc__)
    # print(variablearguments(10, 10, 30))
    # myNums = [5, 10, 10, 10]
    # print(variablearguments(*myNums))
    # learnLambdaFunc()
    # keywordArgumentsOnly()
    # namedTuple()
    # learndefdict()
    # learnCounter()
    # learnEnum()
    # learnStringReprOfObjects()
    # learnComputedAttr()
    # learnObjectOps()
    # learnComparisonOps()
    # learnBasicLogging()
    # learnCustomLogging()
    # learnListComprehensions()
    learnDictComprehensions()




