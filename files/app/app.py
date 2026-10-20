# 
fh = open("files/app/hello", "rb") 
print(type (fh))

try:
    tfh = open("data.txt", 'w')
except FileNotFoundError:
    print("File not found")
finally:
    tfh.close()
    
with open("test", 'a+') as file_handler:
    file_handler.write("hello there")
   
with open("test", 'r') as file_handler:
    data = file_handler.read()
print(data)

with open("test", "r") as file:
    str1 = file.readline()
    str2 = file.readline()
print(str1, str2)
# Щоб отримати лише необхідну кількість байтів з файлу.
with open("test", "r") as file:
    str3 = file.readline(10)
print(str3)