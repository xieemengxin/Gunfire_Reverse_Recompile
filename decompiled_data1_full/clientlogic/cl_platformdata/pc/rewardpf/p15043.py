# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15043.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15043.pyc
# Source Generated with Decompyle++
# File: p15043.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 42)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 2217, 0, None) == 0:
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: max(100, int((Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) * 25 / 100 + 0))))


class CPerform(CCustomPerform):
    m_SID = 15043
    m_Name = '灵猫四命'
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

