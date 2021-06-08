def shift_value(txt):
    n = input('enter a number: ')
    try:
        n = int(n)
    except:
        shift_value(txt)
    else:
        if n >= 1 and n <= 25:
            return hack(n, txt)
        else:
            return shift_value(txt)


def hack(n, txt):
    enc = ''
    for ch in txt:
        if not ch.isalpha():
            enc += ch
        else:
            code = ord(ch) + n
            while code > 122: # poderia usar if, pois ja esta checando na funcao shift_value as condicoes 
                code -= 26
            enc += chr(code)

    print(enc)


text = input('enter your text: ')
shift_value(text)
