import shutil
import json
import os
import re
import io
import time
import zipfile
import shutil
from distutils.command.build_py import build_py
from distutils.core import setup
from Cython.Build import cythonize

import os
import re
import shutil
from distutils.command.build_py import build_py
from distutils.core import setup
from Cython.Build import cythonize

def search(content, regexs):
    if isinstance(regexs, str):
        return re.search(regexs, content)

    for regex in regexs:
        if re.search(regex, content):
            return True

def walk_file(file_path):
    if os.path.isdir(file_path):
        all_file_path = []
        for current_path, sub_folders, files_name in os.walk(file_path):
            for file in files_name:
                file_path = os.path.join(current_path, file)
                all_file_path.append(file_path)
    else:
        return ValueError(f"{file_path} must is directory")
    return all_file_path

def get_py_files(files, ignore_files=None):
    """
    @summary:
    ---------
    @param files: 文件列表
    #param ignore_files: 忽略的文件，支持正则
    ---------
    @result:
    """
    actual_files = []
    for file in files:
        if file.endswith(".py"):
            if ignore_files and search(file, regexs=ignore_files):  # 该文件是忽略的文件
                pass
            else:
                actual_files.append(file)
    return actual_files

def filter_cannot_encrypted_py(files, except_main_file):
    """
    过滤掉不能加密的文件，如 __main__.py 以及包含 if __name__ == "__main__": 的文件
    """
    _files = []
    for file in files:
        if search(file, regexs="__.*?.py"):
            continue

        if except_main_file:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
                if search(content, regexs="__main__"):
                    continue

        _files.append(file)

    return _files

def encrypt_py(py_files, temp_dir):
    encrypted_list = []
    total_count = len(py_files)
    for i, py_file in enumerate(py_files):
        try:
            dir_name = os.path.dirname(py_file)   
            file_name = os.path.basename(py_file) 
            print("正在加密 {}/{},  {}".format(i + 1, total_count, file_name))
            setup(
                ext_modules=cythonize([py_file], quiet=True, language_level=3),
                script_args=["build_ext", "-b", temp_dir],
            )
             
            for current_path, sub_folders, files_name in os.walk(temp_dir):
                for file in files_name:
                    file_path = os.path.join(current_path, file)
                    if file_name.split(".")[0] in file_path:
                        new_path = current_path + "/" + file_name.split(".")[0] + ".so"
                        move_path = dir_name + "/" + file_name.split(".")[0] + ".so"
                        # print(file_path, file_name.split(".")[0] , new_path)
                        os.rename(file_path, new_path)
                        shutil.move(new_path, move_path)
            encrypted_list.append(py_file)
            print("加密成功 {}".format(file_name))

        except Exception as e:
            print("加密失败 {} , error {}".format(py_file, e))
            temp_c = py_file.replace(".py", ".c")
            if os.path.exists(temp_c):
                os.remove(temp_c)
    return encrypted_list

def delete_file(encrypted_list):
    try:
        for file in encrypted_list:
            os.remove(file)  # py文件
            os.remove(file.replace(".py", ".c"))  # c文件
    except Exception as e:
        pass

if __name__ == "__main__":
    except_main_file = 1  # 1： 表示去掉py文件中带__main__ 的文件
    temp_dir = "temp"
    src_path = os.getcwd()
    all_file_path = walk_file(src_path)
    actual_files = get_py_files(all_file_path, ignore_files=[".venv", "build"])
    need_encrypted_py = filter_cannot_encrypted_py(actual_files, except_main_file)
    encrypted_list = encrypt_py(need_encrypted_py, temp_dir)
    delete_file(encrypted_list)
    temp_dir_path = src_path + "/" + temp_dir
    if os.path.isdir(temp_dir_path):                     
        shutil.rmtree(temp_dir_path)
    if os.path.isdir(src_path + "/" + "build"):          # 删除编译过程中产生的.o文件
        shutil.rmtree("build")