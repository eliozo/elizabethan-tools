# -*- coding: utf-8 -*-
import configparser
import requests
import time
import sys
import re

id_dict = dict() # vārdnīca atbilstošajām id formulām
def replace_tex_by_id(text):
    global id_dict
    pattern = re.compile(r"\$[^\$]+\$")
    formulas = pattern.findall(text)
    count = 1
    for formula in formulas:
        current_id = "§id{}§".format(count)
        id_dict[current_id] = formula
        text = text.replace(formula, current_id, 1)
        count +=1
    return text

def replace_id_by_tex(text):
    global id_dict
    for key in id_dict:
        formula = id_dict[key]
        text = text.replace(key, formula, 1)
    return text

def xliff_translate(text): #funkcija sarunājas ar tildi - iztulko no angļu uz latviešu
    global id_dict
    id_dict.clear()
    text_snippet = text
    if len(text) > 20:
        text_snippet = text[0:20]
    print("Tulko... <{}>".format(text_snippet))
    configParser = configparser.RawConfigParser()
    configFilePath = 'C:/Users/eliz_/Documents/elizabethan-tools/bin/properties.txt'
    configParser.read(configFilePath)
    client_id = configParser.get('your-config', 'client_id')
    system_id = configParser.get('your-config', 'system_id')
    service_url = configParser.get('your-config', 'service_url')
    text2 = replace_tex_by_id(text)
    response = requests.post(service_url,
                             headers={'Content-Type': 'application/json',
                                      'client-id': client_id},
                             json={'appID': 'TechChillDemo',
                                   'systemID': system_id,
                                   'text': text2,
                                   'options': 'alignment,markSentences,tagged'})
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(e.response.status_code)
        print(e.response.content)
    data = response.json()
    t = data['translation']
    t2 = replace_id_by_tex(t)
    return t2

def main():
    if len(sys.argv) < 2:
        print ("Kļūda! Vajag norādīt faila vārdu!")
        exit(1)
    else:
        filename = sys.argv[1]
    with open(filename, 'r', encoding='UTF-8') as file:
        xliff = file.read()

    xliff_translated = xliff

    rx_source = re.compile(r'<source xml:lang="en">((.|\n|\r)*?)</source>', re.MULTILINE)
    for chunk in rx_source.finditer(xliff):
        translation = xliff_translate(chunk.group(1))
        # translation = translation.replace("   ", "  \r\n")
        # tris_tuksumi = bytes.fromhex('202020')
        # divi_tuksumi = bytes.fromhex('20200D0A')
        # translation_bytes = translation.encode()
        # print(translation_bytes)
        # translation_bytes.replace(tris_tuksumi, divi_tuksumi)
        # translation = translation_bytes.decode()
        time.sleep(0.5)
        xliff_translated = xliff_translated.replace(chunk.group(1) + "</target>", translation + "</target>")
    print(sys.argv[1])
    with open(sys.argv[1], 'wb') as f:
        f.write(xliff_translated.encode('utf-8'))


if __name__ == '__main__':
    main()