import sys
import os
import pytest

print(pytest.__version__)
current_directory = os.getcwd()
sys.path.insert(0, current_directory + "/src")
