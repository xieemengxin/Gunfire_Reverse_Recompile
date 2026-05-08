# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p6555.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p6555.pyc
# Source Generated with Decompyle++
# File: p6555.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import DEFEND_TREND_ARMOR, OBJ_SELF, TYPE_RELIFE_RESCUE
from cl_newformula import Func302, Func304

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckTargetDefendTrend(oWarrior, oLifeCycle, DEFEND_TREND_ARMOR):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 0, 0, 0)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RELIFE, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckRelifeType(oWarrior, oEventCB, TYPE_RELIFE_RESCUE):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * 10 / 100))
        cl_evact.EventChangeArmor(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ArmorMax' }) * 20 / 100))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckRelifeType(oWarrior, oEventCB, TYPE_RELIFE_RESCUE):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        cl_evact.EventChangeHP(oWarrior, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'HPMax' }) * 10 / 100))
        cl_evact.EventChangeShield(oWarrior, oEventCB, (lambda *a: Func302(*a, **{
'sAttr': 'ShieldMax' }) * 20 / 100))


class CPerform(CCustomPerform):
    m_SID = 6555
    m_Name = '返老还童'
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

