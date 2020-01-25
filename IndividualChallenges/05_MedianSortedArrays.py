class Solution05:
    def find_median(self, arr1, arr2):

        len_merge = len(arr1) + len(arr2)

        median_index = []
        median = 0

        if len_merge % 2 != 0:
            median_index.append((len_merge - 1) / 2)
        else:
            median_index.append(int((len_merge - 1) / 2))
            median_index.append(int((len_merge - 1) / 2) + 1)

        cnt1, cnt2 = 0, 0

        while cnt1 + cnt2 <= median_index[-1]:
            if cnt1 < len(arr1) and cnt2 < len(arr2):
                if arr1[cnt1] <= arr2[cnt2]:
                    if (cnt1 + cnt2) in median_index:
                        median += (arr1[cnt1])
                    cnt1 += 1
                else:
                    if (cnt1 + cnt2) in median_index:
                        median += (arr2[cnt2])
                    cnt2 += 1
            else:
                if cnt1 < len(arr1):
                    if (cnt1 + cnt2) in median_index:
                        median += (arr1[cnt1])
                    cnt1 += 1
                else:
                    if (cnt1 + cnt2) in median_index:
                        median += (arr2[cnt2])
                    cnt2 += 1

        if len(median_index) == 2:
            median = median / 2

        return median


if __name__ == "__main__":
    input_s1 = [1, 3]
    input_s2 = [3, 4]

    s = Solution05()
    print("Input: (%s, %s)" % (input_s1, input_s2))
    print("Result: %s" % s.find_median(input_s1, input_s2))
