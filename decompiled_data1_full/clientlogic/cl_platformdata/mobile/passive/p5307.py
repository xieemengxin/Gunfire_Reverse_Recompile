# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/passive/p5307.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/passive/p5307.pyc
# Source Generated with Decompyle++
# File: p5307.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonAddSourceWeaponPerform(oWarrior, oLifeCycle, 1939)
    cl_action.CommonSetSourceWeaponPerformAttr(oWarrior, oLifeCycle, 9418, 'HitStaticCount', (lambda *a: Func717(*a, **{
'sArg': 'HitStaticCount' })))
    cl_action.CommonSetSourceWeaponPerformAttr(oWarrior, oLifeCycle, 9418, 'HitCount', (lambda *a: Func717(*a, **{
'sArg': 'HitCount' })))


class CPerform(CCustomPerform):
    m_SID = 5307
    m_Name = '#NT#水枪泡泡'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'HitCount': 3,
        'HitStaticCount': 1 }
    m_DieDisable = 0

