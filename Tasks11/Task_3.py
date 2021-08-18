class Product:
    def __init__(self, typeof: str, name: str, price: float):
        self.type = typeof
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.type}, {self.name}, {self.price}'


class ProductStoreInfo:
    price_premium = 1.2

    def __init__(self, product: object, amount: int, discount=0):
        self.product = product
        self.amount = amount
        self.discount = discount
        self.price_premium = round(self.price_premium * product.price, 2)

    def __repr__(self):
        return f'({self.product} - Quantity {self.amount}, store price {self.price_premium}$ Discount {self.discount}%)'


class ProductStore:
    income = 0
    all_products = []

    def add(self, product: object, amount: int):
        self.all_products.append(ProductStoreInfo(product, amount))

    def set_discount(self, identifier: str, percent: float, identifier_type='name'):
        if identifier_type == 'name':
            for i, value in enumerate(self.all_products):
                if value.product.name == identifier:
                    self.all_products[i].discount = int(percent * 100)
                    break
            else:
                raise ValueError('Wrong product name, try again')
        elif identifier_type == 'type':
            for i, value in enumerate(self.all_products):
                if value.product.type == identifier:
                    self.all_products[i].discount = int(percent * 100)
                    break
            else:
                raise ValueError('Wrong product name, try again')
        else:
            raise ValueError('Wrong identifier, try again')

    def sell_product(self, product_name: str, amount: int) -> None:
        for i, value in enumerate(self.all_products):
            if value.product.name == product_name:
                value.amount -= amount
                self.income += value.price_premium * amount
                break
        else:
            raise ValueError('Wrong product name, try again')

    def get_income(self) -> float:
        return self.income

    def get_all_products(self) -> list:
        return self.all_products

    def get_product_info(self, product_name) -> tuple:
        for i, value in enumerate(self.all_products):
            if value.product.name == product_name:
                a, b = (value.product.name, value.amount)  # packing a tuple
                break
        else:
            raise ValueError('Wrong product name, try again')
        tuple_value = (a, b)
        return tuple_value


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 200)

print(s.get_all_products(), '\n')
s.set_discount('Ramen', 0.15)

print(s.get_all_products(), '\n')
s.sell_product('Ramen', 10)

print(s.get_all_products())
print(s.get_income())

print(s.get_product_info('Football T-Shirt'))
