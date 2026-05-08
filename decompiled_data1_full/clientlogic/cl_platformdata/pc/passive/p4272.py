# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4272.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4272.pyc
# Source Generated with Decompyle++
# File: p4272.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MODEL_TYPE_BOX, PAMOD_TYPE_DYNA
from cl_pxlayer import PXLAYER_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 1009, 1455, { }, 1)
    cl_action.CommonListenWarMgrMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WARMGR_CG_END, -1, 0)
    cl_action.CommonSetHeightOffset(oWarrior, oLifeCycle, -2)
    cl_action.CommonAddSelfPhyModel(oWarrior, oLifeCycle, MODEL_TYPE_BOX, PAMOD_TYPE_DYNA, PXLAYER_MONSTER, {
        'HalfExtX': 0.5,
        'HalfExtY': 0.5,
        'HalfExtZ': 0.5,
        'CenterX': 0,
        'CenterY': -2,
        'CenterZ': 14 })
    cl_action.CommonAddSelfPhyModel(oWarrior, oLifeCycle, MODEL_TYPE_BOX, PAMOD_TYPE_DYNA, PXLAYER_MONSTER, {
        'HalfExtX': 6,
        'HalfExtY': 0.5,
        'HalfExtZ': 0.5,
        'CenterX': 0,
        'CenterY': -2,
        'CenterZ': 10 })
    cl_action.CommonSetExtraModelDistance(oWarrior, oLifeCycle, 13)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.EventCBCheekFormPointBehavior(oWarrior, oEventCB, 59):
        cl_action.CommonRemoveOwnerState(oWarrior, oEventCB.GetCBLifeCycle(), 1009, 0)


class CPerform(CCustomPerform):
    m_SID = 4272
    m_Name = '夜姬丸小炮开场动画与额外模型'
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

