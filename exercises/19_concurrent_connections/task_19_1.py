# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

from concurrent.futures import *
from ping3 import ping


# ping
def pinger(host):
    result = ping(host)
    if result:
        return True
    else:
        return False


def ping_ip_addresses(ip_list, limit=3):
    with ThreadPoolExecutor(limit) as executor:
        result = executor.map(pinger, ip_list)
        accessible = []
        non_accessible = []
        for ip, output in zip(ip_list, result):
            if output:
                accessible.append(ip)
            else:
                non_accessible.append(ip)
        return accessible, non_accessible
