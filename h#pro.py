
print('Thank you for downloading H# Pro.')
print('You now have access to the best language out there.')
def main():
    command = input('>>>')
    if 'draw' in command:
        char1 = command[5]
        char2 = command[6]
        char3 = command[7]
        char4 = command[8]
        char5 = command[9]
        if command[10] == ')':
            value = char1 + char2 + char3 + char4 + char5
        elif command[11] == ')':
            char6 = command[10]
            value = char1 + char2 + char3 + char4 + char5 + char6
        elif command[12] == ')':
            char6 = command[10]
            char7 = command[11]
            value = char1 + char2 + char3 + char4 + char5 + char6 + char7
        elif command[13] == ')':
            char6 = command[10]
            char7 = command[11]
            char8 = command[12]
            value = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
        elif command[14] == ')':
            char6 = command[10]
            char7 = command[11]
            char8 = command[12]
            char9 = command[13]
            value = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9
        elif command[15] == ')':
            char6 = command[10]
            char7 = command[11]
            char8 = command[12]
            char9 = command[13]
            char10 = command[14]
            value = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9 + char10
        else:
            print('ERROR: Value not in range. Make sure the value is 5-10 characters.')
        print(value)
    elif 'var' in command:
        char1 = command[4]
        char2 = command[5]
        char3 = command[6]
        if command[8] == '=':
            name = char1 + char2 + char3
        elif command[9] == '=':
            char4 = command[7]
            name = char1 + char2 + char3 + char4
        elif command[10] == '=':
            char4 = command[7]
            char5 = command[8]
            name = char1 + char2 + char3 + char4 + char5
        else:
            print('ERROR: Value not in range. Make sure the value is 3-5 characters.')
        value = input('Set value of ' + name + ' >>>')
        print('Value ' + value + ' assigned to ' + name + '.')
        savedvarname = name
        savedvarval = value
    else:
        print('ERROR:Command not recognized. Type a valid command and try again.')
while True:
    main()

# Developer's note: Thanks so much for downloading H#. It is still in the makings, but we are working on it! :)