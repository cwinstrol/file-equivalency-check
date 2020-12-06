import filecmp

file1Path = '' #path to file 1 such as 'c:\\folder\\subfolder\\subsubfolder\\'
file1NameAndExtension = '' #file 1 name and extension such as 'text1.txt'
file2Path = '' #path to file 2 such as 'c:\\folder\\subfolder\\subsubfolder\\'
file2NameAndExtension = '' #file 2 name and extension such as 'text2.txt'

print(filecmp.cmp(file1Path + file1NameAndExtension, file2Path + file2NameAndExtension))
