#User function Template for python3
class Solution:
    def print2largest(self, arr):
        l=0
        sl=0
        for i in range(len(arr)):
            if(arr[i]>sl and arr[i]!=l):
                if(arr[i]>l):
                    sl=l
                    l=arr[i]
                else:
                    sl=arr[i]
        return sl

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.print2largest(arr)
        print(ans)

# } Driver Code Ends