# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5321.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5321.pyc
# Source Generated with Decompyle++
# File: p5321.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import MODEL_TYPE_BOX, PAMOD_TYPE_DYNA
from cl_pxlayer import PXLAYER_ENEMY_BUILD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddSelfPhyModel(oWarrior, oLifeCycle, MODEL_TYPE_BOX, PAMOD_TYPE_DYNA, PXLAYER_ENEMY_BUILD, {
        'HalfExtX': 0.65,
        'HalfExtY': 0.65,
        'HalfExtZ': 0.65,
        'CenterX': 0,
        'CenterY': 0.65,
        'CenterZ': 0 })


class CPerform(CCustomPerform):
    m_SID = 5321
    m_Name = '#NT#明雷法师怪障碍被动'
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

