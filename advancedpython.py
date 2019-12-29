from string import Template
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
def transformation():
if __name__ == "__main__":
    # stringsandbytes()
    # stringformating()
    # anyallminmaxsum()
    # iterationtesting()
    transformation()
