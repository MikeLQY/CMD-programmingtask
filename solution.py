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
    p = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\s)'
    for line in fline:
        # append all IPs to the list
        # if there is no valid IP address in the line, do nothing
        valid_ip = re.match(p,line)
        if valid_ip is None:
            pass
        else:
            ip_address = re.match(p,line).group()
            ip_list.append(ip_address)

    # check if IP only occurred once in the list, if True append to list
    for ip in ip_list:
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
        valid_url = re.search(p,line)
        if valid_url is None:
            pass
        else:
            url_str = re.search(p,line).group().split()[1]
            if url_str not in url_dic:
                url_dic[url_str] = 1
            else:
                url_dic[url_str] += 1
    #sort url dictionary
    url_dic = sorted(url_dic.items(), key=lambda x: x[1], reverse=True)
    f.close
    return key_tuple(url_dic)

#The top 3 most active IP addresses
def active_ip(filename):
    f = open(filename, 'r')
    fline = f.readlines()
    #A dictionary, IP as key, number of appearance as value
    ip_dict = {}
    # IP address pattern
    p = r'((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\s)'
    for line in fline:
        valid_ip = re.match(p,line)
        if valid_ip is None:
            pass
        else:
            ip_address = re.match(p,line).group()
            if ip_address not in ip_dict:
                ip_dict[ip_address] = 1
            else:
                ip_dict[ip_address] += 1

    #sorted list of key value tuples
    ip_dict = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)
    
    #close file
    f.close
    return key_tuple(ip_dict)

# Extract keys from a list of key value tuple
def key_tuple(tuple_list):
    l = []
    # take the first element in the tuple which is the key
    for kv_tuple in tuple_list:
        l.append(kv_tuple[0])
    return l

#check if an element of occured once in a list
def occur_once(l, elem):
    return l.count(elem) == 1

# unit test section
def test_ip():
    # test for unique ip addresses
    assert  len(uniq_ip('test_data.txt')) == 5, "Should be 5"

    # test for the top 3 most active ip addresses
    assert  active_ip('test_data.txt')[0].strip() == '168.41.191.4', "Should be 168.41.191.4"
    assert  active_ip('test_data.txt')[1].strip() == '50.112.00.11', "Should be 50.112.00.11"
    assert  active_ip('test_data.txt')[2].strip() == '88.88.88.88', "Should be 88.88.88.88"

# Test the top 3 most visited URLs
def test_url():
    assert v_url('test_data.txt')[0] == "http://test.com", "Should be http://test.com"
    assert v_url('test_data.txt')[1] == "http://example.net", "Should be http://example.net"
    assert v_url('test_data.txt')[2] == "/newsletter/", "Should be /newsletter/"


if __name__ == '__main__':

    n_uniip = len(uniq_ip('programming-task-example-data_(1).log'))
    top_url = v_url('programming-task-example-data_(1).log')
    top_ip = active_ip('programming-task-example-data_(1).log')
    test_ip()
    test_url()
    print("Passed all tests")

print('The number of unique IP addresses is :',n_uniip,'\n',
            'The top 3 most visited URLs are: ',top_url[0],',',top_url[1],',',top_url[2],'\n',
            'The top 3 most active IP addresses are: ',top_ip[0],',',top_ip[1],',',top_ip[2],'\n')
