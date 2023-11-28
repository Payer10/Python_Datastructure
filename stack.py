def is_balanced(input_str):
    l =list()
    for i in input_str:
        if i == '(':
            l.append(i)
        if i == ')':
            if not l:
                return False
            l.pop()
    return not l
if __name__ == "__main__":
    arr = input()
    if is_balanced(arr):
        print('Is balanced')
    else:
        print('Not is balanced')
    