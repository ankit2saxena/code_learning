class Solution01:
    def is_valid(self, str):

        mapping = {"{": "}", "(": ")", "[": "]"}
        stack = []

        for char in str:
            if char in mapping:
                stack.append(char)
            elif stack and char == mapping[stack[-1]]:
                stack.pop()
            else:
                result = False
                break

        if not stack:
            result = True
        else:
            result = False

        return result


if __name__ == "__main__":
    input_s = "((()(())))"
    s = Solution01()
    print("Input: %s" % input_s)
    print("Result: %s" % s.is_valid(input_s))
