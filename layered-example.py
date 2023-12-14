# person.py -> This will be our model data
# validator.py -> Data validation for Person
# repo.py -> Class for persistence layer that handles persons
# service.py -> Here you can handle business logic
# console.py -> Can be the view of your application, or presentation layer


# The business objects
# ====================
class Person:
    def __init__(self, name, age, id):
        self.id = id
        self.name = name
        self.age = age

class PersonValidator:
    def __init__(self):
        pass

    def validate(self, person):
        if person.name == "":
            raise Exception("Name cannot be empty")
        if person.age < 0:
            raise Exception("Age cannot be negative")
        if person.id < 0:
            raise Exception("Id cannot be negative")

class Room:
#    def __init__(self, ):
#        self.
    pass

def validate(self, person):
    pass
    
# The Repository or Data Access objects
# =====================================
class PersonRepository:
    def __init__(self):
        self.persons = []
        
    def add(self, person):
        self.persons.append(person)

    def get(self, id):
        for person in self.persons:
            if person.id == id:
                return person
        return None

    def get_all(self):
        self.persons.append(Person('Akram Waseem', 43, 99))
        self.persons.append(Person('Jahan Nur', 23, 54))
        self.persons.append(Person('Sharif Admi', 43, 40))
        return self.persons

    def update(self, old_person, new_person):
        self.delete(old_person.id)
        self.add(new_person)
        raise Exception("Person not found")

    def delete(self, id):
        for p in self.persons:
            if p.id == id:
                self.persons.remove(p)
                return
        raise Exception("Person not found")

# The Service or Business Logic objects
# =====================================        
class PersonService:
    def __init__(self):
        self.repository = PersonRepository()
        self.validator = PersonValidator()

    def get(self, id):
        return self.repository.get(id)

    def get_all(self):
        return self.repository.get_all()

    def add(self, person):
        self.repository.add(person)

    def update(self, old_person, new_person):
        self.repository.update(old_person, new_person)

    def delete(self, id):
        self.repository.delete(id)

    # OTHER BUSINESS LOGIC CAN BE ADDED HERE
    def get_by_name(self, name):
        for person in self.repository.get_all():
            if person.name == name:
                return person
        return None
    
    # FILTER PERSON BY AGE
    def filter_by_age(self, age):
        persons = []
        for person in self.repository.get_all():
            if person.age == age:
                persons.append(person)
        return persons
        
class PersonController:
    def __init__(self):
        self.service = PersonService()

    def get(self, id):
        return self.service.get(id)

    def get_all(self):
        return self.service.get_all()

    def add(self, person):
        self.service.add(person)

    def update(self, old_person, new_person):
        self.service.update(old_person, new_person)

    def delete(self, id):
        self.service.delete(id)

    def get_by_name(self, name):
        return self.service.get_by_name(name)
    
    def filter_by_age(self, age):
        return self.service.filter_by_age(age)

# The Presentation objects
# ========================         
class PersonConsole:
    def __init__(self):
        self.controller = PersonService() # PersonController

    def get_all(self):
        persons = self.controller.get_all()
        for person in persons:
            print(person.id, person.name, person.age)

    def get(self, id):
        person = self.controller.get(id)
        if person is None:
            print("Person not found")
        else:
            print(person.id, person.name, person.age)

    def add(self, name, age):
        person = Person(name, age, 0)
        self.controller.add(person)
        print("Person added")

    def update(self, id, name, age):
        person = Person(name, age, id)
        self.controller.update(self.controller.get(id), person)
        print("Person updated")

    def delete(self, id):
        self.controller.delete(id)
        print("Person deleted")

    def get_by_name(self, name):
        person = self.controller.get_by_name(name)
        if person is None:
            print("Person not found")
        else:
            print(person.id, person.name, person.age)
    
    def filter_by_age(self, age):
        persons = self.controller.filter_by_age(age)
        for person in persons:
            print(person.id, person.name, person.age)
    
    # Menu for user input
    def run(self):
        while True:
            print("1. Get all persons")
            print("2. Get person by id")
            print("3. Add person")
            print("4. Update person")
            print("5. Delete person")
            print("6. Get person by name")
            print("7. Filter person by age")
            print("8. Exit")
            print("Enter your choice: ", end="")
            choice = int(input())
            if choice == 1:
                self.get_all()
            elif choice == 8:
                break
            # and other functions for your menu, you got the point
        
def main():
    console = PersonConsole()
    console.run()
    
main()