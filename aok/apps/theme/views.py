#-*- coding:utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from models import Engine, Theme
from utils.decorators import render_to
from scripts import controller
from utils import template_folders
import base64 as kostul
from ditbog.settings import MEDIA_ROOT

@login_required
@render_to('theme/themes.html')
def themes(request, engine_id=0):
    if engine_id == 0:
        title = 'All themes'
        themes = Theme.objects.filter()
    else:
        title = Engine.objects.get(id=engine_id).name
        themes = Theme.objects.filter(engine_id = engine_id)

    return { 'active_page':'themes', 'active_engine':int(engine_id), 'engines':Engine.objects.filter(), 'title':title,
             'themes': themes}

@login_required
@render_to('theme/theme.html')
def show(request, theme_id=0):
    title=Theme.objects.get(id=theme_id).title
    c = { 'active_page':'themes', 'active_engine':0, 'engines':Engine.objects.filter(), 'title':title,
             'theme':Theme.objects.get(id=theme_id) }
    c.update(csrf(request))
    return c

@login_required
@render_to('theme/theme_add.html')
def add(request):
    if request.method == 'POST':
        if len(request.POST['theme']) > 0:
            theme = Theme()
            theme_engine = Engine.objects.get(id=request.POST['engine'])
            theme.engine = theme_engine
            theme.title = request.POST['theme']
            theme.package_name = controller.generate_package_name(theme_engine.package_template_name, request.POST['theme'])
            theme.save()
            return  HttpResponseRedirect('/theme/themes/')
    c = {}
    c.update(csrf(request))
    return { 'active_page':'add_theme', 'title':'Add theme', 'active_engine':0, 'engines':Engine.objects.filter() }

@login_required
@render_to('theme/themes.html')
def zip(request, type='nobody'):
    if request.method == 'POST':
        file_content = request.POST['file']
        file_content = kostul.b64decode(file_content)
        theme_id = int(request.POST.get('theme_id'))
        theme = Theme.objects.get(id=theme_id)
        f = open(MEDIA_ROOT+'/'+str(theme.path_res_folder), 'w')
        f.write(file_content)
        f.close()
    return  HttpResponseRedirect('/theme/themes/')

@login_required
@render_to('theme/themes.html')
def change(request):
    action = request.POST['sender']
    themes = request.POST['selected'].split(';')
    print action, themes
    for theme_id in themes:
        if len(theme_id)<1:
            continue
        theme = Theme.objects.get(id=theme_id)
        if action == 'btn_vers':
            theme.version = controller.add_version(theme.version)
        elif action == 'btn_desc':
            controller.generate_desc(theme)
        elif action == 'btn_res':
            controller.generate_res(theme, template_folders.PATH_TO_MEDIA_FOLDER,
                                        theme.engine.path_script_res, template_folders.UPLOAD_RES_FOLDER )
        elif action == 'btn_asset':
            controller.generate_asset(theme, template_folders.PATH_TO_MEDIA_FOLDER,
                                        theme.engine.path_script_asset, template_folders.UPLOAD_ASSET_FOLDER )
        elif action == 'btn_adv':
            controller.generate_adv(theme, theme.package_name,
                                                    template_folders.PATH_TO_MEDIA_FOLDER, theme.engine.path_info_appdf)
        elif action == 'btn_apk':
            theme.path_to_apk = controller.generate_apk(theme)
        elif action == 'btn_all':
            theme.version = controller.add_version(theme.version)
            controller.generate_desc(theme)
            controller.generate_res(theme, template_folders.PATH_TO_MEDIA_FOLDER,
                                        theme.engine.path_script_res, template_folders.UPLOAD_RES_FOLDER )
            controller.generate_asset(theme, template_folders.PATH_TO_MEDIA_FOLDER,
                                        theme.engine.path_script_asset, template_folders.UPLOAD_ASSET_FOLDER )
            controller.generate_adv(theme, theme.package_name,
                                                    template_folders.PATH_TO_MEDIA_FOLDER, theme.engine.path_info_appdf)
            theme.path_to_apk = controller.generate_apk(theme, template_folders.PATH_TO_MEDIA_FOLDER,
                                                    template_folders.UPLOAD_APK_FOLDER )
        elif action == 'btn_market':
            print 'WARNING: No code to load to market'
        theme.save()
    return HttpResponseRedirect('/theme/themes/')