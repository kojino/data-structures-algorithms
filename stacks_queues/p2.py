from p0 import Stack

'''
Given a string of brackets, determine if the string is balanced

Sample Input
{[()]}
{[(])}
{{[[(())]]}}

Sample Output
YES
NO
YES
'''


def is_balanced(brackets):
    open_brackets = ["(","{","["]
    close_brackets = [")","}","]"]
    bracket_matches = {")":"(", "}":"{", "]":"["}
    stack = Stack()

    # loop through each brackets
    for bracket in brackets:
        # if open,
        if bracket in open_brackets:
            # store in stack
            stack.push(bracket)
        # if closed,
        else:
            # check if the top of the stack is the open bracket of the same type
            if bracket_matches[bracket] == stack.peak():
                # remove the pair
                stack.pop()
            # otherwise,
            else:
                # invalid string
                return False

    # after looping through, valid if the stack is empty
    # invalid otherwise
    return not stack.size()
if __name__ == "__main__":
    print is_balanced("{[()]}")
    print is_balanced("{[(])}")
    print is_balanced("{{[[(())]]}}")
