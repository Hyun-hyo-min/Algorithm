class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num))
        
        last = {}
        for i, x in enumerate(num_str):
            last[int(x)] = i
        
        for i in range(len(num_str)):
            for d in range(9, int(num_str[i]), -1):
                if last.get(d, -1) > i:
                    num_str[i], num_str[last[d]] = num_str[last[d]], num_str[i]
                    return int(''.join(num_str))
        
        return num