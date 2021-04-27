# Utwórz klasę sklep. Sklep posiada różne produkty.
# W sklepie można pordukt zobaczyc, przymierzyc, kupic, zwrocic.

class Shop:
    store = [
        'dress',
        't-shirt',
        'shoes',
        'skirt',
        'trousers'
    ]

    def show(self, index):
        print(self.store[index])

    def try_product(self, item):
        print('product was tired')

    def buy(self, item):
        if item in self.store:
            for index, value in enumerate(self.store):
                if value == item:
                    product_to_buy = self.store.pop(index)
                    return product_to_buy
        else:
            return 'brak produktu'

    def return_product(self, item):
        self.store.append(item)

if __name__ == '__main__':
    my_shop = Shop()
    print(my_shop.store)
    my_shop.show(3)
    my_shop.try_product('dress')
    print(my_shop.buy('dress'))
    print(my_shop.store)
    print(my_shop.buy('dress'))
    print(my_shop.store)
    print(my_shop.buy(my_shop.store[1]))
    print(my_shop.store)





#
# if __name__ == '__main__':
#     my_shop = Shop()
#     print(my_shop.store)
#
#
#
#     def __init__(self, product, size, price, quality, quantity):
#         self.product = product
#         self.size = size
#         self.price = price
#         self.quality = quality
#         self.quantity = quantity
#
#     def show(self):
#         return 'see' * self.product
#
#
#     def put_on(self):
#         return 'put' * self.product
#
#
#     def count_stock(self):
#         return self.product * self.quantity
#
#     def buy(self):
#         return self.product * self.quantity - buy(self)
#
#
