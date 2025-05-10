class RomanNumerals:
    __ROMAN_MAP = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    __ROMAN_VALUES = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
        'C': 100, 'XC': 90, 'L': 50, 'XL': 40,
        'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1
    }

    @staticmethod
    def to_roman(val: int) -> str:
        if not 0 < val < 4000:
            raise ValueError("Value must be between 1 and 3999")

        result = []
        for num, roman in RomanNumerals.__ROMAN_MAP:
            while val >= num:
                result.append(roman)
                val -= num
        return ''.join(result)

    @staticmethod
    def from_roman(roman_num: str) -> int:
        result = 0
        i = 0
        while i < len(roman_num):
            if i + 1 < len(roman_num) and roman_num[i:i + 2] in RomanNumerals.__ROMAN_VALUES:
                result += RomanNumerals.__ROMAN_VALUES[roman_num[i:i + 2]]
                i += 2
            else:
                result += RomanNumerals.__ROMAN_VALUES[roman_num[i]]
                i += 1
        return result

print(RomanNumerals.from_roman('MMVIII')) # 2008
print(RomanNumerals.to_roman(1990))     # MCMXC
print(RomanNumerals.from_roman('XIV'))