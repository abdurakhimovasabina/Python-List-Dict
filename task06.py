def get_unique_countries(users: list[dict]) -> list[str]:
 
    countries = []
    for u in users:
        country = u["country"]
        if country not in countries:
            countries.append(country)
    return countries


users = [
    {"name": "Ali", "email": "ali0@gmail.com", "age": 25, "phone": "+998901234567", "country": "Uzbekistan"},
    {"name": "Vali", "email": "vali1@yahoo.com", "age": 32, "phone": "+998911112233", "country": "USA"},
    {"name": "Gani", "email": "gani2@hotmail.com", "age": 41, "phone": "+998933334455", "country": "UK"},
    {"name": "Sami", "email": "sami3@mail.ru", "age": 29, "phone": "+998944445566", "country": "Germany"},
    {"name": "Madina", "email": "madina4@outlook.com", "age": 21, "phone": "+998955556677", "country": "France"},
    {"name": "Aziza", "email": "aziza5@gmail.com", "age": 38, "phone": "+998966667788", "country": "Uzbekistan"},
    {"name": "Lola", "email": "lola6@yahoo.com", "age": 27, "phone": "+998977778899", "country": "USA"},
    {"name": "Zarina", "email": "zarina7@hotmail.com", "age": 30, "phone": "+998988889900", "country": "UK"},
    {"name": "Kamol", "email": "kamol8@mail.ru", "age": 22, "phone": "+998901112223", "country": "Germany"},
    {"name": "Umid", "email": "umid9@outlook.com", "age": 35, "phone": "+998912223344", "country": "France"},
    {"name": "Bekzod", "email": "bekzod10@gmail.com", "age": 28, "phone": "+998923334455", "country": "Uzbekistan"},
    {"name": "Dilshod", "email": "dilshod11@yahoo.com", "age": 40, "phone": "+998934445566", "country": "USA"},
    {"name": "Nodir", "email": "nodir12@hotmail.com", "age": 24, "phone": "+998945556677", "country": "UK"},
    {"name": "Shahnoza", "email": "shahnoza13@mail.ru", "age": 26, "phone": "+998956667788", "country": "Germany"},
    {"name": "Nigora", "email": "nigora14@outlook.com", "age": 31, "phone": "+998967778899", "country": "France"},
    {"name": "Sevinch", "email": "sevinch15@gmail.com", "age": 23, "phone": "+998978889900", "country": "Uzbekistan"},
    {"name": "Laziz", "email": "laziz16@yahoo.com", "age": 36, "phone": "+998989990011", "country": "USA"},
    {"name": "Anvar", "email": "anvar17@hotmail.com", "age": 33, "phone": "+998901223344", "country": "UK"},
    {"name": "Javlon", "email": "javlon18@mail.ru", "age": 20, "phone": "+998912334455", "country": "Germany"},
    {"name": "Diyor", "email": "diyor19@outlook.com", "age": 39, "phone": "+998923445566", "country": "France"},
]

print(get_unique_countries(users))
