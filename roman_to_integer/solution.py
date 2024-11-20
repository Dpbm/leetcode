class Solution:
    symbols = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    def romanToInt(self, s: str) -> int:
        total_sum = 0

        i = 0
        while i < len(s):
            char = s[i]
            value = self.symbols[char]

            if(i < len(s)-1):
                next_char = s[i+1]
                next_value = self.symbols[next_char]
            
                if(next_value > value):
                    total_sum += next_value - value
                    i+=2
                    continue
                else:
                    total_sum += value
            else:
                total_sum += value

            i+=1
        return total_sum

if __name__ == "__main__":

    sol = Solution()
    assert sol.romanToInt("III") == 3, "Failed #1"
    assert sol.romanToInt("LVIII") == 58, "Failed #2"
    assert sol.romanToInt("MCMXCIV") == 1994, "Failed #3"
    

