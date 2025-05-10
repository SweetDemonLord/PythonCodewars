import re
text = "Python 3.10, Python 2.7"
new_text = re.sub(r'Python', 'Py', text)
print(new_text)  # Py 3.10, Py 2.7

from re import sub
def printer_error(s):
    return "{}/{}".format(len(sub("[a-m]",'',s)),len(s))

def printer_error2(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))