from typing import List

class Stack:
    def __init__(self):
        self.values = []
    def add(self, value:str):
        self.values.append(value)
    def pop(self):
        self.values.pop(-1)
    def size(self) -> int:
        return len(self.values)
    def last(self) -> str:
        return self.values[-1]
    def isEmpty(self) -> bool:
        return len(self.values) == 0
    def check(self) -> List[str]:
        return self.values
        
class Solution:
    opposites = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    oppenings  = {"(", "[", "{"}


    def isValid(self, s: str) -> bool:
        if(len(s) == 1):
            return False

        stack = Stack()

        for char in s:
            if(stack.isEmpty()):
                stack.add(char)
            elif(stack.last() == self.opposites.get(char)):
                stack.pop()
            elif(char in self.oppenings):
                stack.add(char)
            else:
                break
        return stack.isEmpty()

if __name__ == "__main__":
    sol = Solution()
    assert sol.isValid("()") == True, "Failed #1"
    assert sol.isValid("()[]{}") == True, "Failed #2"
    assert sol.isValid("(]") == False, "Failed #3"
    assert sol.isValid("([])") == True, "Failed #4"
