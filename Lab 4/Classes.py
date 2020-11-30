"""
Person should have:
- name
- age
- address

Student should be a subclass of Person and have:
- Student ID
- Grade Level

Employee should be a subclass of Person and have:
- Salary
- Years on the Job

Faculty should be a subclass of Employee and have:
- Faculty ID
- Subject taught
"""

####### Person Class ################
class Person:
  def __init__(self, name, age, address):
      self._name = name
      self._age = age
      self._address = address

  @property
  def name(self):
      return self._name

  @name.setter
  def name(self, name):
      self._name = name

  @property
  def age(self):
      return self._age

  @age.setter
  def age(self, age):
    self._age = age

  @property
  def address(self):
      return self._address

  @address.setter
  def address(self, address):
    self._address = address

  def __str__(self):
      return f' Name: {self._name}, Age: {self._age},  Address:{self._address}'


####### Student Class ################
class Student(Person):
  def __init__(self, name, age, address, ID, grade_level):
      self._ID = ID
      self._grade_level = grade_level
      Person.__init__(self, name, age, address)

  @property
  def ID(self):
      return self._ID

  @ID.setter
  def ID(self, ID):
      self._ID = ID

  @property
  def grade_level(self):
      return self._grade_level

  @grade_level.setter
  def grade_level(self, grade_level):
    self._grade_level = grade_level

  def __str__(self):
      return f' Name: {self._name}, Age: {self._age},  Address: {self._address} Student ID: {self._ID}, Grade Level: {self._grade_level}'

####### Employee Class ################
class Employee(Person):
  def __init__(self, name, age, address, salary, YOE):
      self._salary = salary
      self._YOE = YOE
      Person.__init__(self, name, age, address)

  @property
  def salary(self):
      return self._salary

  @salary.setter
  def salary(self, salary):
      self._salary = salary

  @property
  def YOE(self):
      return self._YOE

  @YOE.setter
  def YOE(self, YOE):
    self._YOE = YOE

  def __str__(self):
      return f' Name: {self._name}, Age: {self._age},  Address: {self._address} Salary: ${self._salary}, Experience: {self._YOE}'


####### Faculty Class ################
class Faculty(Employee):
  def __init__(self, name, age, address, salary, YOE, fac_ID, subject):
      self._fac_ID = fac_ID
      self._subject = subject
      Employee.__init__(self, name, age, address, salary, YOE)

  @property
  def fac_ID(self):
      return self._fac_ID

  @fac_ID.setter
  def fac_ID(self, fac_ID):
      self._fac_ID = fac_ID

  @property
  def subject(self):
      return self._subject

  @subject.setter
  def subject(self, subject):
    self._subject = subject

  def __str__(self):
      return f' Name: {self._name}, Age: {self._age},  Address: {self._address} Salary: ${self._salary}, Experience: {self._YOE} years, Faculty ID: {self._fac_ID}, Subject: {self._subject}'
