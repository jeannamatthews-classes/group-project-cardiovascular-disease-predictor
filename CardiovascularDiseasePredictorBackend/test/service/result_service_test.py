import unittest

class ResultServiceTest(unittest.TestCase):
    DUMMY_SAMPLE = {'AGE',
                    'GENDER',
                    'SMOKING ',
                    'ALCOHOL',
                    'DM',
                    'HTN',
                    'CAD',
                    'PRIOR CMP',
                    'CKD',
                    'HB',
                    'TLC',
                    'PLATELETS',
                    'GLUCOSE',
                    'UREA',
                    'CREATININE',
                    'BNP',
                    'RAISED CARDIAC ENZYMES', 'EF', 'SEVERE ANAEMIA', 'ANAEMIA',
                           'STABLE ANGINA', 'ACS', 'STEMI', 'ATYPICAL CHEST PAIN', 'HEART FAILURE',
                           'HFREF', 'HFNEF', 'VALVULAR', 'CHB', 'SSS', 'AKI', 'CVA INFRACT',
                           'CVA BLEED', 'AF', 'VT', 'PSVT', 'CONGENITAL', 'UTI',
                           'NEURO CARDIOGENIC SYNCOPE', 'ORTHOSTATIC', 'INFECTIVE ENDOCARDITIS',
                           'DVT', 'CARDIOGENIC SHOCK', 'SHOCK', 'PULMONARY EMBOLISM',
                           'CHEST INFECTION', 'Class1'}


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()







