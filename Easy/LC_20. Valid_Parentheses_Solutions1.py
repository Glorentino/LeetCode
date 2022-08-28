#LeetCode 20. Valid Parentheses
# Easy

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#An input string is valid if:

# 1 Open brackets must be closed by the same type of brackets.
# 2 Open brackets must be closed in the correct order.
s = "()[]{}"

def isValid(s):
    stack = []
    for i in s:
        if i == "("  or i == "[" or i == "{":
            stack.append(i)

        else:
            if stack:
                if i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                return False
    return stack == []