import pytest
import unittest
from unittest.mock import MagicMock 
from tdd_assignment import LargestSubarrayWith0Sum
class TestLargestSubarryWith0Sum:
    @pytest.fixture
    def object(self):
        obj=LargestSubarrayWith0Sum()
        return obj
    @pytest.fixture
    def mock_file(self):
        mock_file=MagicMock()
        return mock_file
    
    def test_can_read_from_file(self,object,mock_file):
        path="shhs"
        with unittest.mock.patch('builtins.open',return_value=mock_file):
            assert object.readFromFile(path)==mock_file

    def test_can_type_cast_input(self,object,mock_file):
        mock_file.read.return_value='4\n5 -4 1 5'
        assert object.getInputValues(mock_file)==[4,[5,-4,1,5]]