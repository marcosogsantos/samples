class Node:
    def __init__(self,data):
        self.item = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.first_node = None
        
    def printList(self):
        if self.first_node == None:
            print('Empty list')
            return
        else:
            node = self.first_node
            while node is not None:
                print(node.item)
                node = node.next
    def insert_item_at_head(self,data):
        if self.first_node == None:
            self.first_node = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.first_node
            self.first_node.previous = new_node
            self.first_node = new_node
    def insert_item_at_end(self,data):
        if self.first_node == None:self.first_node = Node(data)
        else:
            last_node = self.first_node
            while last_node.next is not None:
                last_node = last_node.next
            new_node = Node(data)
            new_node.previous = last_node
            last_node.next = new_node
    def find_item(self,item_to_find):
        if self.first_node == None:print('Empty list')
        else:
            node = self.first_node
            while node is not None:
                if node.item == item_to_find:
                    if node.previous:
                        print('After: {}'.format(node.previous.item))
                    print('{} was found in memory {}'.format(node.item,hex(id(node))))
                    if node.next:
                        print('Before: {}'.format(node.next.item))
                    break
                node = node.next
            return node
ml = DoublyLinkedList()
ml.insert_item_at_head(1)
ml.insert_item_at_head(2)
ml.insert_item_at_head(3)
ml.insert_item_at_end(4)
ml.insert_item_at_end(5)
ml.printList()
