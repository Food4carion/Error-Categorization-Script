import csv
import re

x=[]
path_amt=[]
line_count=0
path_total=0

input_file=str(input("input file path (end path with '[desiredname.txt]'): "))
output_file=str(input("Enter desired output path (end the path with '[desiredname].csv'): "))


with open(input_file,'r') as file:
    ot = open(output_file,'w')
    output = csv.writer(ot)
    temp = file.read().splitlines()

    for line in temp:
        if line == '':
            continue
        else:
            x.append(line)

    
    for i in range(len(x)):
        if x[i] == '-------------NEW-------------------'  :
            output.writerow([x[i+1],x[i+2]])
        
        elif "test(s) failed with similar error:" in x[i]:
            path_count=int(re.search(r'\d+',x[i]).group())
            path_amt.append(path_count) 
            count=1
            for j in range(i,i+path_count):
                output.writerow([count,x[j+1]])
                count+=+1
            output.writerow([''])
            

        else:
            continue
    output.writerow(['Issue number', 'Percentage Err'])
    for i in range(len(path_amt)):
        perc=(path_amt[i])*100/sum(path_amt)
        output.writerow(["Issue {}".format(i+1),"{:.3}%".format(perc)])
print("Process Completed!")

        
