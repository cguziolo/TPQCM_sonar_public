import pytest

from Employee import Employee 

class TestEmployee:
    emp_1 = Employee('John', 'Smith', 30)

    def test_employee_attributes(self): 
        assert self.emp_1.first == 'John'
        assert self.emp_1.last == 'Smith'
        assert self.emp_1.email == 'John.Smith@ec-nantes.fr'
        assert self.emp_1.holiday_left == 20

    def test_fullname(self):
        assert self.emp_1.fullname() == 'John Smith'
