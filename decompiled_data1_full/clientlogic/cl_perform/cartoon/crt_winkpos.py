# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_winkpos.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_winkpos.pyc
# Source Generated with Decompyle++
# File: crt_winkpos.pyc (Python 3.6)

from cl_only import Functor, GAME_FRAME, Second2Frame
from cl_commondefines import VICTIM_STATE_VALID, ATT_SHAPE_LINE, VICTIM_STATE_BLOCK, MODEL_TYPE_BOX, CRT_CHECK_CLIENT
from cl_pxlayer import PXLAYER_EBULLET
from cl_cscommondef.cs_fight import OBJ_ALL
import cllib.lib_cartoon as cartooncheck
import cl_math
import cl_engphyobj
from .mobject import CBaseCartoon

class WinkPosCartoon(CBaseCartoon):
    
    def Trace(cls, oSkill, dCartoon):
        if 'Over' in dCartoon:
            return None
        if oSkill.m_CheckType & CRT_CHECK_CLIENT:
            return None
        oAttack = oSkill.GetAttack()
        if not oAttack:
            return None
        fMoveLen = dCartoon['MoveLen']
        tDir = dCartoon['Dir']
        if not fMoveLen:
            return None
        fTotalSecond = dCartoon['TotalSecond']
        fSpeed = dCartoon['Speed']
        oGame = oSkill.m_Game
        cbfunc = Functor(WinkMoveEnd, oSkill.m_Base['ActNum'], dCartoon['ID'])
        if fTotalSecond:
            fTimeOutSecond = fTotalSecond
            fSpeed = fMoveLen / fTotalSecond
        else:
            fTimeOutSecond = fMoveLen / fSpeed
        iRet = oAttack.m_MoveCtrl.DashMove(oAttack, tDir, fSpeed, fTimeOutSecond, cbfunc)
        if not iRet:
            oSkill.Halt('dashfail')
            return None
        fExtentZ = fSpeed / GAME_FRAME
        oBullet = cl_engphyobj.CreateTraceBullet(oGame, oAttack, {
            'TraceIdx': oSkill.m_Base['PFKey'],
            'LocalPos': (0, 0, fExtentZ),
            'PassID': oAttack.m_ID,
            'LockDirection': tDir }, PXLAYER_EBULLET, {
            'Shape': MODEL_TYPE_BOX,
            'HalfExt': (oAttack.m_ModelRadius, oAttack.m_ModelHeight, fExtentZ) })
        oGame.m_SkillMgr.RegisterBullet(oBullet, oSkill.m_Base['AID'], oSkill.m_Base['ActNum'], dCartoon['ID'])
        dCartoon['BulletKey'] = oBullet.Key()
        oSkill.AddEndFunc(Functor(ClearCartoon, dCartoon))
        if fTotalSecond and dCartoon['WaitOverTime']:
            cls.WaitOverTime(oSkill, dCartoon)

    Trace = classmethod(Trace)
    
    def InitTraceClient(cls, oSkill, dCartoon, fTotalTime, fSpeed, shapeargs = [], ignoreTypeLst = [], dashshape = ATT_SHAPE_LINE, acceleration = 0, decrease = 0, targettype = OBJ_ALL, hitOver = True, bWaitOverTime = False, upSpeed = 0):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        dCartoon['End'] = dClient['End'] if 'End' in dClient else (0, 0, 0)
        dCartoon['TotalSecond'] = fTotalTime * 0.01
        dCartoon['Speed'] = fSpeed
        dCartoon['TargetType'] = targettype
        dCartoon['HitOver'] = hitOver
        dCartoon['UpSpeed'] = upSpeed
        dCartoon['DashShape'] = dashshape
        dCartoon['EffArgs'] = shapeargs
        oAttack = oSkill.GetAttack()
        vStartPos = oAttack.GetPos()
        dCartoon['CurPos'] = vStartPos
        dCartoon['Start'] = vStartPos
        dCartoon['MoveLen'] = cl_math.CalDistance3D(dCartoon['Start'], dCartoon['End'])
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['CurPos']))
        dNet = {
            'End': dCartoon['End'] }
        oSkill.Send(dCartoon['ID'], dNet)
        fTotalTime = dCartoon['TotalSecond']
        fSpeed = dCartoon['Speed']
        if fTotalTime:
            fTimeOut = fTotalTime
            fSpeed = dCartoon['MoveLen'] / fTotalTime
            dCartoon['Speed'] = fSpeed
        elif fSpeed:
            pass
        
        fTimeOut = 0
        bCheck = True
        if 'Over' in dClient:
            cls.Update(oSkill, dCartoon)
            bCheck = False
        elif 'Ray' in dClient:
            cls.Update(oSkill, dCartoon)
            bCheck = CheekDashContinue(oSkill, dClient['Ray'], ignoreTypeLst)
        if bCheck:
            dCtrlCheck = {
                'ActNum': oSkill.m_Base['ActNum'],
                'CartoonID': dCartoon['ID'],
                'ExitCB': ExitDashCheck,
                'Second': fTimeOut,
                'Speed': fSpeed,
                'UpSpeed': upSpeed }
            oAttack.m_MoveCtrl.AddDashCtrlCheck(oAttack, dCtrlCheck)

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID in oSkill.m_NetReceive:
            dClient = oSkill.m_NetReceive[iNodeID]
        dNet = { }
        cartooncheck.CheckDataWinkPos(oSkill, dCartoon)
        iHit = 0
        if 'Ray' in dClient:
            iHit = 1
            lstRay = dClient['Ray']
            lstVLST = []
            lstSend = []
            for vHitPos, vNormal, iVictim, iHitPart in lstRay:
                iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
                dCartoon['Final'] = vHitPos
                if iVictimState == VICTIM_STATE_BLOCK:
                    dCartoon['Over'] = 1
                    lstSend.append((vHitPos, vNormal, 0, iHitPart))
                    continue
                if iVictimState == VICTIM_STATE_VALID and iVictim not in lstVLST:
                    lstVLST.append(iVictim)
                    lstSend.append((vHitPos, vNormal, iVictim, iHitPart))
            
            oSkill.m_Update['LastVLST'] = lstVLST
            dNet['Ray'] = dClient['Ray']
        if 'Over' in dClient:
            dCartoon['Over'] = 1
            dCartoon['Final'] = dClient['End']
            dNet['Over'] = 1
        oSkill.Send(dCartoon['ID'], dNet)
        if 'Trigger' in dClient:
            dNet['Trigger'] = 1
            cls.Trigger(oSkill)
        return iHit

    HitTargetClient = classmethod(HitTargetClient)
    
    def InitTraceServer(cls, oSkill, dCartoon, EndPos, TotalTime, fSpeed, shapeargs = [], ignoreTypeLst = [], dashshape = ATT_SHAPE_LINE, acceleration = 0, decrease = 0, targettype = OBJ_ALL, hitOver = True, bWaitOverTime = False, upSpeed = 0, *args, **kwargs):
        EndPos = oSkill.m_Game.Scene_NavMeshRayCast(oSkill.m_Base['Scene'], oSkill.m_Base['vStart'], EndPos)
        dCartoon['End'] = EndPos
        dCartoon['TotalSecond'] = TotalTime / 100
        dCartoon['Speed'] = fSpeed
        dCartoon['TargetType'] = targettype
        dCartoon['HitOver'] = hitOver
        dCartoon['WaitOverTime'] = bWaitOverTime
        oAttack = oSkill.GetAttack()
        vStartPos = oAttack.GetPos()
        dCartoon['CurPos'] = vStartPos
        dCartoon['Start'] = vStartPos
        dCartoon['MoveLen'] = cl_math.CalDistance3D(dCartoon['Start'], dCartoon['End'])
        dNet = {
            'End': dCartoon['End'] }
        oSkill.Send(dCartoon['ID'], dNet)
        if dCartoon['End'] == dCartoon['CurPos']:
            dCartoon['Over'] = 1
            if dCartoon['TotalSecond'] and dCartoon['WaitOverTime']:
                cls.WaitOverTime(oSkill, dCartoon)
            else:
                oSkill.Send(dCartoon['ID'], {
                    'Over': 1 })
                cls.Disable(oSkill, dCartoon)
            return None
        dCartoon['Dir'] = cl_math.Vec3Normalize(cl_math.Vec3Minus(dCartoon['End'], dCartoon['CurPos']))

    InitTraceServer = classmethod(InitTraceServer)
    
    def WaitOverTime(cls, oSkill, dCartoon):
        iWaitFrame = Second2Frame(dCartoon['TotalSecond']) + 1
        dCartoon['EndFrame'] = dCartoon['StartFrame'] + iWaitFrame
        oSkill.Call_Out(iWaitFrame, dCartoon['ID'])

    WaitOverTime = classmethod(WaitOverTime)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        if 'WinkEnd' not in dCartoon:
            return 0
        dCartoon['Over'] = 1
        oGame = oSkill.m_Game
        iAttack = oSkill.m_Base['AID']
        oAttack = oGame.GetObject(iAttack)
        if not oAttack or oAttack.IsDead():
            return 0
        oAttack.m_MoveCtrl.Stop(oAttack)
        lstVictim = []
        lstHit = dCartoon.get('TargetList', [])
        dCartoon['TargetList'] = []
        if not lstHit:
            return 0
        for iVictim in lstHit:
            iVictimState = cls.CheckVictimState(oSkill, dCartoon, iVictim)
            if iVictimState == VICTIM_STATE_VALID and iVictim not in lstVictim:
                lstVictim.append(iVictim)
        
        if not lstVictim:
            return 0
        oSkill.m_Update['LastVLST'] = lstVictim
        dNet = {
            'LastVLST': lstVictim }
        oSkill.Send(dCartoon['ID'], dNet)
        return 1

    HitTargetServer = classmethod(HitTargetServer)
    
    def AddHitTarget(cls, oSkill, dCartoon, iTarget, dHit):
        if 'WinkEnd' in dCartoon:
            return None
        lstHit = dCartoon.get('TargetList', [])
        if iTarget not in lstHit:
            lstHit.append(iTarget)
        dCartoon['TargetList'] = lstHit
        cls.WinkMoveEnd(oSkill, dCartoon)

    AddHitTarget = classmethod(AddHitTarget)
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        iOver = 0
        if 'Over' in dCartoon:
            if 'EndFrame' not in dCartoon or dCartoon['EndFrame'] <= oSkill.m_Game.GetFrameNum():
                iOver = 1
        if iOver:
            ClearCartoon(dCartoon, oSkill)
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def WinkMoveEnd(cls, oSkill, dCartoon):
        if 'WinkEnd' not in dCartoon:
            dCartoon['WinkEnd'] = 1
            iAttack = oSkill.m_Base['AID']
            oAttack = oSkill.m_Game.GetObject(iAttack)
            oAttack.m_MoveCtrl.m_WinkMoveCB = None

    WinkMoveEnd = classmethod(WinkMoveEnd)
    
    def OnSuspend(cls, oSkill, dCartoon):
        if 'BulletKey' in dCartoon:
            oBullet = oSkill.m_Game.m_SkillMgr.GetBullet(dCartoon['BulletKey'])
            oBullet.Disable()

    OnSuspend = classmethod(OnSuspend)
    
    def OnRestore(cls, oSkill, dCartoon):
        if 'BulletKey' in dCartoon:
            oBullet = oSkill.m_Game.m_SkillMgr.GetBullet(dCartoon['BulletKey'])
            oBullet.Enable()

    OnRestore = classmethod(OnRestore)


