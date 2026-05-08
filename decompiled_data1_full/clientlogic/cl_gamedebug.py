# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_gamedebug.pyc
# RelativePath: clientlogic/cl_gamedebug.pyc
# Source Generated with Decompyle++
# File: cl_gamedebug.pyc (Python 3.6)

from cl_only import Functor, log_file, CELL_SPACESIZE, OutputPos, GetServerIndex, GAME_FRAME, TraceLog, PythonError
from cllib.lib_net import UnpackInt, UnpackString, UnpackBinaryString, SetPacketDataForUnpack
from cl_propdata import BASIC_PROP_NAME
from cl_commondefines import WARRIOR_BOSS, WARRIOR_ELITE, STATE_TIME_FOREVER, DISABLE_TYPE_RELIC, RELIC_5776
from cl_object.logging import SkillLog
import re
import sys
import linecache
import collections
import zlib
import marshal
import cllib.lib_flag
import cl_duonet.dn_cl_gamedebug
import cl_math
import cl_netattr
import cl_item
import cl_notify

def GetMembers(obj):
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, list) or isinstance(obj, tuple):
        return dict(enumerate(obj))


def WalkObj(obj, setID, dObjInfo, sPre):
    if sPre:
        sPre += '.'
    setID.add(id(obj))
    dobj = GetMembers(obj)
    if dobj is None:
        return None
    for k in sorted(list(dobj.keys())):
        v = dobj[k]
        if id(v) in setID:
            continue
        if not isinstance(v, int):
            setID.add(id(v))
        if isinstance(v, collections.deque):
            continue
        if isinstance(v, set):
            dObjInfo['%s%s' % (sPre, k)] = tuple(v)
            continue
        if GetMembers(v) is None and not hasattr(v, '__call__'):
            dObjInfo['%s%s' % (sPre, k)] = v
            continue
        WalkObj(v, setID, dObjInfo, sPre + str(k))
    


def StacksWithLocals(f = None, iLog = 0, limit = 50):
    if f is None:
        
        try:
            raise ZeroDivisionError
        except ZeroDivisionError:
            f = sys.exc_info()[2].tb_frame.f_back

    lstStack = []
    for _ in range(limit):
        lineno = f.f_lineno
        co = f.f_code
        localvar = f.f_locals
        filename = co.co_filename
        name = co.co_name
        linecache.checkcache(filename)
        line = linecache.getline(filename, lineno, f.f_globals)
        if line:
            line = line.strip()
        else:
            line = None
        onlylocals = { }
        for k, v in localvar.items():
            if k in f.f_globals:
                continue
            onlylocals[k] = v
        
        lstStack.append((filename, lineno, name, line, LocalsWithoutObjID(onlylocals)))
        f = f.f_back
        if f is None:
            break
    
    lstStack.reverse()
    if iLog:
        LogStacksWithLocals(lstStack, 'debug/nosame')
    return lstStack


def LocalsWithoutObjID(dLocal):
    s = str(dLocal)
    return re.sub('at 0x(\\S+)>', '>', s)


def PrintStacksWithLocals(lstStack, PrintFunc = None):
    if PrintFunc is None:
        PrintFunc = sys.stderr.write
    for filename, lineno, name, line, locals in lstStack:
        PrintFunc('  File "%s", line %d, in %s' % (filename, lineno, name))
        if line:
            PrintFunc('    %s' % line.strip())
        PrintFunc('    Locals: "%s"' % locals)
    


def LogStacksWithLocals(lstStack, sPath):
    if cllib.lib_flag.g_IsLogicLayer:
        
        def _print(text):
            print(text)

        func = _print
    else:
        func = Functor(log_file, sPath)
    PrintStacksWithLocals(lstStack, func)

if 'g_RecordCallFrom' not in globals():
    g_RecordCallFrom = { }

def RecordCallFrom(func):
    
    def _(*args, **kwargs):
        
        try:
            raise ZeroDivisionError
        except ZeroDivisionError:
            f = sys.exc_info()[2].tb_frame.f_back

        lineno = f.f_lineno
        co = f.f_code
        filename = co.co_filename
        name = co.co_name
        key = ' '.join([
            filename,
            str(lineno),
            name])
        if key not in g_RecordCallFrom:
            g_RecordCallFrom[key] = 0
        g_RecordCallFrom[key] += 1
        return func(*args, **kwargs)

    return _


def TraceCmd(oGame, iFrame, k, v):
    
    def _Trace(f, e, a):
        if e == 'call' or e == 'c_call':
            return _LocalTrace

    
    def _LocalTrace(f, e, a):
        if iFrame != oGame.GetFrameNum():
            return None
        print('Debugging...')
        lstAttr = k.split('.')
        obj = oGame
        for sAttr in lstAttr:
            if hasattr(obj, sAttr):
                obj = getattr(obj, sAttr)
                continue
            
            try:
                obj = obj[int(sAttr)]
            except:
                try:
                    obj = obj[sAttr]
                except:
                    return _LocalTrace

        
        if obj == v:
            StacksWithLocals(f, 1)
            print('LogStack Over!')
            sys.settrace(None)
            return None
        return _LocalTrace

    
    def _Run(func):
        
        def _(*args, **kwargs):
            sys.settrace(_Trace)
            func(*args, **kwargs)
            sys.settrace(None)

        return _

    return _Run

LINE_NORMAL = 100
LINE_GMCMD = 103
LINE_TILE = 104
LINE_QUAD = 105
LINE_MESHLINE = 106
LINE_FLYLINE = 107
LINE_CLIENTPATH = 109
LINE_BOX = 119

