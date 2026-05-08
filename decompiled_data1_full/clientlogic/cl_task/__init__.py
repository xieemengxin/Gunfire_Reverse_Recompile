# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_task/__init__.pyc
# RelativePath: clientlogic/cl_task/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

import cl_platformdata

def NewTask(iTask, iID, oGame, iHero):
    clsTask = cl_platformdata.GetTaskClass(iTask)
    if not clsTask:
        return None
    return clsTask(iID, oGame, iHero)

