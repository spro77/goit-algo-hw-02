import collections

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if not c.isspace())
    my_deque = collections.deque(cleaned)
    while len(my_deque) > 1:
        if my_deque.popleft() != my_deque.pop():
            print(f"{s}: Not a palindrome")
            return
    print(f"{s}: Is a palindrome")

def check_brackets(s):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for c in s:
        if c in brackets:
            stack.append(c)
        elif c in brackets.values():
            if not stack:
                print(f"{s}: Not symmetric (extra closing bracket)")
                return
            if brackets[stack.pop()] != c:
                print(f"{s}: Not symmetric (mismatched brackets)")
                return
    if stack:
        print(f"{s}: Not symmetric (extra opening bracket)")
    else:
        print(f"{s}: Symmetric")

def main():
    is_palindrome("A man a plan a canal Panama")
    is_palindrome("abcde")
    is_palindrome("abccba")

    check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}")
    check_brackets("( 23 ( 2 - 3);")
    check_brackets("({[)]}")

if __name__ == "__main__":
    main()