def DebugSector(oGame, vPos, r, vDir, iAngle, iType, rgb = 16711680, pid = 0):
    vLastPos = cl_math.Vec3DisplaceDir(vPos, vDir, r)
    DebugLine(oGame, vPos[0], vPos[1], vPos[2], vLastPos[0], vLastPos[1], vLastPos[2], rgb, iType, pid)
    for iIndex in range(int(iAngle)):
        vOffsetDir = cl_math.RotateAroundVector(vDir, (0, 1, 0), iIndex + 1)
        vOffsetPos = cl_math.Vec3DisplaceDir(vPos, vOffsetDir, r)
        DebugLine(oGame, vLastPos[0], vLastPos[1], vLastPos[2], vOffsetPos[0], vOffsetPos[1], vOffsetPos[2], rgb, iType, pid)
        vLastPos = vOffsetPos
    
    DebugLine(oGame, vPos[0], vPos[1], vPos[2], vLastPos[0], vLastPos[1], vLastPos[2], rgb, iType, pid)


def DebugCircle(oGame, vPos, r, iType, rgb = 16711680, pid = 0):
    (ox, oy, oz) = vPos
    DebugLine(oGame, ox, oy, oz + r, ox + r * 0.707, oy, oz + r * 0.707, rgb, iType, pid)
    DebugLine(oGame, ox, oy, oz + r, ox - r * 0.707, oy, oz + r * 0.707, rgb, iType, pid)
    DebugLine(oGame, ox, oy, oz - r, ox + r * 0.707, oy, oz - r * 0.707, rgb, iType, pid)
    DebugLine(oGame, ox, oy, oz - r, ox - r * 0.707, oy, oz - r * 0.707, rgb, iType, pid)
    DebugLine(oGame, ox + r, oy, oz, ox + r * 0.707, oy, oz + r * 0.707, rgb, iType, pid)
    DebugLine(oGame, ox + r, oy, oz, ox + r * 0.707, oy, oz - r * 0.707, rgb, iType, pid)
    DebugLine(oGame, ox - r, oy, oz, ox - r * 0.707, oy, oz + r * 0.707, rgb, iType, pid)
    DebugLine(oGame, ox - r, oy, oz, ox - r * 0.707, oy, oz - r * 0.707, rgb, iType, pid)


def DebugSphere(oGame, vPos, r, iType, rgb = 16711680, pid = 0):
    (ox, oy, oz) = vPos
    DebugLine(oGame, ox, oy - r, oz, ox - r, oy, oz, rgb, iType, pid)
    DebugLine(oGame, ox, oy - r, oz, ox + r, oy, oz, rgb, iType, pid)
    DebugLine(oGame, ox, oy - r, oz, ox, oy, oz - r, rgb, iType, pid)
    DebugLine(oGame, ox, oy - r, oz, ox, oy, oz + r, rgb, iType, pid)
    DebugLine(oGame, ox, oy + r, oz, ox - r, oy, oz, rgb, iType, pid)
    DebugLine(oGame, ox, oy + r, oz, ox + r, oy, oz, rgb, iType, pid)
    DebugLine(oGame, ox, oy + r, oz, ox, oy, oz - r, rgb, iType, pid)
    DebugLine(oGame, ox, oy + r, oz, ox, oy, oz + r, rgb, iType, pid)


def DebugCylinder(oGame, vStart, r, h, iType, rgb = 16711680, pid = 0):
    (ox, oy, oz) = vStart
    DebugCircle(oGame, vStart, r, iType)
    DebugCircle(oGame, (ox, oy - h, oz), r, iType, rgb, pid)
    DebugCircle(oGame, (ox, oy + h, oz), r, iType, rgb, pid)
    DebugLine(oGame, ox, oy - h, oz + r, ox, oy + h, oz + r, rgb, iType, pid)
    DebugLine(oGame, ox, oy - h, oz - r, ox, oy + h, oz - r, rgb, iType, pid)
    DebugLine(oGame, ox + r, oy - h, oz, ox + r, oy + h, oz, rgb, iType, pid)
    DebugLine(oGame, ox - r, oy - h, oz, ox - r, oy + h, oz, rgb, iType, pid)


def DebugBox(oGame, vStart, vDir, fLength, fWidth, fHeight, rgb = 16711680, pid = 0):
    vP1 = cl_math.Vec3DestPosDirPlane(vStart, vDir, fWidth / 2, 90)
    vP2 = cl_math.Vec3DestPosDirPlane(vStart, vDir, fWidth / 2, -90)
    vP3 = cl_math.Vec3DisplaceDir(vP1, vDir, fLength)
    vP4 = cl_math.Vec3DisplaceDir(vP2, vDir, fLength)
    vNormal = cl_math.VectorCross3D(cl_math.Vec3Minus(vP1, vP2), cl_math.Vec3Minus(vP3, vP1))
    vP5 = cl_math.Vec3DisplaceDir(vP1, vNormal, fHeight)
    vP6 = cl_math.Vec3DisplaceDir(vP2, vNormal, fHeight)
    vP7 = cl_math.Vec3DisplaceDir(vP3, vNormal, fHeight)
    vP8 = cl_math.Vec3DisplaceDir(vP4, vNormal, fHeight)
    lstPoint = [
        vP1,
        vP2,
        vP3,
        vP4,
        vP5,
        vP6,
        vP7,
        vP8]
    for i in range(len(lstPoint)):
        for j in range(i + 1, len(lstPoint)):
            vPoint1 = lstPoint[i]
            vPoint2 = lstPoint[j]
            DebugLine(oGame, vPoint1[0], vPoint1[1], vPoint1[2], vPoint2[0], vPoint2[1], vPoint2[2], rgb, LINE_BOX, pid)
        
    


def DebugLine(oGame, ox, oy, oz, x, y, z, rgb = 0, iTypeNum = 100, pid = 0):
    if iTypeNum < 100:
        raise Exception('DebugLine 编号%d 不能小于100' % iTypeNum)
    if pid:
        if pid not in oGame.GetRealPlayers():
            return None
        dPlayer = {
            pid: 1 }
    else:
        dPlayer = oGame.GetRealPlayers()
    netData = {
        'ox': int(ox * CELL_SPACESIZE),
        'oy': int(oy * CELL_SPACESIZE),
        'oz': int(oz * CELL_SPACESIZE),
        'x': int(x * CELL_SPACESIZE),
        'y': int(y * CELL_SPACESIZE),
        'z': int(z * CELL_SPACESIZE),
        'rgb': rgb,
        'iTypeNum': iTypeNum,
        'dPlayer': dPlayer }
    cl_duonet.dn_cl_gamedebug.DN_GS2CDebugLine(netData)


