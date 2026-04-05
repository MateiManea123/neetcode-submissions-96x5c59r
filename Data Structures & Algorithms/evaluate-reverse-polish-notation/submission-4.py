class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        print("-11".isalnum())
        for token in tokens:
            # if not stack and not token.isalphanum():
            #     return -1000
            if token not in "+*/-":
                stack.append(int(token))
            else:
                print(stack)
                print(token)
                val2 = stack.pop()
                val1 = stack.pop()
                match token:
                    case "+": stack.append(val1+val2)
                    case "*": stack.append(val1*val2)
                    case "-": stack.append(val1-val2)
                    case "/": 
                        stack.append(int(val1/val2))
                        print("/////",val1,val2)
        
        return stack.pop()


