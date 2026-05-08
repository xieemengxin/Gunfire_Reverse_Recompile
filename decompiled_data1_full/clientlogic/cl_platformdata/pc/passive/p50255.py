# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p50255.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p50255.pyc
# Source Generated with Decompyle++
# File: p50255.pyc (Python 3.6)

from cl_platformdata.custom.passive.customaction import CustomAction50255 as CustomAction
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import FIGHT_KEY_WUDI

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetBarrierDeviceInitArgs(oWarrior, oLifeCycle, {
        'AttBuff': 20,
        'SubSpeed': 6000 })
    cl_action.CommonAddSpecialKey(oWarrior, oLifeCycle, FIGHT_KEY_WUDI, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_RECEIVEDAMED, -1, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })


class CPerform(CCustomPerform):
    m_SID = 50255
    m_Name = '#NT#屏障装置初始化属性'
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

