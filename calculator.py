# Reverse Polish Notation calculator

def plus(stack):
    stack.append(stack.pop() + stack.pop())

def minus(stack):
    stack.append(stack.pop() - stack.pop())

def multiply(stack):
    stack.append(stack.pop() * stack.pop())

def divide(stack):
    stack.append(stack.pop() / stack.pop())

def powerOf(stack):
    stack.append(stack.pop() ** stack.pop())

operators =  {
    "+": plus,
    "-": minus,
    "*": multiply,
    "/": divide,
    "**": powerOf
}

def main():
    tokens = stackInput()
    try:
        processedStack, processedList = processStack(tokens)
        print(f"The result of {processedList} is {processedStack}")
    except:
        print("Stack empty")
        exit()

def stackInput():
    return input("Input using Reverse Polish notation: ").strip().split()

def processStack(tokens):
    stack = []
    validList = []

    for token in tokens:
        if token in operators:
            operators[token](stack)
            validList.append(token)
        else:
            try:
                stack.append(float(token))
                validList.append(token)
            except ValueError:
                print("Error: Only Operands and Operators are accepted.")
    if stack[0]:
        return str(stack[0]), ' '.join(validList)
    else: 
        raise Exception()


if __name__ == "__main__":
    main()