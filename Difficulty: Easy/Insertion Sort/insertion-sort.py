#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        key=alist[index+1]
        while index>=0 and alist[index]>key:
            alist[index+1]=alist[index]
            index-=1
        alist[index+1]=key
        
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        l=len(alist)
        for i in range(1,l):
            j=i-1
            self.insert(alist,j,len(alist))
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        Solution().insertionSort(arr, n)

        for i in range(n):
            print(arr[i], end=" ")

        print()

# } Driver Code Ends