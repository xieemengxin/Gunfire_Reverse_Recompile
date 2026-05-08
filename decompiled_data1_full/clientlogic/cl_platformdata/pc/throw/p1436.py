# Path: /Users/caoguangpei/个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/throw/p1436.pyc
# RelativePath: clientlogic/cl_platformdata/pc/throw/p1436.pyc
# Source Generated with Decompyle++
# File: p1436.pyc (Python 3.6)

import cl_math
import cl_msgcenter
import cl_action
import cl_condition
import cl_evact
import cl_evcon
import cl_object
from cl_commondefines import DAM_TYPE_PERFORM, DAM_USE_HP
from cl_only import PY_FLAG_DEAD
from cl_object.logging import GardenerLog
from cl_perform.cartoon.defines import DirectPosCartoon, ThrowByPowerCartoon, TimerCartoon
from cl_commondefines import ATT_SHAPE_SPHERE, CRT_CHECK_SERVER, CRT_EXTCHECK_NONE, GARDENER_THROW_DAMAGE, HIT_OVER_GROUND, HIT_OVER_NORMAL, OBJ_ENEMY, SKILLCACHE_INT, SKILLCACHE_LSTINT, SKILLCACHE_LSTPOS, WARRIOR_MONSTER

class CCartoon29(ThrowByPowerCartoon):
    m_SID = 29
    
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
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 0 or cl_action.CheckClientCtrl(skill):
            cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTPOS)
            cl_action.CreateSeedByPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[0] if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)) == 1 else cl_action.GetEndPositionInCrt(skill, 29), 0, 1)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 5 or cl_action.CrtArgRandomNum(skill, 0, 100) <= 15:
            cl_action.CreateRandomNumWarriorAtPointPos(skill, [
                cl_action.GetEndPositionInCrt(skill, 29)], WARRIOR_MONSTER, {
                cl_action.GetThrowCreateMonsterSID(skill, cl_action.GetSkillVarCache(skill, 'ThrowParam')[3]): 1 }, { }, cl_math.Vec3Minus(cl_action.CrtArgSelfPos(skill), cl_action.GetEndPositionInCrt(skill, 29)))
            if len(cl_action.GetSkillSummonCreate(skill)) == 1:
                cl_action.TargetAddState(skill, 33869, 1000, 0, { }, cl_action.GetSkillSummonCreate(skill)[0])
            elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 6:
                cl_action.CreatePlantByPos(skill, cl_action.GetEndPositionInCrt(skill, 29), 0, (0, 0, 0), 0, cl_action.GetSkillCustomData(skill, 'PlantPhase', defaultValue = 1), 1)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold')) if cl_action.CheckClientCtrl(skill) else cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0.1, 0.7))):
                return None
            cls.EnableShow(skill, 0.5, (0, cl_action.GetSkillVarCache(skill, 'ThrowParam')[1] * 1 / 100, 0), (cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100, cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100), skill.m_Cache['ExplodeDelay'], False, False, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_GROUND, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)
        elif cl_action.CheckClientCtrl(skill):
            pass
        
        skill(cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold')), cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0.1, 0.7)), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold')) if cl_action.CheckClientCtrl(skill) else cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0.1, 0.7)), cl_action.GetSceneCenterPosition(skill, cartoon), (3, 0, 0), baseHorizontal = False), cl_action.GetSkillVarCache(skill, 'ThrowParam')[0] * 1 / 100, 0.5, (0, cl_action.GetSkillVarCache(skill, 'ThrowParam')[1] * 1 / 100, 0), (cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100, cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100), skill.m_Cache['ExplodeDelay'], False, False, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_GROUND, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False, iTriggerBullet = 0, ignoreShield = False, checkWeaknessAngle = 0, checkWeaknessDis = 0, canPierceWeakness = False, hitFallAcc = 100, verticalThreshold = 0.4)

    InitSuccess = classmethod(InitSuccess)


