import os

# command = "cmd"
# os.system(command)
str1 = os.getcwd()+"\\Graphics in Dev C++\\graphics.h"
# print(str)
str2 = os.getcwd()+"\\Graphics in Dev C++\\winbgim.h"

str3 = os.getcwd()+"\\Graphics in Dev C++\\libbgi.a"

str4 = os.getcwd()+"\\Graphics in Dev C++\\6-ConsoleAppGraphics.template"

str5 = os.getcwd()+"\\Graphics in Dev C++\\ConsoleApp_cpp_graph.txt"


# print(os.getcwd()+"Graphics in Dev C++")
# os.chdir("Graphics in Dev C++")
# os.rename(str , "C:/Users/ayush/Desktop/abc/aaa.txt")
os.rename(str1 , "C:/Program Files (x86)/Dev-Cpp/MinGW64/x86_64-w64-mingw32/include/graphics.h")
os.rename(str2 , "C:/Program Files (x86)/Dev-Cpp/MinGW64/x86_64-w64-mingw32/include/graphics.h")
os.rename(str3 , "C:/Program Files (x86)/Dev-Cpp/MinGW64/x86_64-w64-mingw32/lib/libbgi.a")
os.rename(str4 , "C:/Program Files (x86)/Dev-Cpp/Templates/6-ConsoleAppGraphics.template")
os.rename(str5 , "C:/Program Files (x86)/Dev-Cpp/Templates/ConsoleApp_cpp_graph.txt")

# str = "..\C:\\Users\\ayush\\Desktop"
# C:\Program Files (x86)\Dev-Cpp\MinGW64\x86_64-w64-mingw32

# os.system("cd hh")
# try :
#     os.chdir("C:\\Users\\ayush\\Desktop")
#
# finally:
#     os.chdir("C:/Users/ayush/Desktop")
