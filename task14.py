def get_most_expensive_product(products: list[dict]) -> dict:
    mx_price = products[0]
    for i in products:
        if i['price'] > mx_price['price']:
            mx_price = i
        
    return mx_price


products = [
    {"name": "iPhone 15", "price": 1200, "category": "Electronics"},
    {"name": "Samsung TV", "price": 800, "category": "Electronics"},
    {"name": "Nike Shoes", "price": 150, "category": "Fashion"},
    {"name": "Adidas Shoes", "price": 120, "category": "Fashion"},
    {"name": "Couch", "price": 500, "category": "Furniture"},
    {"name": "Chair", "price": 100, "category": "Furniture"},
    {"name": "MacBook Pro", "price": 2000, "category": "Electronics"},
    {"name": "T-shirt", "price": 25, "category": "Fashion"},
    {"name": "Desk", "price": 220, "category": "Furniture"},
    {"name": "Monitor", "price": 300, "category": "Electronics"},
    {"name": "Keyboard", "price": 50, "category": "Electronics"},
    {"name": "Mouse", "price": 30, "category": "Electronics"},
    {"name": "Jeans", "price": 80, "category": "Fashion"},
    {"name": "Jacket", "price": 200, "category": "Fashion"},
    {"name": "Bed", "price": 700, "category": "Furniture"},
    {"name": "Lamp", "price": 60, "category": "Furniture"},
    {"name": "iPad", "price": 900, "category": "Electronics"},
    {"name": "Watch", "price": 250, "category": "Fashion"},
    {"name": "Bookshelf", "price": 400, "category": "Furniture"},
    {"name": "Headphones", "price": 180, "category": "Electronics"},
]


print(get_most_expensive_product(products))