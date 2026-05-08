# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6912.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6912.pyc
# Source Generated with Decompyle++
# File: p6912.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform
from cl_commondefines import PICK_INKBEAD, PICK_SPECIALINKBEAD
from cl_newformula import Func361, Func407

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_INKBEAD, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PICK, PICK_SPECIALINKBEAD, 0, 0, 0)
    cl_action.CommonChangePerformAttr(oWarrior, oLifeCycle, 1326, 'Att', 0, 15000)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 33044, (lambda *a: 300 * max(Func361(*a, **{
'sid': 3611,
'sArgs': 'Times' }), 1)), (lambda *a: Func407(*a, **{
'sid': 33044 })))


class CPerform(CCustomPerform):
    m_SID = 6912
    m_Name = '水墨画师lv.2'
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

