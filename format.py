import black
import autopep8

# Złe odstępy
def formatMyCode (code): 

    try: 
        formattedCode = black.format_file_contents(code, fast=False, mode=black.FileMode())
        return formattedCode
    
    except:
        print('Error')

if __name__ == '__main__':
    code_to_format =  '''
def        exampleFirstFunction             ():
    print              ('Test pierwszy')
'''

formattedCodeOne = formatMyCode(code_to_format)

print(formattedCodeOne)

# Złe wcięcia 

