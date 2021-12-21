# -*- coding: utf-8 -*-
import configparser
import requests
import time
import sys
import json
import os
#from xml.dom import minidom
import xml.etree.ElementTree
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
    # namespaces = {'default': 'urn:oasis:names:tc:xliff:document:1.2',
    #               'okp': 'okapi-framework:xliff-extensions',
    #               'its': 'http://www.w3.org/2005/11/its',
    #               'itsxlf': 'http://www.w3.org/ns/its-xliff/'}

    # text = "$999$ aaa $1$ 333"
    # global id_dict
    # text = replace_tex_by_id(text)
    # print(text)
    # print(id_dict)


    #filename = '../test-standalone/manual.md.xlf'
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
        time.sleep(0.5)
        # print("1111111111111111111111111111111111111111")
        # print(translation)
        # print("22222222222222222222222222222222222222222")
        # print(chunk.group(1))
        # print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        xliff_translated = xliff_translated.replace(chunk.group(1) + "</target>", translation + "</target>")
        # print(xliff_translated)
    #print(xliff_translated)
    #save_path = (os.path.dirname(os.path.realpath(__file__)))
    #completeName = os.path.join(save_path, sys.argv[1])
    #text_file = open("C:/Users/eliz_/Documents/elizabethan-tools/test-standalone/data_structures/translated_airports.md.xlf", "wb")
    # text_file = open(completeName, "wb")
    # text_file.write(xliff_translated.encode('utf-8')) #vajadzētu saprast, kāpēc neieraksta xlf_translated strigu failā
    # text_file.close()
    print(sys.argv[1])
    with open(sys.argv[1], 'wb') as f:
        f.write(xliff_translated.encode('utf-8'))


if __name__ == '__main__':
    main()