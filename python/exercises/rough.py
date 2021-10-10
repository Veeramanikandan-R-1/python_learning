class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        emp_lis = []
        len_s = len(s)
        for i in range(len_s):
            emp_lis1 = []
            emp_lis1.append(s[i])
            for j in range(i + 1, len_s ):
                print(1)
                if ((s[j - 1] != s[j]) and (s[j] not in emp_lis1)):
                    emp_lis1.append(s[j])
                else:
                    break
            emp_lis.append(emp_lis1)
        print(emp_lis)
        len_max = [len(x) for x in emp_lis]
        if (len_max):
            max_v = max(len_max)
            return max_v
        else:
            return 0

sol=Solution()
print(sol.lengthOfLongestSubstring('au'))