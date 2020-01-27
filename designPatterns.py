from abc import ABC, abstractmethod
import sys
import pickle

class SubsystemA:
    def method1(self):
        print('SubsystemA method1..')

    def method2(self):
        print('SubsystemA method2..')


class SubsystemB:
    def method1(self):
        print('SubsystemB method1..')

    def method2(self):
        print('SubsystemB method2..')


class Facade():
    def __init__(self):
        self._subsystemA = SubsystemA()
        self._subsystemB = SubsystemB()

    def method(self):
        self._subsystemA.method1()
        self._subsystemA.method2()
        self._subsystemB.method1()
        self._subsystemB.method2()


def facade():
    facade = Facade()
    facade.method()


class Command:
    def execute(self):
        pass


class Copy(Command):
    def execute(self):
        print('Copying...')


class Paste(Command):
    def execute(self):
        print('Pasting...')


class Cut(Command):
    def execute(self):
        print('Cuting...')


class Macro:
    def __init__(self):
        self.commands = []

    def add(self, Command):
        self.commands.append(Command)

    def run(self):
        for command in self.commands:
            command.execute()


def commandPattern():
    macro = Macro()
    macro.add(Copy())
    macro.add(Cut())
    macro.add(Paste())

    macro.run()


class AbstractExpression:
    @abstractmethod
    def interpret(self):
        pass


class NonTerminalExpression(AbstractExpression):
    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        print("non terminal")
        self._expression.interpret()


class TerminalExpression(AbstractExpression):
    def interpret(self):
        print('terminal')


def interpreterPattern():
    ast = NonTerminalExpression(NonTerminalExpression(TerminalExpression()))
    ast.interpret()


class Colleague(object):
    def __init__(self, mediator, id):
        self._mediator = mediator
        self._id = id

    def getID(self):
        return self._id

    def send(self, msg):
        pass

    def receive(self, msg):
        pass


class ConcreteColleague(Colleague):
    def __init__(self, mediator, id):
        super().__init__(mediator, id)

    def send(self, msg):
        print(f'Message: {msg} send by colleage {str(self._id)}')
        self._mediator.distribute(self, msg)
    def receive(self, msg):
        print(f'Messge: {msg} received by colleage  {str(self._id)}')


class Mediator:
    def add(self, colleague):
        pass

    def distribute(self, sender, msg):
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        Mediator.__init__(self)
        self._colleague = []

    def add(self, colleague):
        self._colleague.append(colleague)

    def distribute(self, sender, msg):
        for colleague in self._colleague:
            if colleague.getID() != sender.getID():
                colleague.receive(msg)


def mediatorPattern():
    mediator = ConcreteMediator()

    c1 = ConcreteColleague(mediator, 1)
    c2 = ConcreteColleague(mediator, 2)
    c3 = ConcreteColleague(mediator, 3)

    mediator.add(c1)
    mediator.add(c2)
    mediator.add(c3)

    c1.send("Good Morning!")

class Originator:
    def __init__(self):
        self._state = None
    def create_memento(self):
        return pickle.dumps(vars(self))
    
    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)


def mementoPattern():
    originator = Originator()
    
    print(vars(originator))

    memento = originator.create_memento()

    originator._state = True

    print(vars(originator))

    originator.set_memento(memento)

    print(vars(originator))
class AtmState():
    name = "state"
    allowed = []
    def goNext(self, state):
        if state.name in self.allowed:
            print(f'Current state: {self} switched on to: {state.name}  ')
            self.__class__ = state
        else:
            print(f'Current state: {self} switched on to: {state.name} not possible')

    def __str__(self):
        return self.name
class Off(AtmState):
    name = "off"
    allowed = ['on']
class On(AtmState):
    name = "on"
    allowed = ['off']

class ATM():
    def __init__(self):
        self.current = Off()
    def setState(self, state):
        self.current.goNext(state)


def statePattern():
    atm = ATM()
    atm.setState(On)
    atm.setState(On)
    atm.setState(Off)

class AbstractClass(ABC):
#This class inherit from Abstract Base Class to allow the use of the @abstractmethod decorator
    
	def template_method(self):
		"""Ths is the template method that contains a collection of 
		methods to stay the same, to be overriden, and to be overriden optionally.
		"""

		self.__always_do_this()
		self.do_step_1()
		self.do_step_2()
		self.do_this_or()

	def __always_do_this(self):
		#This is a protected method that should not be overriden.

		name = sys._getframe().f_code.co_name
		print('{}.{}'.format(self.__class__.__name__, name))

	@abstractmethod
	def do_step_1(self):
		#This method should be overriden
		pass

	@abstractmethod
	def do_step_2(self):
		#This method should be overriden
		pass

	def do_this_or(self):
		print('You can overide me but you do not have to')

class ConcreteClassA(AbstractClass):
#This class inherits from the Abstract class featuring the template method. 

	def do_step_1(self):
		print('Doing step 1 for ConcreteClassA ...')

	def do_step_2(self):
		print('Doing step 2 for ConcreteClassA ...')

class ConcreteClassB(AbstractClass):
#This class inherits from the Abstract class featuring the template method.

	def do_step_1(self):
		print('Doing step 1 for ConcreteClassB ...')

	def do_step_2(self):
		print('Doing step 2 for ConcreteClassB ...')

	def do_this_or(self):
		print('Doing my own business ...')

def templatePattern():
	print('==ConcreteClassA==')
	a = ConcreteClassA()
	a.template_method()

	print('==ConcreteClassB==')
	b = ConcreteClassB()
	b.template_method()



if __name__ == "__main__":
    # facade()
    # commandPattern()
    # interpreterPattern()
    # mediatorPattern()
    # mementoPattern()
    # statePattern()
    templatePattern()
