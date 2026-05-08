# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/relic/p5863.pyc
# RelativePath: clientlogic/cl_platformdata/pc/relic/p5863.pyc
# Source Generated with Decompyle++
# File: p5863.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relic import CRelic as CCustomPerform
from cl_commondefines import PF_SUBMSG_FILLBULLET, QUALITY_TYPE_NORMAL, RELIC_TYPE_NORMAL
from cl_newformula import Func555

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1718)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 1, 0, 0)
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1718)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1718, {
            'Count': (lambda *a: Func555(*a, **{
'sAttr': 'FillTime' }) // 50),
            'hittimes': (lambda *a: Func555(*a, **{
'sAttr': 'Trajectory' })) })
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 300)


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.PassiveCheckInColdTime(oWarrior, oEventCB, 1):
        cl_action.CommonUsePerform(oWarrior, oEventCB.GetCBLifeCycle(), 1718, {
            'Count': (lambda *a: Func555(*a, **{
'sAttr': 'FillTime' }) // 50 + 1),
            'hittimes': (lambda *a: Func555(*a, **{
'sAttr': 'Trajectory' })) })
        cl_evact.PassiveCBSetLiteCD(oWarrior, oEventCB, 300)


class CPerform(CCustomPerform):
    m_SID = 5863
    m_Name = '爆破弹夹'
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
    m_DropShape = 5524
    m_ValidRemove = 1
    m_BasePrice = 60
    m_bCanSell = 1
    m_Quality = QUALITY_TYPE_NORMAL

