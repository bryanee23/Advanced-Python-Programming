from Classes import Person, Student, Employee, Faculty
import random

class generators:
  """class to generate random values for driver code"""
  def id_generator():
    result = ""
    for _ in range(0,4):
      result += str(random.randint(0, 99))

    return result

  def name_generator():
    names = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan", "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul", "Afonso", "Ahmad", "Ahmed", "Ahmed-Aziz", "Ahoua", "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Brydon-Craig", "Bryn", "Brynmor", "Bryson", "Buddy", "Bully", "Burak", "Burhan", "Butali", "Butchi", "Byron", "Cabhan", "Cadan", "Cade", "Caden", "Cadon", "Cadyn", "Caedan", "Caedyn", "Cael", "Caelan", "Caelen", "Caethan", "Cahl", "Cahlum", "Cai", "Caidan", "Caiden", "Caiden-Paul", "Caidyn", "Caie", "Cailaen", "Cailean", "Caileb-John", "Cailin", "Cain", "Caine", "Cairn", "Cal"]

    return f'{names[random.randint(0, 30)]} {names[random.randint(0, 30)]}'

  def grade_generator():
    level = ["1st year", "2nd Year", "3rd Year", "4th year"]
    return level[random.randint(0, 3)]



human1 = Person(generators.name_generator(), random.randint(18, 99), '1114 S Juanita Ave, Redondo Beach, CA, 90277')

human2 = Student(generators.name_generator(), random.randint(18, 99), '5412 Pebble Ln, Loves Park, IL, 61111', generators.id_generator(),generators.grade_generator())

human3 = Employee(generators.name_generator(), random.randint(18, 99), '5412 Pebble Ln, Loves Park, IL, 61111', random.randint(30000, 1000000),random.randint(0, 40))

human4 = Faculty(generators.name_generator(), random.randint(18, 99), '5412 Pebble Ln, Loves Park, IL, 61111', random.randint(30000, 1000000),random.randint(0, 40), generators.id_generator(), "Math" )

if __name__ == "__main__":
  print("\n Person class: \n{}\n\n Student class: \n{}\n\n Employee class: \n{}\n\n Faculty class: \n{}\n\n  ".format(human1, human2, human3, human4))