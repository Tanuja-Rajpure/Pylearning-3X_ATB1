letters = ['a', 'b', 'e', 'i', 'o', 'j', 'd']

#filter the vowels - a, e, i, o ,u

def is_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter in vowels

#result = is_vowels('u')
#print(result)

filtered_vowels = filter(is_vowels, letters)
print(list(filtered_vowels))