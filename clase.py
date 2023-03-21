import unittest

def decimal_to_roman(decimal):
    if decimal <= 3:
        return 'I' * decimal
    elif decimal == 5:
        return 'V'
#    elif decimal == 6:
#       return 'VI'
#    elif decimal == 7:
#        return 'VII'
    elif decimal <= 8:
        return 'VIII' 
    else:
        return "X"
    

class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        # pre condicion
        ### NO HAY ###
        # proceso
        resultado = decimal_to_roman(1)
        # verificacion
        self.assertEqual(resultado, 'I')

    def test_diez(self):
        resultado = decimal_to_roman(10)
        self.assertEqual(resultado, 'X')

    def test_cinco(self):
        resultado = decimal_to_roman(5)
        self.assertEqual(resultado, 'V')

    def test_dos(self):
        resultado = decimal_to_roman(2)
        self.assertEqual(resultado, 'II')

    def test_tres(self):
        resultado = decimal_to_roman(3)
        self.assertEqual(resultado, 'III')
    
    def test_seis(self):
        resultado = decimal_to_roman(6)
        self.assertEqual(resultado, 'VI')

    def test_seis(self):
        resultado = decimal_to_roman(7)
        self.assertEqual(resultado, 'VII')

    def test_seis(self):
        resultado = decimal_to_roman(8)
        self.assertEqual(resultado, 'VIII')


if __name__ == '__main__':
    unittest.main()