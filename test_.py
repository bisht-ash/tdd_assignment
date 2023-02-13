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
    
    def test_invalid_input_empty(self,object,mock_file):
        mock_file.read.return_value=''
        with pytest.raises(Exception):
            object.getInputValues(mock_file)
        
    def test_invalid_input(self,object,mock_file):
        mock_file.read.return_value='4'
        with pytest.raises(Exception):
            object.getInputValues(mock_file)
    
    def test_one_value_no_ans(self,object):
        input_values=[1,[4]]
        assert object.largestSubarryWith0Sum(input_values)==-1
    
    def test_one_value_with_ans(self,object):
        input_values=[1,[0]]
        expected=[0,0]
        ans=object.largestSubarryWith0Sum(input_values)
        assert len(expected) == len(ans)
        assert all([a == b for a, b in zip(expected, ans)])