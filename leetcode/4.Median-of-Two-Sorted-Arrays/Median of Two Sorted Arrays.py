#Coding Utf-8
####################################################################################################################
#                                                                                                                  #
#      首先我们来看如何找到两个数列的第k小个数，即程序中getKth(A, B , k)函数的实现。                               #
#      用一个例子来说明这个问题：A = {1，3，5，7}；B = {2，4，6，8，9，10}；                                       #
#      如果要求第7个小的数，A数列的元素个数为4，B数列的元素个数为6；k/2 = 7/2 = 3，而A中的第3个数A[2]=5；          #       
#      B中的第3个数B[2]=6；而A[2]<B[2]；则A[0]，A[1]，A[2]中必然不可能有第7个小的数。                              #
#      因为A[2]<B[2]，所以比A[2]小的数最多可能为A[0], A[1], B[0], B[1]这四个数，                                   #
#      也就是说A[2]最多可能是第5个大的数，由于我们要求的是getKth(A, B, 7)；                                        #
#      现在就变成了求getKth(A', B, 4)；即A' = {7}；B不变，求这两个数列的第4个小的数，                              #
#      因为A[0]，A[1]，A[2]中没有解，所以我们直接删掉它们就可以了。这个可以使用递归来实现。                        #
#                                                                                                                  #
####################################################################################################################

def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1); l2 = len(nums2)
        if (l1 + l2) % 2 == 1: 
            return self.getKth(nums1, nums2, (l1 + l2)/2 + 1)
        else:
            return (self.getKth(nums1, nums2, (l1 + l2)/2) + self.getKth(nums1, nums2, (l1 + l2)/2 + 1)) * 0.5
    def getKth(self, nums1, nums2, k):
        l1 = len(nums1)
        l2 = len(nums2)
        if l1 > l2: return self.getKth(nums2, nums1, k)
        if l1 == 0 : return nums2[k-1]
        if k == 1: return min(nums1[0], nums2[0])
        pa = min(k/2, l1) 
        pb = k - pa
        if nums1[pa - 1] <= nums2[pb - 1]:
            return self.getKth(nums1[pa:], nums2, pb)
        else:
            return self.getKth(nums1, nums2[pb:], pa)
