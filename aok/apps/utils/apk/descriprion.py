from apps.utils.config import template_folders

__author__ = 'Detonavomek'

from apps.theme.models import Description
from apps.theme.models import Language
from apps.theme.models import TemplateDescription

from apps.utils import utils

IDENT = "/{0.engine.name}_{0.title}_"

FULL_DESC = template_folders.UPLOAD_FULL_DESC_FOLDER + "{0}full_desc.txt"
SHORT_DESC = template_folders.UPLOAD_SHORT_DESC_FOLDER + "{0}short_desc.txt"

APP_ICON = template_folders.UPLOAD_APP_ICON_FOLDER + "{0}icon.png"
LARGE_PROMO = template_folders.UPLOAD_LARGE_PROMO_FOLDER + "{0}promo.png"
SCREENS = template_folders.UPLOAD_SCREENS_FOLDER + "{0}screen_{1}.png"


def __get_template_desc(lang, theme):
    template = TemplateDescription.objects.filter(language=lang, engine=theme.engine)
    desc = ""
    if template:
        desc = template[0].template_description
    else:
        desc = TemplateDescription.objects.filter(language=Language.objects.filter(name_short="en")[0], engine=theme.engine)[0].template_description
        desc = utils.translate(desc, lang.name_short)

    return desc.encode("UTF-8")

def __save_desc(path, lang, theme):
    with open(path.path, 'w') as f:
        f.write(__get_template_desc(lang, theme))

def __generate_def_desc(theme):
    en_desc = Description()

    en_desc.language = Language.objects.filter(name_short="en")[0];

    en_desc.theme = theme
    en_desc.title = theme.engine.name + " " + theme.title
    
    en_desc.keywords = utils.tuple2str(utils.associate(theme.title), ", ");
    
    en_desc.path_full_description = FULL_DESC.format(IDENT.format("en"))
    __save_desc(en_desc.path_full_description, en_desc.language, theme)
    en_desc.path_short_description = SHORT_DESC.format(IDENT.format("en"))
    __save_desc(en_desc.path_short_description, en_desc.language, theme)

    en_desc.path_app_icon = APP_ICON.format(IDENT.format("en"))
    utils.downloadIcon(theme.title, en_desc.path_app_icon.path)
    en_desc.path_large_promo = LARGE_PROMO.format(IDENT.format("en"))
    utils.downloadPromo(theme.title, en_desc.path_large_promo.path)
    en_desc.path_screens_folder = SCREENS.format(IDENT.format("en"), "0")
    
    en_desc.save()

    return en_desc

def generate_desc(theme):

    global IDENT
    IDENT = "/{0.engine.name}_{0.title}_"
    IDENT = IDENT.format(theme) + "{0}_"

    def_desc = __generate_def_desc(theme)

    for lang in Language.objects.all():
        if lang.name_short != "en":
            desc = Description()
            desc.language = lang;

            desc.theme = theme
            desc.title = utils.translate(theme.engine.name + " " + theme.title, lang.name_short)
    
            keywords = []
            for keyword in def_desc.keywords.split(", "):
                keywords.append(utils.translate(keyword, lang.name_short))
    
            if len(keyword) == 1:
                desc.keywords = keywords[0]
            else:
                desc.keywords = utils.tuple2str(keywords, ", ")
            
            desc.path_full_description = FULL_DESC.format(IDENT.format(lang.name_short))
            __save_desc(desc.path_full_description, lang, theme)
            desc.path_short_description = SHORT_DESC.format(IDENT.format(lang.name_short))
            __save_desc(desc.path_short_description, lang, theme)

            desc.save()
