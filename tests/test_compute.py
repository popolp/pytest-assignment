import pytest
from classes.person import Person
from classes.obj_generator import person_generator

def test_compute(person):

    assert person.age.result() == 50