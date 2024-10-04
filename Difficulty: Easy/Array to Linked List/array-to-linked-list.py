#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
# Node Class

class Solution:
    
    def constructLL(self, arr):
        root:Node = None
        last:Node=None
        
        for item in arr:
            new=Node(item)
            if root is None:
                root=new
                last=root
            else:
                last.next=new
                last=new
        return root
            
            

#{ 
 # Driver Code Starts.
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        # n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.constructLL(arr)
        while res:
            print(res.data, end = ' ')
            res = res.next
        print()
# } Driver Code Ends