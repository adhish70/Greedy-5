# 1057. Campus Bikes
# https://leetcode.com/problems/campus-bikes/

# Logic: We make a hashmap with distance as the key and pair of worker 
# and bike as the value. We compute all possible distances. We then 
# iterate over sorted keys of the hashmap and if the worker and bike 
# has not been aloted we alot it.

# Time Complexity: O((b*w)log(b*w))
# Space Complexity: O(b*w)

class Solution:
    def assignBikes(self, workers, bikes):
        n = len(workers)
        m = len(bikes)
        
        workerSet = [False for i in range(n)]
        bikeSet = [False for i in range(m)]
        hashmap = dict()
        
        # Make hashmap with dist as key and (worker, bike) pair as values
        for i in range(n):
            for j in range(m):
                dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                
                if dist not in hashmap:
                    hashmap[dist] = [(i, j)]
                else:
                    hashmap[dist].append((i, j))
                
        res = [-1 for i in range(n)]
        
        # iterate over hashmap
        for i in sorted(hashmap.keys()):            
            pairs = hashmap[i]
            
            for p in pairs:
                w, b = p
                
                if not workerSet[w] and not bikeSet[b]:
                    workerSet[w] = True
                    bikeSet[b] = True
                    res[w] = b
            
        return res

obj = Solution()
print(obj.assignBikes([[0,0],[2,1]], [[1,2],[3,3]]))