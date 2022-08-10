#import module Regular Expression
import re

#The number of unique IP addresses
#The top 3 most visited URLs
#The top 3 most active IP addresses
f = open('programming-task-example-data_(1).log', 'r')
fline = f.readlines()
p = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

ip_list=[]
ip_dic={}

for line in fline:
    ip_address = p.search(line)[0]
    if ip_address not in ip_list:
        ip_list.append(ip_address)    


print(len(ip_list))


f.close