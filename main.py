class Animal():
    def __init__(self, name, age, food, sound):
        self.name = name
        self.age = age
        self.food = food
        self.sound = sound

    def make_sound(self):
        pass

    def eat(self):
        print(f'{self.name} ест {self.food}')

class Bird(Animal):
    def __init__(self, name, age, food, sound, animal_class='Птицы'):
        super().__init__(name, age, food, sound)
        self.animal_class = animal_class

    def make_sound(self):
        print(f'{self.name} кричит {self.sound}')

class Mammal(Animal):
    def __init__(self, name, age, food, sound, animal_class='Млекопитающие'):
        super().__init__(name, age, food, sound)
        self.animal_class = animal_class

    def make_sound(self):
        print(f'{self.name} говорит {self.sound}')

class Reptile(Animal):
    def __init__(self, name, age, food, sound, animal_class='Рептилии'):
        super().__init__(name, age, food, sound)
        self.animal_class = animal_class

    def make_sound(self):
        print(f'{self.name} издает звук {self.sound}')

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo():
    def __init__(self, zoo_name, location):
        self.zoo_name = zoo_name
        self.location = location
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'{animal} добавлен в список животных зоопарка "{self.zoo_name}", {self.location}')

    def add_staff(self, staffer):
        self.staff.append(staffer)
        print(f'{staffer.staffer_name} добавлен в список сотрудников зоопарка "{self.zoo_name}", {self.location} в должности {staffer.post}')

    def print_staff_list(self):
        print(f'Список сотрудников зоопарка "{self.zoo_name}", {self.location}:')
        for staffer in self.staff:
            print(f'Имя: {staffer.staffer_name}; Должность: {staffer.post}')

    def print_animal_list(self):
        print(f'Список животных зоопарка "{self.zoo_name}", {self.location}:')
        for animal in self.animals:
            print(f'Название: {animal.name}; Возраст: {animal.age}; Еда: {animal.food}')

class Zookeeper():
    def __init__(self, staffer_name, post='Смотритель зоопарка'):
        self.staffer_name = staffer_name
        self.post = post

    def feed_animal(self, animal):
        print(f'{self.staffer_name} кормит {animal.name}. Корм -  {animal.food}')

class Veterinarian():
    def __init__(self, staffer_name, post='Ветеринар'):
        self.staffer_name = staffer_name
        self.post = post

    def heal_animal(self, animal):
        print(f'{self.staffer_name} лечит {animal.name}.')

zoo = Zoo('В мире животных', "г. Москва")
keeper = Zookeeper('Олег')
vet = Veterinarian('Изольда')

zoo.add_staff(keeper)
zoo.add_staff(vet)

zoo.print_staff_list()

bird1 = Bird('Филин', 5, "мыши", "У-у-у")
bird2 = Bird('Кукушка', 1, "черви", "Ку-ку")

mam1 = Mammal('Корова', 3, "трава", "Мууу")
mam2 = Mammal('Лев', 10, "мясо", "Ррррр")

rep1 = Reptile('Черепаха', 15, "водоросли", "Шшшшшш")
rep2 = Reptile('Крокодил', 6, "мясо", "Щелк пастью")

zoo.add_animal(bird1)
zoo.add_animal(bird2)
zoo.add_animal(mam1)
zoo.add_animal(mam2)
zoo.add_animal(rep1)
zoo.add_animal(rep2)

zoo.print_animal_list()

rep2.eat()

animal_sound(zoo.animals)

keeper.feed_animal(mam1)

vet.heal_animal(bird1)