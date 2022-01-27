#leetcode algorithem
#13. Roman to Integer(easy)
class Solution:
    def romanToInt(self, s: str) -> int:
        #create a table for translation from Roman to integer
        hashmap={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        #initialize the total
        numeral=0
        #for every Roman number but the last one
        for i in range(len(s)-1):
            #compare two consecutive positions , if first position is smaller then it must be 4 or 9 multiples
            #so we use the second substract the first
            if hashmap[s[i]]<hashmap[s[i+1]]:
                numeral=numeral-hashmap[s[i]]
            #otherwise, we just add it to the total
            else:
                numeral=numeral+hashmap[s[i]]
        #add the last element to get the final total
        return (numeral+hashmap[s[-1]])
