# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/clinterface/cllib/lib_cartoon.pyc
# RelativePath: clientlogic/clinterface/cllib/lib_cartoon.pyc
# Source Generated with Decompyle++
# File: lib_cartoon.pyc (Python 3.6)

import cllib.lib_flag
if cllib.lib_flag.g_IsLogicLayer:
    
    def CheckDataRayCast(oSkill, dCartoon):
        pass

    
    def CheckDataWinkPos(oSkill, dCartoon):
        pass

    
    def CheckDataAnnulus(oSkill, dCartoon):
        pass

    
    def CheckPosAround(oSkill, dCartoon):
        pass

    
    def CheckDataDiffuseRay(oSkill, dCartoon):
        pass

else:
    from cl_only import PY_FLAG_DEAD, GAME_FRAME_SECOND
    from cl_pxlayer import PXMASK_SKILLBLK, PXMASK_OBJECT, PXMASK_LIVEOBJ
    from cl_commondefines import WARRIOR_MONSTER, ATT_SHAPE_SECTOR
    from cl_perform.cartoon.argcheck import PosAroundCheck
    import cl_math
    import cl_modeldefine
    
    def CheckDataRayCast(oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Ray' not in dClient:
            return None
        oGame = oSkill.m_Game
        oAttack = oSkill.GetAttack()
        if oAttack and oAttack.m_NoRayCheck:
            return None
        lstRay = []
        vStart = dCartoon['Start']
        iHitFrame = dClient['Frame']
        fRadius = dCartoon['Radius'] if 'Radius' in dCartoon else 0
        for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
            if iVictim:
                if not ('PierceStatic' in dCartoon or dCartoon['PierceStatic']) and 'LockTarget' in dClient and iVictim in dClient['LockTarget']:
                    if fRadius:
                        vCheckEnd = cl_math.Vec3DisplacePos(dCartoon['Start'], dCartoon['End'], cl_math.CalDistance3D(vHitPos, dCartoon['Start']))
                    else:
                        vCheckEnd = vHitPos
                    r = oGame.Scene_RaycastSingle(oSkill.m_Base['Scene'], vStart, vCheckEnd, PXMASK_SKILLBLK)
                    if r[0] != -1:
                        vHitStaticPos = r[1]
                        lstCheck = oGame.Scene_RaycastMultiple(oSkill.m_Base['Scene'], vHitStaticPos, vStart, PXMASK_LIVEOBJ, {
                            'BlockMask': PXMASK_SKILLBLK,
                            'ExcludeFlag': PY_FLAG_DEAD })
                        for iCheck, _ in lstCheck:
                            if iVictim == iCheck:
                                break
                        
                oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
                if oVictim and not oVictim.IsNeglectAttack(oSkill) and not oVictim.SkillCheckHitPos(oSkill, iHitFrame, vHitPos):
                    oSkill.LogCheckErr('posfail %s %s %s %s %s %s' % (iVictim, oVictim.m_Shape, iHitFrame, vHitPos, oGame.GetFrameNum(), oVictim.GetPos()))
                    continue
                continue
            lstRay.append((vHitPos, vNormal, iVictim, iHitPart))
        
        dClient['Ray'] = lstRay

    
    def CheckDataWinkPos(oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID in oSkill.m_NetReceive:
            dClient = oSkill.m_NetReceive[iNodeID]
        else:
            return None
        if 'Ray' in dClient:
            lstRay = []
            oGame = oSkill.m_Game
            iHitFrame = dClient['Frame']
            oAttack = oSkill.GetAttack()
            fSpeed = dCartoon['Speed']
            vHero = cl_math.Vec3Add(oAttack.GetCenterPosition(), (0, 0.2, 0))
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                if iVictim:
                    oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
                    if not oVictim:
                        continue
                    fAdjust = 0.1
                    if oVictim.m_FightType & WARRIOR_MONSTER == WARRIOR_MONSTER:
                        fAdjust += 0.2
                    iMaxDelayFrame = 3
                    if 'DashShape' in dCartoon and dCartoon['DashShape'] == ATT_SHAPE_SECTOR:
                        fAdjust += dCartoon['EffArgs'][0]
                    fCheckDistance = fSpeed * GAME_FRAME_SECOND * iMaxDelayFrame + oAttack.m_ModelRadius + fAdjust
                    if not oVictim.IsNeglectAttack(oSkill):
                        if not oVictim.SkillCheckHitPos(oSkill, iHitFrame, vHitPos) or not cl_math.CheckDistance(vHero, vHitPos, fCheckDistance):
                            oSkill.LogCheckErr('winkpos posfail %s %s %s %s %s %s %s %s' % (iVictim, oVictim.m_Shape, iHitFrame, vHitPos, oGame.GetFrameNum(), oVictim.GetPos(), fCheckDistance, cl_math.CalDistance3D(vHero, vHitPos)))
                            continue
                        continue
                    ret = oGame.Scene_RaycastSingle(oAttack.m_Scene, vHero, vHitPos, PXMASK_SKILLBLK | PXMASK_OBJECT, {
                        'PassID': oAttack.m_ID,
                        'Normal': 1 })
                    if ret[0] == 0:
                        oSkill.LogCheckErr('winkpos raycast checkfail %s %s %s' % (vHero, vHitPos, ret))
                        continue
                    continue
                lstRay.append((vHitPos, vNormal, iVictim, iHitPart))
            
            dClient['Ray'] = lstRay

    
    def CheckDataAnnulus(oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID in oSkill.m_NetReceive:
            dClient = oSkill.m_NetReceive[iNodeID]
        lstRay = []
        oAttack = oSkill.GetAttack()
        if not oAttack:
            return None
        if 'Ray' in dClient:
            iHitFrame = dClient['Frame']
            for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
                oVictim = oSkill.m_Game.GetObject(iVictim, PY_FLAG_DEAD)
                if not oVictim:
                    continue
                if not oVictim.IsNeglectAttack(oSkill) and not oVictim.SkillCheckHitPos(oSkill, iHitFrame, vHitPos):
                    oSkill.LogCheckErr('posfail %s %s %s %s %s %s' % (iVictim, oVictim.m_Shape, iHitFrame, vHitPos, oSkill.m_Game.GetFrameNum(), oVictim.GetPos()))
                    continue
                oWeapon = oAttack.m_WieldCon.GetItemByID(oSkill.m_Base['Weapon'])
                fCurAnnulusRadius = oWeapon.Query('CurAnnulusRadius', dCartoon['CurAnnulusRadius'])
                vPos = oAttack.GetLastPos(iHitFrame)
                vPos = (vPos[0], vPos[1] + 1, vPos[2])
                fDistance = cl_math.CalDistance3D(vPos, vHitPos)
                tModelArgs = cl_modeldefine.GetModelDefine(oVictim.m_Shape, 'Physx')
                fCheckRadius = tModelArgs[0]
                fCheckDistance = 2 + fCheckRadius * 2 + oWeapon.m_ExtItemAttr['Weight']
                if fCheckDistance < abs(fCurAnnulusRadius - fDistance):
                    oSkill.LogCheckErr('annulusradiusposfail %s %s %s %s %s %s' % (iVictim, oVictim.m_Shape, iHitFrame, vHitPos, oSkill.m_Game.GetFrameNum(), oVictim.GetPos()))
                    continue
                lstRay.append((vHitPos, vNormal, iVictim, iHitPart))
            
        dClient['Ray'] = lstRay

    
    def CheckPosAround(oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Ray' not in dClient:
            return None
        if 'FollowID' in dCartoon:
            oAttack = oSkill.m_Game.GetObject(dCartoon['FollowID'])
        else:
            oAttack = oSkill.GetAttack()
        if oAttack and oAttack.m_NoRayCheck:
            return None
        lstRay = []
        iHitFrame = dClient['Frame']
        vLast = oAttack.GetLastPos(iHitFrame)
        (fRadius, fHeight) = oAttack.SkillCheckArgs
        for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
            if not PosAroundCheck(oSkill, vHitPos, vLast, fRadius * 2, fHeight):
                continue
            lstRay.append((vHitPos, vNormal, iVictim, iHitPart))
        
        dClient['Ray'] = lstRay

    
    def CheckDataDiffuseRay(oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Ray' not in dClient:
            return None
        oGame = oSkill.m_Game
        oAttack = oSkill.GetAttack()
        if oAttack and oAttack.m_NoRayCheck:
            return None
        lstRay = []
        vStart = dCartoon['Start']
        iHitFrame = dClient['Frame']
        iScene = oSkill.m_Base['Scene']
        for vHitPos, vNormal, iVictim, iHitPart in dClient['Ray']:
            if iVictim:
                oVictim = oGame.GetObject(iVictim, PY_FLAG_DEAD)
                if not oVictim:
                    continue
                if not ('PierceStatic' in dCartoon or dCartoon['PierceStatic']) and 'LockTarget' in dClient and iVictim in dClient['LockTarget']:
                    r = oGame.Scene_RaycastSingle(iScene, vStart, vHitPos, PXMASK_SKILLBLK)
                    if r[0] != -1:
                        for vPos in oVictim.GetKeyPoint():
                            r2 = oGame.Scene_RaycastSingle(iScene, vStart, vPos, PXMASK_SKILLBLK)
                            if r2[0] == -1:
                                break
                        else:
                            vHitStaticPos = r[1]
                            oSkill.LogCheckErr('diffuseraystaticfail %s %s %s' % (vStart, vHitPos, vHitStaticPos))
                if not oVictim.IsNeglectAttack(oSkill) and not oVictim.SkillCheckHitPos(oSkill, iHitFrame, vHitPos):
                    oSkill.LogCheckErr('diffuseposfail %s %s %s %s %s %s' % (iVictim, oVictim.m_Shape, iHitFrame, vHitPos, oGame.GetFrameNum(), oVictim.GetPos()))
                    continue
                lstRay.append((vHitPos, vNormal, iVictim, iHitPart))
        
        dClient['Ray'] = lstRay

