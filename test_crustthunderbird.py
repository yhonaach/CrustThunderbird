# test_crustthunderbird.py
"""
Tests for CrustThunderbird module.
"""

import unittest
from crustthunderbird import CrustThunderbird

class TestCrustThunderbird(unittest.TestCase):
    """Test cases for CrustThunderbird class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrustThunderbird()
        self.assertIsInstance(instance, CrustThunderbird)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrustThunderbird()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
