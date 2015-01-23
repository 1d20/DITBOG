__author__ = 'Detonavomek'
from scripts.standart import version, package_name, resources, assets, advertisement, apk, descriprion

def add_version(currentVersion):
    return version.add_version(currentVersion)

def generate_package_name(templatePackageName, themeTitle):
    return package_name.generate_package_name(templatePackageName, themeTitle)

def generate_res(theme_object, parent_path, path_to_script, path_to_out_folder):
    return resources.generate_res(theme_object, parent_path, path_to_script, path_to_out_folder)

def generate_asset(theme_object, parent_path, path_to_script, path_to_out_folder):
    return assets.generate_asset(theme_object, parent_path, path_to_script, path_to_out_folder)


def generate_adv(theme_object, package_name, parent_path, path_info_appdf):
    return advertisement.generate_advertisement(theme_object, package_name, parent_path, path_info_appdf)


def generate_apk(theme_object):
    return apk.generate_apk(theme_object)


def generate_desc(theme_object):
    return descriprion.generate_desc(theme_object)
