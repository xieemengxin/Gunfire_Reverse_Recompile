# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/rewardpf/p15158.pyc
# RelativePath: clientlogic/cl_platformdata/pc/rewardpf/p15158.pyc
# Source Generated with Decompyle++
# File: p15158.pyc (Python 3.6)

from cl_platformdata.custom.seasonsuit.customaction import CustomAction15122 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CPerform as CCustomPerform
from cl_commondefines import PF_SUBMSG_THROW
from cl_newformula import Func602, Func651

def Action1(oWarrior, oLifeCycle):
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 215):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 21, 0, 0)
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8007)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 217):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 22, 0, 0)
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8009)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 212):
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_TRIGGERCARTOON, -1, 23, 0, 0)
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8013)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 206):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8012)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 207):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1413)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 213):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 8014)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 216):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 12008)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 214):
        cl_action.CommonAddPerform(oWarrior, oLifeCycle, 1430)
    if cl_condition.CheckHero(oWarrior, oLifeCycle, 219) or cl_condition.CheckHero(oWarrior, oLifeCycle, 201) or cl_condition.CheckHero(oWarrior, oLifeCycle, 221) or cl_condition.CheckHero(oWarrior, oLifeCycle, 218) or cl_condition.CheckHero(oWarrior, oLifeCycle, 205):
        cl_action.PassiveEnableBulletChangeRule(oWarrior, oLifeCycle, 11134, 1)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_THROW, 1, 0, 0)


def DoCallBackAction1(oEventCB, oWarrior):
    if cl_evcon.CheckFromThrowPerform(oWarrior, oEventCB, None):
        if cl_condition.CalFormula(oWarrior, oEventCB.GetCBLifeCycle(), (lambda *a: Func602(*a))) >= 20:
            if cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 50):
                cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'P15122', 1, 0)
                if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 206) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 213) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 216):
                    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33429, 0, {
                        'Count': 1 }, 1, 0, 0)
                elif cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 214) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 207):
                    cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33427, 0, {
                        'Count': 1 }, 1, 0, 0)
                elif cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 205) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 201) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 219) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 218):
                    cl_evact.EventCBSetEventPerformAttr(oWarrior, oEventCB, 'TriggerTimes', 0, 1)
        elif cl_evcon.CheckRandom(oWarrior, oEventCB, 100, 20):
            cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'P15122', 1, 0)
            if cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 206) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 213) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 216):
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33429, 0, {
                    'Count': 1 }, 1, 0, 0)
            elif cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 214) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 207):
                cl_evact.PassiveCBAddState(oWarrior, oEventCB, 33427, 0, {
                    'Count': 1 }, 1, 0, 0)
            elif cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 205) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 201) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 219) or cl_condition.CheckHero(oWarrior, oEventCB.GetCBLifeCycle(), 218):
                cl_evact.EventCBSetEventPerformAttr(oWarrior, oEventCB, 'TriggerTimes', 0, 1)


def DoCallBackAction21(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'P15122', 0):
        CustomAction(oWarrior, oEventCB, {
            'Perform': 8007,
            'Count': 1,
            'StateSID': 33428 })


def DoCallBackAction22(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'P15122', 0) and cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func651(*a, **{
'sKey': 'RayActive' }))) == 0:
        CustomAction(oWarrior, oEventCB, {
            'Perform': 8009,
            'Count': 1,
            'StateSID': 33428 })


def DoCallBackAction23(oEventCB, oWarrior):
    if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'P15122', 0):
        CustomAction(oWarrior, oEventCB, {
            'Perform': 8013,
            'Count': 1,
            'StateSID': 33428 })


class CPerform(CCustomPerform):
    m_SID = 15158
    m_Name = '#NT#双生法术套装'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        1: DoCallBackAction1,
        21: DoCallBackAction21,
        22: DoCallBackAction22,
        23: DoCallBackAction23 }
    m_BaseArgData = { }
    m_DieDisable = 0

