#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        total=0
        max_len=0
        pre_sum={}
        
        for i in range(n):
            total=total+arr[i]
            
            if(total==k):
                max_len=i+1
                
            if(pre_sum.get(total-k,-1)!=-1):
                max_len=max(max_len,i-pre_sum[total-k])
            
            if(pre_sum.get(total,-1)==-1):
                pre_sum[total]=i
        
        return max_len
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends