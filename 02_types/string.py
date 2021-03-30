word = 'tea'
print(word, '- ilość znaków: ', len(word), "\n")

txt = 'Python'
print(txt[0])
print("\t", txt[1])
print(txt[2:])
print(txt[1:-1])
print(txt[:-1])
print(txt[0:])
print(txt[:-2])
print(txt[-1:])
print(txt[-6:])
print(txt[:2])
print(txt[:2] + txt[2:])
print(txt[:3] + txt[4:])
print(txt[::2])
print(txt[::3])
print(txt[::4])
print(txt[::5], "\n")

txt_2 = "abrakadabra"
print(txt_2.count('a'))
print(txt_2.count('ab'), "\n")

# 1. Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7
# i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

txt = "telewizor"
middle = len(txt)//2
element = txt[middle]
prev = txt[middle-1]
post = txt[middle + 1]
print(prev + element + post)
print(txt[middle-1:middle+2], "\n")

ex_1 = str(input("Wpisz wyraz o długości nieparzystej większej niż 7: "))
mid = len(ex_1) // 2
print(ex_1[mid-1:mid+2])


# 2. Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.

s1 = 'word'
s2 = "wo"
mid_s1 = len(s1) // 2
print(s1[:mid_s1] + s2 + s1[mid_s1:], "\n")

ss1 = str(input("wpisz jakiś wyraz: "))
ss2 = str(input("wpisz inny wyraz: "))
mid_ss1 = len(ss1) // 2
print(ss1[:mid_ss1] + ss2 + ss1[mid_ss1:], "\n")


# 3. Do zmiennej quote przypisz zdanie: „Honesty is the first chapter in the book of wisdom.”

quote = "Honesty is the first chapter in the book of wisdom."

# Policz wszystkie znaki w napisie
print(len(quote))

# Nie modyfikując zmiennej wyświetl słowo wisdom
lengh = len(quote)
print(quote[lengh-7:lengh-1])
# ale po co tak komplikować ??
print(quote[-7:-1])
print(quote[-7: -1:1])

# Wyświetl tylko pierwszą połowę tekstu
mid_quote = len(quote) // 2
print(quote[:mid_quote])

# Wyświetl tylko kropkę
print(quote[-1])

# Wyświetl od połowy tylko co trzecią literę cytatu
print(quote[mid_quote::3])

# Wyświetl ‘Hnsyi h is hpe ntebo fwso.’
print(quote[::2])

# Wyświetl cały cytat odwrotnie
print(quote[::-1])

# Zamień wisdom na słowo friendship
print(quote.replace("wisdom", "frendship"), "\n")


# 4. Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron

book_title = str(input("Podaj tytuł książki: "))
author = str(input("Podaj autora tej książki: "))
pages = str(input("Podaj liczbę stron: "))

# Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.

print(book_title.isalpha())
print(author.isalpha())
print(pages.isdigit())

# Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich

correct_book_title = book_title.title()
print(correct_book_title)
correct_autor = author.title()
print(correct_autor)

# Połącz dane w jeden ciąg book za pomocą spacji

data = [correct_book_title, correct_autor, pages]
book = " "
book = book.join(data)
print(book, "\n")


# 5. Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
# Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.

word = "kajak"
print(word)
print(word[::-1])
print("słowo jest palindromem -", word == word[::-1], "\n")

sentence = "Kobyła ma mały bok"
sentence = sentence.replace(" ", "")
sentence = sentence.lower()
print(sentence)
print(sentence[::-1])
print("zdanie jest palindromem -", sentence == sentence[::-1], "\n")


your_sentence = str(input("Wpisz zdanie, które jest palindromem: "))
your_sentence = your_sentence.replace(" ", "")
your_sentence = your_sentence.replace(".", "")
your_sentence = your_sentence.replace(",", "")
your_sentence = your_sentence.replace("!", "")
your_sentence = your_sentence.replace("?", "")
your_sentence = your_sentence.replace("-", "")
your_sentence = your_sentence.lower()
print(your_sentence[0::])
print(your_sentence[::-1])
print("zdanie jest palindromem -", your_sentence == your_sentence[::-1], "\n")


# panildron = (input("wpisz zdanie:"))
#
# pal=panildron()
# print(pal[::-1])
# print(pal[0::])


# 6. Przekopiuj zawartość import this do zmiennej.

zen = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""


# Policz liczbę wystąpień słowa better.

print(zen.count('better'))

# Usuń z tekstu symbol gwiazdki

zen = zen.replace("*", "")
print("\n", zen)

# Zamień jedno wystąpienie explain na understand

zen = zen.replace("explain", "understand", 1)
print(zen, "\n")

# Usuń spacje i połącz wszystkie słowa myślnikiem

zen = zen.replace(" ", "-")
print(zen, "\n")

zen = zen.replace("\n", "")

# Podziel tekst na osobne zdania za pomocą kropki

zen = zen.split('.')
print(zen)


# 7 Stwórz dwie dowolne zmienne przechowujące wartość liczbową i tekstową.
# Użyj funkcji format(), by wyświetlić zdanie zawierające te wartości.

# chyba o to chodziło....

ex_7_a = "zima"
ex_7_b = 31 + 21

print("\nDziś jest {}, {} dzień roku 2021.".format(ex_7_a, ex_7_b))


# a to wcześniejsze luźne impresje...

print("\nThe product of 5 * 2 is {}, the product of 10 * 2 is {}.".format(5 * 2, 10 * 2))

ex_7_1 = "The product of 5 * 2 is {}, the product of 10 * 2 is {}."
print(ex_7_1.format(5 * 2, 10 * 2))

part_1 = "The product of 5 * 2 is {},"
part_2 = "the product of 10 * 2 is {}."

print(part_1.format(5 * 2), part_2.format(10*2))
