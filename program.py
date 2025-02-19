# Define the person class
class Person:
    people_count = 0
    
    def __init__(self, name:str, age:int, dob:str, country:str, job:str):
        self.name = name
        self.age = age
        self.dob = dob
        self.country = country
        self.job = job
        
        type(self).people_count += 1
        
    def get_row(self):
        return f"{self.name};{self.age};{self.dob};{self.country};{self.job}"
    
    @classmethod
    def number_of_people(cls) -> int:
        return cls.people_count
    @classmethod
    def clear(cls):
        cls.people_count = 0
    
    @staticmethod
    def get_columns() -> str:
        return "Countains 5 data columns:\n[0] Name (str); [1] Age (int); [2] Date of birth (YYYY-MM-DD) (str); [3] Country (Two letter code) (str); [4] Occupation (str)"
    
    @staticmethod
    def get_header() -> str:
        return "Name;Age;Date of Birth;Birth Country;Occupation"

def import_db(path:str, sep: str) -> list:
    people = []
    
    with open(path, 'r', encoding='utf-8') as db:
        next(db)
        for line in db:
            row = line.strip().split(sep)
            person = Person(row[0], int(row[1]), row[2], row[3], row[4])
            people.append(person)
            
    return people

def export_db(data:list, name:str):
    with open(f"./{name}", 'w', encoding='utf-8') as db:
        db.write(f"{Person.get_header()}\n")
        for person in data:
            db.write(f"{person.get_row()}\n")
            
def search(field_id:int, value:str, data:list) -> list:
    found = []
    
    for person in data:
        if field_id == 0 and person.name == value:
            found.append(person)
        elif field_id == 1 and person.age == int(value):
            found.append(person)
        elif field_id == 2 and person.dob == value:
            found.append(person)
        elif field_id == 3 and person.country == value:
            found.append(person)
        elif field_id == 4 and person.job == value:
            found.append(person)
    
    return found

# Start program
personList = []

while True:
    try:
        print("\n\n\n\n\n\n\n\n\n\n\nProgram Menu:")
        if len(personList) < 1:
            print("[1] Import list")
        else:
            print("[1] Export list")
            print("[2] Search in data")
            print("[3] Remove Import")
        print("[Q] Quit")
        choice = input("Enter your choice: ")
        if choice == 'Q':
            break;
        elif choice == '1':
            if len(personList) < 1:
                path = input("Enter the path to the file here (without delimiting characters): ")
                sep =  input("Separator character used in database: ")
                personList = import_db(path, sep)
                print("Import done.")
                print(f"Number of people: {Person.number_of_people()}")
            else:
                name = input("Give the name of the file to export the file in: ")
                export_db(personList, name)
                personList.clear()
                Person.clear()
                print("Export done.")
        elif choice == '2' and len(personList) > 1:
            print(Person.get_columns())
            id = int(input("Give a column to search in: "))
            val = input("Give the value to search: ")
            hits = search(id, val, personList)
            print("Found:")
            for hit in hits:
                print(hit.get_row())
            print(f"Matches with {len(hits)} out of {Person.number_of_people()} entries")
            choice = input("Do you want to expost the searces? [y/N]: ")
            if choice.lower() == "y":
                name = input("Give the name of the file to export the file in: ")
                export_db(hits, name)
                print("Export done.")
        elif choice == '3' and len(personList) > 1:
            personList.clear()
            Person.clear()
            print("Import removed. You can now import another file.")
        else:
            print("Not a valid choice!")
    except:
        print("\nERROR! Something happened.\n")
    
    print("Press Enter to continue...")
    input()