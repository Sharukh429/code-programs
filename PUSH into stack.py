
class stack:

    def_init_(self):
        self.stack=[]

      def add(self,dataval):

 # Use list append method to add element

         if dataval not in self.stack:

             self.stack.append(data val)

             return True
           else:
               return False
   # Use peek to look at the top of the stack

       def peek(self):

           return self.stack[-1]


 AStack = Stack()

 AStack.add("Mon")

 AStack.add("Tue")

 AStack.peek()
