def sprialOrder(matrix):
    
    row = len(matrix)
    col = len(matrix[0])
    count = 0
    total = row * col
    ans = []
    
    
    #index initalisation 
    startingRow = 0
    startingCol = 0
    endingRow = row - 1
    endingCol = col - 1
    
    while(count  < total):
        
        #print starting row
        for i in range(startingRow,endingCol + 1 ):
            ans.append(matrix[startingRow][i])
            count += 1
            
        startingRow += 1
            
        #print ending column
        for i in range(startingRow,endingRow + 1 ):
            ans.append(matrix[i][endingCol])
            count += 1
        endingCol -= 1
        #print ending row
        
        if(startingRow <= endingRow):
            for i in range(endingCol,startingCol -1, -1 ):
                ans.append(matrix[endingRow][i])
                count += 1
            endingRow -= 1
            
        #print starting column
        if startingCol <= endingCol:
            for i in range(endingRow,startingRow -1,-1 ):
                ans.append(matrix[i][startingCol])
                count += 1
            startingCol += 1       
        
    return ans
    
    
    
matrix = [[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]]


print(sprialOrder(matrix))

     
            
            
            
            
        