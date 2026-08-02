class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        X=len(arr)
        for i in range(X-1):
          n=-1
          for j in range(i+1,X):
             n=max(n,arr[j])
          arr[i]=n

        arr[X-1]=-1
        return arr        