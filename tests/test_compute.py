from concurrent.futures import ThreadPoolExecutor
from person_api import call_person_api

params = [
    "agify",
    "genderize",
    "nationalize"
]

"""
Verify status code -> verify person data
"""
def test_compute(person):
    expected_name = person.name
    with ThreadPoolExecutor(max_workers = 3) as executor:
        results = [executor.submit(call_person_api, param, expected_name) for param in params]
    
    # Check status codes before accessing data
    for result in results:
        assert result.result().status_code == 200
    
    expected_age = results[0].result().json()["age"]
    expected_gender = results[1].result().json()["gender"]
    expected_nationality = results[2].result().json()["country"][0]["country_id"]

    assert person.age.result() == expected_age and person.gender.result() == expected_gender and person.nationality.result() == expected_nationality