class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        k = [" "]
        for i in range(len(s)):
            if(s[i]!=k[-1]):
                k.append(s[i])
            else:
                k.pop()
        return "".join(k)[1:]

ans = Solution()
print(ans.removeDuplicates(input("Enter your String: ")))