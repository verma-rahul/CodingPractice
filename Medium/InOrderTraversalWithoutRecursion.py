# Q : Given a Tree, print it in order without Traversal
# Example:    1
#            / \
#           2   3     => 4 2 5 1 3
#          / \
#         4   5
import  sys
import random
# To set static Seed
random.seed(1)
class Node():
    """
    Node Struct
    """
    def __init__(self,val=None):
        self.val=val
        self.right=None
        self.left=None

class BinaryTree():
    def __init__(self,root=None):
        self.root=root
    def make_random_balnaced_tree(self,size):
        """
        Constructs a random Balanced Tree &
        prints as an Array
        Ex: [1,2,3,4,5] =>        1
                                 / \
                                2   3
                               / \
                              4   5
        """
        val=random.randint(0, 100)
        self.root=Node(val)
        stack=[self.root];size=size-1;arr_tree=[val]
        while size>0:
            node=stack.pop(0)
            val=random.randint(0,100)
            left=Node(val)
            arr_tree.append(val)
            node.left=left
            stack.append(left)
            size=size-1
            if size>0:
                val=random.randint(0,100)
                right=Node(val)
                node.right=right
                arr_tree.append(val)
                stack.append(right)
                size=size-1
        print("Balanced Tree as Array: ", arr_tree)

    def print_inorder(self):
        """
        Prints the Tree Inorder
        """
        stack=[self.root]
        node=self.root
        print("Inorder Traversal of Tree: ")
        while len(stack)>0:
            if node!=None and node.left!=None:
                stack.append(node.left)
                node=node.left
            else:
                poped=stack.pop()
                print(poped.val)
                node=poped.right
                if node!=None:
                    stack.append(node)


def main(args):
    tree=BinaryTree()
    tree.make_random_balnaced_tree(10)
    tree.print_inorder()


if __name__=='__main__':
    main(sys.argv[1:])
