def generate(numRows):
    triangle = []
    
    for row_num in range(numRows):
        # The first and last row elements are always 1.
        row = [None] * (row_num + 1)
        row[0], row[-1] = 1, 1
        
        # Each triangle element is equal to the sum of the elements
        # directly above-left and above-right.
        for j in range(1, len(row) - 1):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            
        triangle.append(row)
        
    return triangle

if __name__ == "__main__":
    numRows = 5
    result = generate(numRows)
    print(f"Pascal's Triangle with {numRows} rows:")
    for row in result:
        print(row)
