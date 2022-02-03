def targetSum(items, targetSum):
  itemsList = []
  
  for item in items:
    for currentItem in items:
      sum = item + currentItem
      
      if (sum == targetSum):
      
        if item != currentItem:
    
          if (item not in itemsList):
            itemsList.append(item)
           
          if (currentItem not in itemsList):
            itemsList.append(currentItem)
            
  return itemsList
       
print(targetSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
