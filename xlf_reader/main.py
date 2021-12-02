import requests
import json
#from xml.dom import minidom
import xml.etree.ElementTree


def xliff_translate(text): #funkcija sarunājas ar tildi - iztulko no angļu uz latviešu
    print('Text = {} '.format(text))

    client_id = '123'
    system_id = '456'
    response = requests.post('https://www.letsmt.eu/ws/service.svc/json/TranslateEx',
                             headers={'Content-Type': 'application/json',
                                      'client-id': client_id},
                             json={'appID': 'TechChillDemo',
                                   'systemID': system_id,
                                   'text': text,
                                   'options': 'alignment,markSentences,tagged'})
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(e.response.status_code)
        print(e.response.content)
    #print(json.dumps(response.json(), indent=4, sort_keys=True))
    #print(response.json())
    data = response.json()
    t = data['translation']
    return t

def main():
    namespaces = {'default': 'urn:oasis:names:tc:xliff:document:1.2',
                  'okp': 'okapi-framework:xliff-extensions',
                  'its': 'http://www.w3.org/2005/11/its',
                  'itsxlf': 'http://www.w3.org/ns/its-xliff/'}
    #t = xliff_translate("Description")
    #print(t)
    #filename = input('Ievadiet xlf faila vārdu: ')
    #file = minidom.parse(filename)
    filename = '../test-standalone/manual.md.xlf'
    file = xml.etree.ElementTree.parse(filename)
    parent_data = {}
    #file.findall('source', namespaces)
    for item in file.iter('default:source'):

        box_id_match = item.find('box_id')
        print(item)

if __name__ == '__main__':
    main()
