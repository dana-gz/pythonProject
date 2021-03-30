# 1. Jak sprawdzić czy ciąg znaków składa się tylko z cyfr?
numeric = "1234567"
mixed = "1234asdf12!"

print(numeric, "- ciąg znaków składa się tylko z cyfr:", numeric.isdigit())
print(mixed, "- ciąg znaków składa się tylko z cyfr:", mixed.isdigit())

sequence = str(input("Wprowadź ciąg znaków: "))
print("Ciąg znaków składa się tylko z cyfr:", sequence.isdigit() )
print()

# 2. Jak wyświetlić wyśrodkowany tekst o zadanej szerokości i dodatkowo puste miejsca wypełnić gwiazdką?
txt = 'mata'
new_txt = txt.center(20, '*')
print(new_txt)
print()

# 3. Jaka metoda usunie znaki tylko z prawej strony?
print(new_txt.rstrip('*'))
print()

# 4. Jak sprawdzić czy ciąg ma co najmniej jedną dużą literę ?

up_sequence = str(input("Wprowadź ciąg znaków: "))
print("Ciąg znaków składa się tylko z cyfr:", up_sequence.isdigit() )
print("Ciąg znaków składa się tylko ze znaków alfanumerycznych:", up_sequence.isalnum() )
print("Ciąg znaków składa się tylko z małych liter:", up_sequence.islower() )
print()

# 5 Policz ile razy zadany ciąg znaków wystąpił w ciągu znaków

txt_2 = "banananana"
print("W ciągu", txt_2, "'na' występuje", txt_2.count('na'), "razy.")

