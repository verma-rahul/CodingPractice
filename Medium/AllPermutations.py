# Q : Given a String, return all of its permutations
# Example "ABC" => ["ABC","ACB","BCA","BAC","CAB","CBA"]
import sys

class Solution():
    def __init__(self):
        self.permutations_arr=[]
    def find_permutations(self,str):
        self.next_permutation("",str)

    def next_permutation(self,str,rest):
        if rest=='':
            self.permutations_arr.append(str)
            return
        for i in range(len(rest)):
            self.next_permutation(str+rest[i],rest[:i]+rest[i+1:])

    def print_permutations(self):
        for str in self.permutations_arr:
            print(str)

def main(args):
    permutations=Solution()
    permutations.find_permutations("ABCD")
    permutations.print_permutations()

if __name__=='__main__':
    main(sys.argv[1:])
