def find_word(word1, word2):
    li = []
    ind = 0
    for ch in word1:
        if ch in word2[ind:]:
            ind += word2[ind:].find(ch)
            li.append(ind)
        else: return False

    x = li[:]
    x.sort()

    if li == x and len(word1) == len(li): return True
    else: return False


word1 = input('First word: ').lower()
word2 = input('Second word: ').lower()

print(find_word(word1, word2))
