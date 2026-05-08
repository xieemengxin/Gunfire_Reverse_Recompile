# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4380.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4380.pyc
# Source Generated with Decompyle++
# File: p4380.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_platformdata.custom.passive.customaction import CustomAction4380 as CustomAction
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MODEL_TYPE_BOX, PAMOD_TYPE_DYNA
from cl_pxlayer import PXLAYER_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DIE_EXECUTE_BEFORE, -1, 0, 0, 0)
    cl_action.CommonAddSelfPhyModel(oWarrior, oLifeCycle, MODEL_TYPE_BOX, PAMOD_TYPE_DYNA, PXLAYER_MONSTER, {
        'HalfExtX': 20,
        'HalfExtY': 1.2,
        'HalfExtZ': 3,
        'CenterX': 0,
        'CenterY': 0,
        'CenterZ': 22 })
    cl_action.CommonAddSelfPhyModel(oWarrior, oLifeCycle, MODEL_TYPE_BOX, PAMOD_TYPE_DYNA, PXLAYER_MONSTER, {
        'HalfExtX': 20,
        'HalfExtY': 1.2,
        'HalfExtZ': 3,
        'CenterX': 0,
        'CenterY': 0,
        'CenterZ': -22 })
    cl_action.CommonAddSelfPhyModel(oWarrior, oLifeCycle, MODEL_TYPE_BOX, PAMOD_TYPE_DYNA, PXLAYER_MONSTER, {
        'HalfExtX': 3,
        'HalfExtY': 1.2,
        'HalfExtZ': 20,
        'CenterX': 22,
        'CenterY': 0,
        'CenterZ': 0 })
    cl_action.CommonAddSelfPhyModel(oWarrior, oLifeCycle, MODEL_TYPE_BOX, PAMOD_TYPE_DYNA, PXLAYER_MONSTER, {
        'HalfExtX': 3,
        'HalfExtY': 1.2,
        'HalfExtZ': 20,
        'CenterX': -22,
        'CenterY': 0,
        'CenterZ': 0 })
    cl_action.CommonSetExtraModelDistance(oWarrior, oLifeCycle, 11)


def DoCallBackAction0(oEventCB, oWarrior):
    CustomAction(oWarrior, oEventCB, { })


class CPerform(CCustomPerform):
    m_SID = 4380
    m_Name = '罗睺-常驻弱点随本体死亡与额外模型'
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

