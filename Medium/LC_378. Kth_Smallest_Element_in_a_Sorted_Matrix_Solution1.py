"""
378. Kth Smallest Element in a Sorted Matrix

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

"""
from heapq import heapify

def kthSmallest(self, matrix, k) -> int:
    curList = []
    rankList = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            curList.append(matrix[i][j])
    heapq.heapify(rankList)
    for i in curList:
        heapq.heappush(rankList, i)
    for i in range(len(curList)):
        x = heapq.heappop(rankList)
        if i + 1 == k:
            return x 