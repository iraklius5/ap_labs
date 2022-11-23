import unittest
from main import RabinKarp


class Test(unittest.TestCase):
    def test_with_basic_mod_and_base(self):
        rabin_karp = RabinKarp()
        text = "adbmkdlbnadfbipoad;kfj.balkfbnajdafgdsh"
        pattern = "nadfb"
        expected_result = [8]
        actual_result = rabin_karp.find(pattern, text)
        self.assertEqual(expected_result, actual_result)

    def test_with_custom_mod_and_base(self):
        rabin_karp = RabinKarp(256, 1000)
        text = "jdfioadfiuhiopdfgijskdflkdfnmxcvblkx.cv"
        pattern = "flkd"
        expected_result = [22]
        actual_result = rabin_karp.find(pattern, text)
        self.assertEqual(expected_result, actual_result)

    def test_no_match(self):
        rabin_karp = RabinKarp()
        text = "jdfioadfiuhiopdfgijskdflkdfnmxcvblkx.cv"
        pattern = "flkdddfh"
        expected_result = []
        actual_result = rabin_karp.find(pattern, text)
        self.assertEqual(expected_result, actual_result)

    def test_multiple_matches(self):
        rabin_karp = RabinKarp(256, 1000)
        text = "ababaadfgjikoddbababadlkfmmkbababadfg;lsmkfnababa"
        pattern = "ababa"
        expected_result = [0, 16, 29, 44]
        actual_result = rabin_karp.find(pattern, text)
        self.assertEqual(expected_result, actual_result)

    def test_long_text_short_pattern(self):
        rabin_karp = RabinKarp(256, 10000)
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In id ullamcorper turpis, non faucibus justo. Aenean iaculis neque orci, id pellentesque risus ornare sit amet. Cras eget posuere urna, sit amet vehicula lorem. Ut eros erat, lobortis et magna sagittis, porttitor dignissim ex. Fusce vestibulum dolor quis est commodo, sed gravida nibh volutpat. Sed sagittis velit mi, eleifend tristique velit pharetra vitae. Aenean feugiat, erat et porttitor scelerisque, ipsum nibh faucibus libero, sit amet auctor dui elit sed odio. Nulla eu arcu nunc. Proin nec pellentesque dui, non facilisis ex. Vivamus tincidunt odio libero, vel luctus dui faucibus eu. Donec ut cursus elit, vel porttitor leo. Duis tortor purus, efficitur id odio at, viverra interdum ante. Nunc vel luctus sapien."
        pattern = "viverra interdum"
        expected_result = [733]
        actual_result = rabin_karp.find(pattern, text)
        self.assertEqual(expected_result, actual_result)

    def test_long_text_long_pattern(self):
        rabin_karp = RabinKarp(256, 10000)
        text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In id ullamcorper turpis, non faucibus justo. Aenean iaculis neque orci, id pellentesque risus ornare sit amet. Cras eget posuere urna, sit amet vehicula lorem. Ut eros erat, lobortis et magna sagittis, porttitor dignissim ex. Fusce vestibulum dolor quis est commodo, sed gravida nibh volutpat. Sed sagittis velit mi, eleifend tristique velit pharetra vitae. Aenean feugiat, erat et porttitor scelerisque, ipsum nibh faucibus libero, sit amet auctor dui elit sed odio. Nulla eu arcu nunc. Proin nec pellentesque dui, non facilisis ex. Vivamus tincidunt odio libero, vel luctus dui faucibus eu. Donec ut cursus elit, vel porttitor leo. Duis tortor purus, efficitur id odio at, viverra interdum ante. Nunc vel luctus sapien."
        pattern = "id pellentesque risus ornare sit amet. Cras eget posuere urna, sit amet vehicula lorem. Ut eros erat, lobortis et magna sagittis,"
        expected_result = [130]
        actual_result = rabin_karp.find(pattern, text)
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()