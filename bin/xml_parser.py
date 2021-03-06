# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import configparser
import requests
import re
import lxml.etree as etree
from io import StringIO, BytesIO

id_dict = dict() # vārdnīca atbilstošajām id formulām
def replace_tex_by_id(text):
    global id_dict
    count = 1  # skaitītājs unikālu id veidošanai

    pattern_block = re.compile(r"\$\$[^\$]+\$\$") # meklējam visas block latex formulas
    formulas_block = pattern_block.findall(text)
    for formula in formulas_block:
        current_id = "§id{}§".format(count)
        id_dict[current_id] = formula
        # aizstāj formulu tikai 1 reizi
        text = text.replace(formula, current_id, 1)
        count +=1

    pattern = re.compile(r"\$[^\$]+\$") # meklējam visas inline latex formulas
    formulas = pattern.findall(text)
    for formula in formulas:
        current_id = "§id{}§".format(count)
        id_dict[current_id] = formula
        # aizstāj formulu tikai 1 reizi
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

def innertext(tag):
    return (tag.text or '') + ''.join(innertext(e) for e in tag) + (tag.tail or '')

def myfun(arg):
    if type(arg) == 'NoneType':
        return ''
    else:
        return arg

def test():
    root = etree.parse('../test-standalone/manual.md.xlf')
    for trans_unit in root.findall('.//{urn:oasis:names:tc:xliff:document:1.2}trans-unit'):
        # print("AAAAAAAAAA")
        source = trans_unit.find('{urn:oasis:names:tc:xliff:document:1.2}source')
        if (source.text == None):
            result = ''.join(etree.tostring(e).decode("utf-8") for e in source)
        else:
            result = source.text + ''.join(etree.tostring(e).decode("utf-8") for e in source)
        print(result)
        # print(innertext(source))

def main():
    # test()
    # exit(0)
    mytree = etree.parse('../test-standalone/manual.md.xlf')
    for trans_unit in mytree.findall('.//{urn:oasis:names:tc:xliff:document:1.2}trans-unit'):
        # print("AAAAAAAAAA")
        source = trans_unit.find('{urn:oasis:names:tc:xliff:document:1.2}source')
        print ("BBBBBBBBBB")
        if (source.text == None):
            result = ''.join(etree.tostring(e).decode("utf-8") for e in source)
        else:
            result = source.text + ''.join(etree.tostring(e).decode("utf-8") for e in source)
        print(result)

# See https://www.geeksforgeeks.org/automated-software-testing-with-python/


if __name__ == '__main__':
    main()
