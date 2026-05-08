# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4377.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4377.pyc
# Source Generated with Decompyle++
# File: p4377.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_TRUE, DAM_TYPE_WEAPON, DAM_USE_ALL, EQUIP_TYPE_FUNDAMENTALWEAPON, OBJ_VICTIM
from cl_newformula import Func302

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAM, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0) and cl_evcon.CheckEventWeaponType(oWarrior, oEventCB, EQUIP_TYPE_FUNDAMENTALWEAPON):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_VICTIM)
        if cl_evcon.CheckHitWeakness(oWarrior, oEventCB, 0):
            cl_evact.EventTargetDamage(oWarrior, oEventCB, (lambda *a: (Func302(*a, **{
'sAttr': 'HPMax' }) + Func302(*a, **{
'sAttr': 'ArmorMax' }) + Func302(*a, **{
'sAttr': 'ShieldMax' })) * 50 / 100), DAM_TYPE_WEAPON | DAM_TYPE_TRUE | DAM_USE_ALL, 1, 1, 0, 0, 0, -1, -1, -1, None, None, None)
        else:
            cl_evact.EventChangeDamFactor(oWarrior, oEventCB, OBJ_VICTIM, 0, -9000, 0, '')


class CPerform(CCustomPerform):
    m_SID = 4377
    m_Name = '返璞归真（轮回九）'
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

