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

def tokenizer(text):
    tokens = []
    #text is enumerated to be able to get indexes and it reads individual characters
    for i, ch in enumerate(text):
        #checks if its an alphanumeric character
        if ch.isalpha():
            #if theres a left parenthesis before the character and the next one is a digit then
            #it is appended to be treated as a single token
            if (text[i] == '(' and text[i+1].isdigit()):
                tokens.append(tokens[i] + tokens[i+1])

            #same thing as above but for if there is a / before the parenthesis 
            elif (text[i] == '(' and text[i-1] == '/'):
                tokens.append(tokens[i-1] + tokens[i])

            #otherwise append it as normal
            else:
                tokens.append(ch)
    return tokens


def accept(input_string):
    #opens the file to be read
    data_structure = open("DataStructure.txt", "r")

    #keeps track of the current line being read
    curLine = 1

    #tokenizes the string to get the special ones in the alphabet
    myTokens = tokenizer(input_string)

    #These are the things from our data structure we were required to have in there but I dont
    #think we actually end up needing to use them for the code
    for line in data_structure:
        if (curLine == 1):
            states = line.split(" ")
        elif (curLine == 2):
            inputs = line.split(" ")
        elif (curLine == 3):
            start_state = line.strip()
        elif (curLine == 4):
            global accept_state
            accept_state = line.strip()
        elif (curLine == 5):
            stop_state = line.strip()
        curLine += 1
        #reads all the transitions in the data structure and will run through them
    accepted = transition(line, myTokens, 0)
        

    #determines if the input is valid
    if accepted == 1:
        print("The the input is invalid")
    if accepted == 0:
        print("The input is invalid")


def transition(line, myTokens, curToken):
    global curState
    stack = []
    #sets the initial state to the first one
    if (curState == ""):
        curState = start_state
    
    #if we are in the accept state and theres nothing on the stack we return 1 to indicate the input is valid
    if (curState == accept_state):
        if (stack[-1] == "LAMBDA"):
            return 1
    #if the stack becomes empty we want it to be lambda
    if len(stack) == 0:
        stack = ["LAMBDA"]

    
    #index 0 is the state being left from,
    #index 1 is the symbol being read,
    #index 2 is the variable being popped,
    #index 3 is the variable being pushed, 
    #index 4 is the state the transition goes to
    transition_stuff = line.strip().split(" ")
    print(transition_stuff)
    prestate = transition_stuff[0]
    symbol = transition_stuff[1]
    popped_var = transition_stuff[2]
    pushed_var = transition_stuff[3]
    poststate = transition_stuff[4]

    #Compares the input with the given transition and will pop and push the necessary variables
    if (curState == prestate and myTokens[curToken] == symbol and stack[-1] == popped_var):
        #pop from the stack
        if (popped_var != "LAMBDA"):
            stack.pop()
        #push to the stack
        stack.append(pushed_var)
        #update the current state
        curState = poststate
        #update the current token
        curToken += 1
    else:
        return 0

    


user_input = input("Enter a valid arithmetic equation:\n")
accept(user_input)


