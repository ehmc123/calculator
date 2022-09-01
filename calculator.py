# Reverse Polish Notation calculator

class Colors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
        print(f"The result of {Colors.PINK}{processedList}{Colors.ENDC} is {Colors.GREEN}{processedStack}{Colors.ENDC}")
    except:
        print(f"{Colors.RED}Stack empty{Colors.ENDC}")
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
                print(f"{Colors.RED}Error: Only Operands and Operators are accepted.{Colors.ENDC}")
    if stack[0]:
        return str(stack[0]), ' '.join(validList)
    else: 
        raise Exception()


if __name__ == "__main__":
    main()