class CCartoon2(DirectPosCartoon):
    m_SID = 2
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'BoomPos', cl_action.GetStartPositionInCrt(skill, 2))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'VID': cl_action.GetCurVID(skill),
            'GardenThrowHit': 1 }, sSubMsgKey = '')
        if cl_action.CheckClientCtrl(skill):
            cl_action.AddParasiticState(skill, cl_action.GetCurVID(skill), skill.m_Cache['DamInterval'] + cl_action.GetSkillCustomData(skill, 'ExtraAddParasiticCount', defaultValue = 0))
            cl_action.ParasiticDamage(skill, cl_action.GetCurVID(skill), cl_action.GetPerformArgValue(skill, 'ParasiticMul', iDefault = 2), cl_action.GetTransDamFactor(skill), 0)
        else:
            cl_action.PerformDamage(skill, {
                'Att': 100 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon3(DirectPosCartoon):
    m_SID = 3
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'BoomPos', cl_action.GetStartPositionInCrt(skill, 3))

    Active = classmethod(Active)
    
    def End(cls, skill):
        if cl_action.GetSkillCustomData(skill, 'CanReward', defaultValue = 0) == 1:
            cl_action.CustomPerformAction(skill, 1436, 'KillJar', {
                'BoomPos': cl_action.GetSkillVarCache(skill, 'BoomPos') })

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'VID': cl_action.GetCurVID(skill),
            'GardenThrowHit': 1 }, sSubMsgKey = '')
        if cl_action.CheckClientCtrl(skill):
            cl_action.AddParasiticState(skill, cl_action.GetCurVID(skill), skill.m_Cache['DamInterval'] + cl_action.GetSkillCustomData(skill, 'ExtraAddParasiticCount', defaultValue = 0))
            cl_action.ParasiticDamage(skill, cl_action.GetCurVID(skill), cl_action.GetPerformArgValue(skill, 'ParasiticMul', iDefault = 2), cl_action.GetTransDamFactor(skill), 0)
        else:
            cl_action.PerformDamage(skill, {
                'Att': 100 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon9(DirectPosCartoon):
    m_SID = 9
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'VID': cl_action.GetCurVID(skill),
            'GardenThrowHit': 1 }, sSubMsgKey = '')
        if cl_action.CheckClientCtrl(skill):
            cl_action.AddParasiticState(skill, cl_action.GetCurVID(skill), skill.m_Cache['DamInterval'] + cl_action.GetSkillCustomData(skill, 'ExtraAddParasiticCount', defaultValue = 0))
            cl_action.ParasiticDamage(skill, cl_action.GetCurVID(skill), cl_action.GetPerformArgValue(skill, 'ParasiticMul', iDefault = 2), cl_action.GetTransDamFactor(skill), 0)
        else:
            cl_action.PerformDamage(skill, {
                'Att': 100 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                cl_action.GetThrowBoomRadiusByShape(skill, cl_action.GetSkillVarCache(skill, 'ThrowParam')[3], skill.m_Cache['Radius'])], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgWarriorPos(skill, cl_action.GetCurVID(skill)), (0, 0, 0), [
                cl_action.GetThrowBoomRadiusByShape(skill, cl_action.GetSkillVarCache(skill, 'ThrowParam')[3], skill.m_Cache['Radius'])], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon6(DirectPosCartoon):
    m_SID = 6
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        if cl_action.CheckClientCtrl(skill):
            cl_action.AddParasiticState(skill, cl_action.GetCurVID(skill), skill.m_Cache['DamInterval'] + cl_action.GetSkillCustomData(skill, 'ExtraAddParasiticCount', defaultValue = 0))
            cl_action.ParasiticDamage(skill, cl_action.GetCurVID(skill), cl_action.GetPerformArgValue(skill, 'ParasiticMul', iDefault = 2), cl_action.GetTransDamFactor(skill), 0)
        else:
            cl_action.PerformDamage(skill, {
                'Att': 100 })
        if cl_action.GetSkillVarCache(skill, 'ThrowParam')[4] == 1 and cl_action.GetSkillVarCache(skill, 'ExtraBoomNum') < 3:
            cl_action.AddSkillVarCache(skill, 'ExtraBoomNum', 1)
            if cl_action.GetSkillVarCache(skill, 'ThrowParam')[3] == cl_action.GetTargetShape(skill, cl_action.GetCurVID(skill)):
                cartoon = { }
                CCartoon9.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                cl_action.GetThrowBoomRadiusByShape(skill, cl_action.GetSkillVarCache(skill, 'ThrowParam')[3], skill.m_Cache['Radius'])], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), (0, 0, 0), [
                cl_action.GetThrowBoomRadiusByShape(skill, cl_action.GetSkillVarCache(skill, 'ThrowParam')[3], skill.m_Cache['Radius'])], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon20(DirectPosCartoon):
    m_SID = 20
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'VID': cl_action.GetCurVID(skill),
            'GardenThrowHit': 1 }, sSubMsgKey = '')
        if cl_action.CheckClientCtrl(skill):
            cl_action.AddParasiticState(skill, cl_action.GetCurVID(skill), skill.m_Cache['DamInterval'] + cl_action.GetSkillCustomData(skill, 'ExtraAddParasiticCount', defaultValue = 0))
            cl_action.ParasiticDamage(skill, cl_action.GetCurVID(skill), cl_action.GetPerformArgValue(skill, 'ParasiticMul', iDefault = 2), cl_action.GetTransDamFactor(skill), 0)
        else:
            cl_action.PerformDamage(skill, {
                'Att': 100 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.GetEndPositionInCrt(skill, 14), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = True, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_action.GetEndPositionInCrt(skill, 14), (0, 0, 0), [
                4], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = True, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon14(ThrowByPowerCartoon):
    m_SID = 14
    
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
        CCartoon20.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), (0, 0.3, 0))):
                return None
            cls.EnableShow(skill, 0.1, (0, cl_action.GetSkillVarCache(skill, 'ThrowParam')[1] * 1 / 100, 0), (cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100, cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100), 180, False, False, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 4, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)
        else:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), (0, 0.3, 0)), cl_action.GetSkillVarCache(skill, 'ThrowDir'), cl_action.GetSkillVarCache(skill, 'ThrowParam')[0] * 1 / 100, 0.1, (0, cl_action.GetSkillVarCache(skill, 'ThrowParam')[1] * 1 / 100, 0), (cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100, cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100), 180, False, False, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 4, ignorePetrochemical = False, iTriggerBullet = 0, ignoreShield = False, checkWeaknessAngle = 0, checkWeaknessDis = 0, canPierceWeakness = False, hitFallAcc = 50, verticalThreshold = 0.4)

    InitSuccess = classmethod(InitSuccess)


