# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25734.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25734.pyc
# Source Generated with Decompyle++
# File: p25734.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import DAM_TYPE_HARDNESS, OBJ_VICTIM, QUALITY_TYPE_HIGH
from cl_newformula import Func304, Func423, Func557

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 20)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: max(100, int((Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) * 14 / 100 + 0))))
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func423(*a))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func557(*a) * 14 / 100)):
        cl_evact.EventCBAddHitPart(oWarrior, oEventCB, DAM_TYPE_HARDNESS)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 10000, 0, 0, '')


class CPerform(CCustomPerform):
    m_SID = 25734
    m_Name = '灵猫九命'
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
    m_RelicType = 0
    m_HeroRelic = 5734
    m_Quality = QUALITY_TYPE_HIGH
    m_ExcludeRelic = ()

