def search(array, element1, element2):
  for e in array:
    if e == element1:
      for f in array:
        if f == element2:
          return True
  return False
