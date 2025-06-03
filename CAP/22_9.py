import re

def main(input_string):
    pattern = r"equ\s+'(\w+)'\s*:\s*(\w+)."
    matches = re.findall(pattern, input_string)
    result = [(match[0], match[1]) for match in matches]
    return result

input_string = "equ'usdi_537' : enar. equ'lareza_850' :ceti. equ 'edat' : enor.\nequ'isge' :inma."
result = main(input_string)
print(result)