# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p5341.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p5341.pyc
# Source Generated with Decompyle++
# File: p5341.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform
from cl_newformula import Func304, Func717

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonSetShape(oWarrior, oLifeCycle, 1105, 0)
    cl_action.CommonSetPlantCanTransferState(oWarrior, oLifeCycle, {
        33733: 1 })
    cl_action.PassiveAddState(oWarrior, oLifeCycle, 33668, 0, {
        'DotDam': (lambda *a: Func717(*a, **{
'sArg': 'DotDam' })) }, 1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'Grade' }))) == 1:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33710, 0, {
            'AttSpeed': 5000,
            'AttParasiticCnt': 1,
            'AttCnt': 3 }, 1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'Grade' }))) == 2:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33710, 0, {
            'AttSpeed': 5000,
            'AttParasiticCnt': 1,
            'AttCnt': 4 }, 1)
    if cl_condition.CalFormula(oWarrior, oLifeCycle, (lambda *a: Func304(*a, **{
'sAttr': 'Grade' }))) == 3:
        cl_action.PassiveAddState(oWarrior, oLifeCycle, 33710, 0, {
            'AttSpeed': 5000,
            'AttParasiticCnt': 2,
            'AttCnt': 3 }, 1)


class CPerform(CCustomPerform):
    m_SID = 5341
    m_Name = '园丁狂暴植物被动'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = { }
    m_BaseArgData = {
        'DotDam': 1000 }
    m_DieDisable = 0

