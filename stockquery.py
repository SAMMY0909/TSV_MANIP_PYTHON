import csv

fp=open('file1.tsv','r')
reader=csv.reader(fp)
rows=list(reader)
num_lines=len(rows)

print("This is a NASDAQ TESLA(SINCE ELON MUSK IS IN NEWS) stock file with numbers sorted by date...")
print("The number of lines in the file are:", num_lines)
print("The file table format is:")

print (rows[0][0])
myrow=rows[1][0]
myrow1=rows[num_lines-1][0]
mylist=myrow.split("\t")
mylist1=myrow1.split("\t")
print(mylist)
print(mylist1)
print(mylist[0],mylist[1])
print(mylist1[0],mylist1[1])
print("This data file has data from date:",mylist1[0],"to date:",mylist[0],"\n")

getdata=input("Enter the stock_HIGH value below which you want stock listings and the program will output the date for the stock listings below that: \t")

fp.seek(0)
print("The header is:",rows[0][0].split("\t"))

j=0
for j in range(0,num_lines-1):
    s0=rows[j+1][0]
    getdat=s0.split("\t")
    if float(getdat[1])<=float(getdata):
        print(getdat[0],getdat[1])

test=True
while test==True:
    var=input("Enter the date for which you want the data in strict YYYY-MM-DD format,or simply press enter to exit, the input loops if you have finished one query :")
    if not var:
        print("Exiting...\n")
        break
    i=0
    flag=True
    if flag==True:
        for i in range(0,num_lines-1):
            s3=rows[i][0]
            ndata=s3.split("\t")
            if var==ndata[0]:
                print("YOUR QUERY IS FOUND AT ROW",i+1,"and data is\n" ,rows[0][0],"\n",rows[i][0],"\n")
            else:
                 flag=False
    elif flag==False:
        print("Hi, bad query. Grab a donut and call the pro\
                    gram again!!:P")

fp.seek(0)
fp.close()
exit()
