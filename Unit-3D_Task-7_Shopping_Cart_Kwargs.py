def shopping_cart(**products):
    for item,price in products.items():
        print(f"{item}:${price}")
shopping_cart(orange=15,apple=12,banana=20)