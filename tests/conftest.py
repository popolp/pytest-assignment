from obj_generator import person_generator

def pytest_addoption(parser):
    parser.addoption(
        "--persons",
        type=int,
        action="store",
        metavar="num",
        help="generates 'persons' number of persons to test",
    )

def pytest_generate_tests(metafunc):
    if "person" in metafunc.fixturenames:
        if metafunc.config.getoption("persons"):
            num_of_persons = metafunc.config.getoption("persons")
        else:
            num_of_persons = 5
            
        generator = person_generator()
        persons_list = generator.generate_persons(num_of_persons)
        metafunc.parametrize("person", persons_list)

