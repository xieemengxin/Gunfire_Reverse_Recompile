# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/customaction.pyc
# RelativePath: clientlogic/cl_achievement/customaction.pyc
# Source Generated with Decompyle++
# File: customaction.pyc (Python 3.6)

from cl_only import Frame2Time
import cl_evact

def CustomCBAction1035(oListener, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'LastFrame' not in dMsgInfo:
        return None
    iTime = Frame2Time(dMsgInfo['LastFrame'])
    cl_evact.AchieveCBAddStat(oListener, oEventCB, iTime)

