
 Class Node:

     def_init_(self,dataval=None):
         self.dataval = dataval
         self.dataval = None

   Class SLinkedList:

       def_init_(self):
           self.headeval = None


  # Print SLinked list

    def listPrint(self):

        Printval = self.headval

        while printval is not None:

            print(printval.dataval)

            printval=printval.nextval

      def AtBegining(self,newdata)

         NewNode = Node(newdata)


   # Update the new next val to existing node

         NewNode.nextval = self.headval

         self.headval = NewNode

   List = SLinkedList()

   List.headval = Node("Mon")

   e2 = Node("Tue")

   e3 = Node("Wed")

   list.headval.nextval = e2

   e2.nextval = e3

   list.AtBegigining("Sun")
   
