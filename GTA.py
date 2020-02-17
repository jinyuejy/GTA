import numpy as np
class Gta():
    def kruskal(self,matrix):
        l=list(matrix.shape)[0]
        x=[0]
        b=list(range(1,l))
        result=[]
        for i in range(l):
            for j in range(l):
                if matrix[i][j]==0:
                    matrix[i][j]=np.inf
        result=[]
        while 1:
            mins=np.inf
            for item in x:
                for num in b:
                    if matrix[item][num]<mins:         ## rounding for searching the minimum
                        mins=matrix[item][num]
                        pos2=num
                        pos1=item
            result.append([pos1,pos2,mins])
            x.append(pos2)
            b.remove(pos2)
            if not b:                                  ## if the 'b' is blank,programs will break out
                break


        print(result)                                 ## the result include the node and values