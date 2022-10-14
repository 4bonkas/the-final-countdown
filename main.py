import requests
import webbrowser
# grab plaintext from endopoints
slay1 = requests.get('https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D') # replace each one of these with your link
slay2 = requests.get('https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D') # replace each one of these with your link
slay3 = requests.get('https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D') # replace each one of these with your link
slay4 = requests.get('https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D') # replace each one of these with your link
slay5 = requests.get('https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D') # replace each one of these with your link

# collect text from endpoints
secretLink = (slay1.text + slay2.text + slay3.text + slay4.text + slay5.text)

# open secret link in browser
bestSlay = ('https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string='+secretLink)
webbrowser.open_new_tab(bestSlay)
