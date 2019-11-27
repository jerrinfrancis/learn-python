#
# Example file for working with classes
#
class myClass():
  def method1(self):
    print("myclass method")
  def method2(self, someString):
    print("myclass method2 " + someString)
class anotherClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("anotherclass method1")
  def method2(self, someString):
    print("anotherclass method2 " )
def main():
  c = myClass()
  c.method1()
  c.method2("testing")
  c2 = anotherClass()
  c2.method1()
  c2.method2("TEsting")

  
if __name__ == "__main__":
  main()
