#!/usr/bin/env python
# -*- coding:utf-8 -*-


import requests
import sys
import os
import thread


def phpscanf(url):
    try:
        ftext = open(url + '.txt', 'w+')
        url = 'http://%s' % url
        for result in open('php.txt','r'):
            result = result.strip()
            netcode = requests.get(str(url) + str(result))#Maybe can add a multi thread setting.
            if netcode.status_code == 200:
                ftext.write(netcode.url[:-1]+'\n')
                print 'the urls :\n' + netcode.url[:-1] + ' found - 200'
            else:
                continue
        ftext.close()
        
    except:
       print 'Input Error\n'

def aspscanf(url):
    try:
        ftext = open(url + '.txt', 'w+')
        url = 'http://%s' % url
        
        for result in open('asp.txt','r'):
            result = result.strip()
            netcode = requests.get(str(url) + str(result))
            if netcode.status_code == 200:
                ftext.write(netcode.url[:-1]+'\n')
                print 'the urls :\n' + netcode.url[:-1] + ' found - 200'
            else:
                continue
        ftext.close()
        
    except:
       print 'Input Error\n'

def jspscanf(url):
    try:
        ftext = open(url + '.txt', 'w+')
        url = 'http://%s' % url
        
        for result in open('jsp.txt','r'):
            result = result.strip()
            netcode = requests.get(str(url) + str(result))
            if netcode.status_code == 200:
                ftext.write(netcode.url[:-1]+'\n')
                print 'the urls :\n' + netcode.url[:-1] + ' found - 200'
            else:
                continue
        ftext.close()
        
    except:
       print 'Input Error\n'

def aspxscanf(url):
    try:
        ftext = open(url + '.txt', 'w+')
        url = 'http://%s' % url
        
        for result in open('aspx.txt','r'):
            result = result.strip()
            netcode = requests.get(str(url) + str(result))
            if netcode.status_code == 200:
                ftext.write(netcode.url[:-1]+'\n')
                print 'the urls :\n' + netcode.url[:-1] + ' found - 200'
            else:
                continue
        ftext.close()
        
    except:
       print 'Input Error\n'


def Init(choice,url):
    {'1':jspscanf,'2':phpscanf,'3':aspscanf,'4':aspxscanf}.get(choice)(url)

if __name__ == '__main__':

    os.system('cls')
    print 'Please Input GankWebsite！\nFor example:www.baidu.com'
    url = raw_input()
    print 'Please Input Website_scripts\nOptions:\n1.jsp\n2.php\n3.asp\n4.aspx'
    choice = raw_input()
    Init(choice,url)
    
    
    
    
    
