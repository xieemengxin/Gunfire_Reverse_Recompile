# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/inscription/p13055.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/inscription/p13055.pyc
# Source Generated with Decompyle++
# File: p13055.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import INSCRIPTION_TYPE_GEMINI, ITEMPERFORM_ENABLE_HOLD, OBJ_SELF, PF_SUBMSG_FILLBULLET
from cl_newformula import Func510, Func555

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_PERFORM_START, PF_SUBMSG_FILLBULLET, 0, 0, 0)
    cl_action.CommonListenMsgCallBack(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_CHANGE_WEAPON, -1, 2, 0, 0)
    cl_action.CommonDirectEventCBFunc(oWarrior, oLifeCycle, 2, None, None)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.PassiveCheckFromSameItem(oWarrior, oEventCB):
        cl_evact.EventGetTargetByType(oWarrior, oEventCB, OBJ_SELF)
        if cl_evcon.PassiveCBCheckTargetHasState(oWarrior, oEventCB, 1751, 0, 0, None):
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1751, 1, 0, 0, None)
            cl_evact.PassiveAddStateTime(oWarrior, oEventCB, 1751, 500, 500)
        else:
            cl_evact.PassiveAddTargetState(oWarrior, oEventCB, 1751, 500, { }, 0, 0, None)
            cl_evact.EventCBAddTargetStateCount(oWarrior, oEventCB, 1751, 1, 0, 0, None)


def DoCallBackAction2(oEventCB, oWarrior):
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func555(*a, **{
'sAttr': 'Att' }) * Func555(*a, **{
'sAttr': 'Trajectory' }))) >= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func510(*a, **{
'sAttr': 'Att' }) * Func510(*a, **{
'sAttr': 'Trajectory' }))):
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'FillTime', 0, -5000)
    if cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func555(*a, **{
'sAttr': 'Att' }) * Func555(*a, **{
'sAttr': 'Trajectory' }))) <= cl_evcon.GetFormula(oWarrior, oEventCB, (lambda *a: Func510(*a, **{
'sAttr': 'Att' }) * Func510(*a, **{
'sAttr': 'Trajectory' }))):
        cl_action.PassiveChangeSourceWeaponAttr(oWarrior, oEventCB.GetCBLifeCycle(), 'LuckyHit', 70, 0)


class CPerform(CCustomPerform):
    m_SID = 13055
    m_Name = '拔枪射击'
    m_MaxLevel = 1
    m_MaxStack = 1
    m_ExtPerform = ()
    m_EnableActionInfo = {
        1: Action1 }
    m_DisableActionInfo = { }
    m_ColdDownCBActionInfo = { }
    m_CBFuncAction = {
        0: DoCallBackAction0,
        2: DoCallBackAction2 }
    m_BaseArgData = { }
    m_DieDisable = 0
    m_ItemAttr = {
        'MaxBullet': (0, 0, 1) }
    m_InscriptionType = INSCRIPTION_TYPE_GEMINI
    m_ElementType = None
    m_LimitList = ((), (), ())
    m_ExcludeList = ((6, 12, 15, 16, 20, 23), (), (1415, 1416))
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