class CCartoon11(DirectPosCartoon):
    m_SID = 11
    
    def Active(cls, skill):
        pass

    Active = classmethod(Active)
    
    def End(cls, skill):
        for i1 in range(0, 5, 1):
            cl_action.SetSkillVarCache(skill, 'ThrowDir', cl_action.CrtArgGetCustomDir(skill, cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), cl_action.GetSkillVarCache(skill, 'PosOnCirle')[i1], (0, i1 * 360, 0), baseHorizontal = False))
            cartoon = { }
            CCartoon14.Init(skill, cartoon, casting = 0, index = 0)
        

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'VID': cl_action.GetCurVID(skill),
            'GardenThrowHit': 1 }, sSubMsgKey = '')
        if cl_action.CheckClientCtrl(skill):
            cl_action.AddParasiticState(skill, cl_action.GetCurVID(skill), skill.m_Cache['DamInterval'] + cl_action.GetSkillCustomData(skill, 'ExtraAddParasiticCount', defaultValue = 0))
            cl_action.ParasiticDamage(skill, cl_action.GetCurVID(skill), cl_action.GetPerformArgValue(skill, 'ParasiticMul', iDefault = 2), cl_action.GetTransDamFactor(skill), 0)
        else:
            cl_action.PerformDamage(skill, {
                'Att': 100 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), (0, 0.1, 0)), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), (0, 0.1, 0)), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon5(ThrowByPowerCartoon):
    m_SID = 5
    
    def Active(cls, skill):
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 0:
            cartoon = { }
            CCartoon29.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 5:
            cartoon = { }
            CCartoon29.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 6:
            cartoon = { }
            CCartoon29.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        cl_action.SetSkillServerCache(skill, 'EndPos', cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 5), (0, 0.1, 0)))
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'GardenThrowDes': 1 }, sSubMsgKey = '')

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SetSkillVarCache(skill, 'ThrowEndPos', cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 5), (0, 0.1, 0)))
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 0:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 2:
            cl_action.SetThrowElementTypeByShape(skill, cl_action.GetSkillVarCache(skill, 'ThrowParam')[3])
            cl_action.SetSkillVarCache(skill, 'ExtraBoomNum', 0)
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 3:
            cl_action.CustomPerformAction(skill, 1436, 'KillJar', {
                'BoomPos': cl_action.GetSkillVarCache(skill, 'ThrowEndPos') })
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 4:
            cl_action.SetSkillVarCache(skill, 'PosOnCirle', cl_action.CreatePosOnCircle(skill, cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), skill.m_Cache['Radius'], 5))
            cartoon = { }
            CCartoon11.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 5:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 6:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cl_action.SetSkillVarCache(skill, 'ThrowEndPos', cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 5), (0, 0.1, 0)))
        if cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 0:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 1:
            cartoon = { }
            CCartoon3.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 2:
            cl_action.SetThrowElementTypeByShape(skill, cl_action.GetSkillVarCache(skill, 'ThrowParam')[3])
            cl_action.SetSkillVarCache(skill, 'ExtraBoomNum', 0)
            cartoon = { }
            CCartoon6.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 3:
            cl_action.CustomPerformAction(skill, 1436, 'KillJar', {
                'BoomPos': cl_action.GetSkillVarCache(skill, 'ThrowEndPos') })
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 4:
            cl_action.SetSkillVarCache(skill, 'PosOnCirle', cl_action.CreatePosOnCircle(skill, cl_action.GetSkillVarCache(skill, 'ThrowEndPos'), skill.m_Cache['Radius'], 5))
            cartoon = { }
            CCartoon11.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 5:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)
        elif cl_action.GetSkillCacheData(skill, SKILLCACHE_INT) == 6:
            cartoon = { }
            CCartoon2.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold')) if cl_action.CheckClientCtrl(skill) else cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0.1, 0.7))):
                return None
            cls.EnableShow(skill, 0.5, (0, cl_action.GetSkillVarCache(skill, 'ThrowParam')[1] * 1 / 100, 0), (cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100, cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100), skill.m_Cache['ExplodeDelay'], True, True, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)
        elif cl_action.CheckClientCtrl(skill):
            pass
        
        skill(cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold')), cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0.1, 0.7)), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold')) if cl_action.CheckClientCtrl(skill) else cl_action.VectorShiftForAttDir(skill, cl_action.GetCameraCenterPosition(skill, cartoon), (0, 0.1, 0.7)), cl_action.GetSceneCenterPosition(skill, cartoon), (3, 0, 0), baseHorizontal = False), cl_action.GetSkillVarCache(skill, 'ThrowParam')[0] * 1 / 100, 0.5, (0, cl_action.GetSkillVarCache(skill, 'ThrowParam')[1] * 1 / 100, 0), (cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100, cl_action.GetSkillVarCache(skill, 'ThrowParam')[2] * 1 / 100), skill.m_Cache['ExplodeDelay'], True, True, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False, iTriggerBullet = 0, ignoreShield = False, checkWeaknessAngle = 0, checkWeaknessDis = 0, canPierceWeakness = False, hitFallAcc = 50, verticalThreshold = 0.4)

    InitSuccess = classmethod(InitSuccess)


