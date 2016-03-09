# -*- coding: utf-8 -*-
#利用字典进行优化
def twoSum(self, nums, target):
        i =  0
        dnums = {}
        while i < len(nums):
            dnums[nums[i]] = i
            i = i + 1

        i = 0
        result = []
        while i < len(nums):
            if dnums.get(target-nums[i]) and dnums.get(target-nums[i]) != i:
                if dnums.get(target-nums[i]) > i:
                    result.append(i+1)
                    result.append(dnums.get(target-nums[i])+1)
                    break
                else:
                    result.append(i+1)
                    result.append(dnums.get(target-nums[i])+1)
                    break
            i = i + 1

        return result
