def is_anagram(txt1, txt2):
    count = 0
    if len(txt1) == len(txt2) and len(txt1) > 0:
        for ch in txt1:
            if ch in txt2:
                count += 1
    if count == len(txt1) and len(txt1) > 0:
        return print('Anagrams')
    else:
        return print('Not anagrams')


txt1 = input('First word: ').lower().replace(' ', '')
txt2 = input('Second word: ').lower().replace(' ', '')

is_anagram(txt1, txt2)
