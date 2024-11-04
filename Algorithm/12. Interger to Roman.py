class Solution:
    def intToRoman(self, num: int) -> str:
        num_map = {1:"I", 
            4:"IV", 5:"V", 
            9:"IX", 10:"X", 
            50: "L",   40: "XL",
            100: "C",  90: "XC",
            500: "D",  400: "CD",
            1000: "M", 900: "CM"}
        string = ''
        for n in [1000,900,500,400,100,90,50,40,10,9,5,4,1]:
            while n <= num:
                string += num_map[n]
                num -= n
        return string