class CCartoon8(ThrowByPowerCartoon):
    m_SID = 8
    
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
        cl_action.AddSkillCacheData(skill, SKILLCACHE_LSTPOS)
        if cl_action.CheckClientCtrl(skill):
            cl_action.CreateSeedByPos(skill, cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)[0] if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTPOS)) == 1 else cl_action.GetEndPositionInCrt(skill, 8), 0, 1)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold'))):
                return None
            cls.EnableShow(skill, 0.1, (0, [
                6000,
                0,
                30][1] * 1 / 100, 0), ([
                6000,
                0,
                30][2] * 1 / 100, [
                6000,
                0,
                30][2] * 1 / 100), skill.m_Cache['ExplodeDelay'], False, False, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_GROUND, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold')), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold')), cl_action.GetSceneCenterPosition(skill, cartoon), (3, 0, 0), baseHorizontal = False), [
                6000,
                0,
                30][0] * 1 / 100, 0.1, (0, [
                6000,
                0,
                30][1] * 1 / 100, 0), ([
                6000,
                0,
                30][2] * 1 / 100, [
                6000,
                0,
                30][2] * 1 / 100), skill.m_Cache['ExplodeDelay'], False, False, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_GROUND, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False, iTriggerBullet = 0, ignoreShield = False, checkWeaknessAngle = 0, checkWeaknessDis = 0, canPierceWeakness = False, hitFallAcc = 50, verticalThreshold = 0.4)

    InitSuccess = classmethod(InitSuccess)


