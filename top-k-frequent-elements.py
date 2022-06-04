class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #create a dictionary and store the frequency of all nums
        num_frequencies = {}
        most_nums = []

        #loop through and append k amount, any after remove min
        for number in nums:
            if number in num_frequencies:
                num_frequencies[number] += 1
            else:
                num_frequencies[number] = 1

        while k > 0:
            #grab current max
            max_key = max(num_frequencies, key=num_frequencies.get)
            #remove current max
            num_frequencies.pop(max_key)
            #append current max
            most_nums.append(max_key)
            #lower amount needed
            k = k - 1

        return most_nums
