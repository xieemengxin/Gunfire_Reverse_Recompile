# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5362.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5362.pyc
# Source Generated with Decompyle++
# File: p5362.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_MASK_SRC, OBJECT_SERVANT, OBJ_ATTACK, OBJ_VICTIM
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenServantMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
    if cl_evcon.CheckTargetDist(oWarrior, oEventCB, 10, 0, OBJECT_SERVANT):
        cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_ATTACK, 0, (lambda *a: Func717(*a, **{
'sArg': 'DamMul' }) * 100), DAM_MASK_SRC, '')


class CPerform(CCustomPerform):
    m_SID = 5362
    m_Name = '#NT#小玖升级1'
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
        'DamMul': 50 }
    m_DieDisable = 0

