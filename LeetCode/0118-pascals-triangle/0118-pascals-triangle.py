class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]

        for i in range(1, numRows):
            prev_row = rows[i-1]
            current_row = [1]

            for j in range(1, i):
                current_row.append(prev_row[j-1] + prev_row[j])
            
            current_row.append(1)
            rows.append(current_row)
        
        return rows