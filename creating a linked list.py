
 Class Node:

     def_init_(self,dataval=None):

         self.dataval = dataval

         self.nextval = None

  Class SlinkedList:

      def_init_(self):

          self.headval = None

  List1=SLinkedList()

  List1.headval=Node("Mon")

  e2 =  Node("Tue")

  e3 = Node("Wed")

  # Link first  Node to second node
  list.headval.nextval = e2

  # Link second Node to third node

  e2.nextval = e3
