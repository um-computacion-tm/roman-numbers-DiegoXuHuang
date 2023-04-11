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


if __name__ == '__main__':
    unittest.main()