import pytest
import unittest
from unittest.mock import MagicMock 
from tdd_assignment import LargestSubarrayWith0Sum
class TestLargestSubarryWith0Sum:
    @pytest.fixture
    def object(self):
        obj=LargestSubarrayWith0Sum()
        return obj
    
    def test_can_read_from_file(self,object):
        path="shhs"
        mock_file=MagicMock()
        with unittest.mock.patch('builtins.open',return_value=mock_file):
            assert object.readFromFile(path)==mock_file


