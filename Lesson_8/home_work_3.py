# Завдання 3
#
# Створіть список товарів в інтернет-магазині.
# Серіалізуйте його за допомогою pickle та збережіть у JSON.
import json
import pickle
from typing import TypedDict


class Product(TypedDict):
    id: int
    name: str
    price: float
    currency: str
    category: str


# Data
COFFEE_SHOP_PRODUCTS: list[Product] = [
    {"id": 1, "name": "Espresso", "price": 2.50, "currency": "USD", "category": "Coffee"},
    {"id": 2, "name": "Americano", "price": 3.00, "currency": "USD", "category": "Coffee"},
    {"id": 3, "name": "Cappuccino", "price": 3.50, "currency": "USD", "category": "Coffee"},
    {"id": 4, "name": "Latte", "price": 3.75, "currency": "USD", "category": "Coffee"},
    {"id": 5, "name": "Mocha", "price": 4.00, "currency": "USD", "category": "Coffee"},
    {"id": 6, "name": "Macchiato", "price": 3.25, "currency": "USD", "category": "Coffee"},
    {"id": 7, "name": "Flat White", "price": 3.75, "currency": "USD", "category": "Coffee"},
    {"id": 8, "name": "Cold Brew", "price": 4.00, "currency": "USD", "category": "Coffee"},
    {"id": 9, "name": "Iced Latte", "price": 4.25, "currency": "USD", "category": "Coffee"},
    {"id": 10, "name": "Iced Mocha", "price": 4.50, "currency": "USD", "category": "Coffee"},
    {"id": 11, "name": "Chai Latte", "price": 3.75, "currency": "USD", "category": "Tea"},
    {"id": 12, "name": "Matcha Latte", "price": 4.00, "currency": "USD", "category": "Tea"},
    {"id": 13, "name": "Green Tea", "price": 2.75, "currency": "USD", "category": "Tea"},
    {"id": 14, "name": "Black Tea", "price": 2.50, "currency": "USD", "category": "Tea"},
    {"id": 15, "name": "Herbal Tea", "price": 3.00, "currency": "USD", "category": "Tea"},
    {"id": 16, "name": "Hot Chocolate", "price": 3.50, "currency": "USD", "category": "Hot Beverage"},
    {"id": 17, "name": "Steamed Milk", "price": 2.00, "currency": "USD", "category": "Hot Beverage"},
    {"id": 18, "name": "Caramel Macchiato", "price": 4.25, "currency": "USD", "category": "Coffee"},
    {"id": 19, "name": "Vanilla Latte", "price": 4.25, "currency": "USD", "category": "Coffee"},
    {"id": 20, "name": "Pumpkin Spice Latte", "price": 4.50, "currency": "USD", "category": "Coffee"},
    {"id": 21, "name": "Espresso Con Panna", "price": 3.00, "currency": "USD", "category": "Coffee"},
    {"id": 22, "name": "Affogato", "price": 4.75, "currency": "USD", "category": "Coffee/Dessert"},
    {"id": 23, "name": "Nitro Cold Brew", "price": 4.75, "currency": "USD", "category": "Coffee"},
    {"id": 24, "name": "Iced Americano", "price": 3.50, "currency": "USD", "category": "Coffee"},
    {"id": 25, "name": "Iced Black Tea", "price": 2.75, "currency": "USD", "category": "Tea"},
    {"id": 26, "name": "Lemonade", "price": 3.00, "currency": "USD", "category": "Cold Beverage"},
    {"id": 27, "name": "Iced Chai Latte", "price": 4.00, "currency": "USD", "category": "Tea"},
    {"id": 28, "name": "Orange Juice", "price": 3.50, "currency": "USD", "category": "Cold Beverage"},
    {"id": 29, "name": "Bottled Water", "price": 1.50, "currency": "USD", "category": "Cold Beverage"},
    {"id": 30, "name": "Croissant", "price": 2.75, "currency": "USD", "category": "Pastry"},
    {"id": 31, "name": "Muffin", "price": 2.50, "currency": "USD", "category": "Pastry"},
    {"id": 32, "name": "Bagel with Cream Cheese", "price": 3.00, "currency": "USD", "category": "Pastry"},
    {"id": 33, "name": "Banana Bread", "price": 3.25, "currency": "USD", "category": "Pastry"},
    {"id": 34, "name": "Chocolate Chip Cookie", "price": 1.75, "currency": "USD", "category": "Pastry"},
    {"id": 35, "name": "Oatmeal Cookie", "price": 1.75, "currency": "USD", "category": "Pastry"},
    {"id": 36, "name": "Blueberry Scone", "price": 3.00, "currency": "USD", "category": "Pastry"},
    {"id": 37, "name": "Cinnamon Roll", "price": 3.50, "currency": "USD", "category": "Pastry"},
    {"id": 38, "name": "Quiche", "price": 4.75, "currency": "USD", "category": "Savory"},
    {"id": 39, "name": "Ham & Cheese Croissant", "price": 4.50, "currency": "USD", "category": "Savory"},
    {"id": 40, "name": "Turkey Sandwich", "price": 5.00, "currency": "USD", "category": "Savory"},
    {"id": 41, "name": "Veggie Wrap", "price": 4.50, "currency": "USD", "category": "Savory"},
    {"id": 42, "name": "Chicken Salad", "price": 5.25, "currency": "USD", "category": "Savory"},
    {"id": 43, "name": "Greek Yogurt Parfait", "price": 4.00, "currency": "USD", "category": "Breakfast"},
    {"id": 44, "name": "Granola Bar", "price": 2.00, "currency": "USD", "category": "Snack"},
    {"id": 45, "name": "Fruit Cup", "price": 3.50, "currency": "USD", "category": "Snack"},
    {"id": 46, "name": "Almond Milk", "price": 0.75, "currency": "USD", "category": "Milk Alternative"},
    {"id": 47, "name": "Oat Milk", "price": 0.75, "currency": "USD", "category": "Milk Alternative"},
    {"id": 48, "name": "Soy Milk", "price": 0.75, "currency": "USD", "category": "Milk Alternative"},
    {"id": 49, "name": "Extra Shot of Espresso", "price": 1.00, "currency": "USD", "category": "Add-on"},
    {"id": 50, "name": "Whipped Cream", "price": 0.50, "currency": "USD", "category": "Add-on"},
    {"id": 51, "name": "Кава Їжачок", "price": 50, "currency": "USD", "category": "Кава"},
]


def save_to_file(data: list[Product], file_name: str, by_pickle=False) -> None:
    if not by_pickle:
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    else:
        with open(file_name, 'wb') as f:
            # noinspection PyTypeChecker
            pickle.dump(data, f)


def show_from_file(file_name: str, by_pickle=False) -> None:
    # Get data from file
    if not by_pickle:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        with open(file_name, 'rb') as f:
            data = pickle.load(f)

    # Display data
    for index, product in enumerate((data or [])):
        print(f'{index + 1}. {product['name']}, {product['price']} {product['currency']}')


if __name__ == '__main__':
    # Json
    # save_to_file(COFFEE_SHOP_PRODUCTS, 'products.json')
    # show_from_file('products.json')

    # Pickle
    save_to_file(COFFEE_SHOP_PRODUCTS, 'products.pkl', True)
    show_from_file('products.pkl', True)
