# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/monsterpf/p39026.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/monsterpf/p39026.pyc
# Source Generated with Decompyle++
# File: p39026.pyc (Python 3.6)

from cl_only import SendAlert
import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
from cl_perform.cartoon.defines import TimerCartoon
from cl_commondefines import CRT_CHECK_SERVER

class CCartoon2(TimerCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

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
            cls.EnableCtrl(skill, 100, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon2.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

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
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(TimerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

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
            cls.EnableCtrl(skill, 50, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(TimerCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cartoon = { }
        CCartoon4.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 430 if cl_action.GetMonsterPhase(skill) >= 3 else 470 if cl_action.GetMonsterPhase(skill) >= 2 else 570, 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon1.Init(skill, cartoon, casting = 1, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cartoon = { }
        CCartoon11.Init(skill, cartoon, casting = 1, index = 0)

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.CustomPerformAction(skill, 39026, 'BalanceChoosePos', [
            3 if cl_action.GetSkillVarCache(skill, 'RemainCnt') >= 3 else cl_action.GetSkillVarCache(skill, 'RemainCnt')])
        cl_action.AttackerUsePerform(skill, 39029, {
            'LaunchCnt': 3 if cl_action.GetSkillVarCache(skill, 'RemainCnt') >= 3 else cl_action.GetSkillVarCache(skill, 'RemainCnt'),
            'LaunchStartPosList': cl_action.GetSkillServerCache(skill, 'LaunchStartPosList') }, 0, 0)
        cl_action.SetSkillVarCache(skill, 'RemainCnt', cl_action.ToInt(skill, cl_action.GetSkillVarCache(skill, 'RemainCnt') - (3 if cl_action.GetSkillVarCache(skill, 'RemainCnt') >= 3 else cl_action.GetSkillVarCache(skill, 'RemainCnt'))))

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 15, cl_action.FloatToIntFloor(skill, (cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = False) * 2 + 2) // 3))

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(TimerCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        cl_action.SetSkillVarCache(skill, 'RemainCnt', cl_action.ToInt(skill, cl_action.GetAllHeroCnt(skill, False, bUseRidingAloneCnt = False) * 2))
        cartoon = { }
        CCartoon0.Init(skill, cartoon, casting = 1, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableCtrl(skill, 10, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'LeftPosList', cl_action.GetListByShuffleAndNumber(skill, [
        (-29, 42, -11),
        (-29, 53, -11),
        (-29, 31, -11),
        (-18, 42, -11),
        (-40, 42, -11)], 0))
    cl_action.SetSkillServerCache(skill, 'RightPosList', cl_action.GetListByShuffleAndNumber(skill, [
        (29, 42, -11),
        (29, 53, -11),
        (29, 31, -11),
        (18, 42, -11),
        (40, 42, -11)], 0))
    cartoon = { }
    CCartoon3.Init(skill, cartoon, casting = 1, index = 0)


def Halt(skill):
    pass


def End(skill):
    pass


def GetSkillCacheIndex():
    return []


def GetOtherMonster():
    return []

from cl_perform.monsterpf import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_NORMAL, MONSTERPF_TYPE_OTHER, NONE_DISTANCE

class CPerform(CCustomPerform):
    m_SID = 39026
    m_Name = '罗睺远程光波'
    m_ExtPerform = ()
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_BaseAttrData = {
        'ColdTime': 600,
        'AttDistance': 99,
        'ChargeTime': 0,
        'DebuffProb': 2000,
        'MaxCover': 1 }
    m_ElementType = DAM_TYPE_NORMAL
    m_SkillShotType = NONE_DISTANCE
    m_AttackType = MONSTERPF_TYPE_OTHER
    m_ForbidRule = 0
    m_Resend = 1
    m_CacheAttr = [
        'DebuffProb']


def BalanceChoosePos(oSkill, *args):
    iSum = args[0][0]
    lstPos = []
    lstLeftPos = oSkill.m_Collect['LeftPosList']
    lstRightPos = oSkill.m_Collect['RightPosList']
    iNum = iSum // 2
    oGame = oSkill.m_Game
    if len(lstLeftPos) < iNum or len(lstRightPos) < iNum:
        SendAlert('err', '39026可抽取发射点不够，请检查 %d %d %d' % (len(lstLeftPos), len(lstRightPos), iNum))
        iFlag = 1
        for _ in range(iSum):
            lstPos.append((29 * iFlag, 42, -11))
            iFlag = -iFlag
        
        oSkill.m_Collect['LaunchStartPosList'] = lstPos
        return None
    for _ in range(iNum):
        vPos1 = lstLeftPos.pop()
        vPos2 = lstRightPos.pop()
        lstPos.append(vPos1)
        lstPos.append(vPos2)
    
    if iSum % 2 == 1:
        if 'RandomChoose' not in oSkill.m_Collect:
            iChoose = oGame.Random(2)
        else:
            iChoose = oSkill.m_Collect['RandomChoose']
        if iChoose:
            lstTargetPos = lstLeftPos
            iChoose = 0
        else:
            lstTargetPos = lstRightPos
            iChoose = 1
        oSkill.m_Collect['RandomChoose'] = iChoose
        if len(lstTargetPos) < 1:
            SendAlert('err', '39026可抽取发射点不够，请检查 %d %d %d' % (len(lstLeftPos), len(lstRightPos), iSum))
            vPos = (29, 42, -11)
        else:
            vPos = lstTargetPos.pop()
        lstPos.append(vPos)
    oSkill.m_Collect['LaunchStartPosList'] = lstPos

