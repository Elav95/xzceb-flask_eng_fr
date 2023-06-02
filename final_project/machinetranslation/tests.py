from translator import *
import unittest

class TestEn2Fr(unittest.TestCase): 
    def test1(self):
        self.assertEqual(english_to_french("thank you"), "merci") 
        self.assertEqual(english_to_french("Ball"), "Balle")  
        self.assertEqual(english_to_french("hello"), "bonjour")  
        
class TestFr2En(unittest.TestCase): 
    def test1(self):
        self.assertEqual(french_to_english("serpent"), "snake") 
        self.assertEqual(french_to_english("Au revoir"), "Goodbye")  
        self.assertEqual(french_to_english("Bonjour"), "Hello")  

unittest.main()
