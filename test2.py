def spiralOrder(matrix):
    row = len(matrix)
    col = len(matrix[0])
    count = 0
    total = row * col
    ans = []

    # Index initialization
    startingRow = 0
    startingCol = 0
    endingRow = row - 1
    endingCol = col - 1

    while count < total:
        # Print starting row
        for i in range(startingCol, endingCol + 1):  # Changed 'and' to '+'
            ans.append(matrix[startingRow][i])  # Fixed the indexing
            count += 1

        startingRow += 1

        # Print ending column
        for i in range(startingRow, endingRow + 1):  # Changed 'and' to '+'
            ans.append(matrix[i][endingCol])
            count += 1
        endingCol -= 1

        # Print ending row
        if startingRow <= endingRow:  # Check if startingRow is still valid
            for i in range(endingCol, startingCol - 1, -1):  # Changed 'and' to '-1' and added startingCol - 1
                ans.append(matrix[endingRow][i])
                count += 1
            endingRow -= 1

        # Print starting column
        if startingCol <= endingCol:  # Check if startingCol is still valid
            for i in range(endingRow, startingRow - 1, -1):  # Changed 'and' to '-1' and added startingRow - 1
                ans.append(matrix[i][startingCol])
                count += 1
            startingCol += 1

    return ans

matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

print(spiralOrder(matrix))