def ClearDebugLine(oGame, iTypeNum = 0, pid = 0):
    if pid:
        if pid not in oGame.GetRealPlayers():
            return None
        dPlayer = {
            pid: 1 }
    else:
        dPlayer = oGame.GetRealPlayers()
    netData = {
        'iTypeNum': iTypeNum,
        'dPlayer': dPlayer }
    cl_duonet.dn_cl_gamedebug.DN_GS2CClearDebugLine(netData)


def DebugMonsterConfig(oGame, pid, dInfo):
    netData = {
        'oGame': oGame,
        'pid': pid }
    netData.update(dInfo)
    cl_duonet.dn_cl_gamedebug.DN_GS2CMonsterConfig(netData)


def MonsterDebug(oGame, iShow, iID, iNo, sInfo):
    dPlayer = oGame.GetRealPlayers()
    netData = {
        'oGame': oGame,
        'iShow': iShow,
        'iID': iID,
        'iNo': iNo,
        'sInfo': sInfo,
        'dPlayer': dPlayer }
    cl_duonet.dn_cl_gamedebug.DN_GS2CMonsterDebug(netData)


def BuildDebug(oGame, iShow, iID, iNo, sInfo):
    dPlayer = oGame.GetRealPlayers()
    netData = {
        'oGame': oGame,
        'iShow': iShow,
        'iID': iID,
        'iNo': iNo,
        'sInfo': sInfo,
        'dPlayer': dPlayer }
    cl_duonet.dn_cl_gamedebug.DN_GS2CBuildDebug(netData)


def ServantDebug(oGame, iShow, iID, sInfo):
    dPlayer = oGame.GetRealPlayers()
    netData = {
        'oGame': oGame,
        'iShow': iShow,
        'iID': iID,
        'sInfo': sInfo,
        'dPlayer': dPlayer }
    cl_duonet.dn_cl_gamedebug.DN_GS2CServantDebug(netData)


def SeedDebug(oGame, pid, sSeed):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'sSeed': sSeed }
    cl_duonet.dn_cl_gamedebug.DN_GS2CSendSeed(netData)


def CreateLogSeed(oHero):
    dData = oHero.GetHeroDetailData(bCreateSeed = True)
    dData['WarMgr'] = oHero.m_Game.m_WarMgr.SaveSeed(oHero)
    sLogSeed = zlib.compress(marshal.dumps(dData))
    return sLogSeed


def GetMonsterStateInfo(oMonster):
    dInfo = { }
    for oState in oMonster.m_State.m_Item.values():
        if oState.m_SID in (20026, 20027, 20028, 20029, 20030, 20031):
            continue
        iOldRemainTime = dInfo[oState.m_SID] if oState.m_SID in dInfo else 0
        if iOldRemainTime == -1:
            continue
        if oState.m_TimeType == STATE_TIME_FOREVER:
            dInfo[oState.m_SID] = -1
            continue
        iRemainTime = oState.GetRemainTime()
        if iRemainTime > iOldRemainTime:
            dInfo[oState.m_SID] = iRemainTime
    
    return dInfo


def GetMonsterPerformInfo(oMonster):
    lstPerform = []
    for oPerform in oMonster.m_Perform.m_Perform.values():
        if not oPerform.m_Enable:
            continue
        lstPerform.append(oPerform.m_SID)
    
    return lstPerform


