import webbrowser
import urllib.error


def checksuffix():
    for i in range(len(suffix)):
        if suffix[i] == address[-(len(suffix[i])):]:
            print('s is true')
            return True
    # return False


def checkprefix():
    for j in range(len(prefix)):
        if prefix[j] == address[0:(len(prefix[j]))]:
            print('p is true')
            return True
    # return False


def open_url():
    if checkprefix() is True and checksuffix() is True:
        webbrowser.open(address)
    else:
        raise urllib.error.URLError('URLError')


prefix = ['https://', 'http://', 'www']
suffix = ['.com', '.pl']
address = input('Write internet page address : ')


try:
    open_url()
except urllib.error.URLError as e:
    print('Check the address - URLError')
