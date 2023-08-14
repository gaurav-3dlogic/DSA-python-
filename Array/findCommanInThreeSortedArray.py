class Solution:
    def commonElements(self, ar1, ar2, ar3):
        i, j, k = 0, 0, 0
        ans = []
        prev1 = prev2 = prev3 = float('-inf')
        
        while i < len(ar1) and j < len(ar2) and k < len(ar3):
            
            while ar1[i] == prev1 and i < len(ar1):
                i += 1
            
            while ar2[j] == prev2 and j < len(ar2):
                j += 1
            
            while ar3[k] == prev3 and k < len(ar3):
                k += 1
            
            if ar1[i] == ar2[j] == ar3[k]:
                ans.append(ar1[i])
                prev1 = ar1[i]
                prev2 = ar2[j]
                prev3 = ar3[k]
                i += 1
                j += 1
                k += 1
            
            elif ar1[i] < ar2[j]:
                prev1 = ar1[i]
                i += 1
            
            elif ar2[j] < ar3[k]:
                prev2 = ar2[j]
                j += 1
            
            else:
                prev3 = ar3[k]
                k += 1
        
        return ans
        
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Create an instance of the Solution class
solution = Solution()

# Call the commonElements function
common_elements = solution.commonElements(ar1, ar2, ar3)

# Print the common elements
print("Common Elements:", common_elements)


#output Common Elements: [20, 80]