class Employee:
    """
    A class used to represent an Employee
    Attributes
    ----------
    first : str
        the first name of the employee
    last : str
        the last name of the employee
    holiday_left : int
        the number of holiday left in days
    email : srt
        the email generated from first and last name
    """
    

    def __init__(self, first, last, left):
        self.first = first
        self.last = last
        assert left >0
        self.holiday_left = left
        self.email = first + '.' + last + '@ec-nantes.fr'


    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def newHoliday(self, addDay):
        self.holiday_left = self.holiday_left + addDay
    
    def __str__(self):
        return self.first+" "+self.last+" "+self.email+", jours restants : "+ str(self.holiday_left)