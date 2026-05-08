# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4124.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4124.pyc
# Source Generated with Decompyle++
# File: p4124.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func14, Func620, Func651

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_BEFORE, -1, 0, 1, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBUsePerform(oWarrior, oEventCB, 1609, 0, {
        'TriggerID': (lambda *a: Func651(*a, **{
'sKey': 'AID' })),
        'OriginID': (lambda *a: Func620(*a)),
        'TriggerFrame': (lambda *a: Func14(*a)) })


class CPerform(CCustomPerform):
    m_SID = 4124
    m_Name = '毒桶死前爆炸被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0 }
    m_BaseArgData = { }
    m_DieDisable = 0

