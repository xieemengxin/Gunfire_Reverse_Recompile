# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4268.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4268.pyc
# Source Generated with Decompyle++
# File: p4268.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MODEL_TYPE_BOX, PAMOD_TYPE_DYNA
from cl_pxlayer import PXLAYER_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 8031, 1260, { }, 1)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_CG_END, -1, 0)
    cl_action.CommonAddSelfPhyModel(oWarrior, oLifeCycle, MODEL_TYPE_BOX, PAMOD_TYPE_DYNA, PXLAYER_MONSTER, {
        'HalfExtX': 0.5,
        'HalfExtY': 0.5,
        'HalfExtZ': 0.5,
        'CenterX': 0,
        'CenterY': 0,
        'CenterZ': 0 })


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheekFormPointBehavior(oWarrior, oEventCB, 80):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 8031, 0)


class CPerform(CCustomPerform):
    m_SID = 4268
    m_Name = '风神boss开场动画与额外模型'
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

