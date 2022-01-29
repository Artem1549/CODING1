print("Please input a list of numbers separated with a comma.")
nums = input()
listofnums = nums.split(',')


print(int(listofnums[0]) * int(listofnums[1]) * int(listofnums[2]) * int(listofnums[3]))

print("Please input a list of words separated with a comma.")
word = input()
listofwords = word.split(',')
p = 0
w = 0
for x in listofwords:
    w = 0
    for y in listofwords:
        if(p != w):
            print(listofwords[p] + " " + listofwords[w] + ", ")
        w += 1
    p += 1     


