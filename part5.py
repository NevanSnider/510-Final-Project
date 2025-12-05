def accept(input_string):
    data_structure = open("DataStructure.txt", "r")
    states = []
    inputs = []
    three_ops = ["+", "-", "x"]
    normal_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    funky_ones =["(0", "(1", "(2", "(3", "(4", "(5", "(6", "(7", "(8", "(9"]
    start_state = ""
    accept_state = ""
    output = ""
    curState = ""
    valid = True

    curLine = 1

    myTokens = tokenize(input_string)
    for line in text:
        if (curLine = 1):
            states = line.split(" ")
        else if (curLine = 2):
            inputs = line.split(" ")
        else if (curLine = 3):
            start_state = line
        else if (curLine = 4):
            accept_state = line
            
        #index 0 is the state being left from,
        #index 1 is the symbol being read,
        #index 2 is the variable being popped,
        #index 3 is the variable being pushed, 
        #index 4 is the state the transition goes to
        else if (curLine >= 5):
            accepted = transition(line, myTokens, 0)
            if accepted = 1:
                print("The input is valid!")
                break
            if accepted = 0:
                continue
        curLine += 1
    print("The the input is invalid")


def transition(line, myTokens, curToken):
    if (curState == ""):
        curState = start_state
    if (curState == accept_state):
        if (stack[-1] = "LAMBDA"):
            return 1
    if len(stack) == 0:
    stack = ["LAMBDA"]
    transition_stuff = line.split(" ")
    prestate = transition_stuff[0]
    symbol = transition_stuff[1]
    popped_var = transition_stuff[2]
    pushed_var = transition_stuff[3]
    poststate = transition_stuff[4]


    if (curState = prestate and curToken == symbol and stack[-1] = popped_var):
        stack.push(pushed_var)
        curState = poststate
        curToken += 1
    else:
        return 0

        

    

def tokenizer(text)
    tokens = []
    for i, ch in enumerate(text):
        if ch.isalpha():
            if (text[i] == '(' and text[i+1].isdigit()):
                tokens.append[tokens[i] + tokens[i+1]]
            else if (text[i] == '(' and text[i-1] == '/'):
                tokens.append[tokens[i-1] + tokens[i]]
            else:
                tokens.append(ch)
    return tokens

def main():
    user_input = input("Enter a valid arithmetic equation:\n")
    accept(user_input)



