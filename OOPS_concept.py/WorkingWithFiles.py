# r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data then it will be overridden.
# a:  open an existing file for append operation. It won’t override existing data.
#  r+:  To read and write data into the file. The previous data in the file will be overridden.
# w+: To write and read data. It will override existing data.
# a+: To append and read data from the file. It won’t override existing data.


with open("sample1.txt","r") as file:
    readlns = file.readlines()
    for line in readlns:
        if "Python" not in line:
            with open("sample2", "a")as f:
                f.write(line)
        else:
            continue
    print("New File created")

with open("sample2.txt","r") as file2:
    print(file2)
        