def GameNowInfo(oHero):
    
    def GetMonsterInfo(oGame, iMonster):
        oMonster = oGame.GetObject(iMonster)
        iExtraInfo = 0
        if oMonster:
            sPos = OutputPos(oMonster.GetPos())
            sMonsterInfo = '%s_%s_%s_%s' % (oMonster.m_LineIdx, oMonster.m_SID, iMonster, sPos)
            vBornPos = oMonster.m_Agent.GetData('BornPos') if oMonster.m_Agent else None
            sMonsterInfo += ' bornpos: %s' % (OutputPos(vBornPos) if vBornPos else None)
            dInfo = GetMonsterStateInfo(oMonster)
            lstPerform = GetMonsterPerformInfo(oMonster)
            if 'SpecialKey' in oMonster.m_PrivateAttr:
                sMonsterInfo += ' special:%s' % oMonster.m_PrivateAttr['SpecialKey'].m_BitList
            if 'LogicKey' in oMonster.m_PrivateAttr:
                sMonsterInfo += ' logic:%s' % oMonster.m_PrivateAttr['LogicKey'].m_BitList
            dDiePriority = oMonster.Query('DiePriority', { })
            sMonsterInfo += ' hp:%s armor:%s shield:%s stateinfo:%s perform:%s diepriority:%s' % (oMonster.HP(), oMonster.Armor(), oMonster.Shield(), dInfo, lstPerform, dDiePriority)
            iExtraInfo = 1
            oAgent = oMonster.m_Agent
            if oAgent:
                oCurrentBT = oAgent.PYGetCurrentBT()
                sTree = oCurrentBT.GetPathName() if oCurrentBT else 'None'
                iTarget = oMonster.Query('LockEnemy', 0)
                sMonsterInfo += ' tree:%s target:%s' % (sTree, iTarget)
                if not oAgent.m_bActive:
                    sMonsterInfo += ' pause:%s' % oAgent.m_Pause
            if oMonster.m_ImmobilizeSource:
                sMonsterInfo += ' lock:%s' % oMonster.m_ImmobilizeSource
            if oMonster.m_FightType & WARRIOR_BOSS == WARRIOR_BOSS or oMonster.m_FightType & WARRIOR_ELITE == WARRIOR_ELITE:
                if oAgent:
                    iCurFrame = oGame.GetFrameNum()
                    iValidFrame = iCurFrame - 5 * GAME_FRAME
                    dHate = { }
                    for iHateTarget, dData in oAgent.GetData('HateData', { }).items():
                        dFrame = { }
                        iTotalDam = 0
                        for iFrame, iDam in dData['Dam'].items():
                            if iFrame < iValidFrame:
                                continue
                            dFrame[iFrame] = 1
                            iTotalDam += iDam
                        
                        dNewData = dict(dData)
                        dNewData.pop('Dam')
                        dNewData['lstFrame'] = list(dFrame)
                        dNewData['TotalDam'] = iTotalDam
                        dHate[iHateTarget] = dNewData
                    
                else:
                    dHate = { }
                lstState = []
                if oMonster.m_State:
                    lstState = [ iSID for iSID, lstState in oMonster.m_State.m_StateBySid.items() if lstState ]
                sMonsterInfo += 'hate: %s state:%s phase:%s' % (dHate, lstState, oMonster.m_Phase)
            return (sMonsterInfo, iExtraInfo)
        return ('%s_()' % iMonster, iExtraInfo)

    
    def GetServantInfo(oGame, iServant):
        oServant = oGame.GetObject(iServant)
        if not oServant:
            return ''
        sAllAttr = ''
        lstAttr = [
            'HP',
            'HPMax',
            'Speed',
            'Phase']
        for sAttr in lstAttr:
            if sAttr in BASIC_PROP_NAME:
                (_, _, _, _, iMode) = BASIC_PROP_NAME[sAttr]
                iVal = cl_netattr.GetPropValue(oServant, sAttr, iMode)
            else:
                iVal = oServant.QueryAttr(sAttr)
            sAllAttr += '%s:%s, ' % (sAttr, iVal)
        
        sServantInfo = '%s_%s 属性:[%s] 移动模式:%d 坐标:%s' % (oServant.m_SID, iServant, sAllAttr, oServant.m_MoveMode, OutputPos(oServant.GetPos()))
        oMoveCtrl = oServant.m_MoveCtrl
        if oMoveCtrl:
            sServantInfo += ' 移动路径:%s' % oMoveCtrl.E_GetPathData()
        if oServant.m_TransferHistory:
            sServantInfo += ' 最近传送记录:%s' % oServant.m_TransferHistory[-10:]
        oAgent = oServant.m_Agent
        if oAgent:
            oCurrentBT = oAgent.PYGetCurrentBT()
            sTreeInfo = oCurrentBT.GetPathName() if oCurrentBT else 'None'
            iTarget = oServant.Query('LockEnemy', 0)
            dHate = oAgent.GetData('HateData', { })
            sServantInfo += ' 行为树:%s 锁定目标:%s 仇恨列表:%s' % (sTreeInfo, iTarget, list(dHate))
            if not oAgent.m_bActive:
                sServantInfo += ' 暂停原因:%s' % oAgent.m_Pause
        return sServantInfo

    
    def GetDeviceInfo(oGame, oDevice):
        sAllAttr = ''
        lstAttr = [
            'Speed',
            'ActiveStatus',
            'DeployStatus']
        for sAttr in lstAttr:
            if sAttr in BASIC_PROP_NAME:
                (_, _, _, _, iMode) = BASIC_PROP_NAME[sAttr]
                iVal = cl_netattr.GetPropValue(oDevice, sAttr, iMode)
            else:
                iVal = oDevice.QueryAttr(sAttr)
            sAllAttr += '%s:%s, ' % (sAttr, iVal)
        
        sDeviceInfo = '%s_%s 属性:[%s]' % (oDevice.m_SID, oDevice.m_ID, sAllAttr)
        oAgent = oDevice.m_Agent
        if oAgent:
            oMoveCtrl = oDevice.m_MoveCtrl
            sDeviceInfo += ' 移动模式:%d 坐标:%s' % (oDevice.m_MoveMode, OutputPos(oDevice.GetPos()))
            if oMoveCtrl:
                sDeviceInfo += ' 移动路径:%s' % oMoveCtrl.E_GetPathData()
            oCurrentBT = oAgent.PYGetCurrentBT()
            sTreeInfo = oCurrentBT.GetPathName() if oCurrentBT else 'None'
            iTarget = oDevice.Query('LockEnemy', 0)
            dHate = oAgent.GetData('HateData', { })
            sDeviceInfo += ' 行为树:%s 锁定目标:%s 仇恨列表:%s' % (sTreeInfo, iTarget, list(dHate))
            sDeviceInfo += ' 跟随状态:%s' % oAgent.GetData('FollowMoveStatus')
            if not oAgent.m_bActive:
                sDeviceInfo += ' 暂停原因:%s' % oAgent.m_Pause
        return sDeviceInfo

    
    def GetPetInfo(oGame, oPet):
        sAllAttr = ''
        lstAttr = [
            'HP',
            'HPMax',
            'Speed',
            'Phase',
            'MoveStatus',
            'FightStatus']
        for sAttr in lstAttr:
            if sAttr in BASIC_PROP_NAME:
                (_, _, _, _, iMode) = BASIC_PROP_NAME[sAttr]
                iVal = cl_netattr.GetPropValue(oPet, sAttr, iMode)
            else:
                iVal = oPet.QueryAttr(sAttr)
            sAllAttr += '%s:%s, ' % (sAttr, iVal)
        
        lstAbility = oPet.Ability()
        lstSealedAbility = oPet.SealedAbility()
        sPetInfo = '%s_%s 属性:[%s] 词条:%s 封印词条: %s 偏差值:%s 移动模式:%d 坐标:%s 死亡标记:%s' % (oPet.m_SID, oPet.m_ID, sAllAttr, lstAbility, lstSealedAbility, oPet.m_AttrOffset, oPet.m_MoveMode, OutputPos(oPet.GetPos()), oPet.m_Dead)
        oMoveCtrl = oPet.m_MoveCtrl
        if oMoveCtrl:
            sPetInfo += ' 移动路径:%s' % oMoveCtrl.E_GetPathData()
        oAgent = oPet.m_Agent
        if oAgent:
            oCurrentBT = oAgent.PYGetCurrentBT()
            sTreeInfo = oCurrentBT.GetPathName() if oCurrentBT else 'None'
            iTarget = oPet.Query('LockEnemy', 0)
            dHate = oAgent.GetData('HateData', { })
            sPetInfo += ' 行为树:%s 锁定目标:%s 仇恨列表:%s' % (sTreeInfo, iTarget, list(dHate))
            if not oAgent.m_bActive:
                sPetInfo += ' 暂停原因:%s' % oAgent.m_Pause
        return sPetInfo

    
    def GetNewVerLayerInfo(oGame, oHero):
        dChooseNewLayerInfo = {
            2: {
                'Boss': [
                    39131,
                    39151],
                'TargetNum': 5 },
            3: {
                'Boss': [
                    39051,
                    39201],
                'TargetNum': 5 } }
        dResult = {
            2: {
                'CanChoose': 0,
                'PassNum': 0 },
            3: {
                'CanChoose': 0,
                'PassNum': 0 } }
        for iLayer, dChooseInfo in dChooseNewLayerInfo.items():
            dPassNum = oHero.Query('NewVerLayer', { })
            if iLayer in dPassNum:
                dResult[iLayer]['PassNum'] = dPassNum[iLayer]
            lstBoss = dChooseInfo['Boss']
            iTargetNum = dChooseInfo['TargetNum']
            lstHero = oGame.m_WarMgr.GetRoomHero(iCalAI = 0)
            for iHero in lstHero:
                oHero = oGame.GetObject(iHero)
                if not oHero:
                    continue
                dMonster = oHero.Query('Monster')
                if 'KillBoss' not in dMonster:
                    continue
                iKill = 0
                for iMonsterSID in lstBoss:
                    iKill += dMonster['KillBoss'].get(iMonsterSID, 0)
                
                if iKill >= iTargetNum:
                    dResult[iLayer]['CanChoose'] = 1
                    break
            
        
        sChooseNewLayerInfo = ''
        for iLayer, dInfo in dResult.items():
            sChooseNewLayerInfo += '新%d幕: 通关次数: %s, 是否能抽取到: %s \n' % (iLayer, dInfo['PassNum'], dInfo['CanChoose'])
        
        return sChooseNewLayerInfo

    oGame = oHero.m_Game
    lstInfo = []
    sChooseNewLayerInfo = GetNewVerLayerInfo(oGame, oHero)
    lstInfo.append('抽取新幕信息: %s\n' % sChooseNewLayerInfo)
    sAllAttr = ''
    lstAttr = [
        'HP',
        'HPMax',
        'RHP',
        'Shield',
        'ShieldMax',
        'RShield',
        'ShieldRecoverTime',
        'Armor',
        'Speed',
        'Toughness',
        'DefPhysical',
        'DefFire',
        'DefCorrision',
        'DefThunder']
    for sAttr in lstAttr:
        if sAttr in BASIC_PROP_NAME:
            (_, _, _, _, iMode) = BASIC_PROP_NAME[sAttr]
            iVal = cl_netattr.GetPropValue(oHero, sAttr, iMode)
        else:
            iVal = oHero.QueryAttr(sAttr)
        sAllAttr += '%s:%s, ' % (sAttr, iVal)
    
    lstInfo.append('属性:[%s]\n' % sAllAttr)
    sBaseDamRatio = '叠加: %s, 叠乘: %s' % (oHero.GetBaseDamAddRatio(), oHero.GetBaseDamMulRatio())
    lstInfo.append('基础加成:[%s]\n' % sBaseDamRatio)
    oRelicTalentCon = oHero.m_RelicTalentCon
    if oRelicTalentCon and oRelicTalentCon.m_Relic:
        oBasePerorm = oRelicTalentCon.GetPerform(oRelicTalentCon.m_Relic)
        sRelicTalentBasePF = '%s(%s)' % (oBasePerorm.m_Name, oBasePerorm.m_SID) if oBasePerorm else '无'
        sRelicTalent = ''
        for iPF in oHero.m_RelicTalentCon.m_Talent:
            oPerform = oHero.m_RelicTalentCon.GetPerform(iPF)
            if not oPerform:
                continue
            sRelicTalent += '%s(%d)-%d级, ' % (oPerform.m_Name, oPerform.m_SID, oPerform.m_Level)
        
        lstInfo.append('秘能觉醒: 基础秘能：%s，觉醒：[%s]' % (sRelicTalentBasePF, sRelicTalent))
    iRelicSub = 0
    sRelic = ''
    for iPos, oRelic in oHero.m_RelicCon.m_PosPerform.items():
        iRelicSub += 1
        sRelic += '%d:%s(%d)-%s级, ' % (iPos, oRelic.m_Name, oRelic.m_SID, oRelic.m_Level)
        if iRelicSub % 100 == 0:
            iRelicSub = 0
            sRelic += '\n'
    
    lstInfo.append('遗物:[%s]\n' % sRelic)
    oRelicCon = oHero.m_RelicCon
    pfobj = oRelicCon.GetPerform(RELIC_5776)
    if pfobj and DISABLE_TYPE_RELIC in pfobj.m_LifeCycle.m_DisableType:
        lstInfo.append('\n 驱邪护符 禁用诅咒遗物%s' % str(pfobj.m_LifeCycle.m_DisableType[DISABLE_TYPE_RELIC]))
    sTalent = ''
    for oTalent in oHero.m_TalentCon.m_Perform.values():
        sTalent += '%s(%d)-%d级, ' % (oTalent.m_Name, oTalent.m_SID, oTalent.m_Level)
    
    lstInfo.append('天赋:[%s]' % sTalent)
    sBullet = ''
    for iBullet, iAmount in oHero.m_BulletCon.m_Bullet.items():
        clsBullet = cl_item.GetItemCls(iBullet)
        sBullet += '%s(%d):%d颗, ' % (clsBullet.m_Name, iBullet, iAmount)
    
    lstInfo.append('子弹:[%s]' % sBullet)
    sWeapon = ''
    for iPos, oWeapon in sorted(oHero.m_WieldCon.m_Item.items()):
        lstShareInscription = oWeapon.GetComponent('Inscription').m_ShareInscription if oWeapon.GetComponent('Inscription') else []
        sWeapon += '%d号位:%s(%d)%s %s %s %s, ' % (iPos, oWeapon.m_Name, oWeapon.m_SID, oWeapon.CustomAttrValue('Inscription'), oWeapon.GetComponent('Enhance').TraceName(), oWeapon.CustomAttrValue('SealedInscription'), lstShareInscription)
    
    lstInfo.append('武器:[%s]' % sWeapon)
    sExWeaponContainer = ''
    for iPos, oWeapon in sorted(oHero.m_ExWeaponCon.m_Item.items()):
        lstShareInscription = oWeapon.GetComponent('Inscription').m_ShareInscription if oWeapon.GetComponent('Inscription') else []
        sExWeaponContainer += '%d号位:%s(%d)%s %s %s %s, ' % (iPos, oWeapon.m_Name, oWeapon.m_SID, oWeapon.CustomAttrValue('Inscription'), oWeapon.GetComponent('Enhance').TraceName(), oWeapon.CustomAttrValue('SealedInscription'), lstShareInscription)
    
    lstInfo.append('额外背包武器:[%s]' % sExWeaponContainer)
    sWeaponStoreCon = ''
    for iPos, oWeapon in sorted(oHero.m_WeaponStoreCon.m_Item.items()):
        lstShareInscription = oWeapon.GetComponent('Inscription').m_ShareInscription if oWeapon.GetComponent('Inscription') else []
        sWeaponStoreCon += '%d号位:%s(%d)%s %s %s %s, ' % (iPos, oWeapon.m_Name, oWeapon.m_SID, oWeapon.CustomAttrValue('Inscription'), oWeapon.GetComponent('Enhance').TraceName(), oWeapon.CustomAttrValue('SealedInscription'), lstShareInscription)
    
    lstInfo.append('宝库武器:[%s]' % sWeaponStoreCon)
    sBenediction = ''
    for oBenediction in oHero.m_BenedictionCon.m_Perform.values():
        sBenediction += '%s(%d), ' % (oBenediction.m_Name, oBenediction.m_SID)
    
    lstInfo.append('祝福:[%s]' % sBenediction)
    sTaskInfo = GetTaskInfo(oHero)
    if sTaskInfo:
        lstInfo.append('任务:[%s]' % sTaskInfo)
    iServant = oHero.m_Servant
    if iServant:
        sServantInfo = GetServantInfo(oGame, iServant)
        if sServantInfo:
            lstInfo.append('仆从: %s' % sServantInfo)
    oDevice = oHero.GetDevice()
    if oDevice:
        sComponet = ''
        oDevicePerformCon = oHero.m_DevicePerformCon
        dPerform = oDevicePerformCon.m_Perform
        for iSID in oDevicePerformCon.m_Component:
            iPos = oDevicePerformCon.GetComponentPos(iSID)
            oComponent = dPerform[iSID]
            sComponet += '%d:%s(%d)-%d级, ' % (iPos, oComponent.m_Name, iSID, oComponent.m_Level)
        
        lstInfo.append('组件:[%s]' % sComponet)
        lstInfo.append('装置:%s' % GetDeviceInfo(oGame, oDevice))
    if oHero.m_PetCon:
        oCurPet = oHero.m_PetCon.GetCurPet()
        if oCurPet:
            sPetInfo = GetPetInfo(oGame, oCurPet)
            if sPetInfo:
                lstInfo.append('妖灵:%s' % sPetInfo)
    lstAIHero = oGame.m_WarMgr.GetAllAIHero()
    sAIInfo = '' if lstAIHero else '无'
    for iAIHero in lstAIHero:
        oAIHero = oGame.GetObject(iAIHero)
        if not oAIHero:
            continue
        oCurrentBT = oAIHero.m_Agent.PYGetCurrentBT() if oAIHero.m_Agent else None
        sTreeInfo = oCurrentBT.GetPathName() if oCurrentBT else 'None'
        iLockTarget = oAIHero.m_Agent.GetData('LockTarget', 0) if oAIHero.m_Agent else 0
        sAIInfo += '\n%s:场景%s 坐标%s 树%s 仇恨目标%s' % (oAIHero.m_PlayerID, oAIHero.m_Scene, OutputPos(oAIHero.GetPos()), sTreeInfo, iLockTarget)
    
    lstInfo.append('队友AI:%s' % sAIInfo)
    sArea = '区域路线'
    sMonster = '怪物:'
    lstGoalPos = []
    iScene = oHero.m_Scene
    oScene = oGame.m_SceneMgr.GetScene(iScene)
    iLevel = oScene.m_Level if oScene else 0
    lstGroupLive = set()
    oLevelCtrl = oGame.m_WarMgr.GetComponent('LevelCtrl')
    if oScene:
        oLevelNode = oLevelCtrl.GetLevelNode(iLevel)
        iMonsterNum = 0
        for lstLine in oLevelNode.m_RoomList:
            sArea += ' | '
            sArea += '.'.join([ oLine.m_Name for oLine in lstLine ])
            for oLine in lstLine:
                if oLine.IsGoal():
                    continue
                lstLive = []
                lstWait = []
                for iGroup, dGroup in oLine.m_MonsterCtrl.m_GroupInfo.items():
                    iWait = len(dGroup['Wait'])
                    if iWait:
                        lstWait.append('%d_%d' % (iGroup, iWait))
                    for iMonster in dGroup['Live']:
                        iMonsterNum += 1
                        (sMonsterInfo, _) = GetMonsterInfo(oGame, iMonster)
                        lstLive.append('%d_' % iGroup + sMonsterInfo)
                        lstGroupLive.add(iMonster)
                        if iMonsterNum % 10 == 0:
                            iMonsterNum = 0
                            lstLive.append('\n')
                    
                
                if not lstWait:
                    if lstLive:
                        sMonster += '%s:' % oLine.m_Name
                        if lstWait:
                            sMonster += '未刷新:(%s)' % '|'.join(lstWait)
                        if lstLive:
                            sMonster += ' 存活:(%s)' % '|'.join(lstLive)
                            continue
                        continue
            
        
        sArea += ' | '
        oMiniMap = oLevelCtrl.m_LevelMiniMap.GetMiniMap(iLevel)
        if oMiniMap and oHero.m_PlayerID in oMiniMap.m_GoalPos:
            dGoalPos = oMiniMap.m_GoalPos[oHero.m_PlayerID]
            for oPos in dGoalPos.values():
                lstGoalPos.append('目标点%d Pos:%s, Mode:%d' % (oPos.m_ID, oPos.m_Pos, oPos.m_ShowMode))
            
        lstMonster = oScene.GetObjectsByType('Monster')
        lstMonsterSID = []
        lstOtherLive = []
        iMonsterSub = 0
        for iMonsterID in lstMonster:
            oTarget = oGame.GetObject(iMonsterID)
            if not oTarget or oTarget.IsDead():
                continue
            if iMonsterID not in lstGroupLive:
                iMonsterSub += 1
                (sMonsterInfo, iExtra) = GetMonsterInfo(oGame, iMonsterID)
                lstOtherLive.append(sMonsterInfo)
                if iExtra or iMonsterSub % 10 == 0:
                    iMonsterSub = 0
                    lstOtherLive.append('\n')
            lstMonsterSID.append(str(oTarget.m_SID))
        
        if lstOtherLive:
            sMonster += ' 其他存活:(%s)' % '|'.join(lstOtherLive)
        if lstMonsterSID:
            sMonster += ' 场景存在怪物:(%s)' % '|'.join(lstMonsterSID)
    oSurvivorElement = oGame.m_WarMgr.GetSurvivorElement()
    if oSurvivorElement:
        sModule = ''
        lstAnimalModule = oHero.Query('AnimaModule', [])
        for iMoudle, _, _, _ in lstAnimalModule:
            oPerform = oHero.m_Perform.GetPerform(iMoudle)
            if oPerform:
                sModule += '%s(%d), ' % (oPerform.m_Name, iMoudle)
        
        lstInfo.append('模块:[%s]' % sModule)
        sSurvivor = '幸存者阶段 %d' % oSurvivorElement.m_Phase
        iNew = oSurvivorElement.m_CallFlag == 'NewSurvivorElement'
        if iNew:
            dMonsterSpawnInfo = oSurvivorElement.m_CurLine.m_MonsterCtrl.m_SpecialMonster if oSurvivorElement.m_CurLine else { }
            sSurvivor += '当前刷怪区域%s 怪物数据%s' % (oSurvivorElement.m_CurSpawn, dMonsterSpawnInfo)
        else:
            oSurvivorUpgradeMgr = oSurvivorElement.m_UpgradeMgr
            if oHero.m_ID in oSurvivorUpgradeMgr.m_HeroUpgradeInfo:
                (_, iGrade, _, _, _, _) = oSurvivorUpgradeMgr.m_HeroUpgradeInfo[oHero.m_ID]
                sSurvivor += ' 等级%d' % iGrade
        lstInfo.append(sSurvivor)
    oEndlessElement = oGame.m_WarMgr.GetEndlessElement()
    if oEndlessElement:
        lstInfo.append('幕数%d 无尽关数%d' % (oLevelCtrl.m_LayerNum, oEndlessElement.m_CurLevelNum))
    sGoalPos = '目标点:%s' % '|'.join(lstGoalPos)
    iMap = oScene.SID() if oScene else 0
    vPos = oHero.GetPos()
    vFace = cl_math.Vec3MulF(oHero.GetFacing(), 100)
    lstInfo.append('所在关卡%d 地图%d %s 坐标%s 面向%s 当前帧数%s 赛季 %s' % (iLevel, iMap, sArea, OutputPos(vPos), OutputPos(vFace), oGame.GetFrameNum(), oGame.m_WarMgr.m_SeasonNum))
    lstInfo.append(sMonster)
    lstInfo.append(sGoalPos)
    lstInfo.append('玩家ID:%d, 所在服务器:%d, GameID:%d, WarNo:%d, Round:%d, Cycle:%d, ModeType:%s' % (oHero.m_PlayerID, GetServerIndex(), oGame.m_ID, oGame.m_WarMgr.m_SID, oGame.m_WarMgr.m_Round, oGame.m_WarMgr.m_Cycle, oGame.m_WarMgr.m_ModeType))
    return '\n'.join(reversed(lstInfo))


