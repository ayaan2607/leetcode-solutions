class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        highest = 0
        output = []
        for i in range(len(candies)):
            if candies[i] > highest:
                highest = candies[i]
        for j in range(len(candies)):
            if candies[j] + extraCandies >= highest:
                output.append(True)
            else:
                output.append(False)
        return output
