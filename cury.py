import os
import sys
import time
import code
import random
import requests
import marshal
from uncompyle6.main import decompile

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.1)

def lisensi():
    os.system('clear')
    mengetik('#####################################')
    mengetik('#### \t</> \x1b[31;1mLICENSE LOGIN \x1b[37;1m</>    ####')
    mengetik('#####################################')
    username = raw_input('[*] Username : ')
    passw = raw_input('[*] Password : ')
    r = requests.get('https://pastebin.com/raw/wGWY2A3T').text
    if passw == '':
        print '\x1b[1;91m[!] U/P Salah!!!'
        keluar()
    elif len(passw) < 10:
        print '\x1b[1;91m[!] Silakan Beli Licensi Terlebih Dahulu Sebelum Memakai Toolsnya :)'
        keluar()
    elif passw in r:
        print '\x1b[1;91mLogin Succesfully'
        time.sleep(1)

def Py3():
    print 'Decompile code python3'
    c = raw_input('> File : ')
    print ''
    x = marshal.loads(code.py3)
    xx = decompile(3.7, x, sys.stdout)
    xxx = '# Python 3.7.x\n# Decompile Code by ./ExGeneralTz\n' + xx.text
    with open(c + '.py', 'w') as (f):
        f.write(xxx)
    print '\n\n[]Saved] file : \x1b[32m%s.py' % c
    print ''

def Py2():
    print 'Decompile code python2'
    c = raw_input('> File : ')
    print ''
    x = marshal.loads(code.py2)
    xx = decompile(2.7, x, sys.stdout)
    xxx = '# Python 2.7.x\n# Decompile Code by ./ExGeneralTz\n' + xx.text
    with open(c + '.py', 'w') as (f):
        f.write(xxx)
    print '\n\n[Saved] file : \x1b[32m%s.py' % c
    print ''


lisensi()

try:
    os.system('clear')
    mengetik('#####################################')
    mengetik('#### </> \x1b[31;1mProgram Information \x1b[37;1m</> ####')
    mengetik('#####################################')
    mengetik('- Author       : ./ExGeneralTz')
    mengetik('- Name Program : Decompile Marshall 2.7.x And 3.7.x')
    mengetik('- Created Date : 23-09-2019')
    print ''
    if sys.version[0] in '3':
        Py3()
    elif sys.version[0] in '2':
        Py2()
except Exception as F:
    print 'Err: %s' % F
