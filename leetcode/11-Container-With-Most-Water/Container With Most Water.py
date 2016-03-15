class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j,maxs=0,len(height)-1,0
        while True:
            if i == j:
                break
            if height[i] < height[j]:
                maxs = max(maxs, height[i] * (j - i))
                i += 1
            else:
                maxs = max(maxs, height[j] * (j - i))
                j -= 1
        return maxs
