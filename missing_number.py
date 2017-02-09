
def find_missing(list1, list2):
  '''
  Finds and returns the extra element that is in one ofthe lists: list1 or list 2
  Returns zero if the lists are empty or have same elements
  '''
  if not (list1 and list2) or list1 == list2: 
      return 0
  elif len(list1) > len(list2):
      difference= set(list1).difference(set(list2)) # use the difference method of the set type
      return difference.pop() # the only element left in difference will be removed and returned
  else:
      difference= set(list2).difference(set(list1))
      return difference.pop()
