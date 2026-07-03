class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # -4, -1, -1, 0, 1, 2
        sol = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while (left < right):
                sums = nums[i] + nums[left] + nums[right]

                if (sums == 0):
                    sol.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                elif (sums < 0):
                    left += 1

                else:
                    right -= 1

        return sol
