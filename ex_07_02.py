# X-DSPAM-Confidence: 0.8475
# Count these lines and extract the floating point values
# from each of the lines and compute the average of those
# values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Error: file can not be opened:', fname)
    # don't forget to quit if an incorrect file name in entered.
    quit()
count = 0
total = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    # be careful of the indentation. 
    copos = line.find(":")
    lx = line[copos + 1:len(line)]
    try:
        ly = float(lx)
    except:
        print('Error: this line does NOT have a float number')
        continue
    total = total + ly
    count = count + 1
print('Average spam confidence:', total / count)
