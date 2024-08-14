class Solution:
    #Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        dic={}
        for i in range(1,N+1):
            dic[i]=0
        for ele in arr:
            if(ele<=N):
                dic[ele]+=1
        i=0
        for v in dic.values():
            arr[i]=v
            i+=1
            
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == "__main__":
    T = int(input())
    while (T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        P = int(input())
        ob = Solution()
        ob.frequencyCount(arr, N, P)
        for i in arr:
            print(i, end=" ")
        print()
        T -= 1

# } Driver Code Ends