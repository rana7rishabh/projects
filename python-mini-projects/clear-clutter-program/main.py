import os
files=os.listdir("sample")
i=1
for file in files:
    if file.endswith(".txt"):
        os.rename(f"sample/{file}", f"sample/{i}")
        i+=1
 