import sys
import random
# Definition for singly-linked list.
class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution Class
class SortLinkList:

    @staticmethod
    def sortList(head):
        """
        Sorts The Link List and Returns the head of the list
        """
        end,mid=SortLinkList.find_mid(head)
        if end!=head:
            mid_next=mid.next
            mid.next=None
            head=SortLinkList.sortList(head)
            mid_next=SortLinkList.sortList(mid_next)
            return SortLinkList.merge(head,mid_next)
        else:
            return head


    @staticmethod
    def merge(st1,st2):
        """
        Merges Two Sorted list into one and
        returns the head of the Merged Sorted List
        """
        start=ListNode(0)
        curr=start
        while st1!=None and st2!=None:
            if st1.val<st2.val:
                curr.next=st1
                st1=st1.next
            else:
                curr.next=st2
                st2=st2.next
            curr=curr.next
        while st1!=None:
            curr.next=st1
            st1=st1.next
            curr=curr.next
        while st2!=None:
            curr.next=st2
            st2=st2.next
            curr=curr.next

        return start.next
    @staticmethod
    def find_mid(st):
        """
        Returns the Middle and End of the List
        """
        mid=st;end=st;
        while end.next!=None:
            end=end.next
            if end.next!=None:
                mid=mid.next
                end=end.next
        return end,mid


def main(args):
    head=generate_list_nodes(5)
    print_list(head)
    new_head=SortLinkList.sortList(head)
    print_list(new_head)


def print_list(list):
    while list!=None:
        print(list.val)
        list=list.next
    print("--end---")

def generate_list_nodes(size):
    head=ListNode(random.randint(1,10))
    curr=head
    for i in range(size-1):
        curr.next=ListNode(random.randint(1,10))
        curr=curr.next
    return head


ListNode(5),ListNode(10),ListNode(200),ListNode(0),ListNode(-9)
if __name__=="__main__":
    main(sys.argv[1:])
