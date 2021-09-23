from helper_functions import process_csv_supplies
from collections import deque

# The first row is skipped since it only contains labels
csv_data = process_csv_supplies()[1:]

# Here is a sample of 2 elements in csv_data:
# [ ['nylon', '10', 'unimportant'], ['wool', '1', 'important'] ]


supplies_deque = deque()
for data in csv_data:
  if data[2] == 'important':
    supplies_deque.appendleft(tuple(data))
  else:
    supplies_deque.append(tuple(data))


ordered_important_supplies = deque()
for i in range(1, 26):
  popped = supplies_deque.popleft()
  ordered_important_supplies.appendleft(popped)

print(ordered_important_supplies)

ordered_unimportant_supplies = deque()
for i in range(1, 11):
  popped = supplies_deque.pop()
  ordered_unimportant_supplies.appendleft(popped)
  

print(ordered_unimportant_supplies)
