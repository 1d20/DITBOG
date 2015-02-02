import subprocess

path_to_script = '/Users/Detonavomek/Documents/Python_projects/Django/ditbog/support_scripts/working/printer.py'
theme_name = 'theme N'
command = 'python '+path_to_script+' \''+theme_name+'\''

result = subprocess.check_output(command, shell=True)
print 'Result: '+ result[:-1]