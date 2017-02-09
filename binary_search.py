
class BinarySearch(list):
    '''
        BinarySearch class inherits list class
    '''
    def __init__(self, a, b):
      '''
          Initialising method passes modifeid arguments a, b to the list class to initialise
          a number list object of length a and step b
      '''
      super(BinarySearch, self).__init__(range(0, (a * b) + 1, b)[1:])
      self.length = len(self)


    def search(self, item):
      '''
          Employs binary search algorithm to search a list for the item and returns a dictionary
          of {numner of iterations : index of item}. returns special results if item is last
          or second last in the list or doesnot exist in the list
      '''
      lower = 0
      upper = len(self)
      count = 0
      while lower < upper:
          if item == self[-1]:
              return  {'count':count, 'index': len(self) - 1} 
          elif item == self[-2]:
            return  {'count':count + 1, 'index': len(self) - 2}
          else: 
              x = lower + (upper - lower) // 2
              val = self[x]
              if item == val:
                  return {'count':count, 'index':x}
              elif item > val:
                  if lower == x:  
                      break        
                  lower = x
              elif item < val:
                  upper = x
          count += 1
      return {'count': 3, 'index':-1}
  
