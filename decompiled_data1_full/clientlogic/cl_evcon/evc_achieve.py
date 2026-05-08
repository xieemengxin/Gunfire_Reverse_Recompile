# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_evcon/evc_achieve.pyc
# RelativePath: clientlogic/cl_evcon/evc_achieve.pyc
# Source Generated with Decompyle++
# File: evc_achieve.pyc (Python 3.6)

from cl_only import Frame2Time
import cl_formula
import cl_math

def AchieveCBCheckWarStat(oListener, oEventCB, iTarget):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'AchieveStatSID' not in dEventInfo:
        return 0
    sKey = 'achieve%s' % dEventInfo['AchieveStatSID']
    iCur = oListener.QuerySavedData(sKey)
    return iCur >= iTarget


def AchieveCBGetCounting(oListener, oEventCB):
    dEventInfo = oEventCB.GetCBEventInfo()
    if 'AchieveStatSID' not in dEventInfo:
        return 0
    sKey = 'achieve%sCount' % dEventInfo['AchieveStatSID']
    iCountedFrame = oListener.Query(sKey, 0)
    if not iCountedFrame:
        sKey = 'achieve%sCountStart' % dEventInfo['AchieveStatSID']
        iStartFrame = oListener.Query(sKey, 0)
        if not iStartFrame:
            return 0
        oGame = oListener.m_Game
        iCurFrame = oGame.GetFrameNum()
        iCountedFrame = iCurFrame - iStartFrame
    return Frame2Time(iCountedFrame)

