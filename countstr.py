def CountString(word):
    counter = {}
    word = word.lower()
    for c in word:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1
    
    print(counter)

print("文字数カウンター")
CountString("abbcccddddeeeeeffffff")