def GetTaskInfo(oHero):
    sTaskInfo = ''
    for oTask in oHero.m_TaskCon.m_Task.values():
        dStats = { }
        dStats.update(oTask.m_TargetStats)
        dStats.update(oTask.m_CurStats)
        dStats.update(oTask.m_LimitStats)
        sTaskInfo += '(SID: %d, 状态:%d, 进度:%s, 技能:%s), ' % (oTask.m_SID, oTask.m_Status, dStats, list(oTask.m_Perform))
    
    return sTaskInfo


def FlowDebug(oGame, pid, iMsg, iTotalNumber, iCurNumber, sMsg, sFunction):
    netData = {
        'oGame': oGame,
        'pid': pid,
        'iMsg': iMsg,
        'iTotalNumber': iTotalNumber,
        'iCurNumber': iCurNumber,
        'sMsg': sMsg,
        'sFunction': sFunction }
    cl_duonet.dn_cl_gamedebug.DN_GS2CFlowDebug(netData)


def C2GSFlowDebug(oHero, pid, iMsg):
    oTextSender = oHero.m_Game.m_TextSender
    oTextSender.PopMsg(oHero.m_ID, iMsg, '')


def C2GSReceiveSeed(oHero, sSeed):
    if not cllib.lib_flag.g_IsAuthorityRun:
        return None
    import cl_gamegm
    
    try:
        dBuildInfo = marshal.loads(zlib.decompress(sSeed))
    except:
        cl_notify.GS2CMessage(oHero, '种子错误,请检查')
        return None

    cl_gamegm.copyseed(oHero, dBuildInfo)


