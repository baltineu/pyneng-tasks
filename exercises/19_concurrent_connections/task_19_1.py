from concurrent.futures import *
from ping3 import ping


# ping
def pinger(host):
    result = ping(host)
    if result:
        return True
    else:
        return False


'''
def ping_ip_addresses(ip_list, limit=3):
    with ThreadPoolExecutor(limit) as executor:
        result = executor.map(pinger, ip_list)
        print("Выполнение идет сразу")
        accessible = []
        non_accessible = []
        for ip, output in zip(ip_list, result):
            if output:
                accessible.append(ip)
            else:
                non_accessible.append(ip)
    return accessible, non_accessible
'''


def ping_ip_addresses(ip_list, limit=3):
    with ThreadPoolExecutor(limit) as executor:

        future_result_list = []

        for ip in ip_list:
            future_result = executor.submit(pinger, ip)
            future_result_list.append(future_result)

        accessible = []
        non_accessible = []
        for ip, output in zip(ip_list, future_result_list):
            if output.result():
                accessible.append(ip)
            else:
                non_accessible.append(ip)
    return accessible, non_accessible
