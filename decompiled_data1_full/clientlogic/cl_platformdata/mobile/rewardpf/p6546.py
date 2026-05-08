# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/rewardpf/p6546.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/rewardpf/p6546.pyc
# Source Generated with Decompyle++
# File: p6546.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func509

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_ADDALLPLAYER, -1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetOwnerWeaponExtraInscriptionCost(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: min(10000, int(Func509(*a, **{
'sAttr': 'ItemBaseGrade' }) * 200))))


class CPerform(CCustomPerform):
    m_SID = 6546
    m_Name = '鬼斧神工'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0
    
    def Enable(self, oWarrior, iNotify = 0):
        oWarrior.Set('ExtraInscription', 1)
        super(CCustomPerform, self).Enable(oWarrior, iNotify)

    
    def Disable(self, oWarrior, iNotify = 1, iReleaseFlag = 0):
        oWarrior.Delete('ExtraInscription')
        super(CCustomPerform, self).Disable(oWarrior, iNotify, iReleaseFlag)


