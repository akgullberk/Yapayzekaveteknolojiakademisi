class Product:
    def __init__(self, name: str, price:float,in_stock:bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock

if __name__ == "__main__":
    external_data = {
        "name": "Laptop",
        "price": 123,
        "in_stock": False
    }

product = Product(
    name = external_data.get("name"),
    price = external_data.get("price"),
    in_stock = external_data.get("in_stock")
)

print(type(product.name))
print(type(product.price))
print(type(product.in_stock))
