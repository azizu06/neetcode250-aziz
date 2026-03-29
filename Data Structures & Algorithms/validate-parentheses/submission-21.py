class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == ')' or s[0] == '}' or s[0] == ']' or len(s) % 2 != 0:
            return False
        valid = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                valid.append(s[i])
            elif valid:
                if s[i] == ')' and valid[-1] != '(':
                    return False
                elif s[i] == ']' and valid[-1] != '[':
                    return False
                elif s[i] == '}' and valid[-1] != '{':
                    return False
                valid.pop()
        return True if not valid else False