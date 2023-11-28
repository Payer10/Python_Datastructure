
class Solution:
    def kThSmallestFactor(self, N , K):
        # code here 
        l=[]
        i=1
        while i<=N:
            if N%i==0:
                l.append(i)
        if len(l)<=K:
            return -1
        else:
            return l[K-1]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        
        ob = Solution()
        print(ob.kThSmallestFactor(N,K))
# } Driver Code Ends