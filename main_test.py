import unittest

from main import calculate_hits


class MainTest(unittest.TestCase):

  def test_calculate_hits_no_match(self):
    actual = calculate_hits('punto', 'raise')
    self.assertEqual(([], []), actual)

  one_match = [
      ('abcde', 'afghi', ([0], [])),
      ('abcde', 'fbghi', ([1], [])),
      ('abcde', 'fgchi', ([2], [])),
      ('abcde', 'fghdi', ([3], [])),
      ('abcde', 'fghie', ([4], [])),
  ]

  def test_calculate_hits_one_match(self):
    for (ans, word, expected) in self.one_match:
      with self.subTest(ans=ans, word=word):
        actual = calculate_hits(ans, word)
        self.assertEqual(expected, actual)
