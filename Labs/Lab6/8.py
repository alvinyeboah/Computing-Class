def clean_string(input_string):
    cleaned_string = ""
    for x in input_string:
        if x.isalpha():
            cleaned_string += x.lower()
    return cleaned_string

def anagrams(string1, string2):
    string1fixed = clean_string(string1)
    string2fixed = clean_string(string2)
    dictionary1 = dict()
    dictionary2 = dict()

    for x in string1fixed:
        if x in dictionary1:
            dictionary1[x] += 1
        else:
            dictionary1[x] = 1

    for x in string2fixed:
        if x in dictionary2:
            dictionary2[x] += 1
        else:
            dictionary2[x] = 1

    return dictionary1 == dictionary2




print(anagrams("alvin ", "ni Vla "))