import subprocess
import time
from fping import FastPing
import os


def save(filename, comando):
    comando_completo = f"{comando} > {filename}"
    os.system(comando_completo)


save('ips.txt', 'fping -d -a -q -g -a -i 1 -r 0 192.168.1.0/24')


linhasrede = open("/home/whoami/Desktop/ipver/ips.txt", "r")
linhasbh = open("/home/whoami/Desktop/ipver/bhsoft.txt", "r")
bhsoft = open("/home/whoami/Desktop/ipver/bhsoft.txt", "r")
rede = open("/home/whoami/Desktop/ipver/ips.txt", "r")

conteudobh = bhsoft.readlines()
conteudorede = rede.readlines()
redecounter = 0
bhcounter = 0

p = 0
q = 0
x = 0
totalrede = sum(1 for line in linhasrede)
totalbh = sum(1 for line in linhasbh)
xtotalbh = totalrede


while x == 0:
    time.sleep(300)
    print('------ ===== X ===== ------')
    bhcounter = 0
    p = 0
    q = 0
    if totalrede < totalbh:
        xtotalbh = totalrede
    else:
        xtotalbh = totalbh
    while bhcounter < xtotalbh:
        if conteudobh[p] == conteudorede[q]:
            q = q + 1
            p = 0
            bhcounter = bhcounter + 1
        else:
            p = p + 1
            if p >= totalbh:
                print(conteudorede[q])
                q = q + 1
                p = 0
                bhcounter = bhcounter + 1
bhsoft.close()
rede.close()
