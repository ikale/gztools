"""
# 打包whl文件,并发布到pypi.org
"""
# python setup.py bdist_wheel
# python -m twine upload ./dist/*
import os
import subprocess

def get_last_whl_file(whl_dir:str)->str:
    dist_path = os.path.abspath(whl_dir)
    files = os.listdir(dist_path)
    last_whl_file = ''
    _max = 0
    for f in files:
        _whl_file = '\\'.join([dist_path,f])
        t = os.path.getmtime(_whl_file)
        if t>_max:
            _max = t
            last_whl_file = _whl_file
    if not last_whl_file:
        raise RuntimeError("没有找到.whl文件")
    return last_whl_file