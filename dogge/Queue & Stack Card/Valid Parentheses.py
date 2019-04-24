class Solution:
    def isValid(self, s: str) -> bool:
        """
        '(', ')', '{', '}', '[' , ']'
        """
        rb_lb = {')': '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i not in rb_lb:
                stack.append(i)
            elif not stack or rb_lb[i] != stack.pop():
                return False
        return not stack
