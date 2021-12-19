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

def xliff_translate(text): #funkcija sarunājas ar tildi - iztulko no angļu uz latviešu
    configParser = configparser.RawConfigParser()
    configFilePath = 'C:/Users/eliz_/Documents/elizabethan-tools/xlf_reader/properties.txt'
    configParser.read(configFilePath)
    client_id = configParser.get('your-config', 'client_id')
    system_id = configParser.get('your-config', 'system_id')
    service_url = configParser.get('your-config', 'service_url')
    response = requests.post(service_url,
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
    data = response.json()
    t = data['translation']
    return t

def main():
    # namespaces = {'default': 'urn:oasis:names:tc:xliff:document:1.2',
    #               'okp': 'okapi-framework:xliff-extensions',
    #               'its': 'http://www.w3.org/2005/11/its',
    #               'itsxlf': 'http://www.w3.org/ns/its-xliff/'}


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
        xliff_translated = xliff_translated.replace(chunk.group(1)+"</target>",translation+"</target>")
    #print(xliff_translated)
    save_path = (os.path.dirname(os.path.realpath(__file__)))
    completeName = os.path.join(save_path, sys.argv[1])
    #text_file = open("C:/Users/eliz_/Documents/elizabethan-tools/test-standalone/data_structures/translated_airports.md.xlf", "wb")
    text_file = open(completeName, "wb")
    text_file.write(xliff_translated.encode("utf-8"))
    text_file.close()



if __name__ == '__main__':
    main()