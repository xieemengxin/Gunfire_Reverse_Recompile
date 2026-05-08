# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5305.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5305.pyc
# Source Generated with Decompyle++
# File: p5305.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_item.defines import MSG_ITEM_MAXPFBULLET_CHANGE
from cl_commondefines import DPSUBMSG_NOFIRE, SKILLCACHE_PERFORMMODE
from cl_newformula import Func686

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonWeaponMsgCallBack(oWarrior, oLifeCycle, MSG_ITEM_MAXPFBULLET_CHANGE, 0, 0, 1)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DP, DPSUBMSG_NOFIRE, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetSourceWeaponPerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 9094, 'ChargeTime', (lambda *a: Func686(*a, **{
'iPerform': 9094,
'sAttr': 'MaxPFBullet' }) / 60))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.EventCBCheckSkillCache(oWarrior, oEventCB, SKILLCACHE_PERFORMMODE):
        cl_evact.EventCBClearCollectInfo(oWarrior, oEventCB, 'NoPFBulletUse', 0)
    else:
        cl_evact.EventCBSetCollectInfo(oWarrior, oEventCB, 'NoPFBulletUse', 1, 0)


class CPerform(CCustomPerform):
    m_SID = 5305
    m_Name = '六方-同步消耗'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0

