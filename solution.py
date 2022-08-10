#import module Regular Expression
import re

#The number of unique IP addresses
#The top 3 most visited URLs
#The top 3 most active IP addresses

#open file
f = open('programming-task-example-data_(1).log', 'r')
fline = f.readlines()
def uniq_ip(filename):
    f = open(filename, 'r')
    ip_list=[]
    # pattern for ip address, from 0.0.0.0 to 255.255.255.255
    p = r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' 

    for line in fline:
        ip_address = re.findall(p,line)
        if ip_address not in ip_list:
            ip_list.append(ip_address)    

    #close file
    f.close
    return len(ip_list)


if __name__ == '__main__':
    n_uniip = uniq_ip('programming-task-example-data_(1).log')


    print('The number of unique IP addresses is :',n_uniip,'\n',
            'The top 3 most visited URLs are: ','\n',
            'The top 3 most active IP addresses are: ', '\n')