import pytest
import sys
import os

sys.path.insert(0, f"{os.getcwd()}/ftimecache")

@pytest.fixture
def generator():
    return (i for i in range(100))
