class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        arr = [0]*26
        for i in sentence:
            
            arr[ord(i)-97]+=1
        for i in arr:
            if not i>0:
                return False
        return True
        

p = Solution()
print(p.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))