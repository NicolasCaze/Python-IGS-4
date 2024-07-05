import unittest
from check_updates import check_updates

class TestCheckUpdates(unittest.TestCase):
    def test_wordpress_major(self):
        result = check_updates('5.4.9', 'wordpress')
        self.assertEqual(result['major'], '6.5.2')

    def test_wordpress_minor(self):
        result = check_updates('5.4.9', 'wordpress')
        self.assertEqual(result['minor'], '5.4.15')

    def test_plugin_major(self):
        result = check_updates('3.0.0', 'plugin', 'akismet')
        self.assertEqual(result['major'], '5.1.1')

    def test_plugin_minor(self):
        result = check_updates('3.0.0', 'plugin', 'akismet')
        self.assertEqual(result['minor'], '5.1.1')

    def test_plugin_string_version(self):
        result = check_updates('20240308', 'plugin', 'ga-google-analytics')
        self.assertEqual(result['major'], '20240308')
        self.assertEqual(result['minor'], None)

if __name__ == '__main__':
    unittest.main()
