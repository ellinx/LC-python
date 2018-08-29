"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1

Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1

Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1


"""
class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split(".")
        v2 = version2.split(".")
        #print(v1,v2)
        index = 0
        while index<len(v1) and index<len(v2):
            if int(v1[index])<int(v2[index]):
                return -1
            elif int(v1[index])>int(v2[index]):
                return 1
            index += 1
        while index<len(v1):
            if int(v1[index])!=0:
                return 1
            index += 1
        while index<len(v2):
            if int(v2[index])!=0:
                return -1
            index += 1
        return 0
