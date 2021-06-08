def is_palindrome(txt):
    txt = txt.lower().replace(' ', '')
    t = txt[::-1]
    if txt == t:
        print("It's palindrome")
    else:
        print("It's not a palindrome")

txt = input('Enter your text: ')
is_palindrome(txt)

