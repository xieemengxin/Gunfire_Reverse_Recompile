# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4236.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4236.pyc
# Source Generated with Decompyle++
# File: p4236.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import CURE_TYPE_PERFORM, DAM_USE_SHIELD, OBJ_SELF, OBJ_VICTIM, PF_TYPE_CAREERPF, PF_TYPE_THROW
from cl_newformula import Func221, Func224, Func225, Func304, Func361, Func367

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8008, 1000, { }, -1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 7, None, None)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def DisableAction1(oWarrior, oLifeCycle):
    oWarrior.Delete('PF4236_Task1014')


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, None) or cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_THROW, None):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, 15000, 0, '')
    else:
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, 7500, 0, '')


def DoCallBackAction1(oEventCB, oWarrior):
    if oWarrior.Energy() == cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func304(*a, **{
'sAttr': 'EnergyMax' }))):
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 8001, 0, { }, 0, 0, None)
        cl_action.CommonSetCustomData(oWarrior, oEventCB.GetCBLifeCycle(), 'PF4236_Task1014', 1)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
    cl_evact.EventTargetCure(oWarrior, oEventCB, (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' })), CURE_TYPE_PERFORM | DAM_USE_SHIELD, 0, 1, None)


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func221(*a))) == 0:
        cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: Func367(*a, **{
'sAttr': 'HPMax' }) * (1 + (Func224(*a) - 1) * 200 / 100) * (1 + Func225(*a, **{
'sAttr': 'HPMax' }) + Func221(*a) * 160 / 100) * 0.72))
    elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func221(*a))) >= 8:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func221(*a))) >= 10:
            cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: (Func361(*a, **{
'sid': 14415,
'sArgs': 'ShieldMaxMul' }) / 100) * Func304(*a, **{
'sAttr': 'HPMax' })))
        elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func224(*a))) == 1:
            cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: Func367(*a, **{
'sAttr': 'HPMax' }) * (1 + (Func224(*a) - 1) * 400 / 100) * (1 + Func225(*a, **{
'sAttr': 'HPMax' }) + (Func221(*a) - 1) * 160 / 100) * 0.72 - (Func221(*a) - 1) * 100000000))
        else:
            cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: (Func367(*a, **{
'sAttr': 'HPMax' }) * (1 + (Func224(*a) - 1) * 400 / 100) * (1 + Func225(*a, **{
'sAttr': 'HPMax' }) + (Func221(*a) - 1) * 160 / 100) * 0.72 - (Func221(*a) - 1) * 100000000) * Func224(*a) ** -0.47 * 0.47))
    elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func224(*a))) == 1:
        cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: Func367(*a, **{
'sAttr': 'HPMax' }) * (1 + (Func224(*a) - 1) * 200 / 100) * (1 + Func225(*a, **{
'sAttr': 'HPMax' }) + Func221(*a) * 160 / 100) * 0.72 - Func221(*a) * 100000000))
    else:
        cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: (Func367(*a, **{
'sAttr': 'HPMax' }) * (1 + (Func224(*a) - 1) * 200 / 100) * (1 + Func225(*a, **{
'sAttr': 'HPMax' }) + Func221(*a) * 160 / 100) * 0.72 - Func221(*a) * 100000000) * Func224(*a) ** -0.2 * 0.53))


def DoCallBackAction7(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func224(*a))) > 0:
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func221(*a))) == 0:
            cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: Func367(*a, **{
'sAttr': 'HPMax' }) * (1 + (Func224(*a) - 1) * 200 / 100) * (1 + Func225(*a, **{
'sAttr': 'HPMax' }) + Func221(*a) * 160 / 100) * 0.72))
        elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func221(*a))) >= 8:
            if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func221(*a))) >= 10:
                cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: (Func361(*a, **{
'sid': 14415,
'sArgs': 'ShieldMaxMul' }) / 100) * Func304(*a, **{
'sAttr': 'HPMax' })))
            elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func224(*a))) == 1:
                cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: Func367(*a, **{
'sAttr': 'HPMax' }) * (1 + (Func224(*a) - 1) * 400 / 100) * (1 + Func225(*a, **{
'sAttr': 'HPMax' }) + (Func221(*a) - 1) * 160 / 100) * 0.72 - (Func221(*a) - 1) * 100000000))
            else:
                cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: (Func367(*a, **{
'sAttr': 'HPMax' }) * (1 + (Func224(*a) - 1) * 400 / 100) * (1 + Func225(*a, **{
'sAttr': 'HPMax' }) + (Func221(*a) - 1) * 160 / 100) * 0.72 - (Func221(*a) - 1) * 100000000) * Func224(*a) ** -0.47 * 0.47))
        elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func224(*a))) == 1:
            cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: Func367(*a, **{
'sAttr': 'HPMax' }) * (1 + (Func224(*a) - 1) * 200 / 100) * (1 + Func225(*a, **{
'sAttr': 'HPMax' }) + Func221(*a) * 160 / 100) * 0.72 - Func221(*a) * 100000000))
        else:
            cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', (lambda *a: (Func367(*a, **{
'sAttr': 'HPMax' }) * (1 + (Func224(*a) - 1) * 200 / 100) * (1 + Func225(*a, **{
'sAttr': 'HPMax' }) + Func221(*a) * 160 / 100) * 0.72 - Func221(*a) * 100000000) * Func224(*a) ** -0.2 * 0.53))
    else:
        cl_action.CommonForceSetAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'ShieldMax', 10000000)


class CPerform(CCustomPerform):
    m_SID = 4236
    m_Name = '妖王-阶段5-逆散'
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
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        7: DoCallBackAction7 }
    m_BaseArgData = { }
    m_DieDisable = 0

