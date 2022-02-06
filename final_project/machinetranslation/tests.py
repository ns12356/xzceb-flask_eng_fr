import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class TestTranslator_e2f(unittest.TestCase):
    def test_e2f1(self):
        self.assertNotEqual(englishToFrench("None"), '')
        self.assertNotEqual(englishToFrench(0), 0)
        self.assertEqual(englishToFrench('Thank you'), 'Je vous remercie')
        self.assertEqual(englishToFrench('Goodbye'), 'Au revoir')

class TestTranslator_f2e(unittest.TestCase):
    def test_f2e1(self):
        self.assertNotEqual(frenchToEnglish("Non"), '')
        self.assertNotEqual(frenchToEnglish(0),0)
        
        self.assertEqual(frenchToEnglish('Au revoir'),'Goodbye')

unittest.main()
