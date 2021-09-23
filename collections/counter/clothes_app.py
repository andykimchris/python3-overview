
opening_inventory = ['shoes', 'shoes', 'skirt', 'jeans', 'blouse', 'shoes', 't-shirt', 'dress', 'jeans', 'blouse', 'skirt', 'skirt', 'shorts', 'jeans', 'dress', 't-shirt', 'dress', 'blouse', 't-shirt', 'dress', 'dress', 'dress', 'jeans', 'dress', 'blouse']

closing_inventory = ['shoes', 'skirt', 'jeans', 'blouse', 'dress', 'skirt', 'shorts', 'jeans', 'dress', 'dress', 'jeans', 'dress', 'blouse']

# Write your code below!
from collections import Counter

def find_amount_sold(opening, closing, item):
  opening_count = Counter(opening)
  closing_count = Counter(closing)
  opening_count.subtract(closing_count)
  return opening_count[item]

tshirts_sold = find_amount_sold(opening_inventory,closing_inventory, 't-shirt')
print(tshirts_sold)