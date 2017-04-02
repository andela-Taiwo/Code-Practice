class ShoppingCart(object):
    total = 0
    items = {}

    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name,quantity,price):
        self.quantity = quantity
        self.price =price
        self.items[item_name] =  quantity
        self.total += price*quantity
        

    def remove_item(self, item_name,quantity,price):
        
        if(self.items.has_key(item_name)):
            if(self.items[item_name] <= quantity):
                del items[item_name]
                raise RunTimeError("You have exceeded the quantity")
                
            else:
                self.total
                self.items[item_name] -= quantity
                
                self.total -= (price*quantity)
                
                

    def checkout(self,cash_paid):
        if(cash_paid < self.total):
            return("Cash paid not enough")
        else:
            return(cash_paid - self.total)


class Shop(ShoppingCart):

    def __init__(self):
        self.quantity = 100
                
    def remove_item(self):
        
        self.quantity -=1

    
        
