# coding: latin-1
import os
import sys

if len(sys.argv) < 2:
    print('not found patch folder in run arguments!')
    sys.exit(1)
patch_folder = sys.argv[1]
sql_files = []
workflow_files = []
for file in os.listdir(patch_folder + '/'):
    if '.sql' in file.lower():
        sql_files.append(file)
    elif '.xml' in file.lower():
        workflow_files.append(file)


file_list = open(patch_folder + '/file_list.txt', 'w')
if workflow_files:
    file_list.write(str('В патч идут потоки:\n'))
    for sql_item in sql_files:
        file_list.writelines(sql_item + '\n')

if sql_files:
    file_list.write(str('В патч идут скрипты:\n'))
    for sql_item in sql_files:
        file_list.writelines(sql_item + '\n')


file_list.close()
