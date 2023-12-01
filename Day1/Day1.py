import re

numberTotal = 0

try:
    with open('Day1/input.txt','r') as file:
        
        for line in file:
            
            lineAllNumbers = re.sub(r'\D','',line)
            
            if(len(lineAllNumbers) > 1):
                newNumber = int(lineAllNumbers[0] + lineAllNumbers[len(lineAllNumbers) - 1])
            else:
                newNumber = int(lineAllNumbers + lineAllNumbers)
                
            numberTotal = numberTotal + newNumber
            
        print(numberTotal)     
        
except FileNotFoundError:
    print('file not found')
    
except IOError:
    print('unavble to read file')