# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13547.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13547.pyc
# Source Generated with Decompyle++
# File: p13547.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import SKILLCACHE_LSTINT
from cl_newformula import Func555, Func576

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_REMOVEBENED_BEFORE, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_WEAPONPEOFROM_START, -1, 1, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 6556)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonRemovePerform(oWarrior, oLifeCycle, 6556)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventCBSetSavedData(oWarrior, oEventCB, 'BeneReward13547', 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        8505: 1,
        1319: 1,
        1315: 1 }, 1, 0):
        cl_evact.EventSetSkillCacheData(oWarrior, oEventCB, SKILLCACHE_LSTINT, (lambda *a: Func576(*a, **{
'sAttr': 'ItemType' })))
        cl_evact.EventAddSkillCacheData(oWarrior, oEventCB, SKILLCACHE_LSTINT, (lambda *a: Func555(*a, **{
'sAttr': 'ItemType' })))


class CPerform(CCustomPerform):
    m_SID = 13547
    m_Name = '石破天惊'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 111

