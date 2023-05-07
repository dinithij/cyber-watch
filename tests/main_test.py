import unittest

# Import the test case class
from cyber_watch_test import CyberWatchTestCase

# Create a test suite
test_suite = unittest.TestLoader().loadTestsFromTestCase(CyberWatchTestCase)

# Run the test suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
