#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import requests, time, os

session = requests.Session()

session.headers = { 'User-Agent': 'Opera/9.80 (Windows NT 6.1) Presto/2.12.388 Version/12.15', 'Host': 'www.leadboltnetwork.net', 'Accept': 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1', 'Accept-Language': 'ru-RU,ru;q=0.9,en;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Referer': 'https://www.leadboltnetwork.net/publisher/login', 'Content-Type': 'application/x-www-form-urlencoded' , 'Connection': 'Keep-Alive'}

def AuthorizationLeadbolt(params):
    session.post("https://www.leadboltnetwork.net/publisher/login/index", params)
    print 'Authorization: '+params['email']

def AddNewProject(projectName, contentTypeId, categoryId):
    projectPostData = {
        'SiteName':projectName,
        'PlatformId':'2', #2 - Android
        'Url':'https://play.google.com/store/apps/details?id=com.fivemobile.thescore',
        'ContentTypeId':contentTypeId, #9 - game
        'CategoryId':categoryId, #20 - gaming
        'OptInType':'Full',
        'DemoPercentage':'60',
        'DemoAge':'18-25',
        'DemoGender':'Male',
        'DemoPercentage2':'40',
        'DemoAge2':'18-25',
        'DemoGender2':'Female'
    }
    session.post("https://www.leadboltnetwork.net/publisher/app/ajaxAdd/expand:1", projectPostData)
    print 'Add: '+projectName

def GetReEngegement(projectName):
    request = session.post("https://www.leadboltnetwork.net/publisher/app/action", {'q':projectName,'search':'go'})
    soup = BeautifulSoup(request.text)
    return soup.findAll('a',{'sectiontypeid':'16'})[0]['rel'][13:]

def GetBanner(projectName):
    request = session.post("https://www.leadboltnetwork.net/publisher/app/action", {'q':projectName,'search':'go'})
    soup = BeautifulSoup(request.text)
    for link in soup.findAll('em'):
        if link.text == 'Banner (320x50)':
            return link['rel'][17:]

def GetIdProjectByName(projectName):
    request = session.post("https://www.leadboltnetwork.net/publisher/app/action", {'q':projectName,'search':'go'})
    soup = BeautifulSoup(request.text)
    return soup.findAll('a',{'class':'title'})[0]['rel'][11:]

def AddBannerToProject(projectId):
    projectPostData = {
        'SectionTypeId':'5',
        'SectionName':'App Ad #4', #!!!!!!!!!!!!!!!
        'CustomBackground':'',
        'AppTemplateId':'2',
        'DockingY':'Top',
        'MarginY':'0',
        'AdFormat':'TextImage',
        'TeaseTime':'0',
        'PopupEnabled':'1',
        'TestEnabled':'1',
        'Opacity':'0',
        'EffectOpen':'none',
        'BackgroundColor':'#FFFFFF',
        'TitleText':'',
        'TitleColor':'#000000',
        'TitleBackground':'',
        'Description':'',
        'DescriptionColor':'#000000',
        'OfferBackground':'#000000',
        'OfferBorderColor':'#000000',
        'OfferTitleColor':'#FFFFFF',
        'OfferSubTitleColor':'#AACCFF',
        'OfferTextColor':'#FFFFFF'
    }
    session.post("https://www.leadboltnetwork.net/publisher/app/ajaxSectionAddApp/id:"+projectId+"/tid:2", projectPostData)
    print 'Add banner: '+projectId

def WorkWithRow(fullName,projectName,package,contentTypeId,categoryId):
    AddNewProject(fullName,contentTypeId,categoryId)
    AddBannerToProject(GetIdProjectByName(fullName))
    return projectName+','+package[package.rindex(".")+1:]+','+GetReEngegement(fullName)+','+GetBanner(fullName) #engineName+'_'+projectName


result = 'appname,package_last_word,lbReEngegement,lbBanner\n'
rows = open('/Users/Detonavomek/Documents/Python_projects/ads/inYarik122o2.csv', 'r').readlines()
engineName = rows[0][:rows[0].index(',,')].replace(',','_').replace(' ','_').replace('-','_')
AuthorizationLeadbolt({'email':'plazmist@i.ua', 'password' : 'RGBkf,jhfnjhbz2012'})
for row in rows[1:]:
    row = row[:-1].split(',')
    result+=WorkWithRow(engineName+'_'+row[0].replace(' ','_').replace('-','_'),row[0],row[1],row[4],row[3])+'\n'
print result
open('/Users/Detonavomek/Documents/Python_projects/ads/out.csv', 'w').write(result)