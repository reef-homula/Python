def C_Anagram(w1, w2):
    # Pythonは、英単語の大文字・小文字の区別をする。したがって比べる場合は、小文字に揃える必要がある。
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(C_Anagram("conda", "danco"))
print(C_Anagram("Kanazawa", "Ritsu"))