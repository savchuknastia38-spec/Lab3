# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
products = [
    {"id": 1, "name": "Ноутбук", "price": 25000.00, "stock": 5},
    {"id": 2, "name": "Навушники", "price": 1500.50, "stock": 10},
    {"id": 3, "name": "Мишка", "price": 800.00, "stock": 15},
    {"id": 4, "name": "Клавіатура", "price": 1200.99, "stock": 7}
]

cart = []


def show_catalog():
    print("\n=== КАТАЛОГ ===")

    for product in products:
        print(
            f"{product['id']}. {product['name']} — "
            f"{product['price']:.2} грн | "
            f"Залишок: {product['stock']}"
        )
def add_to_cart():
    show_catalog()

    try:
        product_id = int(input("Введіть ID товару: "))

        product = next(
            (p for p in products if p["id"] == product_id),
            None
        )

        if product is None:
            print("Такого товару немає.")
            return

        if product["stock"] <= 0:
            print("Товару немає в наявності.")
            return

        cart.append(product)
        product["stock"] -= 1

        print(f"{product['name']} додано до кошика.")

    except ValueError:
        print("Введіть число.")
def show_cart():
    print("\n=== КОШИК ===")

    if not cart:
        print("Кошик порожній.")
        return

    total = 0

    for index, product in enumerate(cart, 1):
        print(
            f"{index}. {product['name']} — "
            f"{product['price']:.2f} грн"
        )
        total += product["price"]

    print(f"Разом: {total:.2f} грн")
def remove_from_cart():
    show_cart()

    if not cart:
        return

    try:
        number = int(input("Введіть номер товару для видалення: "))

        if number < 1 or number > len(cart):
            print("Неправильний номер.")
            return

        product = cart.pop(number - 1)
        product["stock"] += 1

        print(f"{product['name']} видалено з кошика.")

    except ValueError:
        print("Введіть число.")
def buy_products():
    if not cart:
        print("Кошик порожній.")
        return

    show_cart()

    answer = input("Підтвердити покупку? (так/ні): ").lower()

    if answer == "так":
        cart.clear()
        print("Покупку успішно оформлено!")

    else:
        print("Покупку скасовано.")
def admin_login():
    password = input("Введіть пароль адміністратора: ")

    if password != "admin123":
        print("Неправильний пароль.")
        return

    print("\n=== ПАНЕЛЬ АДМІНІСТРАТОРА ===")

    for product in products:
        print(
            f"{product['name']} — "
            f"залишок: {product['stock']}"
        )
def sort_products():
    sorted_products = sorted(
        products,
        key=lambda item: item["price"]
    )

    print("\n=== ТОВАРИ ЗА ЦІНОЮ ===")

    for product in sorted_products:
        print(
            f"{product['name']} — "
            f"{product['price']:.2} грн"
        )
def main():
    while True:
        print("\n=== МІНІ-МАГАЗИН ===")
        print("1. Переглянути каталог")
        print("2. Додати товар у кошик")
        print("3. Переглянути кошик")
        print("4. Видалити товар з кошика")
        print("5. Купити товари")
        print("6. Увійти як адміністратор")
        print("7. Сортувати товари за ціною")
        print("0. Вийти")

        choice = input("Оберіть дію: ")

        if choice == "1":
            show_catalog()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            show_cart()

        elif choice == "4":
            remove_from_cart()

        elif choice == "5":
            buy_products()

        elif choice == "6":
            admin_login()

        elif choice == "7":
            sort_products()

        elif choice == "0":
            print("До побачення!")
            break

        else:
            print("Невірний вибір.")
if __name__ == "__main__":
    main()
cart = []
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
