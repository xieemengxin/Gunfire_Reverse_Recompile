# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p6968.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p6968.pyc
# Source Generated with Decompyle++
# File: p6968.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction6968 as CustomAction
from cl_platformdata.custom.passive.customaction import CustomActionInitChoosePF
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import BIGLION_STATE_BEGIN, BIGLION_STATE_END
from cl_newformula import Func201

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'HPMax', 5500)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldMax', 4500)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'RShield', 15)
    cl_action.CommonForceSetAttr(oWarrior, oLifeCycle, 'ShieldRecoverTime', 300)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1330, 'AddStateTime', 0, 300)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1434, 'ColdTime', 300)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1336, 'MinUseEnergy', 0)
    cl_action.CommonSetPerformAttr(oWarrior, oLifeCycle, 1329, 'MinUseEnergy', 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_END, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_BIGLION, BIGLION_STATE_BEGIN, 2, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1329, 'PerformCD', (lambda *a: 2000 - 400 * min(int(Func201(*a)), 4)), 1)
    cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1329, 'StateTime', (lambda *a: 3000 + 500 * min(int(Func201(*a)), 4)), 1)
    CustomActionInitChoosePF(oWarrior, oEventCB, {
        'FristLayer': {
            1: 1,
            3: 1 },
        'OtherLayer': {
            1: 1,
            2: 1,
            3: 1 },
        'Layer': 1,
        'Benediction': 13563,
        'BenedictionType': {
            4: 1 } })
    if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func201(*a))) >= 2:
        cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33855, 0, { }, 1, 0, 0)
    if cl_condition.CheckInPointLevel(oWarrior, oEventCB.GetCBLifeCycle(), {
        1101009: 1,
        1301002: 1,
        1301003: 1,
        1403003: 1,
        1403004: 1 }):
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'BanTurn', 1)
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33604, 0)
    else:
        cl_evact.EventCBSetCustomData(oWarrior, oEventCB, 'BanTurn', 0)


def DoCallBackAction1(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, {
        'Perform': 1329 })


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonSetPerformForceAttr(oWarrior, oEventCB.GetCBLifeCycle(), 1336, 'MinUseEnergy', 0)


class CPerform(CCustomPerform):
    m_SID = 6968
    m_Name = '苍玦队友AI属性强制值'
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
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0

