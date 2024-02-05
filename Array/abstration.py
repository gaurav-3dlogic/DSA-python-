from abc import ABC, abstractmethod
class Company(ABC):

    def work(self):
        pass

class Manager(Company):

    def work(self):
        print("I assign work to team and manage team")

class Employee(Company):

    def work(self):
        print("I complete the work assigned to me")

# Driver code
R = Manager()
R.work()

K = Employee()
K.work()