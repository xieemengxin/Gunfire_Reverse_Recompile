# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/passive/p4087.pyc
# RelativePath: clientlogic/cl_platformdata/pc/passive/p4087.pyc
# Source Generated with Decompyle++
# File: p4087.pyc (Python 3.6)

from cl_only import Functor
from cl_commondefines import WARRIOR_BOSSDM, DAM_TYPE_TRUE, DAM_USE_HP
import cl_msgcenter
import cl_math
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.passive import CPerform as CCustomPerform

def Action1(oWarrior, oLifeCycle):
    oLifeCycle.m_Owner.CustomAction(oWarrior, oLifeCycle, {
        'PosList': ((-21, 6.91, 9.09), (-14.46, 5.4, 9.09), (-9.96, 5.4, 9.09), (-3.33, 4.2, 9.09), (5.12, 4.2, 9.09), (11.82, 5.4, 9.09), (16.33, 5.4, 9.09), (22.6, 6.91, 9.09)),
        'MonsterSID': 39052,
        'CannonCheck': (50, 30),
        'BossCheck': (100, 165) })


class CPerform(CCustomPerform):
    m_SID = 4087
    m_Name = '三幕Boss生命连结'
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
    
    def CustomAction(self, oWarrior, oLifeCycle, dInfo):
        if oWarrior.m_FightType != WARRIOR_BOSSDM:
            return None
        cl_msgcenter.AddFunction(oWarrior, cl_msgcenter.MSG_WAR_ENTERSCENE, Functor(OnEnterScene, oLifeCycle.GetObject().m_SID, dInfo), oLifeCycle.Key(), -1, 1)



def OnEnterScene(iPerform, dActionInfo, oWarrior, dInfo):
    pfobj = oWarrior.GetPerform(iPerform)
    if not pfobj:
        return None
    oGame = oWarrior.m_Game
    iScene = oWarrior.m_Scene
    iMonsterSID = dActionInfo['MonsterSID']
    vFace = oWarrior.GetFacing()
    sKey = pfobj.Key()
    vOriPos = oWarrior.GetPos()
    iAngle = cl_math.CalAngle3D(vFace, (0, 0, 1))
    if vFace[0] < 0:
        iAngle = -iAngle
    lstMonster = []
    dMonsterHP = { }
    if 'BossCheck' in dActionInfo:
        oWarrior.SetSkillCheckArgs(*dActionInfo['BossCheck'])
    for vOffset in dActionInfo['PosList']:
        vOffset = cl_math.RotateAroundVector(vOffset, (0, 1, 0), iAngle)
        vPos = cl_math.Vec3Add(vOriPos, vOffset)
        oMonster = oGame.m_ResMgr.CreateMonster(iScene, iMonsterSID, vPos, vFace, oWarrior.m_Side, oWarrior.m_Grade, dExtInfo = {
            'Owner': oWarrior.m_ID })
        if not oMonster:
            continue
        if 'CannonCheck' in dActionInfo:
            oMonster.SetSkillCheckArgs(*dActionInfo['CannonCheck'])
        iMonster = oMonster.m_ID
        dMonsterHP[iMonster] = oMonster.HP()
        cl_msgcenter.AddAttentionFunc(oWarrior, iMonster, cl_msgcenter.MSG_WAR_HP_CHANGE, OnMonsterHPChange, sKey)
        cl_msgcenter.AddAttentionFunc(oWarrior, iMonster, cl_msgcenter.MSG_WAR_DIE, OnMonsterDie, sKey)
        cl_msgcenter.AddAttentionFunc(oWarrior, iMonster, cl_msgcenter.MSG_WAR_RELIFE, OnMonsterRelife, sKey)
        cl_msgcenter.AddAttentionFunc(oMonster, oWarrior.m_ID, cl_msgcenter.MSG_WAR_DIE, OnWarriorDie, sKey)
        lstMonster.append(iMonster)
    
    oWarrior.Set('CannonList', lstMonster)
    oWarrior.Set('CannonHP', dMonsterHP)


def OnMonsterDie(oListener, oSender, dInfo):
    lstMonster = oListener.Query('CannonList', [])
    iSender = oSender.m_ID
    if iSender in lstMonster:
        lstMonster.remove(iSender)
    oListener.Set('CannonList', lstMonster)
    if len(lstMonster) == 4:
        oListener.SetPhase(2)
    elif len(lstMonster) == 0:
        oListener.SetPhase(4)


def OnMonsterHPChange(oListener, oSender, dInfo):
    iAttack = dInfo['AID']
    iFactor = -1 if dInfo['IsDam'] else 1
    for iTrueChange, oReason in dInfo['TrueChange']:
        oListener.HPDirectModify('HP', iAttack, iFactor * iTrueChange, oReason)
    


def OnWarriorDie(oListener, oSender, dInfo):
    oListener.HPDirectModify('HP', dInfo['AID'], -oListener.HP(), dInfo['RS'])


def OnMonsterRelife(oListener, oSender, dInfo):
    oReason = dInfo['RS'].ExtInfo({
        'ShowTips': 0,
        'DamType': DAM_TYPE_TRUE | DAM_USE_HP })
    iAttack = oSender.m_ID
    dMonsterHP = oListener.Query('CannonHP')
    iHP = dMonsterHP[iAttack]
    oListener.HPModifyCure(iAttack, [
        (iHP, oReason)])
    dMonsterHP[iAttack] = oSender.HP()

