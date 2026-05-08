# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5306.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5306.pyc
# Source Generated with Decompyle++
# File: p5306.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW
from cl_newformula import Func686

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_USE_CAREERPF, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 2, 0, 0)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1877, 0, { }, 1)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        1310: 1 }, 0, 0):
        cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9794, (lambda *a: 4 * Func686(*a, **{
'iPerform': 9794,
'sAttr': 'PFBulletRecover' })))


def DoCallBackAction1(oEventCB, oWarrior):
    if not cl_evcon.CheckPerformUnCrtByOwner(oWarrior, oEventCB):
        cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9794, (lambda *a: 2 * Func686(*a, **{
'iPerform': 9794,
'sAttr': 'PFBulletRecover' })))


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
        9704: 1,
        9705: 1,
        9706: 1,
        9707: 1 }, 0, 0):
        if cl_evcon.CheckWeaponHasInscription(oWarrior, oEventCB, 13095):
            cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9794, (lambda *a: 2 * Func686(*a, **{
'iPerform': 9794,
'sAttr': 'PFBulletRecover' })))
        else:
            cl_action.CommonAddSourceWeaponPFBullet(oWarrior, oEventCB.GetCBLifeCycle(), 9794, (lambda *a: Func686(*a, **{
'iPerform': 9794,
'sAttr': 'PFBulletRecover' })))


class CPerform(CCustomPerform):
    m_SID = 5306
    m_Name = '#NT聚能法杖被动'
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

