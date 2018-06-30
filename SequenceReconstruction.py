"""
Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs.
The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104.
Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it).
Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.

Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].

Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].

Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true

"""
class Solution:
    """
    Thoughts:
    1. Topology sort
    2. During the process of topology sort, there should not be more than one node whose indegree is 0

    Time: O(v+e) where v, e is total number of nodes and edges in the graph
    Space: O(v)
    """
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        # check if there is unique topology sort sequence
        g = collections.defaultdict(set)
        indegree = dict()
        topoSeq = []
        for seq in seqs:
            for i in range(len(seq)):
                if seq[i] not in indegree:
                    indegree[seq[i]] = 0
                if i+1>len(seq)-1:
                    break
                if seq[i+1] not in indegree:
                    indegree[seq[i+1]] = 0
                if seq[i+1] not in g[seq[i]]:
                    g[seq[i]].add(seq[i+1])
                    indegree[seq[i+1]] += 1
        q = collections.deque()
        for k in indegree:
            if indegree[k]==0:
                q.append(k)

        while len(q):
            # multiple nodes with indegree==0 will make the topoSeq not unique
            if len(q)>1:
                return False
            cur = q.popleft()
            topoSeq.append(cur)
            for each in g[cur]:
                indegree[each] -= 1
                if indegree[each]==0:
                    q.append(each)
            #print(q)

        #print(topoSeq,org)
        if len(topoSeq)!=len(indegree):
            return False
        return topoSeq==org
