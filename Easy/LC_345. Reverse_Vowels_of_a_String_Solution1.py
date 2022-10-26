"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


"""
def reverseVowels(self, s: str) -> str:
    lit = []
    t = ""

    for i in s:
        if i.lower() in "aeiou":
            lit.append(i)
    for i in s:
        if i.lower() in "aeiou":
            t += lit[-1]
            lit.pop()
        else:
            t += i
    return t