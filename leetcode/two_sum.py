def twoSum(nums, target):
        my_map = {}

        for i in range(len(nums)):
            compliment = target - nums[i]

            if compliment in my_map:
                  return [my_map[compliment], i]

            my_map[nums[i]] = i

        return []