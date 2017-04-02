"""
ST2: OBJECT ORIENTED PROGRAMMING LAB

Create a class called ShoppingCart.

Create a constructor that takes no arguments and sets the total attribute to zero, and initializes an empty dict attribute named items.

Create a method add_item that requires item_name, quantity and price arguments. This method should add the cost of the added items to the current value of total. It should also add an entry to the items dict such that the key is the item_name and the value is the quantity of the item.

Create a method remove_item that requires similar arguments as add_item. It should remove items that have been added to the shopping cart and are not required. This method should deduct the cost of the removed items from the current total and also update the items dict accordingly.

If the quantity of an item to be removed exceeds the current quantity of that item in the cart, assume that all entries of that item are to be removed.

Create a method checkout that takes in cash_paid and returns the value of balance from the payment. If cash_paid is not enough to cover the total, return "Cash paid not enough".

Create a class called Shop that has a constructor which takes no arguments and initializes an attribute called quantity at 100.

Make sure Shop inherits from ShoppingCart.

In the Shop class, override the remove_item method, such that calling Shop's remove_item with no arguments decrements quantity by one.



"""

import unittest

from shoppingcart2 import ShoppingCart
from shoppingcart2 import Shop

class ShoppingCartTestCases(unittest.TestCase):
  def setUp(self):
    self.cart = ShoppingCart()
    self.shop = Shop()
    
  def test_cart_property_initialization(self):
    self.assertEqual(self.cart.total, 0, msg='Initial value of total not correct')
    self.assertIsInstance(self.cart.items, dict, msg='Items is not a dictionary')
    
  def test_add_item(self):
    self.cart.add_item('Mango', 3, 10)
    
    self.assertEqual(self.cart.total, 30, msg='Cart total not correct after adding items')
    self.assertEqual(self.cart.items['Mango'], 3, msg='Quantity of items not correct after adding item')
    
  def test_remove_item(self):
    self.cart.add_item('Mango', 3, 10)
    self.cart.remove_item('Mango', 2, 10)
    
    self.assertEqual(self.cart.total, 10, msg='Cart total not correct after removing item')
    self.assertEqual(self.cart.items['Mango'], 1, msg='Quantity of items not correct after removing item')
    
  def test_checkout_returns_correct_balance(self):
    self.cart.add_item('Mango', 3, 10)
    self.cart.add_item('Orange', 16, 10)
    
    self.assertEqual(self.cart.checkout(265), 75, msg='Balance of checkout not correct')
    self.assertEqual(self.cart.checkout(25), 'Cash paid not enough', msg='Balance of checkout not correct')
    
  def test_shop_is_instance_of_shopping_cart(self):
    self.assertTrue(isinstance(self.shop, ShoppingCart), msg='Shop is not a subclass of ShoppingCart')

  def test_shop_remove_item_method(self):
    for i in range(15):
      self.shop.remove_item()

    self.assertEqual(self.shop.quantity, 85)
    
if __name__ == '__main__':
    unittest.main()
