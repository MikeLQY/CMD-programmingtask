#import module Regular Expression
import re

#The number of unique IP addresses

f = open('programming-task-example-data_(1).log', 'r')
fline = f.readlines()
def uniq_ip(filename):
    f = open(filename, 'r')
    ip_list=[]
    # pattern for ip address, from 0.0.0.0 to 255.255.255.255
    # seprate to 3 groups 0-199, 200-249,250-255
    p = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    for line in fline:
        list_ip_address = re.findall(p,line)
        # append to list if the ip has not been seen
        for ip in list_ip_address:
            if ip not in ip_list:
                ip_list.append(ip)   

    #close file
    f.close
    return ip_list

#The top 3 most visited URLs
def v_url(filename):
    f = open(filename, 'r')
    url_list = []
    f.close
    return url_list

#The top 3 most active IP addresses
def active_ip(filename):
    f = open(filename, 'r')
    #A dictionary, IP as key, number of appearance as value
    ip_dict = {}
    p = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    for line in fline:
         ip_address = re.findall(p,line)
         for ip in ip_address:
            if ip not in ip_dict:
                ip_dict[ip] = 1 
            else:
                ip_dict[ip] += 1

    #sorted list of key value tuples
    ip_dict = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)

    # take the first element in the tuple which is the key(IP address)
    ip_list = []
    for kv_tuple in ip_dict:
        ip_list.append(kv_tuple[0])
  
    #close file
    f.close
    return join_tuple(ip_list[0:3])



# convert tuple of string into IP address format
def join_tuple(tup_list):
    l = []
    for i in tup_list:
        l.append('.'.join(i))
    return l
    

if __name__ == '__main__':
    n_uniip = len(uniq_ip('programming-task-example-data_(1).log'))
    top_url = v_url('programming-task-example-data_(1).log')
    top_ip = active_ip('programming-task-example-data_(1).log')

print('The number of unique IP addresses is :',n_uniip,'\n',
            'The top 3 most visited URLs are: ',top_url,'\n',
            'The top 3 most active IP addresses are: ',top_ip, '\n')