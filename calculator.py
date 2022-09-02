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

operators =  {
    "+",
    "-",
    "*",
    "/",
    "**"
}

def main():
    tokens = stack_input()
    try:
        processed_stack, processed_list = process_stack(tokens)
        print(f"The result of {Colors.PINK}{processed_list}{Colors.ENDC} is {Colors.GREEN}{processed_stack}{Colors.ENDC}")
    except:
        print(f"{Colors.RED}Stack empty{Colors.ENDC}")
        exit()

def stack_input():
    return input("Input using Reverse Polish notation: ").strip().split()

def process_stack(tokens):
    stack = []
    valid_list = []

    for token in tokens:
        if token in operators:
            operate(stack, token)
            valid_list.append(token)
        else:
            try:
                stack.append(float(token))
                valid_list.append(token)
            except ValueError:
                print(f"{Colors.RED}Error: Only Operands and Operators are accepted.{Colors.ENDC}")
    if stack[0]:
        return str(stack[0]), ' '.join(valid_list)
    else: 
        raise Exception()

def operate(stack, operator):
    stack.append(eval(f"stack.pop() {operator} stack.pop()"))

if __name__ == "__main__":
    main()