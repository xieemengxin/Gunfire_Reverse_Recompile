# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/benediction/p13556.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/benediction/p13556.pyc
# Source Generated with Decompyle++
# File: p13556.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.benediction.customaction import CustomAction13556 as CustomAction
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INKVALUE_ADD, INKVALUE_SUB, LEVEL_TYPE_BOSS, OBJ_ATTACK
from cl_newformula import Func304, Func360, Func518, Func638

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBackByAttr(oWarrior, oLifeCycle, 'ShieldMax', -1, 0, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenInkValueThreshold(oWarrior, oLifeCycle, 20, INKVALUE_ADD, 1, 0)
    cl_action.CommonListenInkValueThreshold(oWarrior, oLifeCycle, 20, INKVALUE_SUB, 4, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM, ATTACKERSUBMSG_NORMAL, 3, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonChangePerformAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1431, 'Att', (lambda *a: Func304(*a, **{
'sAttr': 'ShieldMax' }) * 2), 0)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func638(*a))) >= 20:
        cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 35, 35, 2)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.PassiveCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle(), 35, 35, 2)


def DoCallBackAction2(oEventCB, oWarrior):
    if not cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func518(*a, **{
'sAttr': 'ActiveHiding' }))):
        cl_action.CommonSendMessage(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WAR_CUSTOM_PERFORMINFO_CHANGE, -1, {
            'pfid': 13556 })
        if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func360(*a, **{
'sid': 1431,
'sAttr': 'ExplodeDelay' }))) or cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
            CustomAction(oWarrior, oEventCB, {
                'Dis': 60,
                'Perform': 12030,
                'State': 33271,
                'StateTime': 1200,
                'TargetBuild': (1169,),
                'CostInkValue': 20 })
        else:
            CustomAction(oWarrior, oEventCB, {
                'Dis': 20,
                'Perform': 12030,
                'State': 33271,
                'StateTime': 1200,
                'TargetBuild': (1169,),
                'CostInkValue': 20 })


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        12030: 1 }, 1, 0) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'Enhance', 0):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, 30000, 0, '')


def DoCallBackAction4(oEventCB, oWarrior):
    cl_action.PassiveCloseCycleExecCBFuncAction(oWarrior, oEventCB.GetCBLifeCycle())


class CPerform(CCustomPerform):
    m_SID = 13556
    m_Name = '韵溢墨涌'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        4: DoCallBackAction4 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = 117

