#import module Regular Expression
import re

#The number of unique IP addresses
def uniq_ip(filename):
    f = open(filename, 'r')
    fline = f.readlines()
    ip_list=[]
    uni_ip=[]
    # pattern for ip address, from 0.0.0.0 to 255.255.255.255
    # seprate to 3 groups 0-199, 200-249,250-255
    p = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    for line in fline:
        # append all IPs to the list
        ip_address = re.search(p,line).group()
        ip_list.append(ip_address)  
    
    # check if IP only occurred once in the list, if True append to list
    for line in fline:
        ip = re.search(p,line).group()
        if occur_once(ip_list, ip):
            uni_ip.append(ip)

    #close file
    f.close
    return uni_ip

#The top 3 most visited URLs
def v_url(filename):
    f = open(filename, 'r')
    fline = f.readlines()
    url_dic = {}
    p = r'https?://\S+|\bGET\s\S+'
    for line in fline:
        #url string after word 'GET'
        url_str = re.search(p,line).group().split()[1]
        if url_str not in url_dic:
            url_dic[url_str] = 1
        else:
            url_dic[url_str] += 1
    #sort url dictionary
    url_dic = sorted(url_dic.items(), key=lambda x: x[1], reverse=True)
    f.close
    return key_tuple(url_dic)[0:3]

#The top 3 most active IP addresses
def active_ip(filename):
    f = open(filename, 'r')
    fline = f.readlines()
    #A dictionary, IP as key, number of appearance as value
    ip_dict = {}
    # IP address pattern
    p = r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)'
    for line in fline:
        ip_address = re.search(p,line).group()
        if ip_address not in ip_dict:
            ip_dict[ip_address] = 1
        else:
            ip_dict[ip_address] += 1

    #sorted list of key value tuples
    ip_dict = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)

    #close file
    f.close
    return key_tuple(ip_dict)[0:3]

# Extract keys from a list of key value tuple
def key_tuple(tuple_list):
    l = []
    # take the first element in the tuple which is the key
    for kv_tuple in tuple_list:
        l.append(kv_tuple[0])
    return l

    
def occur_once(l, elem):
    return l.count(elem) == 1

if __name__ == '__main__':
    n_uniip = len(uniq_ip('programming-task-example-data_(1).log'))
    top_url = v_url('programming-task-example-data_(1).log')
    top_ip = active_ip('programming-task-example-data_(1).log')

print('The number of unique IP addresses is :',n_uniip,'\n',
            'The top 3 most visited URLs are: ',top_url[0],',',top_url[1],',',top_url[2],'\n',
            'The top 3 most active IP addresses are: ',top_ip[0],',',top_ip[1],',',top_ip[2],'\n')