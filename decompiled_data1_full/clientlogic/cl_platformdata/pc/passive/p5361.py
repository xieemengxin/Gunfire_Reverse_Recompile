# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5361.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5361.pyc
# Source Generated with Decompyle++
# File: p5361.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_PERFORM
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonChangeBaseDamRatio(oWarrior, oLifeCycle, 0, (lambda *a: Func717(*a, **{
'sArg': 'SkillDamMul' }) * 100), DAM_TYPE_PERFORM, 1)


class CPerform(CCustomPerform):
    m_SID = 5361
    m_Name = '#NT#小玖改装4'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'SkillDamMul': 75 }
    m_DieDisable = 0

