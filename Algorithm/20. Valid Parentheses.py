#leetcode algorithem
#20. Valid Parentheses (easy)
class Solution:
    def isValid(self, s: str) -> bool:
        #create a list to store unclosed parentheses
        stack=[]
        #hash table to map right parethesis to left parenthesis
        mapping={')':'(',']':'[','}':'{'}
        #iterate all parentheses in string s
        for char in s:
            # if we find a right parenthesis
            if char in mapping:
                #we check if it closes the most recent left parenthesis
                #if yes we pop that left parenthesis from stack
                #if not then it is invalid, so return false
                top_element=stack.pop() if stack else '$'
                if top_element != mapping[char]:
                    return False
            #if we find a left parenthesis we append it to stack
            else:
                stack.append(char)
        #at the end if some parentheses haven't been closed (stack is non-empty), it is invalid
        return not stack