class CCartoon7(DirectPosCartoon):
    m_SID = 7
    
    def Active(cls, skill):
        cl_action.SetSkillVarCache(skill, 'BoomPos', cl_action.GetStartPositionInCrt(skill, 7))

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cl_action.SendCurCartoonTriggerMsg(skill, dInfo = {
            'VID': cl_action.GetCurVID(skill),
            'GardenThrowHit': 1 }, sSubMsgKey = '')
        if cl_action.CheckClientCtrl(skill):
            cl_action.AddParasiticState(skill, cl_action.GetCurVID(skill), skill.m_Cache['DamInterval'] + cl_action.GetSkillCustomData(skill, 'ExtraAddParasiticCount', defaultValue = 0))
            cl_action.ParasiticDamage(skill, cl_action.GetCurVID(skill), cl_action.GetPerformArgValue(skill, 'ParasiticMul', iDefault = 2), cl_action.GetTransDamFactor(skill), 0)
        else:
            cl_action.PerformDamage(skill, {
                'Att': 100 })

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        pass

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 4), (0, 0.1, 0)), end = (0, 0, 0)):
                return None
            cls.EnableShow(skill, [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, multipleExplode = False, explosionDelay = 10)
        else:
            cls.EnableCtrl(skill, cl_math.Vec3Add(cl_action.GetEndPositionInCrt(skill, 4), (0, 0.1, 0)), (0, 0, 0), [
                skill.m_Cache['Radius']], attshape = ATT_SHAPE_SPHERE, targettype = OBJ_ENEMY, pierceStatic = False, explosion = False, extCheck = CRT_EXTCHECK_NONE, multipleExplode = False, explosionDelay = 10)

    InitSuccess = classmethod(InitSuccess)


class CCartoon4(ThrowByPowerCartoon):
    m_SID = 4
    
    def Active(cls, skill):
        cartoon = { }
        CCartoon8.Init(skill, cartoon, casting = 0, index = 0)

    Active = classmethod(Active)
    
    def End(cls, skill):
        pass

    End = classmethod(End)
    
    def Hit(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

    Hit = classmethod(Hit)
    
    def HitStatic(cls, skill):
        cartoon = { }
        CCartoon7.Init(skill, cartoon, casting = 0, index = 0)

    HitStatic = classmethod(HitStatic)
    
    def Trigger(cls, skill):
        pass

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            if not cls.EnableCheck(skill, start = cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold'))):
                return None
            cls.EnableShow(skill, 0.1, (0, [
                6000,
                0,
                30][1] * 1 / 100, 0), ([
                6000,
                0,
                30][2] * 1 / 100, [
                6000,
                0,
                30][2] * 1 / 100), skill.m_Cache['ExplodeDelay'], True, True, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, iTriggerBullet = 0, checkWeaknessAngle = 0, checkWeaknessDis = 0)
        else:
            cls.EnableCtrl(skill, cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold')), cl_action.CrtArgGetCustomDir(skill, cl_action.CrtArgGetTransPos(skill, cl_action.CrtArgMuzzleTransform(skill, Name = '119_throw_hold')), cl_action.GetSceneCenterPosition(skill, cartoon), (3, 0, 0), baseHorizontal = False), [
                6000,
                0,
                30][0] * 1 / 100, 0.1, (0, [
                6000,
                0,
                30][1] * 1 / 100, 0), ([
                6000,
                0,
                30][2] * 1 / 100, [
                6000,
                0,
                30][2] * 1 / 100), skill.m_Cache['ExplodeDelay'], True, True, 0, innerRadius = 0, pierce = 0, ignoreMonster = False, hitUnitBounciness = (0, 0), targettype = OBJ_ENEMY, hitovertype = HIT_OVER_NORMAL, changeRadius = 0, maxRadius = 3, ignorePetrochemical = False, iTriggerBullet = 0, ignoreShield = False, checkWeaknessAngle = 0, checkWeaknessDis = 0, canPierceWeakness = False, hitFallAcc = 50, verticalThreshold = 0.4)

    InitSuccess = classmethod(InitSuccess)


class CCartoon0(TimerCartoon):
    m_SID = 0
    
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
        CCartoon4.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 5, skill.m_Cache['TriggerTimes'] - 1)
        else:
            cls.EnableCtrl(skill, 5, skill.m_Cache['TriggerTimes'] - 1)

    InitSuccess = classmethod(InitSuccess)


class CCartoon1(TimerCartoon):
    m_SID = 1
    
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
        cl_action.SetSkillVarCache(skill, 'ThrowParam', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT) if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) == 6 else [
            6000,
            0,
            30,
            0,
            0,
            0])
        cartoon = { }
        CCartoon5.Init(skill, cartoon, casting = 0, index = 0)
        if not 1 == skill.m_Cache['TriggerTimes']:
            cartoon = { }
            CCartoon0.Init(skill, cartoon, casting = 0, index = 0)

    Trigger = classmethod(Trigger)
    
    def InitSuccess(cls, skill, index, cartoon):
        if not skill.m_CheckType == CRT_CHECK_SERVER:
            cls.EnableShow(skill, 5, 1)
        else:
            cls.EnableCtrl(skill, 5, 1)

    InitSuccess = classmethod(InitSuccess)


