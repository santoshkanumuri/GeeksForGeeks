#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        i=0
        j=0
        temp=[]
        t=0
        while(i<n and j<m):
            if(arr1[i]<=arr2[j]):
                if(t==0 or temp[-1]!=arr1[i]):
                    temp.append(arr1[i])
                i+=1
                t+=1
            else:
                if(t==0 or temp[-1]!=arr2[j]):
                    temp.append(arr2[j])
                j+=1
                t+=1
                
        while(i<n):
            if(temp[-1]!=arr1[i]):
                temp.append(arr1[i])
            i+=1
                
        while(j<m):
            if(temp[-1]!=arr2[j]):
                temp.append(arr2[j])
            j+=1
            
        return temp
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends
