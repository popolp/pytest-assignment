import pytest
from classes.obj_generator import person_generator


def pytest_addoption(parser):
    parser.addoption(
        "--amount",
        type=int,
        action="store",
        metavar="num",
        help="generates 'amount' number of persons to test",
    )


# def pytest_configure(config):
#     # register the "lvl" marker
#     config.addinivalue_line(
#         "markers", "amount(num): mark test to run only on named environment"
#     )


def pytest_generate_tests(metafunc):
    if "persons_list" in metafunc.fixturenames:
        if metafunc.config.getoption("amount"):
            amount = metafunc.config.getoption("amount")
        else:
            amount = 5
        # GENERATE PERSON LIST HERE
        gen = person_generator()
        gen.generate_x(amount)
        persons_list = gen.generate_x(amount)
        metafunc.parametrize("persons_list", persons_list)

