class Solution(object):
    def roman_to_int(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        tot = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                tot -= roman[s[i]]
                print(f'Subtracting int: {roman[s[i]]}, roman: {s[i]}')
            else:
                tot += roman[s[i]]
                print(f'Adding int: {roman[s[i]]}, roman: {s[i]}')
        tot += roman[s[-1]]
        return tot

    def roman_to_int_reversed(self, x):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tot = 0
        for rom in reversed(x):
            tot = 1
        return tot




solution = Solution()
roman_num = solution.roman_to_int_reversed('MCMXCIV')
print(roman_num)