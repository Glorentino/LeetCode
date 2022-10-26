# 383. Ransom Note
# Easy

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note, mag = {}, {}
        
        for i, v in enumerate(ransomNote):
            if v not in note:
                note[v] = 1
            else:
                note[v] += 1
        for i, v in enumerate(magazine):
            if v not in mag:
                mag[v] = 1
            else:
                mag[v] += 1
        
        for i in note:
            if i in mag:
                if note[i] <= mag[i]:
                    continue
                else:
                    return False
            elif i not in mag:
                return False
        return True
        