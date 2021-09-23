clothes = [('t-shirt', 'green', 'large', 9.99),
           ('jeans', 'blue', 'medium', 14.99),
           ('jacket', 'black', 'x-large', 19.99),
           ('t-shirt', 'grey', 'small', 8.99),
           ('shoes', 'white', '12', 24.99),
           ('t-shirt', 'grey', 'small', 8.99)]

from collections import namedtuple
ClothingItem = namedtuple('ClothingItem', ['type','color','size','price'])

new_coat = ClothingItem('coat','black','small',14.99)
coat_cost = new_coat[3]

updated_clothes_data = []
for cloth in clothes:
  updated_clothes_data.append(ClothingItem(cloth[0],cloth[1],cloth[2],cloth[3]))

print(updated_clothes_data)