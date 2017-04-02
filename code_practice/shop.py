from collections import OrderedDict

dico = OrderedDict()
price_list = dict()




for i in range(0,3):
    item_name = raw_input("enter the item name: ")
    item_quantity =int(raw_input("enter the quantity: "))
    item_price = float(raw_input("enter the unit price: "))
    
    if item_name in dico:
        dico[item_name] += item_quantity
    else:
        dico[item_name] = item_quantity
        price_list[item_name] = item_price

for k,v in dico.items():
    if item_name in price_list:
        cost = price_list[item_name]   * dico[k]
        print k ,v
        print cost

