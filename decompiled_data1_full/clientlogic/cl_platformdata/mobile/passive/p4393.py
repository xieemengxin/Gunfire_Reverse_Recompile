# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p4393.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p4393.pyc
# Source Generated with Decompyle++
# File: p4393.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MODEL_TYPE_BOX, PAMOD_TYPE_DYNA
from cl_pxlayer import PXLAYER_MONSTER

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddSelfPhyModel(oWarrior, oLifeCycle, MODEL_TYPE_BOX, PAMOD_TYPE_DYNA, PXLAYER_MONSTER, {
        'HalfExtX': 5,
        'HalfExtY': 0.5,
        'HalfExtZ': 0.5,
        'CenterX': 0,
        'CenterY': 2,
        'CenterZ': 12 })
    cl_action.CommonSetExtraModelDistance(oWarrior, oLifeCycle, 1.5)


class CPerform(CCustomPerform):
    m_SID = 4393
    m_Name = '石巨人boss额外物理模型'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = { }
    m_DieDisable = 0

