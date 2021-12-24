from obj_generator import person_generator
"""
Adopts the "persons" command line flag,
used to provide number of persons to generate (i.e number of test cases)
"""
def pytest_addoption(parser):
    parser.addoption(
        "--persons",
        type=int,
        action="store",
        metavar="num",
        help="generates 'persons' number of persons to test",
    )
      
    """ 
    Description:
        Assertion comparator in case of assertion failure.
        Will print out the description of the failure ,
        inclding the invalid params that failed in the assertion.

    Args:
        op (==): Assertion operator in use
        left ([age: int, gender: str, nationality: str]): Person data generated prior to the tests
        right ([age: int, gender: str, nationality: str]): Person data verified by the APIs with the generated person name

    Returns:
        [list(str)]: Returns description of asserion failure, including the invalid params
    """  
def pytest_assertrepr_compare(op, left, right):
    #Age case
    if isinstance(left, int) and isinstance(right, int) and op == "==":
        return ["Exception when comparing person age instances:",
                f"   vals: {left} != {right}",]
        
    #Nationality & Gender case
    elif isinstance(left, str) and isinstance(right, str) and op == "==":
        return ["Exception when comparing person gender or nationality instances:",
                f"   vals: {left} != {right}",]
        
    """
    Generates test cases.
    Will use "persons" arg if provided in the command line, otherwise will default to 5 tests.
    """
def pytest_generate_tests(metafunc):
    if "person" in metafunc.fixturenames:
        if metafunc.config.getoption("persons"):
            num_of_persons = metafunc.config.getoption("persons")
        else:
            num_of_persons = 5
            
        generator = person_generator()
        persons_list = generator.generate_persons(num_of_persons)
        metafunc.parametrize("person", persons_list)

