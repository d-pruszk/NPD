def set_sum(list1,list2):
  temp = 0
  result = list1
  for i in range(len(list2)):
    temp = 0
    curr = list2[i]
    for j in range(len(list1)):
      if curr == list1[j]:
        temp = 1
        break
    if temp == 0:
      result.append(curr)
  return(result)

print("set_sum([1, 2, 3], [1, 2, 3]) == ", set_sum([1, 2, 3], [1, 2, 3]))
print("set_sum([], [1, 2, 3]) == ", set_sum([], [1, 2, 3]))
print("set_sum([1, 2, 3], []) == ", set_sum([1, 2, 3], []))
print("set_sum([1, 3, -2], [-2, -3, 0, 1, 34]) == ", set_sum([1, 3, -2], [-2, -3, 0, 1, 34]))

def sorted_set_sum(list1,list2):
  temp1=0
  temp2 = 0
  result = []
  for i in range(temp1,len(list2)):
    for j in range(temp2,len(list1)):
      if list2[i] == list1[j]:
        result.append(list1[j])
        temp1=temp1+1
        temp2=temp2+1
        break
      elif list2[i] < list1[j]:
        result.append(list2[i])
        temp1=temp1+1
        break
      else:
        result.append(list1[j])
        temp2=temp2+1
  for i in range(temp2,len(list1)):
    result.append(list1[i])
  for i in range(temp1,len(list2)):
    result.append(list2[i])
  return(result)

print("sorted_set_sum([], []) == ", sorted_set_sum([], []))
print("sorted_set_sum([1, 2, 3], [1, 2, 3]) == ", sorted_set_sum([1, 2, 3], [1, 2, 3]))
print("sorted_set_sum([], [1, 2, 3]) == ", sorted_set_sum([], [1, 2, 3]))
print("sorted_set_sum([1, 2, 3], []) == ", sorted_set_sum([1, 2, 3], []))
print("sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]) == ", sorted_set_sum([-2, 1, 3], [-3, -2, 0, 1, 34]))