# Taking input from file and remove its duplicate and then save output in  another file

count = 0
#Provide the location of file
url = 'C:\\Users\\gupta\\PycharmProjects\\miraa\\duplicate.txt'

# Open file in read mode
f = open(url, 'r')
lines = f.read().split("\n")
print(lines)
for i in lines:
 count = count + 1

#to appending a blank space in the file ' '
f1 = open(url, 'a+')

if len(lines) == count:
     print(len(lines))
     lines.append('')
     f1.close()         #closing file openend in read mode.

line_visible = set()

#open second file in write mode
out_file = open("C:\\Users\\gupta\\PycharmProjects\\miraa\\out.txt", "w")

#removal of duplicates one by one and add into 2 file
#the new file after removing the dulicates will be here
for line in open(url, "r"):
    if line not in line_visible:
        out_file.write(line)
        line_visible.add(line)
        line.rstrip(line)
