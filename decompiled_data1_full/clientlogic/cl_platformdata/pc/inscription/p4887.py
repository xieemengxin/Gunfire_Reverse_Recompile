# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/inscription/p4887.pyc
# RelativePath: clientlogic/cl_platformdata/pc/inscription/p4887.pyc
# Source Generated with Decompyle++
# File: p4887.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD, Functor
from cl_commondefines import OBJ_ATTACK, OBJ_VICTIM, DAM_TYPE_WEAPON, DAM_USE_ALL
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_object.reason
from cl_perform.inscription import CInscription as CCustomPerform
from cl_commondefines import ATTACKERSUBMSG_NORMAL, INSCRIPTION_TYPE_EXCLUSIVE, ITEMPERFORM_ENABLE_HOLD

def Action1(oWarrior, oLifeCycle):
    cl_action.CommonListenSnapshotMsg(oWarrior, oLifeCycle, cl_msgcenter.MSG_WAR_ATTACK, ATTACKERSUBMSG_NORMAL, 0, 0, 0)


def DoCallBackAction0(oEventCB, oWarrior):
    if cl_evcon.CheckFromMinorPerform(oWarrior, oEventCB) == 0:
        CustomAction(oWarrior, oEventCB, { })


class CPerform(CCustomPerform):
    m_SID = 4887
    m_Name = '爆炸弓箭'
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
    m_ItemAttr = { }
    m_InscriptionType = INSCRIPTION_TYPE_EXCLUSIVE
    m_ElementType = None
    m_LimitList = ((), (1505,), ())
    m_ExcludeList = ((), (), ())
    m_ItemEnableType = ITEMPERFORM_ENABLE_HOLD


def GetKey():
    return 'pf4887'


def CustomAction(oWarrior, oEventCB, dInfo):
    dMsgInfo = oEventCB.GetCBMsgInfo()
    if 'Skill' not in dMsgInfo:
        return None
    oSkill = dMsgInfo['Skill']
    dCache = oSkill.m_Cache
    iBaseDam = dCache['Att']
    iLuckyHit = dCache['LuckyHit']
    if cl_evcon.CheckHitWeakness(oWarrior, oEventCB):
        iBaseDam = iBaseDam * dCache['CrazyEff'] // 10000
    sKey = GetKey()
    damageFunc = Functor(DamageFunc, iBaseDam, iLuckyHit)
    dPFCustom = oSkill.m_Custom.setdefault(sKey, { })
    lstFunc = dPFCustom.setdefault('Func', [])
    lstFunc.append(damageFunc)


def HitStatic(oSkill, *args):
    sKey = GetKey()
    damageFunc = Functor(DamageFunc, oSkill.m_Cache['Att'], oSkill.m_Cache['LuckyHit'])
    dPFCustom = oSkill.m_Custom.setdefault(sKey, { })
    lstFunc = dPFCustom.setdefault('Func', [])
    lstFunc.append(damageFunc)


def CustomDamage(oSkill, *args):
    iRatio = args[0][0]
    sKey = GetKey()
    dPFCustom = oSkill.m_Custom.get(sKey, { })
    if dPFCustom:
        dCartoon = oSkill.GetCurCartoon()
        iCartoon = dCartoon['ID']
        if iCartoon in dPFCustom:
            func = dPFCustom[iCartoon]
        else:
            lstFunc = dPFCustom['Func']
            if not lstFunc:
                return None
            func = lstFunc.pop(0)
            dPFCustom[iCartoon] = func
        func(oSkill, iRatio)


def DamageFunc(iBaseDamage, iLuckyHit, oSkill, iRatio):
    oGame = oSkill.m_Game
    iTarget = oSkill.m_Update['CurVID']
    oTarget = oGame.GetObject(iTarget, PY_FLAG_DEAD)
    if not oTarget:
        return None
    iAttack = oSkill.m_Base['AID']
    iElementType = oSkill.m_Cache['ElementType']
    oReason = cl_object.reason.CStrReason('pf%d' % CPerform.m_SID, None, {
        'DamType': DAM_TYPE_WEAPON | DAM_USE_ALL | iElementType,
        'ActNum': oSkill.m_Base['ActNum'] })
    lstDam = [
        (iBaseDamage * iRatio // 100, oReason)]
    dDamage = {
        'AID': iAttack,
        'CurVID': iTarget,
        'MainDam': lstDam,
        'FlowDam': [],
        'RS': oReason,
        'DamFactor': {
            OBJ_VICTIM: { },
            OBJ_ATTACK: { } },
        'LuckyHitEff': oTarget.CalLuckyHitEff({
            'LuckyHit': iLuckyHit })[0] }
    oTarget.ReceiveDamage(iAttack, dDamage)

