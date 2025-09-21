
Class queue:

    def_init_(self):

        self.queue=list()


      def addtoq(self,dataval):

 # Insert method to add element

        if dataval not in self.queue:

            self.queue.insert(0,dataval)

            return True

        return False

  # pop method to remove element

    def removefromq(self):

        if len(self.queue)0:

            return self.queue.pop()
        return("No elements in queue!")
