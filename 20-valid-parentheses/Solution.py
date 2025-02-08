# Easy
# Tags: string, stack

def is_valid(s: str) -> bool:
    opening = ['(', '[', '{']
    closing = [')', ']', '}']
    stack = []

    for c in s:
        if c in opening:
            stack.append(c)
        if c in closing:
            if not stack or stack.pop() != opening[closing.index(c)]:
                return False
    return len(stack) == 0


print(is_valid('()')) # true
print(is_valid('()[]{}')) # true
print(is_valid('(]')) # false
print(is_valid('([])')) # true
