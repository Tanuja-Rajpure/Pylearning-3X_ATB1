letters = ['a', 'b', 'c', 'd', 'e', 'i', 'j', 'o', 'u', 'w']


# filter the vowels

def is_vowels(letter):
    vowels = ['a', 'i', 'o', 'u']
    return letter in vowels


filtered_world = filter(is_vowels, letters)

print("Vowels from above letter: ", list(filtered_world))



