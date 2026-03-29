class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        new = path.split('/')
        for n in new:
            if n != '..' and n != '.' and n != '':
                s.append(n)
            elif s and n == '..':
                s.pop()
        return '/'+'/'.join(s)