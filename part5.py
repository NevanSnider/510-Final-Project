import re #for regex

states = []
inputs = []
start_state = ""
accept_state = ""
curState = ""
valid = True
stack = ["LAMBDA"]


def tokenizer(text):
    return list(text.strip())


def accept(input_string):
    global states, inputs, start_state, accept_state, curState, stack
    #opens the file to be read
    curState = ""
    stack.clear()
    stack.append("LAMBDA")
    with open("DataStructure.txt") as f:
        lines = f.readlines()
    states = lines[0].split()
    inputs = lines[1].split()
    stack_alphabet = lines[2].split()
    start_state = lines[3].strip()      # q0
    accept_state = lines[4].strip()     # q6
    transitions = [line.strip().split() for line in lines[6:]]

    curState = start_state
    myTokens = tokenizer(input_string)
    curToken = 0

    # DEBUG: print tokens
    print("TOKENS:", myTokens)

    while curToken < len(myTokens):

        # ================================
        # DEBUG: STATE + STACK + NEXT TOKEN
        # ================================
        print("\n=== PDA STEP ===")
        print("Current state:", curState)
        print("Stack:", stack)
        print("Token index:", curToken)
        print("Next token:", myTokens[curToken])
        print("=================")

        matched = False
        for t in transitions:
            prestate, symbol, popped_var, pushed_var, poststate = t
            if symbol == "LAMBDA":
                if curState == prestate and stack[-1] == popped_var:
                    print("Checking transition:", t)
                    if popped_var != "LAMBDA":
                        stack.pop()
                    if pushed_var != "LAMBDA":
                        for ch in reversed(pushed_var):
                            stack.append(ch)   
                    curState = poststate
                    matched = True
                    break
            else:    
                if curState == prestate and myTokens[curToken] == symbol and stack[-1] == popped_var:
                    print("Matched NORMAL transition:", t)
                    if popped_var != "LAMBDA":
                        stack.pop()
                    if pushed_var != "LAMBDA":
                        for ch in reversed(pushed_var):
                            stack.append(ch) 
                    curState = poststate
                    curToken += 1
                    matched = True
                    break
        if not matched:
            # DEBUG: Print why we failed
            print("\nNO TRANSITION MATCHED!")
            print("State:", curState)
            print("Stack top:", stack[-1])
            print("Token:", myTokens[curToken])
            print("The input is invalid")
            return
        
    changed = True
    while changed:
        changed = False
        for t in transitions:
            prestate, symbol, popped_var, pushed_var, poststate = t
            if symbol == "LAMBDA" and curState == prestate and stack[-1] == popped_var:
                print("Applying FINAL λ-transition:", t)
                if popped_var != "LAMBDA":
                    stack.pop()
                if pushed_var != "LAMBDA":
                    for ch in reversed(pushed_var):
                        stack.append(ch)
                curState = poststate
                changed = True
                break
        
    print("\n=== FINAL CHECK ===")
    print("State:", curState)
    print("Stack:", stack)

    if curState == accept_state and stack[-1] == "LAMBDA":
        print("The input is valid")
    else:
        print("The input is invalid")


def lambda_closure(transitions):
    global curState, stack
    changed = True
    while changed:
        changed = False
        for t in transitions:
            pre, symbol, popped, pushed, post = t

            if symbol != "LAMBDA":
                continue

            if curState == pre and stack[-1] == popped:
                # apply transition
                if popped != "LAMBDA":
                    stack.pop()
                if pushed != "LAMBDA":
                    stack.append(pushed)

                curState = post
                changed = True
                break  # restart scanning transitions


def transition(line, myTokens, curToken):
    global curState
    global stack
    print(stack)
    #sets the initial state to the first one
    if (curState == ""):
        curState = start_state
    
    #if we are in the accept state and theres nothing on the stack we return 1 to indicate the input is valid
    if (curState == accept_state):
        if (stack[-1] == "LAMBDA"):
            return 1
    #if the stack becomes empty we want it to be lambda
    if len(stack) == 0:
        stack.clear()
        stack.append("LAMBDA")

    
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


