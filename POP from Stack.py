Class Stack:

    def _init_(self):

        self.stack=[]

       def add(self,dataval):

#   Use list append method to add element

     if dataval not in self.stack:

         self.stack.append(dataval)

         return True
       esle:
          return False

 #  Use list pop method to remove element       

       def remove(self):

           if len(self.stack)<=0:

               return ("No element in the stack")
            else:
                return self.stack.pop()
