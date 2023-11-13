
class ValidParentheses:
    def is_valid(self, s):
        """

        :param s:
        :return:
        """
        stack = []
        opening = '([{'
        if len(s) <= 1:
            return False
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                print(stack[-1], char)
                if char == ']' and '[' != stack[-1]:
                    return False
                if char == '}' and '{' != stack[-1]:
                    return False
                if char == ')' and '(' != stack[-1]:
                    return False
                stack.pop()
        print(stack)
        return not stack

validP = ValidParentheses()
valid = validP.is_valid("(([]){})")
print(valid)

