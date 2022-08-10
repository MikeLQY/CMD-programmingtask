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
    # seprate to 3 groups 0-199, 200-249,250-255
    p = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.)(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.)(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?\.)(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    for line in fline:
        ip_address = re.findall(p,line)
        # append to list if the ip has not been seen
        if ip_address not in ip_list:
            ip_list.append(ip_address)    
    #close file
    f.close
    return len(ip_list)

def v_url(filename):
    f = open(filename, 'r')
    url_list = []
    f.close
    return url_list

def active_ip(filename):
    f = open(filename, 'r')
    ip_list = []
    f.close
    return ip_list

if __name__ == '__main__':
    n_uniip = uniq_ip('programming-task-example-data_(1).log')
    top_url = v_url('programming-task-example-data_(1).log')
    top_ip = active_ip('programming-task-example-data_(1).log')
print(n_uniip)
# print('The number of unique IP addresses is :',n_uniip,'\n',
#             'The top 3 most visited URLs are: ',top_url,'\n',
#             'The top 3 most active IP addresses are: ',top_ip, '\n')