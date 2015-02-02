__author__ = 'Detonavomek'
from apps.utils.apk import package_name, resources, assets, apk, descriprion


def add_version(current_version):
    return str(float(current_version)+0.1)


def generate_package_name(template_packagename, theme_title):
    return package_name.generate_package_name(template_packagename, theme_title)


def generate_res(theme_object, parent_path, path_to_script, path_to_out_folder):
    return resources.generate_res(theme_object, parent_path, path_to_script, path_to_out_folder)


def generate_asset(theme_object, parent_path, path_to_script, path_to_out_folder):
    return assets.generate_asset(theme_object, parent_path, path_to_script, path_to_out_folder)


def generate_apk(theme_object):
    return apk.generate_apk(theme_object)


def generate_desc(theme_object):
    return descriprion.generate_desc(theme_object)
