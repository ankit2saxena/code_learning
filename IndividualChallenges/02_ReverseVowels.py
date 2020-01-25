class Solution02:

    def is_vowel(self, c):
        if c.lower() in ['a', 'e', 'i', 'o', 'u']:
            return True
        else:
            return False

    def reverse_vowels(self, s):
        start_index = 0
        end_index = len(s) - 1

        s = list(s)

        while start_index < end_index:
            if not self.is_vowel(s[start_index]):
                start_index += 1
                continue
            if not self.is_vowel(s[end_index]):
                end_index -= 1
                continue
            temp = s[end_index]
            s[end_index] = s[start_index]
            s[start_index] = temp

            start_index += 1
            end_index -= 1

        return "".join(s)


if __name__ == "__main__":
    input_s = "hello world"
    s = Solution02()
    print("Input: %s" % input_s)
    print("Result: %s" % s.reverse_vowels(input_s))
