from requests import get
from colorama import Fore, init
import random
from fake_headers import Headers
import ctypes
import requests
from re import findall
from multiprocessing.dummy import Pool
import sys
import os

os.system('cls' if os.name == 'nt' else 'clear')
if os.name == 'nt':
    ctypes.windll.kernel32.SetConsoleTitleW('REVERSE IP BY ODUL TOOLS')
else:
    sys.stdout.write('REVERSE IP BY ODUL TOOLS')
init(autoreset=True)

fr = Fore.RED
fc = Fore.CYAN
fw = Fore.WHITE
fg = Fore.GREEN
fm = Fore.MAGENTA
header = Headers(browser='chrom', os='win', headers=True)

def process_ip(ip):
    api1(ip)
    api2(ip)
    api3(ip)

def api1(ip):
    try:
        url = 'https://rapiddns.io/s/' + ip + '?full=1&down=1#result'
        send_data = get(headers=header.generate(), url=url, timeout=35).text
        getlist = findall('<td>(?!\\-)(?:[a-zA-Z\\d\\-]{0,62}[a-zA-Z\\d]\\.){1,126}(?!\\d+)[a-zA-Z]{1,63}</td>', send_data)[3:]
        with open('Grabbed.txt', 'a') as revip1_file:
            for domain in getlist:
                domain_lower = domain.lower()
                if 'result' not in domain_lower and 'total' not in domain_lower and (not domain_lower.startswith('webmail.')) and (not domain_lower.startswith('ftp.')) and (not domain_lower.startswith('cpanel.')) and (not domain_lower.startswith('webdisk.')) and (not domain_lower.startswith('cpcalendars.')) and (not domain_lower.startswith('cpcontacts.')) and (not domain_lower.startswith('ns1.')) and (not domain_lower.startswith('ns2.')):
                    domain = domain.replace('www.', '')
                    domain = domain.replace('<td>', '')
                    domain = domain.replace('</td>', '')
                    print('\x1b[1;31m[ODUL_REVERSE]: \x1b[1;32m' + ip + ' ======> ' + '\x1b[0;36m' + domain)
                    revip1_file.write(domain + '\n')
    except:
        pass
    return None

def api2(ip):
    try:
        url = 'https://api.webscan.cc/?action=query&ip=' + ip
        send_data = get(headers=header.generate(), url=url, timeout=35).text
        getlist = findall('"domain": "(.*?)",', send_data)[3:]
        with open('Grabbed.txt', 'a') as revip1_file:
            for domain in getlist:
                domain_lower = domain.lower()
                if 'result' not in domain_lower and 'total' not in domain_lower and (not domain_lower.startswith('webmail.')) and (not domain_lower.startswith('ftp.')) and (not domain_lower.startswith('cpanel.')) and (not domain_lower.startswith('webdisk.')) and (not domain_lower.startswith('cpcalendars.')) and (not domain_lower.startswith('cpcontacts.')) and (not domain_lower.startswith('ns1.')) and (not domain_lower.startswith('ns2.')):
                    domain = domain.replace('www.', '')
                    print('\x1b[1;31m[ODUL_REVERSE]: \x1b[1;32m' + ip + ' ======> ' + '\x1b[0;36m' + domain)
                    revip1_file.write(domain + '\n')
    except:
        pass
    return None

def api3(ip):
    try:
        url = 'http://de-datacenter.xreverselabs.my.id:1337/reverse-ip?apikey=unknown&ip=' + ip
        send_data = get(headers=header.generate(), url=url, timeout=35).text
        getlist = findall('"(.*?)"', send_data)[3:]
        with open('Grabbed.txt', 'a') as revip_file:
            for domain in getlist:
                domain_lower = domain.lower()
                if 'status' not in domain_lower and 'success' not in domain_lower and ('Domains' not in domain_lower) and (not domain_lower.startswith('webmail.')) and (not domain_lower.startswith('ftp.')) and (not domain_lower.startswith('cpanel.')) and (not domain_lower.startswith('webdisk.')) and (not domain_lower.startswith('mail.')) and (not domain_lower.startswith('cpcontacts.')) and (not domain_lower.startswith('ns1.')) and (not domain_lower.startswith('ns2.')):
                    domain = domain.replace('www.', '')
                    domain = domain.replace('Domains', '')
                    print('\x1b[1;31m[ODUL_REVERSE]: \x1b[1;32m' + ip + ' =======> ' + '\x1b[0;36m' + domain)
                    revip_file.write(domain + '\n')
    except:
        pass
    return None

def main():
    print('\x1b[0;36m\n [#] this tool is ::\n\n [YOUR TOOL MESSAGE]\n\n                     telegram: [YOUR TELEGRAM]\n                     owner : [OWNER TELEGRAM]\n        ')
    ad = input('\x1b[1;31mEnter your ip : ')
    poolAmount = int(input('\x1b[1;31mThread: '))
    opens = open(ad, mode='r', errors='ignore').read().splitlines()
    Professor = Pool(poolAmount)
    Professor.map(process_ip, opens)

main()
input('ODUL THINGS!')
