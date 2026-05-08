# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/herogradepf/p6031.pyc
# RelativePath: clientlogic/cl_platformdata/pc/herogradepf/p6031.pyc
# Source Generated with Decompyle++
# File: p6031.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from . import CHeroGradePassive as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    if not cl_condition.CheckHasSavedData(oWarrior, oLifeCycle, 'p6031_rw'):
        cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 0, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    cl_action.CommonSetSavedData(oWarrior, oEventCB.GetCBLifeCycle(), 'p6031_rw', 1)
    cl_evact.PassiveCBGetRandomWeapon(oWarrior, oEventCB, {
        0: '1501|2|3|4801|4804',
        1: '1501|2|3|4806|4815',
        2: '1503|2|3|4816|4824',
        3: '1502|2|3|4803|4825',
        4: '1507|2|3|4869|4849',
        5: '1503|2|3|4861|4876',
        6: '1503|2|3|4932',
        7: '1505|2|3|4935',
        8: '1507|2|3|4946',
        9: '1501|2|3|4930',
        10: '1510|2|3|4849|4803',
        11: '1508|2|3|4889',
        12: '1508|2|3|4820|4866',
        13: '1513|2|3|4801|4853',
        14: '1513|2|3|13045',
        15: '1215|2|3|4961',
        16: '1215|2|3|4962',
        17: '1516|2|3|13110',
        18: '1516|2|3|13111',
        19: '1516|2|3|13116',
        20: '1507|2|3|4945' }, {
        0: 10,
        1: 10,
        2: 10,
        3: 10,
        4: 10,
        5: 10,
        6: 10,
        7: 10,
        8: 10,
        9: 10,
        10: 10,
        11: 10,
        12: 10,
        13: 10,
        14: 10,
        15: 10,
        16: 10,
        17: 10,
        18: 10,
        19: 10,
        20: 10 })


class CPerform(CCustomPerform):
    m_SID = 6031
    m_Name = '游侠【武器】1'
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

