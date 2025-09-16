def vowel_filter(function):

    def wrapper():
        result = function()
        vowels = 'aeiou'
        return [char for char in result if char.lower() in vowels]
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())