def WinkMoveEnd(iActNum, iCartoon, oAttack, iFlag):
    if not oAttack:
        return None
    oGame = oAttack.m_Game
    oSkill = oGame.m_SkillMgr.GetSkill(oAttack.m_ID, iActNum)
    if not oSkill or iCartoon not in oSkill.m_Cartoon:
        return None
    dCartoon = oSkill.m_Cartoon[iCartoon]
    if 'WinkEnd' not in dCartoon:
        clsCartoon = dCartoon['cls']
        clsCartoon.WinkMoveEnd(oSkill, dCartoon)
        oSkill.Update([
            dCartoon['ID']])


def ClearCartoon(dCartoon, oSkill):
    dCartoon['cls'].ClearCartoonBullet(oSkill, dCartoon)


def ExitDashCheck(oAttack, dCtrlCheck):
    oSkill = oAttack.m_Game.m_SkillMgr.GetSkill(oAttack.m_ID, dCtrlCheck['ActNum'])
    if not oSkill:
        return None
    dCartoon = oSkill.GetCartoonByID(dCtrlCheck['CartoonID'])
    if not dCartoon or 'Over' in dCartoon:
        return None
    oSkill.Halt('ServerStop')


def CheekDashContinue(oSkill, lstRay, lstIgnore):
    if not lstIgnore:
        return False
    oGame = oSkill.m_Game
    for _, _, iVictim, _ in lstRay:
        oVictim = oGame.GetObject(iVictim)
        if not oVictim:
            continue
        if oVictim.m_FightType not in lstIgnore:
            break
    else:
        return True
    return False

