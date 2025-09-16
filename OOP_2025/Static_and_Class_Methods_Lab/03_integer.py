class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        roman_numerals = {
            'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
            'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
            'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
            'M': 1000
        }

        i = 0
        result = 0
        while i < len(value):
            # Проверка за двойна буква (напр. IV, IX, CM...)
            if i + 1 < len(value) and value[i:i + 2] in roman_numerals:
                result += roman_numerals[value[i:i + 2]]
                i += 2
            else:
                result += roman_numerals[value[i]]
                i += 1
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):   # ako ne e string
            return "wrong type"
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))




