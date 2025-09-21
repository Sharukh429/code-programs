
Class Queue:

    def_init_(self):

        self.queue=list()

     def addtoq(self,dataval):

  # Insert method to add element

      if dataval not in self.queue:

          self.queue.insert(0,dataval)

          return True

        return False

    def size(self):

        return len(self.queue)
    
