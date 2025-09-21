
Class Node:

    def_init_(self,data=None):

        self.data = data

        self.next = None

Class SLinkedList:
    def_init_(self):
        self.head=None

     def Atbegining(self,data_in)

     NewNode = Node(data_in)

     NewNode.next = NewNode

 #Function to remove node

     def RemoveNode(self,RemoveKey):

         HeadVal = self.head

         if(headVal is not None):

             if(HeadVal.data == RemoveKey):

                  self.head =   HeadVal.next

                      HeadVal = None

                      return

             While (HeadVal is not None):

                 if HeadVal.data == RemoveKey:

                     break

                  prev = HeadVal

                  HeadVal = HeadVal.next

                  if(HeadVal == None):

                      returm
