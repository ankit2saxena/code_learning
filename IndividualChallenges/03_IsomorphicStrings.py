class Solution03:
    def is_isomorphic(self, s1, s2):
        result = True
        sv1, sv2 = {}, {}

        if len(s1) == len(s2):
            for i in range(len(s1)):
                c1, c2 = s1[i], s2[i]

                if c1 not in sv1:
                    sv1[c1] = c2

                if c2 not in sv2:
                    sv2[c2] = c1

                if sv1[c1] != c2 or sv2[c2] != c1:
                    result = False
        else:
            result = False

        return result


if __name__ == "__main__":
    input_s1 = "paper"
    input_s2 = "title"

    s = Solution03()
    print("Input: (%s, %s)" % (input_s1, input_s2))
    print("Result: %s" % s.is_isomorphic(input_s1, input_s2))
