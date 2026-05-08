# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/mobject.pyc
# RelativePath: clientlogic/cl_perform/cartoon/mobject.pyc
# Source Generated with Decompyle++
# File: mobject.pyc (Python 3.6)

from cl_only import PY_FLAG_DEAD, SendAlert
from cl_commondefines import CRT_CHECK_CLIENT, CRT_CHECK_SERVER, VICTIM_STATE_HIT, VICTIM_STATE_BLOCK, VICTIM_STATE_IGNOREONCE, VICTIM_STATE_NOEXIST, VICTIM_STATE_INVALID, VICTIM_STATE_VALID, VICTIM_IGNORE_ONCE, WARRIOR_OBSTACLE_NORMAL, MONSTER_PART_SHIELD, WARRIOR_PERFORM, WARRIOR_MONSTER, WARRIOR_DEVICE_BARRIER, WARRIOR_SERVANT, WARRIOR_SUMMON_BARRIER
import cl_notify
import cl_math
import cl_msgcenter
from . import argcheck

def SetCurCartoon(func):
    
    def _SetCurCrt(*args):
        (cls, oSkill, dCartoon) = args
        iNodeID = dCartoon['ID']
        oSkill.SetCurCartoon(iNodeID)
        r = func(*args)
        oSkill.PopCurCartoon(iNodeID)
        return r

    return _SetCurCrt


