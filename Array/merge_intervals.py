def merge(intervals):
        
        x=[]
        if len(intervals)==0:
            return x
        intervals.sort()
        
        temp=intervals[0]
        for i in intervals:
            
            if temp[1]>=i[0]:
                temp[1]=max(temp[1],i[1])
            
            else:
                x.append(temp)
                temp=i
                
        x.append(temp)     
         
        return x
    
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
