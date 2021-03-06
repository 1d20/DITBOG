from apps.utils.config.template_folders import *

__author__ = 'Detonavomek'

from apps.theme.models import Description
from apps.theme.models import Language
from apps.theme.models import TemplateDescription

from apps.utils.utils import associate, downloadIcon, downloadPromo, translate, tuple2str

IDENT = "/{0.engine.name}_{0.title}_"

APP_ICON = APP_ICON_FOLDER + "{0}icon.png"
LARGE_PROMO = LARGE_PROMO_FOLDER + "{0}promo.png"
SCREENS = SCREENS_FOLDER + "{0}screen_{1}.png"


def __get_template_desc(lang, theme):
    template = TemplateDescription.objects.filter(language=lang, engine=theme.engine)

    if template:
        desc = template[0].template_description
    else:
        desc = TemplateDescription.objects.filter(language=Language.objects.filter(name_short="en")[0], engine=theme.engine)[0].template_description
        desc = translate(desc, lang.name_short)

    return desc

def __generate_def_desc(theme):

    lang = Language.objects.filter(name_short="en")[0]
    if len(Description.objects.filter(theme=theme, language=lang)):
        return Description.objects.filter(theme=theme, language=lang)[0]

    en_desc = Description()

    lang = en_desc.language = Language.objects.filter(name_short="en")[0]

    en_desc.theme = theme
    en_desc.title = theme.engine.name + " " + theme.title
    
    en_desc.keywords = tuple2str(associate(theme.title), ", ")
    
    en_desc.save()

    txt = __get_template_desc(lang, theme)
    en_desc.short_description = txt[:81]
    en_desc.full_description = txt

    en_desc.path_app_icon = APP_ICON.format(IDENT.format("en"))
    downloadIcon(theme.title, en_desc.path_app_icon.path)
    en_desc.path_large_promo = LARGE_PROMO.format(IDENT.format("en"))
    downloadPromo(theme.title, en_desc.path_large_promo.path)
    en_desc.path_screens_folder = SCREENS.format(IDENT.format("en"), "0")
    
    en_desc.save()

    return en_desc

def generate_desc(theme):

    global IDENT
    IDENT = "/{0.engine.name}_{0.title}_"
    IDENT = IDENT.format(theme) + "{0}_"

    def_desc = __generate_def_desc(theme)

    for lang in Language.objects.all():
        if len(Description.objects.filter(theme=theme, language=lang)):
            continue
        if lang.name_short != "en":
            desc = Description()
            desc.language = lang;

            desc.theme = theme
            desc.title = translate(theme.engine.name + " " + theme.title, lang.name_short)

            keywords = []
            for keyword in def_desc.keywords.split(", "):
                keywords.append(translate(keyword, lang.name_short))

            if len(keyword) == 1:
                desc.keywords = keywords[0]
            else:
                desc.keywords = tuple2str(keywords, ", ")

            desc.save()

            txt = __get_template_desc(lang, theme)
            desc.short_description = txt[:81]
            print desc.short_description
            desc.full_description = txt
            desc.save()
