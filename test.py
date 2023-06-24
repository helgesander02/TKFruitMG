# import win32api
# import win32print

# filename2 = r"0012023621.pdf"
# filename = r".\allpdf" + r"\\" + filename2
# win32api.ShellExecute (0,"print",filename,win32print.GetDefaultPrinter(),".",0)

import os
dir_path = os.getcwd() + r"\\allpdf"
print(os.listdir(dir_path)[0])
print(os.getcwd())