# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/commonative/p1904.pyc
# RelativePath: clientlogic/cl_platformdata/pc/commonative/p1904.pyc
# Source Generated with Decompyle++
# File: p1904.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_object.reason
from cl_only import SendAlert, PY_FLAG_DEAD, Functor, PY_FLAG_DEAD
from cl_commondefines import WARRIOR_ELITE, WARRIOR_ELISNIPE, DAM_TYPE_PERFORM, DAM_TYPE_TRUE, DAM_USE_HP
from cl_object.logging import SkillLog
from cl_perform.cartoon.defines import CurveCartoon
from cl_commondefines import CRT_CHECK_SERVER, OBJ_FRIEND_NOSELF

class CCartoon1(CurveCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.CustomPerformAction(skill, 1904, 'CreateMonster', {
            'SnipeSID': 3165,
            'SnipePerform': 31641,
            'CountState': 1773,
            'TriggerCnt': 20 })

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, cl_action.SkillStartPos(skill), cl_action.CrtArgCustomPos(skill, cartoon), 1, 50, 10, 330, 0.7, targettype = OBJ_FRIEND_NOSELF, pierceblock = False, effect = 0, liveTime = 0, trailEffect = None, effectLiveTime = 1, hittarger = True, iVictim = 0)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.commonative import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL

class CPerform(CCustomPerform):
    m_SID = 1904
    m_Name = '召唤怪物特效表现'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_NORMAL
    m_BaseAttrData = {
        'ColdTime': 0,
        'AttDistance': 0,
        'ChargeTime': 0 }
    m_ClientNeed = 0
    m_UseCurWeapon = 0
    m_ForbidRule = 0
    
    def SendUseMsg(self, oWarrior, oSkill):
        pass



def CreateMonster(oSkill, *args):
    oGame = oSkill.m_Game
    oMonster = oGame.GetObject(oSkill.m_Base['AID'], PY_FLAG_DEAD)
    oElement = oGame.m_WarMgr.GetComponent('MonsterRelicElement')
    dInfo = oSkill.m_Custom['Info']
    iRelic = dInfo['Relic']
    dArgs = args[0]
    if not oMonster:
        oElement.AddRelicRoomSummonCnt(iRelic, oSkill.m_Base['AID'], -1)
        oElement.CreateRelicSummonFromQueue(iRelic, 1)
        return None
    sKey = 'PF1904'
    if oMonster.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE and not oMonster.Query('Demon'):
        iSummonSID = oMonster.m_NormalMonster
        if not iSummonSID:
            SendAlert('err', '秘密魔匣召唤失败，请检查 %d 是否有配置对应普通怪' % oMonster.m_SID)
            return None
        if oMonster.m_FightType & WARRIOR_ELISNIPE == WARRIOR_ELISNIPE:
            cl_msgcenter.AddFunction(oMonster, cl_msgcenter.MSG_WAR_PERFORM_START, Functor(OnSnipeEliteUsePerform, dArgs['SnipePerform'], iRelic), sKey, iOnce = 0)
        elif oMonster.m_DataSID == dArgs['SnipeSID']:
            iSummonSID = oMonster.m_NormalMonster
            if not iSummonSID:
                SendAlert('err', '秘密魔匣召唤失败，请检查 %d 是否有配置对应普通怪' % oMonster.m_SID)
                return None
            oSnipeElite = oGame.GetObject(oMonster.m_Owner)
            if oSnipeElite:
                cl_msgcenter.AddFunction(oSnipeElite, cl_msgcenter.MSG_WAR_PERFORM_START, Functor(OnSnipeEliteUsePerform, dArgs['SnipePerform'], iRelic), sKey, iOnce = 0)
            else:
                iSummonSID = oMonster.m_SID
    vPos = None.m_Custom['vEnd']
    oElement.TrueCreateRelicSummon(oMonster, iSummonSID, vPos, dInfo)
    if not oMonster.m_State:
        SkillLog.Alert('PF1904 CreateSummon not oMonster.m_State %d %d %d %s' % (oMonster.m_SID, oMonster.m_Dead, oMonster.m_ReleaseFlag, oMonster.m_LineIdx))
        return None
    oState = oMonster.m_State.GetItemBySID(dArgs['CountState'])
    if oState:
        oState.AddCount(oMonster, -dArgs['TriggerCnt'])


def OnSnipeEliteUsePerform(iSnipePerform, iRelic, oSnipeElite, dMsgInfo):
    oSkill = dMsgInfo['Skill']
    iPerform = oSkill.m_Base['pfid']
    if iPerform != iSnipePerform:
        return None
    oGame = oSnipeElite.m_Game
    cl_msgcenter.DoneEvent(oSnipeElite, cl_msgcenter.MSG_WAR_PERFORM_START, 'PF1904')
    oElement = oGame.m_WarMgr.GetComponent('MonsterRelicElement')
    iSnipeElite = oSnipeElite.m_ID
    iSummonCnt = len(oElement.GetMonsterSummon(iRelic, iSnipeElite))
    oElement.AddRelicRoomSummonCnt(iRelic, iSnipeElite, -iSummonCnt)
    oElement.ClearMonsterSummon(iRelic, iSnipeElite)
    oReason = cl_object.reason.CStrReason('FollowDie', None, {
        'DamType': DAM_TYPE_PERFORM | DAM_TYPE_TRUE | DAM_USE_HP })
    for iFollow in oSnipeElite.m_FollowDieObjs:
        lstFollowSummon = oElement.GetMonsterSummon(iRelic, iFollow)
        for iFollowSummon in lstFollowSummon:
            oFollowSummon = oGame.GetObject(iFollowSummon, PY_FLAG_DEAD)
            if not oFollowSummon:
                continue
            oFollowSummon.HPDirectModify('HP', oFollowSummon.m_Owner, -oFollowSummon.HP(), oReason)
        
    