def Action(skill):
    cl_action.SetSkillServerCache(skill, 'ExShowTips', [
        GARDENER_THROW_DAMAGE][0])
    cl_action.SetSkillCustomDataInt(skill, 'ThrowType', cl_action.GetSkillCacheData(skill, SKILLCACHE_INT))
    cl_action.SetSkillCustomDataInt(skill, 'AimTarget', cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)[5] if len(cl_action.GetSkillCacheData(skill, SKILLCACHE_LSTINT)) == 6 else 0)
    cl_action.SendUseThrowPFMsg(skill)
    cartoon = { }
    CCartoon1.Init(skill, cartoon, casting = 0, index = 0)


def Halt(skill):
    cl_action.CustomPerformAction(skill, 12031, 'RemoveAimJar', { })


def End(skill):
    cl_action.CustomPerformAction(skill, 12031, 'RemoveAimJar', { })


def GetSkillCacheIndex():
    return [
        SKILLCACHE_INT,
        SKILLCACHE_LSTINT,
        SKILLCACHE_LSTPOS]


def GetOtherMonster():
    return []

from cl_perform.throw import CPerform as CCustomPerform
from cl_commondefines import DAM_TYPE_CORRISION

class CPerform(CCustomPerform):
    m_SID = 1436
    m_Name = '森源法球'
    m_ExtPerform = (8019, 12031, 8015)
    m_HaltInfo = { }
    m_IgnoreHalt = { }
    m_ActionInfo = {
        1: Action }
    m_HaltActionInfo = {
        1: Halt }
    m_EndActionInfo = {
        1: End }
    m_ElementType = DAM_TYPE_CORRISION
    m_BaseAttrData = {
        'ColdTime': 50,
        'AttDistance': 0,
        'MaxCover': 1,
        'BulletSID': 4508,
        'Att': 15000,
        'CrazyEff': 0,
        'BulletSpeed': 80,
        'DebuffProb': 1500,
        'ExplodeDelay': 500,
        'Radius': 5,
        'BulletVerticalAcc': 0,
        'AddStateTime': 600,
        'KeepTime': 80,
        'DamInterval': 3,
        'Pierce': 0,
        'TriggerTimes': 1,
        'MinUseEnergy': 0,
        'CommonMaxCount': 20 }
    m_ForbidRule = 0
    m_CheckForbid = 0
    m_BaseArgData = {
        'ImmobilizeTime': 25,
        'ShiftDis': -5,
        'ExtraDamRatio': 0,
        'StateTriggerInterval': 0,
        'NotReduceRatio': 0,
        'Spread': 0,
        'ParasiticMul': 10000 }
    m_AIPerformDam = 2000


def KillJar(oSkill, dInfo, *arg):
    dCustom = oSkill.m_Custom
    if 'AimJar' not in dCustom:
        return None
    if 'BoomPos' not in dInfo:
        return None
    oAttack = oSkill.GetAttack()
    if not oAttack:
        return None
    oGame = oSkill.m_Game
    iJar = dCustom['AimJar']
    oAttack.m_GardenerCon.ClearAimJar(iJar)
    oJar = oGame.GetObject(iJar, PY_FLAG_DEAD)
    if oJar:
        oJar.Goto(oAttack.m_Scene, dInfo['BoomPos'])
    elif 'ExplodeJarInfo' not in dCustom:
        return None
    dExplodeJarInfo = dCustom['ExplodeJarInfo']
    if dExplodeJarInfo:
        dCreateInfo = {
            'Live': 0,
            'Perform': [],
            'Origin': dInfo['BoomPos'] }
        dCreateInfo.update(dExplodeJarInfo)
        oJar = oGame.m_ResMgr.CreateBuild(oAttack.m_Scene, dExplodeJarInfo['SID'], dCreateInfo)
    if not oJar:
        iShape = dCustom['Shape'] if 'Shape' in dCustom else 0
        dExplodeJarInfo = dCustom['dExplodeJarInfo'] if 'dExplodeJarInfo' in dCustom else { }
        GardenerLog.Alert('%s %s not jar %s %s' % (oGame.m_ID, oAttack.m_PlayerID, iShape, dExplodeJarInfo))
        return None
    oReason = cl_object.reason.CStrReason('Skill', None, {
        'DamType': DAM_TYPE_PERFORM | DAM_USE_HP })
    oJar.HPDirectModify('HP', oAttack.m_ID, -oJar.HP(), oReason)

