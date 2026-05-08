# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5324.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5324.pyc
# Source Generated with Decompyle++
# File: p5324.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func717
from cl_commondefines import LEVEL_TYPE_BOSS

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetPlantCanTransferState(oWarrior, oLifeCycle, {
        33733: 1 })
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ENTERSCENE, -1, 0, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33668, 0, {
        'DotDam': (lambda *a: Func717(*a, **{
'sArg': 'DotDam' })) }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckLevelType(oWarrior, oEventCB, LEVEL_TYPE_BOSS):
        cl_action.CommonChangeAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'HitRange', 0, 88, 0)
        if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1301003):
            cl_action.CommonSetAgentInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'HateSummon', 1)
        if cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1403001) or cl_condition.CheckCurLevel(oWarrior, oEventCB.GetCBLifeCycle(), 1403002):
            cl_action.CommonSetAgentInfo(oWarrior, oEventCB.GetCBLifeCycle(), 'HataProtege', 1)


class CPerform(CCustomPerform):
    m_SID = 5324
    m_Name = '园丁植物被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = {
        'DotDam': 1000 }
    m_DieDisable = 0

