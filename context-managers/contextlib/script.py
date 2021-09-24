# Write your code below:
from contextlib import contextmanager
# class PoemFiles
@contextmanager
def poem_files(file, mode):
  print('Opening File')
  open_poem_file = open(file, mode)
  try:
    yield open_poem_file
  finally:
    print('Closing File')
    open_poem_file.close()    

with poem_files('poem.txt', 'a') as opened_file:
 print('Inside yield')
 opened_file.write('Rose is beautiful, Just like you.')


