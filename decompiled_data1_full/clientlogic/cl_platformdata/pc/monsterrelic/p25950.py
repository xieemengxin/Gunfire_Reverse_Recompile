# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/monsterrelic/p25950.pyc
# RelativePath: clientlogic/cl_platformdata/pc/monsterrelic/p25950.pyc
# Source Generated with Decompyle++
# File: p25950.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.monsterrelic import CMonsterRelic as CCustomPerform
from cl_commondefines import QUALITY_TYPE_CURSE
from cl_newformula import Func16, Func304

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonHPModify(oWarrior, oLifeCycle, 'HP', (lambda *a: Func304(*a, **{
'sAttr': 'HPMax' }) * Func16(*a, **{
'a': 50,
'b': 90 }) // 100), 0)


class CPerform(CCustomPerform):
    m_SID = 25950
    m_Name = '霉变包子'
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
    m_RelicType = 0
    m_HeroRelic = 5950
    m_Quality = QUALITY_TYPE_CURSE
    m_ExcludeRelic = (25964,)

