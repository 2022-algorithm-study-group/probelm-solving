class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        # 1 <= n <= 200
        # [nums1,nums2] [nums3,num4] 분할정복
        ans = 0
        nums_1_2_counter = {}
        nums_3_4_counter = {}
        for n1 in nums1:
            for n2 in nums2:
                nums_1_2_counter[n1 + n2] = nums_1_2_counter.get(n1 + n2, 0) + 1
        for n3 in nums3:
            for n4 in nums4:
                nums_3_4_counter[n3 + n4] = nums_3_4_counter.get(n3 + n4, 0) + 1
        ans = 0
        for k, v in nums_1_2_counter.items():
            ans += v * nums_3_4_counter.get(-k, 0)
        return ans
