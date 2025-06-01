# Mohammed Murtuza
# MMM263, 31586302
# Section Number 002
# Spring 2024
# Professor Arashdeep Kaur

class DFA263: # This is a class to implement the DFA for email addresses that satisfies L1 and L2.
    def __init__(self):
        self.totalstates = ["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "qtrap"]
        self.finalstates = {"q7"}
        self.state = "q0"

    def transition263(self, symbol): # This function is the transition function for the DFA that processes the input string. If the input string isn't valid, it will go to either trap state or stop before final state.
        prestate = self.state
        if self.state == "q0" and symbol.isalpha():
            self.state = "q1"  

        elif self.state == "q1":
            if symbol.isalpha():
                self.state = "q1"  
            elif symbol == ".":
                self.state = "q0" 
            elif symbol == "@":
                self.state = "q2"  

        elif self.state == "q2" and symbol.isalpha():
            self.state = "q3"  

        elif self.state == "q3":
            if symbol.isalpha():
                self.state = "q3"
            elif symbol == ".":
                self.state = "q4"

        elif self.state == "q4":
            if symbol.isalpha() and symbol != "g":
                self.state = "q3"
            elif symbol == "g":
                self.state = "q5" 

        elif self.state == "q5":
            if symbol == ".":
                self.state = "q4" 
            elif symbol.isalpha() and symbol != "r" and symbol != "o":
                self.state = "q3"
            elif symbol == "r":
                self.state = "q7"
            elif symbol == "o":
                self.state = "q6"

        elif self.state == "q6":
            if symbol == ".":
                self.state = "q8"  
            elif symbol.isalpha() and symbol != "v":
                self.state = "q3"  
            elif symbol == "v":
                self.state = "q7" 

        elif self.state == "q7":
            if symbol.isalpha():
                self.state = "q3"
            elif symbol == ".":
                self.state = "q8"
            elif symbol == "@":
                self.state = "qtrap"

        elif self.state == "q8":
            if symbol.isalpha() and symbol != "g":
                self.state = "q3"
            elif symbol == "g":
                self.state = "q5" 
            elif symbol == ".":
                self.state = "qtrap"    
        else:
            self.state = "qtrap"  
        return f"Present State: {prestate}, Current input symbol: {symbol}, Next State: {self.state}\n"

    def teststrings263(self, str): # This function is used to print the error or acceptance of the input string. It returns the result of the DFA which will be done through the main function.
        self.state = "q0"
        process = [f"Processing string: {str}\n"]

        for c in str:
            if c not in "abcdefghijklmnopqrstuvwxyz.@":
                process.append(f"Entered string contains invalid input bits: {c}\n")
                return "".join(process) 

            process.append(self.transition263(c))

            if self.state == "qtrap":  
                process.append(f"String w='{str}' is not acceptable because it reached a trap state when being parsed.\n")
                return "".join(process) 

        if self.state in self.finalstates:
            process.append(f"String w='{str}' is accepted by the given DFA.\n")
        else:
            process.append(f"String w='{str}' is not acceptable because the string did not end in a final state when being parsed.\n")

        return "".join(process) 

def main263(): #This function has the main code where it'll ask for the users input and then process the input strings by calling the teststrings263 function. The output is saved inside of the output263.txt file.
    print("Project 1 for CS 341")
    print("Section number: 002")
    print("Semester: Spring 2024")
    print("Written by: Mohammed Murtuza, MMM263")
    print("Instructor: Arashdeep Kaur, ak3257@njit.edu")

    n = int(input("Enter the number of strings to be processed (n must be greater than or equal to 0): "))
    print(f"{n} number of strings are now being processed. Please follow the directions in the console.\n")

    if n == 0:
        print("The number of strings is 0, exiting script.")
        return

    with open("output263.txt", "w") as file:
        dfa = DFA263()
        uprange = n + 1
        for i in range(1, uprange):
            email = input(f"Enter string {i} of {n}: ").strip()
            print(f"Processing string: {email}")
            file.write(f"Test Case {i}: {email}\n")
            result = dfa.teststrings263(email)
            print(result) 
            file.write(result + "\n")
    print("All iterations are complete. The output is saved in 'output263.txt'.")

if __name__ == "__main__":
    main263()
