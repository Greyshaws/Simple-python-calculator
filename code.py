#Functions for mathematical operations

#Addition function
def add(a, b):
    return a + b

#Subtraction function
def subtract(a, b):
    return a - b

#Division function
def divide(a, b):
    return a / b

#Multiplication function
def multiply(a, b):
    return a * b

#Modulus function
def modulus(a, b):
    return a % b

#Available options
print ("These are the available options: ")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Division")
print ("4. Multiplication")
print ("5. Modulus")

listOfOptions = ['1', '2', '3', '4', '5']



while True:

    selectedOption = (input("Please select an option: \n")) #get user input

    #check if user option is among the list of options
    if (selectedOption in listOfOptions): 
        firstNumber = int(input("Enter your first number: \n"))
        secondNumber = int(input("Enter your second number: \n"))

        #if selected option is equal to one of the numbers in the list, add both first number and second number
        # and call the respective function for the operation 
        if (selectedOption == '1'):
           print(firstNumber, "+", secondNumber, "=", add(firstNumber, secondNumber))
           pass
        elif (selectedOption == '2'):
           print(firstNumber, "-", secondNumber, "=", subtract(firstNumber, secondNumber))
           pass
        elif (selectedOption == '3'):
            print(firstNumber, "/", secondNumber, "=", divide(firstNumber, secondNumber))
            pass
        elif (selectedOption == '4'):
            print(firstNumber, "*", secondNumber, "=", multiply(firstNumber, secondNumber))
            pass
        elif (selectedOption == '5'):
           print(firstNumber, "&", secondNumber, "=", modulus(firstNumber, secondNumber))
           pass
         
         #ask if user wants to perform another calculation
        anotherCalculation = (input("Want to perform another calculation? (yes/no): \n")) 
        if (anotherCalculation == "yes"):
            selectedOption = (input("Please select an option: \n"))
        elif (anotherCalculation == "no"):
            break
        else:
            print("Invalid option")
            break
    else:
        print("Invalid input")

               


   