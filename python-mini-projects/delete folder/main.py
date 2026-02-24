import os
a=os.listdir("sample")
print(a)
for i in a:
    os.remove("sample/"+i)
os.rmdir("sample")