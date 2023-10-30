def pig_latin(word):
    if word[0] in "aeiou":
        return (word.lower() + "way")
    else :
        for x in word:
            if x in "aeiou":
                return word[word.index(x):] + word[:word.index(x)] + "ay"
print(pig_latin("Alvin"))