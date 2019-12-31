from string import Template
import itertools
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
if __name__ == "__main__":
    # stringsandbytes()
    # stringformating()
    # anyallminmaxsum()
    # iterationtesting()
    # transformation()
    # itertoolLearn()
    print(documentation.__doc__)
