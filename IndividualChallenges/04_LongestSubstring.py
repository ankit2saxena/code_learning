class Solution04:
    def longest_substring(self, s):
        substring = []
        temp_long = []
        for c in s:
            if c in substring:
                substring = substring[substring.index(c) + 1:]

            substring.append(c)

            if len(substring) > len(temp_long):
                temp_long = substring

        return "".join(temp_long)


if __name__ == "__main__":
    input_s = "pwwkew"
    s = Solution04()
    print("Input: %s" % input_s)

    substring = s.longest_substring(input_s)
    print("Result: %s" % substring)
    print("Length of Longest Substring: %d" % len(substring))
