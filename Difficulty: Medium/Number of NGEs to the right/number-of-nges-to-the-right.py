#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        # Code here
        res=[0]*queries
        for i in range(len(indices)):
            q=indices[i]
            for j in range(q+1,N):
                if arr[j]>arr[q]:
                    res[i]+=1
        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        queries = int(input())
        indices = list(map(int, input().split()))
        ob = Solution()
        NGEs = ob.count_NGEs(N, arr, queries, indices)
        for val in NGEs:
            print(val, end = ' ')
        print()
        print("~")
# } Driver Code Ends