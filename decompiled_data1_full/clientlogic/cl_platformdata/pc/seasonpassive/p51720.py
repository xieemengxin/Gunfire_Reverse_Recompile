# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/seasonpassive/p51720.pyc
# RelativePath: clientlogic/cl_platformdata/pc/seasonpassive/p51720.pyc
# Source Generated with Decompyle++
# File: p51720.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.seasonpassive import CSeasonPassive as CCustomPerform
from cl_commondefines import S8THIRDACTIVE_REFRESH_MAXENERGY, S8_THIRDITEM_ENABLE, S8_THIRDITEM_REMOVE
from cl_newformula import Func717, Func859, Func862

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, S8THIRDACTIVE_REFRESH_MAXENERGY, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, S8_THIRDITEM_ENABLE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, S8_THIRDITEM_REMOVE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)


def Action2(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, S8THIRDACTIVE_REFRESH_MAXENERGY, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, S8_THIRDITEM_ENABLE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, S8_THIRDITEM_REMOVE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)


def Action3(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8THIRDACTIVE_ATT_REFRESH, S8THIRDACTIVE_REFRESH_MAXENERGY, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, S8_THIRDITEM_ENABLE, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_S8_CONTAINER_OPERATION, S8_THIRDITEM_REMOVE, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_UNHOLD_WEAPON, -1, 1, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_evact.PassiveCBSetPFArgs(oWarrior, oEventCB, 'AddCnt', (lambda *a: min(int(Func862(*a, **{
'sAttr': 'MaxEnergy' }) // 10), 15)))
    cl_action.CommonChangeWeaponPFBulletPerfomrAttrByHold(oWarrior, oEventCB.GetCBLifeCycle(), 0, 'MaxPFBullet', 0, (lambda *a: Func717(*a, **{
'sArg': 'AddCnt' }) * Func859(*a, **{
'sAttr': 'PerAddRatio' })))
    cl_action.CommonChangeWeaponPFBulletPerfomrAttrByHold(oWarrior, oEventCB.GetCBLifeCycle(), 0, 'PFBulletUse', 0, (lambda *a: Func717(*a, **{
'sArg': 'AddCnt' }) * Func859(*a, **{
'sAttr': 'PerAddRatio' })))


def DoCallBackAction1(oEventCB, oWarrior):
    cl_evact.EventCBClearWeaponPFAttrChange(oWarrior, oEventCB, 'MaxPFBullet')
    cl_evact.EventCBClearWeaponPFAttrChange(oWarrior, oEventCB, 'PFBulletUse')


class CPerform(CCustomPerform):
    m_SID = 51720
    m_Name = '武器资源上限'
    m_MaxLevel = 3
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1,
        2: Action2,
        3: Action3 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_BaseLevelArgData = {
        1: {
            'PerAddRatio': 200 },
        2: {
            'PerAddRatio': 400 },
        3: {
            'PerAddRatio': 800 } }

