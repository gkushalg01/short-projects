"""
cpp(C++) json11 library by dropbox produces some nasty looking json while debugging in VS Code-
Totally unreadable for any json beautifier, or human if the data is huge.
This program simply converts it to human readable form. 
This program Uses regex to remove
'01 <repeats .1234455' garbage addresses
Uses Python's string manipulation to remove backslashes, unnecessary quotes and so on.
"""
import pyperclip, re, json

def convert():
    lines = []
    print("Enter json:")
    while True:
        user_input = input()

    # 👇️ if user pressed Enter without a value, break out of loop
        if user_input == '':
            break
        else:
            lines.append(user_input + '\n')
    s = "".join(lines).strip()
    istr = s[:]
    if istr[0] == '"':
        istr = istr[1:]
    if istr[-1] == '"':
        istr = istr[:-1]
    istr = istr.replace("\\", "").replace("\n", "")
    istr = re.sub(r"""(", '\d' <repeats .{12})+""", "", istr)
    obj = json.loads(istr)
    res = json.dumps(obj, indent=2)
    pyperclip.copy(res)
    print("Final JSON : \n",res)
    print("JSON COPIED TO CLIPBOARD!\n")

while(True):
    try:
        convert()
    except KeyboardInterrupt:
        print("EXITED.")
        break
    except:
        print("JSON INCORRECT!!! TRY AGAIN...")
        convert()
    
    