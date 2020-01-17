from abc import ABC, abstractmethod
import sys


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


if __name__ == "__main__":
    # facade()
    # commandPattern()
    # interpreterPattern()
    mediatorPattern()
