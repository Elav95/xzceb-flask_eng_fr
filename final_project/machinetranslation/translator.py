"""Module to translate from English to French and from French to English."""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''Takes an english text, returns the translation in french'''
    french_text = MyMemoryTranslator('en', 'fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''Takes a french text, returns the translation in english'''
    english_text = MyMemoryTranslator('fr', 'en').translate(french_text)
    return english_text
