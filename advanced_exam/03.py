def shopping_cart(*args):
    products = {}
    used_products = []
    pizza = 0
    soup = 0
    desert = 0
    for product in args:
        if product == "Stop":
            break
        food = product[0]
        ingredient = product[1]

        if ingredient not in used_products:
            used_products.append(ingredient)
            if food not in products.keys():
                products[food] = []
                if food == "Pizza":
                    if pizza > 4:
                        continue
                    pizza = pizza + 1

                elif food == "Soup":
                    soup += 1
                    if soup > 3:
                        continue
                elif food == "Desert":
                    desert += 1
                    if desert > 2:
                        continue
        else:
            continue
        products[food].append(ingredient)



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
products = {}
    used_ingredients = []
    for product in args:
        if product == "Stop":
            if not products:
                return "No products in the cart!"
            break
        food = product[0]
        ingredient = product[1]
        if food not in products:
            products[food] = []
        if ingredient not in used_ingredients:
            used_ingredients.append(ingredient)
            products[food].append(ingredient)
    return products
