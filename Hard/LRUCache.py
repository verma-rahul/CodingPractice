import sys
import random
class DoubleLinkNode:
    """
    Node Class with Value, previous and next pointers
    """
    def __init__(self,val=None):
        self.__val=val
        self.__next=None
        self.__prev=None
    def get_next(self):
        return self.__next
    def set_next(self,node):
        self.__next=node
    def get_prev(self):
        return self.__prev
    def set_prev(self,node):
        self.__prev=node
    def get_val(self):
        return self.__val
    def set_val(self,value):
            self.__val=value



class LRUCache:
    """
    Cache Class which saves most recently used size items

    Attributes:
    self.__size: Size of Cache
    self.__start_list: Start of the Double Link List
    self.__end_list: End of the Double Link List
    self.__map: HashMap to Store all Values present in cache

    """
    def __init__(self,size=5):
        self.__size=size
        self.__start_list=None
        self.__end_list=None
        self.__map=dict()
    def get(self,key):
        if key not in self.__map:
            return -1
        if self.__end_list.get_val()==key:
            return 1
        node=self.__map[key]
        if self.__start_list.get_val()!=key:
            node.get_prev().set_next(node.get_next())
        else:
            self.__start_list=node.get_next()
        node.get_next().set_prev(node.get_prev())
        self.__end_list.set_next(node)
        node.set_prev(self.__end_list);node.set_next(None)
        self.__end_list=node
        return 1

    def put(self,key):
        if self.__start_list==None:
            self.__start_list=DoubleLinkNode(key)
            self.__end_list=self.__start_list
            self.__map[key]=self.__end_list
            return
        if key in self.__map:
            self.get(key)
            return
        if len(self.__map)>=self.__size:
            prev_key=self.__start_list.get_val()
            self.__start_list=self.__start_list.get_next()
            self.__start_list.set_prev(None)
            del self.__map[prev_key]
        self.__end_list.set_next(DoubleLinkNode(key))
        self.__end_list.get_next().set_prev(self.__end_list)
        self.__end_list=self.__end_list.get_next()
        self.__map[key]=self.__end_list

    def print_cache(self):
        run=self.__start_list
        while run!=None:
            print(run.get_val())
            run=run.get_next()


def main(args):
    run_demo_test()



def run_demo_test():
    cache=LRUCache(3)
    cache.put(1)
    cache.put(2)
    cache.put(3)
    cache.print_cache()
    print("--------------")
    cache.put(1)
    cache.print_cache()
    print("--------------")
    cache.put(4)
    cache.print_cache()
    print("--------------")
    cache.put(3)
    cache.print_cache()
    print("--------------")


if __name__=="__main__":
    main(sys.argv[1:])
