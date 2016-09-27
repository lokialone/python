import os
def rename_file():
    #get all file
    files = os.listdir("/Users/lokalone/code/tech/pythons/img")
    path = os.getcwd()
    print(path)
    #change dir path
    os.chdir("/Users/lokalone/code/tech/pythons/img")
    for file in files:
        print(file)
        os.rename(file, file.translate(None, '0123456789'))
rename_file()
