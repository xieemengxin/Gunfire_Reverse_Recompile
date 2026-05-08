# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4930.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4930.pyc
# Source Generated with Decompyle++
# File: p4930.pyc (Python 3.6)

import cl_msgcenter
import cl_action
import cl_evact
import cl_evcon
from cl_platformdata.custom.inscription.customaction import CustomAction4930 as CustomAction
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD, PF_TYPE_CAREERPF
from cl_newformula import Func336

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_DEALTOTALDAM, ATTACKERSUBMSG_NORMAL, 2, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if not cl_evcon.CheckPerformType(oWarrior, oEventCB, PF_TYPE_CAREERPF, 1):
        if cl_evcon.CheckDirectDamage(oWarrior, oEventCB) and cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4930', None) >= 1:
            CustomAction(oWarrior, oEventCB, {
                'CtrlSkill': 9501,
                'DamageRatio': 50 })
        if cl_evcon.CheckDirectDamage(oWarrior, oEventCB):
            cl_evact.PassiveCBChangeSkillDamFactor(oWarrior, oEventCB, 0, (lambda *a: 2 ** Func336(*a, **{
'sKey': 'p4930' }) * 10000 + -10000), 0, None, None)
        if cl_evcon.CheckSkillCollectInfo(oWarrior, oEventCB, 'p4930', None) <= 5 and cl_evcon.CheckDirectDamage(oWarrior, oEventCB):
            cl_evact.PassiveCBSetCollectInfo(oWarrior, oEventCB, 'p4930', 1, 0)


def DoCallBackAction2(oEventCB, oWarrior):
    cl_evact.EventSetSkillFirstHitFinalDamageInfo(oWarrior, oEventCB)


class CPerform(CCustomPerform):
    m_SID = 4930
    m_Name = '贯日者'
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
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1501,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD

