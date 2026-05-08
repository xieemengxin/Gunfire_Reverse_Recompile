# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relic/p5734.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relic/p5734.pyc
# Source Generated with Decompyle++
# File: p5734.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT, QUALITY_TYPE_HIGH, RELIC_TYPE_NORMAL
from cl_newformula import Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 0, 0, 39)
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, -10000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PREDICTDAMED, -1, 1, 0, 39)
    cl_action.CommonModifyDamResistance(oWarrior, oLifeCycle, -10000, DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 2217, 0, None) == 0:
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: max(100, int((Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) * 14 / 100 + 0))))


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 2217, 0, None) == 0:
        cl_evact.EventSetLimitDamage(oWarrior, oEventCB, (lambda *a: max(100, int((Func304(*a, **{
'sAttr': 'HPMax' }) + Func304(*a, **{
'sAttr': 'ShieldMax' }) + Func304(*a, **{
'sAttr': 'ArmorMax' })) * 11 / 100 + 0))))


class CPerform(CCustomPerform):
    m_SID = 5734
    m_Name = '灵猫九命'
    m_MaxLevel = 2
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_RelicType = RELIC_TYPE_NORMAL
    m_DropShape = 5525
    m_ValidRemove = 1
    m_BasePrice = 100
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_HIGH

