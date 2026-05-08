# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/relictalent/p50014.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/relictalent/p50014.pyc
# Source Generated with Decompyle++
# File: p50014.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.relictalent import CRelicTalent as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, DAM_TYPE_CORRISION, DAM_TYPE_FIRE, DAM_TYPE_THUNDER, OBJ_VICTIM, PF_SUBMSG_COMMON, PF_TYPE_CONSHOOT, USEPERFORM_POSTYPE_DEFAULT
from cl_newformula import Func336, Func361, Func600, Func604

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1908)
    cl_action.CommonSetPerformArgs(oWarrior, oLifeCycle, 50014, 'AttRange', cl_action.CommonGetPerformAttr(oWarrior, oLifeCycle, 1908, 'AttDistance'), None)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 32988, 0, { }, 1)
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33030, 0, { }, 1)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_MAGICPOWERCHANGE, -1, 1, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 3, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CAUSEDEBUFF, -1, 6, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_COMMON, 2, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1908, 'Att', (lambda *a: Func600(*a) * 2000 + 60000), None)
    cl_action.CommonSetPerformArgs(oWarrior, oEventCB.GetCBLifeCycle(), 1908, 'DebuffProb', (lambda *a: Func600(*a) * 300 + 3000), None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.CheckFromPointPerform(oWarrior, oEventCB, 1908, 1, 0):
        cl_evact.EventCBSetPerformAttr(oWarrior, oEventCB, 'AttDistance', (lambda *a: Func604(*a, **{
'sKey': 'pf50010Extra' }) * 2))
        cl_evact.EventSetSkillCache(oWarrior, oEventCB, 'AttDistance', (lambda *a: Func604(*a, **{
'sKey': 'pf50010Extra' }) * 2 + Func361(*a, **{
'sid': 50014,
'sArgs': 'AttRange' })))


def DoCallBackAction3(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32988):
        if cl_evcon.CheckFromWeapon(oWarrior, oEventCB, 0) or cl_evcon.CheckInPointPerform(oWarrior, oEventCB, {
            12013: 1,
            1709: 1,
            1315: 1,
            1319: 1 }, 1, 0):
            if cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CONSHOOT, None):
                cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32988, 0)
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32987, (lambda *a: Func361(*a, **{
'sid': 50014,
'sArgs': 'CDTime' })), { }, 1, -1, None)
                cl_evact.PassiveCBUsePerformAtMsgSkillPos(oWarrior, oEventCB, 1908, {
                    'TargetID': cl_evact.EventGetTargeIDtByType(oWarrior, oEventCB, OBJ_VICTIM),
                    'Element': cl_action.CommonGetRandomCustomValue(oWarrior, oEventCB.GetCBLifeCycle(), {
                        DAM_TYPE_THUNDER: 1,
                        DAM_TYPE_FIRE: 1,
                        DAM_TYPE_CORRISION: 1 }) }, USEPERFORM_POSTYPE_DEFAULT)
            elif cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func336(*a, **{
'sKey': 'pf50014Usead' }))) == 0:
                cl_evact.EventCBAddCollectInfo(oWarrior, oEventCB, 'pf50014Usead', 1, 0)
                cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 32988, 0)
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 32987, (lambda *a: Func361(*a, **{
'sid': 50014,
'sArgs': 'CDTime' })), { }, 1, -1, None)
                cl_evact.PassiveCBUsePerformAtMsgSkillPos(oWarrior, oEventCB, 1908, {
                    'TargetID': cl_evact.EventGetTargeIDtByType(oWarrior, oEventCB, OBJ_VICTIM),
                    'Element': cl_action.CommonGetRandomCustomValue(oWarrior, oEventCB.GetCBLifeCycle(), {
                        DAM_TYPE_THUNDER: 1,
                        DAM_TYPE_FIRE: 1,
                        DAM_TYPE_CORRISION: 1 }) }, USEPERFORM_POSTYPE_DEFAULT)


def DoCallBackAction6(oEventCB, oWarrior):
    if cl_evcon.CheckHasState(oWarrior, oEventCB, 32987) and cl_evcon.CheckHasState(oWarrior, oEventCB, 33030):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 33030, 0)
        cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 32987, -cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CDReduce'), cl_evcon.PassiveCBGetPFArgs(oWarrior, oEventCB, 'CDTime'))


class CPerform(CCustomPerform):
    m_SID = 50014
    m_Name = '元素之环'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        2: DoCallBackAction2,
        3: DoCallBackAction3,
        6: DoCallBackAction6 }
    m_BaseArgData = {
        'CDTime': 1000,
        'CDReduce': 20 }
    m_DieDisable = 0
    m_GrowPF = [
        50008,
        50009,
        50010,
        50011,
        50012,
        50013]
    m_DamagePF = [
        1908,
        12020,
        12021,
        12022]

