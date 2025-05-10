import re

print(True if re.fullmatch(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$', 'abcDE8_') else False)