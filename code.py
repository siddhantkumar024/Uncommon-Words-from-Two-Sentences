class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        d=s1+" "+s2
        w=d.split()
        x=[]
        y={}
        c=0
        for i in w:
            if i not in y:
                
                y[i]=1
            else:
                
                y[i]+=1
                
        for w,c in y.items():
            if c==1:
                x.append(w)
        return x
                


        
