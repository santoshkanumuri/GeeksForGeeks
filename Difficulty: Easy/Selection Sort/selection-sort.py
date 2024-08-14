#User function Template for python3

class Solution: 
    def select(self, arr, i):
        leng=len(arr)
        min_pos=i
        for j in range(min_pos,leng):
            if(arr[j]<arr[min_pos]):
                min_pos=j
        return min_pos
    
    def selectionSort(self, arr,n):
        leng=len(arr)
        
        for i in range(leng):
            min_pos=i
            min_pos=self.select(arr,min_pos)
                    
            arr[i],arr[min_pos]=arr[min_pos],arr[i]
        
        
        
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends