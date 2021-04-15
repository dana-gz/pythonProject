import webbrowser

prefix = ['https://', 'http://', "www."]
suffix = ['.com', '.pl']
# text1 = "www.xkcd.com/353/"
text1 = input('Write address www: ')

i = 0
j = 0

for i in range(len(prefix)):
    if text1.startswith(prefix[i]):
        for j in range(len(suffix)):
            if text1.endswith(suffix[j]):
                webbrowser.open(text1)
                break
            else:
                print('Bad suffix')
                break
    else:
        print('Bad prefix')

   #secon version with try exception

for i in range(len(prefix)):
    try:
       webbrowser.open(text1)

    except URLError:
        print('Bad preffix')



