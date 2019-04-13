def C_Kaibun(word):
    word = word.lower()
    return word[::-1]  == word

print(C_Kaibun("mom"))
print(C_Kaibun("mother"))