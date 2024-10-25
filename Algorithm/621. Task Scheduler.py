class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #create hashmap for each task and count its frequency
        dict = {}
        tasks.sort()
        for char in tasks:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1
        #get the maximum of the frequencies, that task will appear in (max_freq-1) slots with
        #length (n+1)
        max_freq = max(dict.values())
        #we count how many tasks have max_freq to appear in the last slot
        max_freq_cnt = list(dict.values()).count(max_freq)
        #calculate the total intervals
        ans = (max_freq - 1)*(n+1) + max_freq_cnt
        #the final number should be greater or equal to len(tasks)
        return max(ans,len(tasks))
        