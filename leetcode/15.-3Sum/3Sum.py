class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        sortnum = sorted(nums)
        length = len(sortnum)
        # make sure a < b < c
        for i in xrange(length-2):
            a = sortnum[i]
            # remove duplicate a
            if i >= 1 and a == sortnum[i-1]:
                continue
            j = i + 1
            k = length - 1
            while j < k:
                b = sortnum[j]
                c = sortnum[k]
                if b + c == -a:
                    res.append([a,b,c])
                    # remove duplicate b,c
                    while j < k:
                        j += 1
                        k -= 1
                        if sortnum[j] != b or sortnum[k] != c:
                            break
                elif b + c > -a:
                    # remove duplicate c
                    while j < k:
                        k -= 1
                        if sortnum[k] != c:
                            break
                else:
                    # remove duplicate b
                    while j < k:
                        j += 1
                        if sortnum[j] != b:
                            break
        return res
