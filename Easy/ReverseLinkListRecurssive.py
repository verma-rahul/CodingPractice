import sys
import random

random.seed(1)
class Node():
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class LinkList():
    def __init__(self,head=None):
        self.head=head
    @staticmethod
    def get_random_list(size):
        head=Node(random.randint(0,100))
        node=head
        for i in range(size-1):
            node.next=Node(random.randint(0,100))
            node=node.next
        return head

    @staticmethod
    def print_list(head):
        while head!=None:
            print(head.val)
            head=head.next

    def reverse_list(self):
        if self.head!=None:
            self.change_order(self.head,None)

    def change_order(self,curr,prev):
        if curr.next!=None:
            self.change_order(curr.next,curr)
        else:
            self.head=curr
        curr.next=prev


def main(args):
    list=LinkList(LinkList.get_random_list(5))
    print("-----Original List------")
    LinkList.print_list(list.head)
    list.reverse_list()
    print("-----Reverse List------")
    LinkList.print_list(list.head)










if __name__=="__main__":
    main(sys.argv[1:])