class CHugeTextSender(object):
    m_Split = 2000
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_NewID = 0
        self.m_Msg = { }

    
    def Release(self):
        self.m_Game = None

    
    def NewMsgID(self):
        iMsg = self.m_NewID
        self.m_NewID += 1
        return iMsg

    
    def PushMsg(self, pid, sMsg, sFunction):
        iMsg = self.NewMsgID()
        iMax = len(sMsg) // self.m_Split
        if len(sMsg) % self.m_Split:
            iMax += 1
        lstMsg = []
        for i in range(1, iMax + 1):
            iPre = self.m_Split * (i - 1)
            iAft = self.m_Split * i
            lstMsg.append(sMsg[iPre:iAft])
        
        dRecord = self.m_Msg.setdefault(pid, { })
        dRecord[iMsg] = {
            'msg': lstMsg,
            'cur': 0,
            'max': iMax - 1,
            'pid': pid,
            'pend': False }
        if self.m_Msg:
            self.LoopMsg(sFunction)

    
    def PopMsg(self, pid, iMsg, sFunction):
        if pid not in self.m_Msg:
            return None
        if iMsg not in self.m_Msg[pid]:
            return None
        dRecord = self.m_Msg[pid][iMsg]
        dRecord['pend'] = False
        if dRecord['cur'] >= dRecord['max']:
            self.m_Msg[pid].pop(iMsg)
            Master = self.m_Game.GetObject(pid)
            cl_notify.GS2CMessage(Master, '导出信息结束')
        if not self.m_Msg[pid]:
            self.m_Msg.pop(pid)
        dRecord['cur'] += 1
        self.LoopMsg(sFunction)

    
    def LoopMsg(self, sFunction):
        for pid, dMsg in self.m_Msg.items():
            for iMsg, dRecord in dMsg.items():
                if dRecord['pend']:
                    continue
                dRecord['pend'] = True
                iCur = dRecord['cur']
                sSplit = dRecord['msg'][iCur]
                FlowDebug(self.m_Game, pid, iMsg, dRecord['max'], iCur, sSplit, sFunction)
                return None
            
        



