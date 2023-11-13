

class LongestCommonPrefix():

    def find_prefix(self, x):
        """
        Finds the most common prefix in a list of strings
        :param x: List of words
        :return: The longest most common prefix
        """
        longest_prefix = ""
        for letter in range(len(min(x, key=len))):
            prefix = x[0][letter]
            for i in range(len(x)):
                if x[i][letter] != prefix:
                    return longest_prefix
            longest_prefix += x[0][letter]
        return longest_prefix


LCP = LongestCommonPrefix()
lcp = LCP.find_prefix(["flow", "flower", "flight"])
print(lcp)
