
 def bsearch(list,val):

     list_size = len(list)-1

     idx0 = 0

     idxn = List_Size

 # Find the middle most value

    while idx= <= idxn:

        midval = (idx0 + idxn)//2

        if List[midval] == val:

            return midval
# Compare the value the most value

     if val>List[midval]:

         idx0 = midval+1
      else:
         idxn = midval-1

      if idxn > idxn:

          return None

  # Intilize the sorted list

  list = [1,2,3,4,5]

  # Print the search result

  print(bsearch(list,12))
  print(bsearch(list,11))
