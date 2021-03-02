#
# range(10)
# print(list(range(4)))
#
# print(list(range(1,10,2)))
#
# for number in range (1, 10 ,2)
#     print("nr", number)

text = 'herbata'
for letter in text:
    print(letter)
print()

items = ['cukier', 'herbata', 4, 3.5]
for i in items:
    print(i)
print()

names = ["Ada", "Julia", "Ruby"]
for step in names:
    print("Hello", step)
print()

names = ["Ada", "Julia", "Ruby"]
for step in range(3):
    print(step, ": ", names[step])
print()


for i in range(5):
    print(i+1)
print()

for i in range(10, 30, 5):
    print(i)
print()


pa = ""
magic = "hokuspokus"
for num in range(2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)
print()

for val in "string":
    if val == "i":
        break
    print(val)
print("Koniec")


for val in "string":
    if val == "i":
        print('lalala')
        continue
    print(val)
print("Koniec")
