class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        if not len(s)%2 == 0:
            return False;

        for i in range(len(s)):
            isEmpty = not bool(stack)
            if i == 0 and s[i] in ")]}":
                return False;
            if s[i] in "{[(":
                stack.append(s[i])
                print(stack)
            if s[i]==")":
                if isEmpty or not stack[-1] == "(":
                    return False
                else:
                    stack.pop()
            if s[i]=="]":
                if isEmpty or not stack[-1] == "[":
                    return False
                else:
                    stack.pop()
            if s[i]=="}":
                if isEmpty or not stack[-1] == "{":
                    return False
                else:
                    stack.pop()
        if not bool(stack):
            return True
        return False