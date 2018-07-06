"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name,
and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts.
Two accounts definitely belong to the same person if there is some email that is common to both accounts.
Note that even if two accounts have the same name, they may belong to different people as people could have the same name.
A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format:
the first element of each account is the name, and the rest of the elements are emails in sorted order.
The accounts themselves can be returned in any order.

Example 1:

Input:
accounts =
[
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary@mail.com"]
]

Output:
[
    ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
    ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]
]

Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Note:
1. The length of accounts will be in the range [1, 1000].
2. The length of accounts[i] will be in the range [1, 10].
3. The length of accounts[i][j] will be in the range [1, 30].
"""
class Solution:
    """
    Thoughts:
    1. Union&Find
    """
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        def findRoot(roots, node):
            while roots[node]!=node:
                node = roots[node]
            return node

        roots = dict()
        for i in range(len(accounts)):
            roots[i] = i;
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in roots:
                    roots[accounts[i][j]] = i
                else:
                    root1 = findRoot(roots, accounts[i][j])
                    if root1!=i:
                        roots[root1] = i
        merged = collections.defaultdict(set)
        for k in roots:
            if '@' in str(k):
                merged[findRoot(roots,k)].add(k)
        ret = []
        for k in merged:
            ret.append([accounts[k][0]]+sorted(list(merged[k])))
        return ret
