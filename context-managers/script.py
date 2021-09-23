# Write your code below:
class PoemFiles:
  def __init__(self, poem_file, mode):
    print('Starting up a poem context manager')
    self.file = poem_file
    self.mode = mode
  
  def __enter__(self):
    print('Opening poem file')
    self.opened_poem_file = open(self.file, self.mode)
    return self.opened_poem_file

  def __exit__(self, exc_type, exc_value, traceback):
    print(exc_type, exc_value, traceback, '\n')
    # Write your code below:
    if isinstance(exc_value, AttributeError):
      self.opened_poem_file.close()
      return True


with PoemFiles('poem.txt', 'w') as open_poem_file:
   open_poem_file.write('Hope is the thing with feathers')



with PoemFiles('poem.txt', 'r') as file:
  print("---- Exception data below ---- \n ")
  print(file.uppercasewords())

with PoemFiles('poem.txt', 'r') as file2:
  print(file2.read())
  print(" \n ---- Exception data below ---- \n ")


