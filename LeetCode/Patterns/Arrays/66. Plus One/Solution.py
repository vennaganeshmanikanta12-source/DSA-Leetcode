class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a,t=0,0
        for i in digits[::-1]:
            t+=(i*10**a)
            a+=1
        t=t+1
        b=[]
        while(t>0):
            c=t%10
            b.append(c)
            t//=10
        return b[::-1]