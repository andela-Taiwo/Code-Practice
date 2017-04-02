class ShoppingCart(object):
  
  def __init__(self):
    
    self.total = 0
    self.items = dict()
    
  def add_item(self,item_name,quantity,price):
    self.items[item_name] = quantity
    self.price = price
    
    self.total += price*quantity
  
  def remove_item(self,item_name,quantity,price):
    if(self.items.has_key(item_name)) and (quantity >= self.items[item_name]):
        del self.items[item_name]

    elif(self.items.has_key(item_name)) and (quantity < self.items[item_name]):
      self.items[item_name] -=quantity
      self.total -= price*(quantity)
    else:
      raise RunTimeError("Items not in the cart")
      
  def checkout(self,cash_paid):
    if (cash_paid == type(int) or cash_paid ==type(float)):
      if(cash_paid < self.total):
        return("Cash paid not enough")
      else:
        return(cash_paid - self.total)

      


class Shop(ShoppingCart):
  
  def __init__(self):
    
    self.quantity = 100
    
  def remove_item(self):
    self.quantity -= 1
