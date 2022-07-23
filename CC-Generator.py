from requests import post
print("""

 ██████╗ ██████╗               ██████╗ ███████╗███╗   ██╗
██╔════╝██╔════╝              ██╔════╝ ██╔════╝████╗  ██║
██║     ██║         █████╗    ██║  ███╗█████╗  ██╔██╗ ██║
██║     ██║         ╚════╝    ██║   ██║██╔══╝  ██║╚██╗██║
╚██████╗╚██████╗              ╚██████╔╝███████╗██║ ╚████║
 ╚═════╝ ╚═════╝               ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                         
                By @TweakPY - @vv1ck
""")
r=post("https://www.vccgenerator.org/fetchdata/generate-home-credit-card/",headers={'Host': 'www.vccgenerator.org','Cookie': 'csrftoken=yYUFqVjAqOVLWPG5FpEbqG4fO4aup1yJPEmflg0xKkITxmQBcAatOvsV4vLiOKco','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-Csrftoken': 'LCRIQJE48HmOhLMGQAIwxGpmpn8W7qDU2ijiL4l1sd9WSiWcnLeOVvN2FOJKw9hz','X-Requested-With': 'XMLHttpRequest','Content-Length': '25','Origin': 'https://www.vccgenerator.org','Referer': 'https://www.vccgenerator.org/','Te': 'trailers'},data=f'brand=VISA&country=UNITED+STATES&bank=COMMUNITY+NATIONAL+BANK&cvv=&date=&year=&range=500+-+1000&amount=1&dataformat=JSON&pin=on&ctoken=LCRIQJE48HmOhLMGQAIwxGpmpn8W7qDU2ijiL4l1sd9WSiWcnLeOVvN2FOJKw9hz')
try:
    cc_use=str(r.json()['creditCard']).split('[{')[1].split('}]')[0]
    print('-'*30)
    print(f"""
[+] Brand : {cc_use.split('IssuingNetwork')[1].split(',')[0].split("':")[1].split("'")[1]}
[+] Number : {cc_use.split('CardNumber')[1].split(',')[0].split("':")[1].split("'")[1]}
[+] Bank : {cc_use.split('Bank')[1].split(',')[0].split("':")[1].split("'")[1]}
[+] Name : {cc_use.split('Name')[1].split(',')[0].split("':")[1].split("'")[1]}
[+] Address : {cc_use.split('Address')[1].split(',')[0].split("':")[1].split("'")[1]}
[+] Country : {cc_use.split('Country')[1].split(',')[0].split("':")[1].split("'")[1]}
[+] Money : {cc_use.split('MoneyRange')[1].split(',')[0].split("':")[1].split("'")[1]}
[+] cvv : {cc_use.split('CVV')[1].split(':')[1].split(',')[0]}
[+] Expiry : {cc_use.split('Expiry')[1].split(',')[0].split("':")[1].split("'")[1]}
[+] Pin : {cc_use.split('Pin')[1].split(':')[1]}
""")
    print('-'*30)
except:exit('[!] Error ...')