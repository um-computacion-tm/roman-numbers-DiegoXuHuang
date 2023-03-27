import unittest

def decimal_to_roman(decimal):
    total = ''
    if decimal >= 100:
        centena = decimal // 100
        total = 'C' * centena
        decimal = decimal % 100
    if decimal <= 3:
        total += 'I' * decimal
    elif decimal == 5:
        total += 'V'
    elif decimal == 10:
        total += 'X'
    elif decimal == 8:
        total += 'VIII'
    elif decimal == 4:
        total += 'IV'
    elif decimal == 9:
        total += 'IX'
    elif decimal >= 40 and decimal < 50:
        total += 'XL'+ decimal_to_roman(decimal % 10)
    elif decimal >= 90 and decimal < 100:
        total += 'XC'+ decimal_to_roman(decimal % 10)
    elif decimal >= 400 and decimal < 500:
        total += 'CD'+ decimal_to_roman(decimal % 100)
    elif decimal >= 900 and decimal < 1000:
        total += 'CM'+ decimal_to_roman(decimal % 10)
    return total


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
    
    def test_cuatro(self):
        resultado = decimal_to_roman(4)
        self.assertEqual(resultado, 'IV')

    def test_nueve(self):
        resultado = decimal_to_roman(9)
        self.assertEqual(resultado, 'IX')

    def test_cuarenta(self):
        resultado = decimal_to_roman(40)
        self.assertEqual(resultado, 'XL')
    
    def test_cuarenta_uno(self):
        resultado = decimal_to_roman(41)
        self.assertEqual(resultado, 'XLI')

    def test_quinientos_uno(self):
        resultado = decimal_to_roman(501)
        self.assertEqual(resultado, 'DI')


if __name__ == '__main__':
    unittest.main()