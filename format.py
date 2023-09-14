import black
import autopep8

# Złe odstępy
def formatMyCode (code): 

    try: 
        formattedCode = black.format_file_contents(code, fast=False, mode=black.FileMode())
        return formattedCode
    
    except:
        print('Error - eliminacja zbędnych spacji')

if __name__ == '__main__':
    code_to_format =  '''
def        exampleFirstFunction             ():
    print              ('Test pierwszy')
'''

formattedCodeOne = formatMyCode(code_to_format)

print(formattedCodeOne)

# Złe wcięcia 
def formatMyCodeAutopep (code):

    try:
        formattedCodeAutopep = autopep8.fix_code(code)
        return formattedCodeAutopep

    except:
        print('Error - wcięcia')


if __name__ == '__main__':
    code_to_format_autopep =  '''
def exampleSecondFunction():
    print('Popraw wcięcia')
'''

formattedCodeTwo = formatMyCodeAutopep(code_to_format_autopep)

print(formattedCodeTwo)
