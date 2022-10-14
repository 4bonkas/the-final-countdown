import requests
import webbrowser
# grab plaintext from endopoints
e1 = requests.get('https://roambarcelona.com/clock-pt1?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D')
e2 = requests.get('https://roambarcelona.com/clock-pt2?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D')
e3 = requests.get('https://roambarcelona.com/clock-pt3?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D')
e4 = requests.get('https://roambarcelona.com/clock-pt4?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D')
e5 = requests.get('https://roambarcelona.com/clock-pt5?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D')

#Collect text information from endpoints
secretKey = (e1.text + e2.text + e3.text + e4.text + e5.text)

#Open a url in browser
final = ('https://roambarcelona.com/get-flag?verify=Na2Q%2BeqhSP5hTRLDwpTNoA%3D%3D&string='+secretKey)
webbrowser.open_new_tab(final)
