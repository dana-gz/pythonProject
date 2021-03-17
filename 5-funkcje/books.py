def get_book():
    counter = int(input("How many book you wat  to add to the collection? "))

    books_collection = []
    for book in range(counter):
        title = input("book title: ")
        rate = int(input(f'{title} - rate [0-10]: '))
        books_collection.append([title, rate])

    return books_collection


def show_rate(books_list):
    nr = int(input("Which rate you want to see? Give me a number: "))
    index = nr - 1
    print(books_list[index])

    if nr > len(books_list) or nr > 10:
        print("no such a book in the collection")
    else:
        print(f'Book -> {books_list[index][0]} is rated -> {books_list[index][1]} / 10')

# main part -------------


print('Welcome to library! ---')
books = get_book()
print('Added!')

print('-------')
show_rate(books)
