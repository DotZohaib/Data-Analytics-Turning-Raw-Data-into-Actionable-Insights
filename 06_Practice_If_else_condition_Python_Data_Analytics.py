vowels = str(input("Enter a character: "))

# if vowels in "aeiouAEIOU":  #  short way to write
if (vowels in "aeiou")  or (vowels in "AEIOU"): # long way to write
    print(f"{vowels} is a vowel")
else:
    print(f"{vowels} is a consonant")
