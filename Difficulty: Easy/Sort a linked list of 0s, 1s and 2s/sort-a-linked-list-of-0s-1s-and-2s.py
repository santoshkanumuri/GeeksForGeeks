#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        cur=head
        zero=Node(0)
        one=Node(0)
        two=Node(0)
        z=zero
        o=one
        t=two
        while cur:
            if cur.data==0:
                z.next=Node(0)
                z=z.next
            if cur.data==1:
                o.next=Node(1)
                o=o.next
            if cur.data==2:
                t.next=Node(2)
                t=t.next
            cur=cur.next
        o.next=two.next
        z.next=one.next
        
        return zero.next
                
                
        #code here
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))

# } Driver Code Ends