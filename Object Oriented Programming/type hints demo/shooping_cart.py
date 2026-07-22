from product import Product

class ShoppingCartItem:
    def __init__(self, product: Product, quantity:int=1) -> None:
        self.product = product
        self.quantity = quantity
    
class ShoppingCart:
    def __init__(self):
        self.items: list[ShoppingCartItem] = []
    
    def add_product(self, product: Product) -> None:
        existing_item = None 

        for item in self.items:

            if item.product.name == product.name:
                existing_item = item
            
            if existing_item is not None:
                existing_item.quantity += 1
            else:
                new_item = ShoppingCartItem(product)
                self.items.append(new_item)
    
    def total_price(self) -> float:
        total = 0

        for item in self.items:
            total += item.price * item.quantity

        return total
    
