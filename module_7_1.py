class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    def __init__(self, __file_name='products.txt'):
        self.__file_name = __file_name

    def get_products(self):
        try:
            with open(self.__file_name, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = self.get_products().splitlines()
        with open(self.__file_name, 'a', encoding='utf-8') as file:
            for product in products:
                if str(product) in existing_products:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(f'{product}\n')

# Пример использования
s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
