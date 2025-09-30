def get_average_price_per_category(products: list[dict]) -> dict[str, float]:
    grouped = {} 
    
    for product in products:
        category = product['category']
        price = product['price']

         # categoriya oldin bo`lmasa category nomli bitta kalit yaratib unga total va count
         # default 0 qiymati beramiz`
        if category not in grouped:
            grouped[category] = {"total": 0, "count": 0}

        # keyin esa category nomli kalitning total qiymatiga har bitta aylanishdagi price ni
        # qo`shib ketaveramiz va necha marta qushganimizni bilish uchun countga 1 qushib ketamiz
        grouped[category]["total"] += price
        grouped[category]["count"] += 1

    averages = {}
    #o`rtachasini hisoblasj uchun uni hamma itemlarini olvolamiz, key nomi uzi qoladi
    # va uni opshi total summasini countga bulamiz va urtacha qiymat category nomli keyga borib taminlanadi`
    for category, n in grouped.items():
        averages[category] = n["total"] / n["count"]

    return averages


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

print(get_average_price_per_category(products))

