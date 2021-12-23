import names
from person import Person
import requests
from concurrent.futures import ThreadPoolExecutor

"""
    The class is an object generator, intended to be generalized but currently supports only Person objects. 
"""
class person_generator:
    def __init__(self, generated_type = Person) -> None:
        if generated_type is not Person:
            raise ValueError("Types other than person are currently not supported")
        self.generated_type = generated_type
    
    """
        Returns randomly generated num_of_objects objects.
    """
    def generate_x(self, num_of_objects=5):
        return [
            self.populate_person_data(self.generated_type(name = names.get_first_name())) for _ in range(num_of_objects)
            ]

    """
    Grabs data for each person from the APIs.
    Nationality is selected to be the highest probability option.
    """
    def populate_person_data(self, person): 
        with ThreadPoolExecutor(max_workers=3) as executor:
            person.age = executor.submit(lambda: requests.get(f"https://api.agify.io?name={person.name}").json()["age"])
            person.gender = executor.submit(lambda: requests.get(f"https://api.genderize.io?name={person.name}").json()["gender"])
            person.nationality = executor.submit(lambda: requests.get(f"https://api.nationalize.io?name={person.name}").json()["country"][0]["country_id"])
            # person.age = requests.get(f"https://api.agify.io?name={person.name}").json()["age"]
            # person.gender = requests.get(f"https://api.genderize.io?name={person.name}").json()["gender"]
            # person.nationality = requests.get(f"https://api.nationalize.io?name={person.name}").json()["country"][0]["country_id"]
        
        return person

if __name__ == "__main__":
    o = person_generator(Person)
    l = o.generate_x(3)
    for p in l:
        print(p.age)
