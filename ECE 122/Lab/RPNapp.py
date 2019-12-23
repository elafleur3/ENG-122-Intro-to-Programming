from stackcalc import stackcalc

print("Wlecome to the RPN calculator (enter to quit)")
mystack=stackcalc()
while True:
    prompt=input(">")
    if prompt=="":break
    elif prompt=="+":mystack.add()
    elif prompt=="*":mystack.multiply()
    elif prompt=="-":mystack.subtract()
    elif prompt=="/":mystack.divide()
    else: mystack.push(float(prompt))
    if prompt in ["+","-","*","/"]: print(mystack.peek())
print("Thanks for using the RPN calculator")
