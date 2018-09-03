class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums1=copy.deepcopy(nums)
        nums1.sort()
        first=0
        last=len(nums1)-1
        while first<last:
            summ=nums1[first]+nums1[last]
            if summ > target:
                last=last-1
            elif summ < target:
                first=first+1
            elif summ == target:
                firstr=nums.index(nums1[first])
                nums[firstr]=None
                lastr=nums.index(nums1[last])
                return [firstr,lastr]
        return -1
        
        