class CBaseCartoon(object):
    m_SID = 0
    m_PerformSID = 0
    m_NeedCtrlNet = 1
    m_CutClient = 1
    m_WorldLineOutFrame = 0
    m_ContinueShoot = 0
    
    def Init(cls, oSkill, dCartoon, casting, index):
        if not (oSkill.m_Base) or oSkill.m_HaltRS:
            return None
        iCartoonIndex = oSkill.GetCartoonIndex(cls.m_SID)
        iID = (cls.m_SID << 8) + iCartoonIndex
        if 'CartoonStart' in oSkill.m_Custom and iID in oSkill.m_Custom['CartoonStart']:
            dCartoon['StartFrame'] = oSkill.m_Custom['CartoonStart'][iID]
        else:
            dCartoon['StartFrame'] = oSkill.m_Game.GetFrameNum()
        dCartoon['Start'] = oSkill.m_Base['vStart']
        dCartoon['Casting'] = casting
        dCartoon['LoopID'] = index
        dCartoon['ID'] = iID
        dCartoon['cls'] = cls
        dParentCartoon = oSkill.GetCurCartoon()
        if dParentCartoon:
            dCartoon['Parent'] = dParentCartoon['ID']
            oSkill.PassCrtBuff(dParentCartoon['ID'], iID)
        oSkill.AddStack(dCartoon)
        if cls.m_NeedCtrlNet and oSkill.m_CheckType & CRT_CHECK_CLIENT and not oSkill.CheckReceiveCache(iID):
            dCartoon['WaitNet'] = oSkill.GetWaitNetFrame()
            return None
        cls.DelayInit(oSkill, dCartoon)

    Init = classmethod(Init)
    
    def DelayInit(cls, oSkill, dCartoon):
        index = dCartoon['LoopID']
        dCartoon['Enable'] = 1
        oSkill.m_TempInitCrt = dCartoon
        cls.InitSuccess(oSkill, index, dCartoon)

    DelayInit = classmethod(SetCurCartoon(DelayInit))
    
    def EnableCtrl(cls, oSkill, *args, **kwargs):
        dCartoon = oSkill.m_TempInitCrt
        oSkill.m_TempInitCrt = None
        cls.InitTraceServer(oSkill, dCartoon, *args, **kwargs)
        cls.Active(oSkill)
        cls.Trace(oSkill, dCartoon)

    EnableCtrl = classmethod(EnableCtrl)
    
    def EnableShow(cls, oSkill, *args, **kwargs):
        dCartoon = oSkill.m_TempInitCrt
        oSkill.m_TempInitCrt = None
        cls.InitTraceClient(oSkill, dCartoon, *args, **kwargs)
        cls.Active(oSkill)
        cls.Trace(oSkill, dCartoon)

    EnableShow = classmethod(EnableShow)
    
    def EnableCheck(cls, oSkill, *args, **kwargs):
        return cls.InitTraceCheck(oSkill, oSkill.m_TempInitCrt, *args, **kwargs)

    EnableCheck = classmethod(EnableCheck)
    
    def Disable(cls, oSkill, dCartoon):
        cls.End(oSkill)
        oSkill.PopStack(dCartoon)

    Disable = classmethod(Disable)
    
    def Update(cls, oSkill, dCartoon):
        iRet = cls.HitTarget(oSkill, dCartoon)
        if iRet > 0:
            cls.OnArrive(oSkill, dCartoon)
            iHitStatic = oSkill.m_Update.pop('HitStatic', 0)
            if 'LastVLST' in oSkill.m_Update:
                if oSkill.m_CheckType & CRT_CHECK_CLIENT and dCartoon['ID'] in oSkill.m_NetReceive:
                    dClient = oSkill.m_NetReceive[dCartoon['ID']]
                    oSkill.m_Update['PFBuff'] = dClient.pop('CrtUpdateBuff', { })
                lstTemp = oSkill.m_Update['LastVLST']
                if 'HitInfo' in oSkill.m_Update:
                    lstHitInfo = oSkill.m_Update['HitInfo']
                    iHitInfoLen = len(lstHitInfo)
                else:
                    iHitInfoLen = 0
                for idx in range(len(lstTemp)):
                    iVictim = lstTemp[idx]
                    if idx < iHitInfoLen:
                        dHitInfo = lstHitInfo[idx]
                    else:
                        dHitInfo = { }
                    oSkill.m_Update['CurVID'] = iVictim
                    oSkill.m_Update['CurHitArea'] = dHitInfo['HitArea'] if 'HitArea' in dHitInfo else 0
                    if 'HitPos' in dHitInfo:
                        oSkill.m_Update['CurHitPos'] = dHitInfo['HitPos']
                    cls.Hit(oSkill)
                
            if iHitStatic:
                cls.HitStatic(oSkill)
            elif iRet < 0:
                return None
        if None.m_HaltRS:
            return None
        if cls.IsOver(oSkill, dCartoon):
            if 'IgnoreOnce' in oSkill.m_Collect:
                dIgnoreOce = oSkill.m_Collect['IgnoreOnce']
                iOnceTarget = 0
                for iTarget, iIgnoreType in dIgnoreOce.items():
                    if iIgnoreType == VICTIM_IGNORE_ONCE:
                        iOnceTarget = iTarget
                        break
                
                if iOnceTarget:
                    dIgnoreOce.pop(iOnceTarget)
            cls.Disable(oSkill, dCartoon)
        else:
            cls.Restart(oSkill, dCartoon)

    Update = classmethod(SetCurCartoon(Update))
    
    def ClearCartoonBullet(cls, oSkill, dCartoon):
        if 'BulletKey' in dCartoon:
            tBulletKey = dCartoon.pop('BulletKey')
            oSkill.m_Game.m_SkillMgr.DeleteBullet(tBulletKey, 'Clear')

    ClearCartoonBullet = classmethod(ClearCartoonBullet)
    
    def InitTraceClient(cls, oSkill, dCartoon, *args, **kwargs):
        pass

    InitTraceClient = classmethod(InitTraceClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, *args, **kwargs):
        pass

    InitTraceServer = classmethod(InitTraceServer)
    
    def InitTraceCheck(cls, oSkill, dCartoon, *args, **kwargs):
        dClient = oSkill.m_NetReceive[dCartoon['ID']]
        if 'start' in kwargs:
            if 'Start' not in dClient:
                cl_notify.GS2CDebugMsg(oSkill.m_Game, oSkill.m_Base['pid'], '技能%s %s Start节点初始化数据未发送，请联系程序' % (oSkill.m_Base['pfid'], cls.__name__))
                SendAlert('err', '%s %s %s Start节点初始化数据未发送，请联系程序' % (oSkill.m_Game.m_ID, oSkill.m_Base['pfid'], cls.__name__))
                oSkill.Halt('startcheck')
                return False
            vStart = kwargs['start']
            if vStart and not argcheck.PosAroundCheck(oSkill, dClient['Start'], vStart):
                oSkill.LogCheckErr('startfail %s %s' % (dClient['Start'], vStart))
            if 'MuzzlePos' in dCartoon and dCartoon['MuzzlePos'] == vStart:
                dCartoon['MuzzlePos'] = dClient['Start']
        if 'end' in kwargs:
            if 'End' not in dClient:
                cl_notify.GS2CDebugMsg(oSkill.m_Game, oSkill.m_Base['pid'], '技能%s %s End节点初始化数据未发送，请联系程序' % (oSkill.m_Base['pfid'], cls.__name__))
                SendAlert('err', '%s %s %s End节点初始化数据未发送，请联系程序' % (oSkill.m_Game.m_ID, oSkill.m_Base['pfid'], cls.__name__))
                oSkill.Halt('endcheck')
                return False
            vEnd = kwargs['end']
            if vEnd and not argcheck.PosAroundCheck(oSkill, dClient['End'], vEnd):
                oSkill.LogCheckErr('endfail %s %s' % (dClient['End'], vEnd))
        if 'Start' in dClient and 'End' in dClient and dClient['Start'] == dClient['End'] and not cl_math.IsZero(dClient['End']):
            cl_notify.GS2CDebugMsg(oSkill.m_Game, oSkill.m_Base['pid'], '%d %s起点终点相同，请联系程序' % (oSkill.m_Base['pfid'], cls.__name__))
            oSkill.Halt('samepoint')
            return False
        return True

    InitTraceCheck = classmethod(InitTraceCheck)
    
    def Trace(cls, oSkill, dCartoon):
        pass

    Trace = classmethod(Trace)
    
    def HitTarget(cls, oSkill, dCartoon):
        if oSkill.m_CheckType & CRT_CHECK_CLIENT:
            return cls.HitTargetClient(oSkill, dCartoon)
        return cls.HitTargetServer(oSkill, dCartoon)

    HitTarget = classmethod(HitTarget)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        return 0

    HitTargetClient = classmethod(HitTargetClient)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        return 0

    HitTargetServer = classmethod(HitTargetServer)
    
    def CheckVictimState(cls, oSkill, dCartoon, iVictim):
        if 'IgnoreOnce' in oSkill.m_Collect and iVictim in oSkill.m_Collect['IgnoreOnce']:
            return VICTIM_STATE_IGNOREONCE
        if iVictim == 0:
            return VICTIM_STATE_BLOCK
        oGame = oSkill.m_Game
        oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
        if not oVictim:
            return VICTIM_STATE_NOEXIST
        if oVictim.IsNeglectAttack(oSkill):
            return VICTIM_STATE_BLOCK
        if 'TargetType' in dCartoon and not cl_math.CheckTargetType(oGame, oVictim, oSkill.m_Base['AID'], oSkill.m_Cache['Side'], dCartoon['TargetType']):
            return VICTIM_STATE_INVALID
        if 'AllVLST' in dCartoon and iVictim in dCartoon['AllVLST']:
            return VICTIM_STATE_HIT
        return VICTIM_STATE_VALID

    CheckVictimState = classmethod(CheckVictimState)
    
    def PreProcessVictimList(cls, oSkill, dCartoon, lstVictim):
        oAttack = oSkill.GetAttack()
        if oAttack and oAttack.m_FightType & WARRIOR_SERVANT:
            oGame = oSkill.m_Game
            lstBuffID = oSkill.GetCartoonBuffList(dCartoon['ID'])
            dCrtBuff = { }
            lstNewVictim = []
            for iVictim, dHit in lstVictim:
                if iVictim == 0:
                    lstNewVictim.append((iVictim, dHit))
                    break
                oVictim = oGame.GetObject(iVictim)
                if not oVictim:
                    continue
                if (oVictim.m_FightType == WARRIOR_DEVICE_BARRIER or iVictim not in lstBuffID) and oVictim.ActiveStatus():
                    lstBuffID.append(iVictim)
                    continue
                if oVictim.m_FightType == WARRIOR_SUMMON_BARRIER:
                    if not oVictim.CheckAddBuff():
                        continue
                    oDevice = oVictim.GetOwner()
                    if oDevice.m_ID not in lstBuffID:
                        lstBuffID.append(oDevice.m_ID)
                        continue
                lstNewVictim.append((iVictim, dHit))
                if lstBuffID:
                    dCrtBuff[iVictim] = tuple(lstBuffID)
            
            if dCrtBuff:
                oSkill.m_Update['PFBuff'] = dCrtBuff
            if lstBuffID:
                oSkill.m_CrtBuff[dCartoon['ID']] = lstBuffID
            return lstNewVictim
        return lstVictim

    PreProcessVictimList = classmethod(PreProcessVictimList)
    
    def GetVictimPierceCost(cls, oSkill, iVictim):
        oVictim = oSkill.m_Game.GetObject(iVictim)
        if not oVictim:
            return 0
        if oVictim.m_FightType == WARRIOR_PERFORM:
            return 0
        if oSkill.m_CheckType & CRT_CHECK_SERVER:
            return 1
        if oVictim.m_FightType & WARRIOR_OBSTACLE_NORMAL != WARRIOR_OBSTACLE_NORMAL:
            return 1
        return 0

    GetVictimPierceCost = classmethod(GetVictimPierceCost)
    
    def CheckValidDamage(cls, dCartoon, iVictim, iHitPart):
        if iHitPart == MONSTER_PART_SHIELD:
            return False
        if 'AllHitInfo' not in dCartoon:
            return False
        for dHitInfo in dCartoon['AllHitInfo']:
            if dHitInfo['Victim'] != iVictim:
                continue
            if dHitInfo['HitArea'] != MONSTER_PART_SHIELD:
                return False
        
        return True

    CheckValidDamage = classmethod(CheckValidDamage)
    
    def IsOver(cls, oSkill, dCartoon):
        return 1

    IsOver = classmethod(IsOver)
    
    def Restart(cls, oSkill, dCartoon):
        pass

    Restart = classmethod(Restart)
    
    def OnArrive(cls, oSkill, dCartoon):
        pass

    OnArrive = classmethod(OnArrive)
    
    def OnSend(cls, oSkill, dCartoon):
        pass

    OnSend = classmethod(OnSend)
    
    def AddHitTarget(cls, oSkill, dCartoon, iTarget, dHit):
        pass

    AddHitTarget = classmethod(AddHitTarget)
    
    def GetPushStart(cls, oSkill, dCartoon):
        return dCartoon['Start']

    GetPushStart = classmethod(GetPushStart)
    
    def OnSuspend(cls, oSkill, dCartoon):
        pass

    OnSuspend = classmethod(OnSuspend)
    
    def OnChangeSpeed(cls, oSkill, dCartoon):
        pass

    OnChangeSpeed = classmethod(OnChangeSpeed)
    
    def OnRestore(cls, oSkill, dCartoon):
        pass

    OnRestore = classmethod(OnRestore)
    
    def InitSuccess(cls, oSkill, index, cartoon):
        pass

    InitSuccess = classmethod(InitSuccess)
    
    def Active(cls, oSkill):
        pass

    Active = classmethod(Active)
    
    def End(cls, oSkill):
        pass

    End = classmethod(End)
    
    def Hit(cls, oSkill):
        pass

    Hit = classmethod(Hit)
    
    def HitStatic(cls, oSkill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, oSkill):
        pass

    Trigger = classmethod(Trigger)

