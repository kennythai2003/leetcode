class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
    
        for substr in path.split('/'):
            if substr =='' or substr =='.':
                continue
            elif substr == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(substr)
        return '/' + '/'.join(stack)