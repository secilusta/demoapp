def search(array, element1, element2):
  if(array == None):
    return False
  else:
    for e in array:
      if str(e) == str(element1).strip(' '):
        for f in array:
          if str(f) == str(element2).strip(' '):
            return True
  return False
