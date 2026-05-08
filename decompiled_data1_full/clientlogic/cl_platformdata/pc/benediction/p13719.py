# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/benediction/p13719.pyc
# RelativePath: clientlogic/cl_platformdata/pc/benediction/p13719.pyc
# Source Generated with Decompyle++
# File: p13719.pyc (Python 3.6)

from cl_commondefines import LAYER_CHOOSE_EVENTNPC
from cl_only import Functor
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.benediction import CBenediction as CCustomPerform
from cl_commondefines import LAYER_CHOOSE_EVENTNPC

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)
    cl_action.CommonAddBossLevelCnt(oWarrior, oLifeCycle, LAYER_CHOOSE_EVENTNPC, 1)
    if cl_condition.CheckIsAIHero(oWarrior, oLifeCycle):
        cl_action.CommonListenGlobalMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1, 2)
    else:
        cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PLAYERMAPLOADOK, -1, 0, 1, 0)


def DisableAction1(oWarrior, oLifeCycle):
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 1, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 114, 2, None, None)


def DoCallBackAction1(oEventCB, oWarrior):
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 115, 0, None, None)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_action.CommonDoneGlobalMsg(oWarrior, oEventCB.GetCBLifeCycle(), cl_msgcenter.MSG_WARMGR_STARTFIGHT, -1)
    cl_action.CommonTriggerClientBehavior(oWarrior, oEventCB.GetCBLifeCycle(), 114, 0, None, 0)


class CPerform(CCustomPerform):
    m_SID = 13719
    m_Name = '全知之眼'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = {
        1: DisableAction1 }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        1: DoCallBackAction1,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_Career = None

