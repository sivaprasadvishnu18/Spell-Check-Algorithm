from language_tools import LanguageHelper
import unittest

# We define the custom lexicon that we will use for our controlled tests
lexicon = ('car', 'cat', 'Cate', 'cater', 'care',
           'cot', 'cute', 'dare', 'date', 'dog', 'dodge',
           'coffee', 'pickle', 'grate', 'Missouri','a-borning',
           'McGee', 'mucins','multangular','opiniator',
           'presuffering','interunion','cupelling','Washington','bracing',
           'room', 'agglomerative','vice-dean','misrelation','gagroot',"instructors\'")

class BasicTest(unittest.TestCase):

    def setUp(self):
        self.help = LanguageHelper(lexicon)
  
    # make sure that all the words in the lexicon are recognized
    def testContainment(self):
        for w in lexicon:
            self.assertTrue(w in self.help)
  
    def testFailures(self):
        try:
            self.assertFalse('cate' in self.help)     # only allowed when capitalized
            self.assertFalse('fox' in self.help)      # word is not there
            self.assertFalse('cofee' in self.help)    # mis-spell word is not there
            self.assertFalse('missouri' in self.help) # Correct because missouri is not equal to Misouri
            self.assertFalse('aborning' in self.help)
            self.assertFalse('Opiniator' in self.help)
            self.assertFalse('washington' in self.help)
            self.assertFalse('wash-ington' in self.help)
            self.assertFalse('groot' in self.help)
            self.assertFalse('missrelation' in self.help)
            self.assertFalse('Mucins' in self.help)
        except AssertionError:
            print('Word is in list')
    
    def testSuggestInsertion(self):
        self.assertEqual(self.help.getSuggestions('pikle'), ['pickle'])
        self.assertEqual(self.help.getSuggestions('ct'), ['cat','cot'])
        self.assertEqual(self.help.getSuggestions('Mgee'),['Mcgee']) #Needs to add a slash
        self.assertEqual(self.help.getSuggestions('Aborning'),['A-borning']) #Will suggest capital word because query is capital A
        self.assertEqual(self.help.getSuggestions('aborning'),['a-borning']) #Will add a hyphen
        self.assertEqual(self.help.getSuggestions('rom'),['room']) #Add an extra o
        self.assertEqual(self.help.getSuggestions('instructors'),["instructors\'"])
        
    def testSuggestDeletion(self):
        self.assertEqual(self.help.getSuggestions('gratle'), ['grate'])
        self.assertEqual(self.help.getSuggestions('Mu-cins'),['Mucins'])  #Remove the -
        self.assertEqual(self.help.getSuggestions('InterunNion'),['Interunion']) #Remove the extra N
        self.assertEqual(self.help.getSuggestions('braccing'),['bracing']) #Remove the extra c
        self.assertEqual(self.help.getSuggestions('rooom'),['room']) #Remove an extra 0
        self.assertEqual(self.help.getSuggestions('vice--dean'),['vice-dean']) #Remove an extra -

    def testSugeestionsCapitalization(self):
        self.assertEqual(self.help.getSuggestions('Gate'), ['Cate', 'Date', 'Grate'])
        self.assertEqual(self.help.getSuggestions('missouri'),['Missouri']) #missouri has to be capitalized since it is a proper noun
        self.assertEqual(self.help.getSuggestions('washington'),['Washington']) #Capitalize w
        
    def testSuggestionsNone(self):
        self.assertEqual(self.help.getSuggestions('blech'), [])
        self.assertEqual(self.help.getSuggestions('aquarium'),[]) #Not in list
        self.assertEqual(self.help.getSuggestions('prseffaring'),[]) #Multiple errors. Needs to switch first two characters replace e with a
        self.assertEqual(self.help.getSuggestions('misssrelation'),[]) #Multiple errors. Remove 2 s which is not possible
        self.assertEqual(self.help.getSuggestions('groot'),[]) #Multiple errors. Missing two characters from the word in list

    def testSuggestionsSwitch(self):
        self.assertEqual(self.help.getSuggestions('cfofee'), ['coffee'])
        self.assertEqual(self.help.getSuggestions('opiniatro'),['opiniator']) #Last two characters need to switch
        self.assertEqual(self.help.getSuggestions('Rpesuffering'),['Presuffering']) #First two characters need to switch
        self.assertEqual(self.help.getSuggestions("instructor\'s"), ["instructors\'"]) #Switches the last two characters
        
    def testSuggestionsReplace(self):
        self.assertEqual(self.help.getSuggestions('muntangular'),['multangular']) #Replace t with l
        self.assertEqual(self.help.getSuggestions('cupalling'),['cupelling']) #Replace a with e
        self.assertEqual(self.help.getSuggestions('ggglomerative'),['agglomerative']) #Replace a with g
        self.assertEqual(self.help.getSuggestions("instructors-"), ["instructors\'"]) #Replaces - with '

if __name__ == '__main__':
    unittest.main()
