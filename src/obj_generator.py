import names
from concurrent.futures import ThreadPoolExecutor
from person import Person
from person_api import call_person_api

"""
    The class is an object generator, intended to be generalized but currently supports only Person objects. 
"""


class person_generator:
    def __init__(self, generated_type=Person) -> None:
        if generated_type is not Person:
            raise ValueError("Types other than person are currently not supported")
        self.generated_type = generated_type

    def generate_persons(self, num_of_objects=5):
        return [self.populate_person_data() for _ in range(num_of_objects)]

    """
    Grabs data for each person from the APIs.
    Nationality is selected to be the highest probability option.
    """

    def populate_person_data(self):
        person = self.generated_type(name=names.get_first_name())
        with ThreadPoolExecutor(max_workers=3) as executor:
            person.age = executor.submit(
                lambda: call_person_api("agify", person.name).json()["age"]
            )
            person.gender = executor.submit(
                lambda: call_person_api("genderize", person.name).json()["gender"]
            )
            person.nationality = executor.submit(
                lambda: call_person_api("nationalize", person.name).json()["country"][0]["country_id"]
            )
        return person