def C2GSSkillDebugStart(who):
    if cllib.lib_flag.g_IsLogicLayer:
        return None
    import cl_perform.skilldebug
    import server
    if not server.IsInternalNetServer():
        return None
    cl_perform.skilldebug.R_StartSkillDebug(None, who.m_PlayerID)


def C2GSSkillDebug(who, iSkill):
    if cllib.lib_flag.g_IsLogicLayer:
        return None
    who.m_EditorCallBack = Functor(CallBackSkillDebugData, iSkill)


def CallBackSkillDebugData(iSkill, who, sContent):
    import cl_perform.skilldebug
    import mkparser.macro_defines
    oMacro = mkparser.macro_defines.CMacroImport()
    lstDefines = re.findall('@(\\S+)@', sContent)
    for sDefines in lstDefines:
        oMacro.AddMacro(sDefines)
        sContent = sContent.replace('@%s@' % sDefines, sDefines)
    
    if not sContent:
        SkillLog.Alert(f'''pid:{who.m_PlayerID} skill:{iSkill} debugdata empty''')
        return None
    sContent = oMacro.MacroImportText() + sContent
    cl_perform.skilldebug.R_SkillDebugData(None, who.m_PlayerID, iSkill, sContent)


def C2GSTextOP(oGame, who):
    if cllib.lib_flag.g_IsLogicLayer:
        return None
    iSub = UnpackInt(1)
    if iSub == 1:
        who.m_TextBuffer = ''
    elif iSub == 2 or hasattr(who, 'm_TextBuffer'):
        if cllib.lib_flag.g_IsInternalRun or len(who.m_TextBuffer) < 8000:
            iLen = UnpackInt(1)
            sStr = UnpackString(iLen)
            who.m_TextBuffer += sStr
        elif iSub == 3:
            sText = who.m_TextBuffer
            del who.m_TextBuffer
            if not hasattr(who, 'm_EditorCallBack'):
                return None
            func = who.m_EditorCallBack
            func(who, sText)
            del who.m_EditorCallBack


def C2GSSplitPackage(oGame, who):
    import cl_net
    iType = UnpackInt(1)
    dPacketData = who.m_SplitPacket
    if iType == 0:
        icmd = UnpackInt(1)
        dPacketData['Cmd'] = icmd
        dPacketData['Buffer'] = bytearray()
    if 'Buffer' not in dPacketData:
        return None
    iSize = UnpackInt(1)
    if iSize:
        sData = UnpackBinaryString(iSize)
        dPacketData['Buffer'].extend(sData)
    if iType == 2:
        who.m_SplitPacket = { }
        iCmd = dPacketData['Cmd']
        SetPacketDataForUnpack(bytes(dPacketData['Buffer']))
        
        try:
            cl_net.OnProcessFightCommand(oGame, who, iCmd)
        except:
            PythonError()


