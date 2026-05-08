# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_achievement/pc/s1207.pyc
# RelativePath: clientlogic/cl_achievement/pc/s1207.pyc
# Source Generated with Decompyle++
# File: s1207.pyc (Python 3.6)

from cl_object.logging import SuitLog
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from ..mobject import CAchieveStat as CCustom

def EnableAction(oListener, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oListener, oLifeCycle, cl_msgcenter.MSG_WAR_ADDSUIT, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oListener):
    if cl_evcon.EventCBCheckUnLockNewSuit(oListener, oEventCB):
        cl_evact.AchieveCBAddStat(oListener, oEventCB, 1)
        CustomCBAction(oListener, oEventCB, { })


class CAchieveStat(CCustom):
    m_SID = 1207
    m_Name = '实用套路'
    m_TargetValue = 15
    m_Action = (EnableAction, None)
    m_CBFuncAction = {
        0: DoCallBackAction0 }


def CustomCBAction(oListener, oEventCB, dArgs):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'SuitID' not in dMsgInfo:
        return None
    iSuit = dMsgInfo['SuitID']
    dUnlockSuit = oListener.Query('UnlockSuit', { })
    dUnlockSuit[iSuit] = oListener.Query('FightIndex')
    oListener.Set('UnlockSuit', dUnlockSuit)
    SuitLog.Info(f'''achievement1207 addstat suitID:{iSuit} unlocksuit{dUnlockSuit}''')

