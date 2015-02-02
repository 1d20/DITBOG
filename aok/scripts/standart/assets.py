#-*- coding:utf-8 -*-
__author__ = 'Detonavomek'
#-*- coding:utf-8 -*-
import os

def generate_asset(theme_object, parent_path, path_to_script, path_to_out_folder):

    themeTitle = theme_object.title
    engineName = theme_object.engine.name
    outFileName = themeTitle.lower()+engineName+'.zip'

    fullPathToScript = parent_path+'/'+str(path_to_script)
    fullOutFolderPath = parent_path+'/'+path_to_out_folder
    themeTitle = '\'' + themeTitle + '\''
    engineName = '\'' + engineName + '\''
    request = 'python ' + fullPathToScript + ' ' + fullOutFolderPath + ' ' + themeTitle + ' ' + engineName
    print request
    os.system(request)
    theme_object.path_asset_folder = path_to_out_folder+'/'+outFileName
    return True