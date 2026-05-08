# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13519.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13519.pyc
# Source Generated with Decompyle++
# File: p13519.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_WEAPON, OBJ_ATTACK
from cl_newformula import Func361, Func410

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, (lambda *a: (1 + Func410(*a, **{
'sid': 1568 }) / 100) * Func410(*a, **{
'sid': 32775 }) * Func361(*a, **{
'sid': 4347,
'sArgs': 'FullEnergyRatio' }) * 125 / 100), 0, DAM_TYPE_WEAPON, '')


class CPerform(CCustomPerform):
    m_SID = 13519
    m_Name = '左右互搏'
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
    m_Career = 110

