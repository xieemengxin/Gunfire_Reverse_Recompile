# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51618.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51618.pyc
# Source Generated with Decompyle++
# File: p51618.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import DAM_MASK_CLASS, DAM_MASK_ELEMENT
from cl_newformula import Func594, Func717, Func844

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGERESISTANCE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddHPMax', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHPMax', 3000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGERESISTANCE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddHPMax', 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHPMax', 6000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGERESISTANCE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddHPMax', 100)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHPMax', 9000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action4(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGERESISTANCE, -1, 0, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddHPMax', 150)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHPMax', 12000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)


def Action5(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGERESISTANCE, -1, 2, 0, 0)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'ExtraAddHPMax', 200)
    cl_action.PassiveSetSelfArgValue(oWarrior, oLifeCycle, 'AddHPMax', 15000)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -Func844(*a) * 2), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', (lambda *a: Func717(*a, **{
'sArg': 'AddHPMax' }) + Func717(*a, **{
'sArg': 'ExtraAddHPMax' }) * max(0, -Func594(*a) // 100)), 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', (lambda *a: Func717(*a, **{
'sArg': 'AddHPMax' }) + Func717(*a, **{
'sArg': 'ExtraAddHPMax' }) * max(0, -Func594(*a) // 100)), 0, 0)
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -Func844(*a) * 2), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -Func844(*a) * 3), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', (lambda *a: Func717(*a, **{
'sArg': 'AddHPMax' }) + Func717(*a, **{
'sArg': 'ExtraAddHPMax' }) * max(0, -Func594(*a) // 100)), 0, 0)


def DoCallBackAction3(oEventCB, oWarrior):
    cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HPMax', (lambda *a: Func717(*a, **{
'sArg': 'AddHPMax' }) + Func717(*a, **{
'sArg': 'ExtraAddHPMax' }) * max(0, -Func594(*a) // 100)), 0, 0)
    cl_action.CommonModifyDamResistance(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: -Func844(*a) * 3), DAM_MASK_CLASS, DAM_MASK_ELEMENT, 1)


class CPerform(CCustomPerform):
    m_SID = 51618
    m_Name = '生存-生机流转'
    m_MaxLevel = 5
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3,
        4: Action4,
        5: Action5 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3 }
    m_BaseArgData = { }
    m_DieDisable = 0

