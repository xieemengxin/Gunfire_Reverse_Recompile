# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15308.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15308.pyc
# Source Generated with Decompyle++
# File: p15308.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PFBULLET_SUBMSG_ADD_BEFORE
from cl_newformula import Func825

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPFBULLETCHANGE, PFBULLET_SUBMSG_ADD_BEFORE, 0, 0, 0)
    cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11132, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func825(*a))) < 50:
        cl_evact.EventCBAddWeaponPFBulletChangeNum(oWarrior, oEventCB, 2000)


class CPerform(CCustomPerform):
    m_SID = 15308
    m_Name = '枯荣往复'
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

