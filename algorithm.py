def search(array, element1, element2):
  if array is None:
    return False
  if element1 is None or element2 is None:
    return False
  for e in array:
    if e == element1:
      for f in array:
        if f == element2:
          return True
  return False
