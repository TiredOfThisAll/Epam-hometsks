"""
Task 7_2
Create classes Employee, SalesPerson, Manager and Company with predefined functionality.

Create basic class Employee and declare following content:
• Attributes – `name` (str), `salary` and `bonus` (int), set with property decorator
• Constructor - parameters `name` and `salary`
• Method `bonus` - sets bonuses to salary, amount of which is delegated as `bonus`
• Method `to_pay` - returns the value of summarized salary and bonus.

Create class SalesPerson as class Employee inheritor and declare within it:
• Constructor with parameters: `name`, `salary`, `percent` – percent of plan performance (int, without the % symbol), first two of which are passed from basic class constructor
• Redefine method of parent class `bonus` in the following way: if the sales person completed the plan more than 100%, their bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is multiplied by 3)

Create class Manager as Employee class inheritor, and declare within it:
• Constructor with parameters: `name`, `salary` and `client_number` (int, number of served clients), first two of which are passed to basic class constructor.
• Redefine method of parent class `bonus` in the following way: if the manager served over 100 clients, their bonus is increased by 500, and if more than 150 clients – by 1000.

Create class Company and declare within it:
• Constructor with parameters: `employees` – list of company`s employees (made up of Employee/SalesPerson/Manager classes instances) with arbitrary length `n`
• Method `give_everybody_bonus` with parameter company_bonus (int) that sets the amount of basic bonus for each employee.
• Method `total_to_pay` that returns total amount of salary of all employees including awarded bonus
• Method `name_max_salary` that returns name of the employee, who received maximum salary including bonus.

Note:
Class attributes and methods should bear exactly the same names as those given in task description
Methods should return only target values, without detailed explanation within `return`
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.__bonus = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, value):
        self.__bonus = value

    def to_pay(self):
        return self.bonus + self.salary


class SalesPerson(Employee):
    def __init__(self, name, salary, percent):
        self.__percent = percent
        super().__init__(name, salary)

    @Employee.bonus.setter
    def bonus(self, bonus):
        if self.__percent > 200:
            Employee.bonus.fset(self, bonus * 3)
        elif self.__percent > 100:
            Employee.bonus.fset(self, bonus * 2)
        else:
            Employee.bonus.fset(self, bonus)


class Manager(Employee):
    def __init__(self, name, salary, client_number):
        self.__client_number = client_number
        super().__init__(name, salary)

    @Employee.bonus.setter
    def bonus(self, bonus):
        if self.__client_number > 150:
            Employee.bonus.fset(self, bonus + 1000)
        elif self.__client_number > 100:
            Employee.bonus.fset(self, bonus + 500)
        else:
            Employee.bonus.fset(self, bonus)


class Company:
    def __init__(self, employees, n):
        self.__employees = employees

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        self.__employees = value

    def give_everybody_bonus(self, company_bonus):
        for i in self.__employees:
            i.bonus = company_bonus

    def total_to_pay(self):
        return sum(map(lambda x: x.to_pay(), self.__employees))

    def name_max_salary(self):
        return (lambda temp: self.__employees[temp.index(max(temp))].name)(list(map(lambda x: x.to_pay(), self.__employees)))
