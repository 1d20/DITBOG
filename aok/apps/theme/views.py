import base64
import os
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from forms import DescriptionForm
from models import Engine, Theme, Description
from apps.utils.config import template_folders
from apps.utils import apk_controller as controller
from source.settings import MEDIA_ROOT
from apps.image_processor import resize


@login_required
def themes(request, engine_id=0):
    if engine_id == 0:
        title = 'All themes'
        themes = Theme.objects.filter()
    else:
        title = Engine.objects.get(id=engine_id).name
        themes = Theme.objects.filter(engine_id=engine_id)

    return render(request, 'theme/themes.html',
                  {'active_page': 'themes', 'active_engine': int(engine_id),
                    'engines': Engine.objects.filter(), 'title': title, 'themes': themes})

@login_required
def show(request, theme_id=0):
    title=Theme.objects.get(id=theme_id).title
    c = { 'active_page':'themes', 'active_engine':0, 'engines':Engine.objects.filter(), 'title':title,
             'theme':Theme.objects.get(id=theme_id), 'form': DescriptionForm() }
    return render(request, 'theme/theme.html', c)

@login_required
def edit_description(request, desc_id=0):
    desc = get_object_or_404(Description, pk=desc_id)
    if request.method == 'GET':
        form = DescriptionForm(instance=desc)
    else:
        form = DescriptionForm(request.POST, instance=desc)
        if form.is_valid():
            form.save()
            return HttpResponse({'result': 'ok'}, content_type='application/json')
    data = {'form': form, 'desc': desc}
    return render(request, 'theme/elements/description_form.html', data)

@login_required
def add(request): 
    if request.method == 'POST':
        if len(request.POST['theme']) > 0:
            theme = Theme()
            theme_engine = Engine.objects.get(id=request.POST['engine'])
            theme.engine = theme_engine
            theme.title = request.POST['theme']
            theme.package_name = controller.generate_package_name(theme_engine.package_template_name, request.POST['theme'])
            theme.save()
            
            controller.generate_desc(theme)
            theme.generate_res()
            
            return HttpResponseRedirect('/theme/themes/')
    c = {}
    return render(request, 'theme/theme_add.html', { 'active_page':'add_theme', 'title':'Add theme', 'active_engine':0, 'engines':Engine.objects.filter() })

@login_required
def zip(request, type='nobody'):
    if request.method == 'POST':
        file_content = request.POST['file']
        file_content = base64.b64decode(file_content)
        theme_id = int(request.POST.get('theme_id'))
        theme = Theme.objects.get(id=theme_id)
        f = open(MEDIA_ROOT+'/'+str(theme.path_res_folder), 'w')
        f.write(file_content)
        f.close()
    return HttpResponseRedirect('/theme/themes/')

@login_required
def desc(request, theme_id=0):
    theme = Theme.objects.get(id=theme_id)
    theme_desc = None
    for desc in Description.objects.filter(theme=theme):
        if desc.language.name_short == "en":
            theme_desc = desc

    if request.method == 'POST':
        theme_desc.title = request.POST['title']
        theme_desc.short_description = request.POST['short_description']
        theme_desc.full_description = request.POST['full_description']

        if request.FILES['path_app_icon']:
            theme_desc.path_app_icon.save('icon', request.FILES['path_app_icon'])
            resize(theme_desc.path_app_icon.url, theme_desc.path_app_icon.url, (512, 512))

        theme_desc.save()

        return HttpResponseRedirect('/theme/themes/')
    

    return render(request, 'theme/descr.html', { 'theme':theme, 'desc': theme_desc, 'icon': os.path.basename(theme_desc.path_app_icon.url)})

@login_required
def res(request, theme_id=0):
    theme = Theme.objects.get(id=theme_id)

    item = theme.themedownloaditems_set.all()[0]

    if request.method == 'POST':
        if request.FILES['path_app_icon']:
            item.path.save('icon', request.FILES['path_app_icon'])
            resize(item.path.url, item.path.url, (640, 480))
        return HttpResponseRedirect('/theme/themes/')  

    # resize(item.path, item.path, (640, 480))
    return render(request, 'theme/res.html', { 'theme':theme, 'item': os.path.basename(item.path.url)})

@login_required
def apk(request, theme_id=0):
    theme = Theme.objects.get(id=theme_id)
    return HttpResponseRedirect('/media/apk/'+ controller.generate_apk(theme))

@login_required
def appdf(request, theme_id=0):
    theme = Theme.objects.get(id=theme_id)
    return HttpResponseRedirect('/media/appdf/'+ controller.generate_appdf(theme))

@login_required
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
            theme.generate_res()
            #controller.generate_res(theme, template_folders.PATH_TO_MEDIA_FOLDER,
            #                            theme.engine.path_script_res, template_folders.UPLOAD_RES_FOLDER )
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