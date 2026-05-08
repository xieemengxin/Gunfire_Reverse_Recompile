# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_war.pyc
# RelativePath: clientlogic/cl_war.pyc
# Source Generated with Decompyle++
# File: cl_war.pyc (Python 3.6)

from cl_commondefines import SKILLRET_SUCCESS, SKILLRET_FAIL, PF_TYPE_FILLBULLET
from cl_commondefines import PF_TYPE_CONSHOOT, PF_TYPE_SHOOT, PF_TYPE_CHARGE, WARRIOR_HERO
from cl_only import Functor
import importlib
import importlib.util
import marshal
import os
import struct
import sys
import traceback
import types
import cl_test as cl_customconfig
CACHE_SLICE = 5
if '_LOADED_FLEXIBLE_MODS_ROOTS' not in globals():
    _LOADED_FLEXIBLE_MODS_ROOTS = set()
VALID_FLEXIBLE_PYC_MAGIC = (
    0x0A0D0D33,
    0x330D0DA0)


def _AppendFlexibleLog(sRoot, sMsg):
    if not sRoot:
        return None
    try:
        sLogPath = os.path.join(sRoot, 'mod_runtime.log')
        with open(sLogPath, 'a', encoding = 'utf-8', errors = 'ignore') as oFile:
            oFile.write(sMsg + '\n')
    except Exception:
        pass


def _IterFlexibleModRoots():
    setSeen = set()
    lstEnv = os.environ.get('GUNFIRE_FLEXIBLE_MODS', '')
    if lstEnv:
        for sPath in lstEnv.split(os.pathsep):
            if not sPath:
                continue
            sPath = os.path.abspath(sPath)
            if sPath in setSeen:
                continue
            setSeen.add(sPath)
            if os.path.isdir(sPath):
                yield sPath
    lstCandidate = [
        os.path.join(os.getcwd(), 'flexible_mods')]
    for sPath in list(sys.path):
        if not sPath:
            continue
        sAbsPath = os.path.abspath(sPath)
        if os.path.isfile(sAbsPath):
            lstCandidate.append(os.path.join(os.path.dirname(sAbsPath), 'flexible_mods'))
            continue
        lstCandidate.append(os.path.join(sAbsPath, 'flexible_mods'))
    for sPath in lstCandidate:
        sPath = os.path.abspath(sPath)
        if sPath in setSeen:
            continue
        setSeen.add(sPath)
        if os.path.isdir(sPath):
            yield sPath


def _LoadFlexibleRuntimeByFile(sRoot):
    sFlexmodsDir = os.path.join(sRoot, 'flexmods')
    sRuntimePycPath = os.path.join(sFlexmodsDir, 'runtime.pyc')
    sRuntimePyPath = os.path.join(sFlexmodsDir, 'runtime.py')
    if not os.path.isfile(sRuntimePycPath) and not os.path.isfile(sRuntimePyPath):
        return None
    sPkgName = 'flexmods'
    sModName = 'flexmods.runtime'
    if sPkgName not in sys.modules:
        oPkg = types.ModuleType(sPkgName)
        oPkg.__path__ = [sFlexmodsDir]
        oPkg.__package__ = sPkgName
        sys.modules[sPkgName] = oPkg
    sApiPycPath = os.path.join(sFlexmodsDir, 'api.pyc')
    if os.path.isfile(sApiPycPath) and 'flexmods.api' not in sys.modules:
        _LoadFlexibleModuleByFile('flexmods.api', sApiPycPath, 'flexmods')
    if os.path.isfile(sRuntimePycPath):
        return _LoadFlexibleModuleByFile(sModName, sRuntimePycPath, sPkgName)
    oSpec = importlib.util.spec_from_file_location(sModName, sRuntimePyPath)
    if not oSpec or not oSpec.loader:
        return None
    oMod = importlib.util.module_from_spec(oSpec)
    sys.modules[sModName] = oMod
    oSpec.loader.exec_module(oMod)
    return oMod


def _LoadFlexibleModuleByFile(sModName, sFilePath, sPackage = None):
    if sModName in sys.modules:
        return sys.modules[sModName]
    if sFilePath.endswith('.pyc'):
        with open(sFilePath, 'rb') as oFile:
            sData = oFile.read()
        if len(sData) < 16:
            raise ValueError('invalid pyc header: %s' % sFilePath)
        iMagic = struct.unpack('<I', sData[:4])[0]
        if iMagic not in VALID_FLEXIBLE_PYC_MAGIC:
            raise ValueError('unsupported flexible pyc magic %s: %s' % (hex(iMagic), sFilePath))
        oCode = None
        for iOffset in (16, 12, 8):
            if len(sData) <= iOffset:
                continue
            try:
                oCode = marshal.loads(sData[iOffset:])
            except Exception:
                continue
            if isinstance(oCode, type((lambda : None).__code__)):
                break
            oCode = None
        if oCode is None:
            raise ValueError('invalid pyc payload: %s' % sFilePath)
        oMod = types.ModuleType(sModName)
        oMod.__file__ = sFilePath
        if sPackage:
            oMod.__package__ = sPackage
        sys.modules[sModName] = oMod
        exec(oCode, oMod.__dict__)
        return oMod
    oSpec = importlib.util.spec_from_file_location(sModName, sFilePath)
    if not oSpec or not oSpec.loader:
        raise ImportError('cannot build spec for %s' % sFilePath)
    oMod = importlib.util.module_from_spec(oSpec)
    if sPackage:
        oMod.__package__ = sPackage
    sys.modules[sModName] = oMod
    oSpec.loader.exec_module(oMod)
    return oMod


def EnsureFlexibleMods():
    for sRoot in _IterFlexibleModRoots():
        if sRoot in _LOADED_FLEXIBLE_MODS_ROOTS:
            return None
        try:
            _AppendFlexibleLog(sRoot, '[FlexibleMods] try root: %s' % sRoot)
            if sRoot not in sys.path:
                sys.path.insert(0, sRoot)
            try:
                oRuntime = importlib.import_module('flexmods.runtime')
            except Exception:
                oRuntime = _LoadFlexibleRuntimeByFile(sRoot)
            if not oRuntime:
                _AppendFlexibleLog(sRoot, '[FlexibleMods] runtime not found')
                continue
            if hasattr(oRuntime, 'load_user_mods'):
                oRuntime.load_user_mods(sRoot)
                _LOADED_FLEXIBLE_MODS_ROOTS.add(sRoot)
                _AppendFlexibleLog(sRoot, '[FlexibleMods] loaded root ok')
                print('[FlexibleMods] loaded root:', sRoot)
                return None
        except Exception:
            _AppendFlexibleLog(sRoot, '[FlexibleMods] load failed')
            _AppendFlexibleLog(sRoot, traceback.format_exc())
            print('[FlexibleMods] load failed:', sRoot)
            traceback.print_exc()
    return None


def EnsureRuntimePatches():
    cl_customconfig.ApplyRuntimePatches()
    EnsureFlexibleMods()


def UsePerform(oAttack, pfobj, dData):
    iCanUse = pfobj.CanUse(oAttack, dData)
    if iCanUse == SKILLRET_SUCCESS:
        oSkill = oAttack.m_Game.m_SkillMgr.NewSkill(oAttack, pfobj, dData)
        if oSkill:
            if 'BulletChange' in dData:
                TriggerBulletChange(oAttack, oSkill, dData['BulletChange'])
            oSkill.Start(oAttack, pfobj)
        else:
            iCanUse = SKILLRET_FAIL
    if iCanUse == SKILLRET_FAIL:
        TryFallBackBullet(oAttack, dData.get('Weapon', 0), pfobj)
    return iCanUse


def UseOnlyServerPerform(oAttack, pfobj, dData):
    oSkill = oAttack.m_Game.m_SkillMgr.NewSkill(oAttack, pfobj, dData)
    oSkill.StartOnlyServer(oAttack, pfobj)


def UseCachePerform(oAttack, iPerform, dData, lstTriggerCache):
    iWeapon = dData['Weapon'] if 'Weapon' in dData else 0
    pfobj = oAttack.GetPerform(iPerform, iWeapon)
    if not pfobj:
        return SKILLRET_FAIL
    iRet = UsePerform(oAttack, pfobj, dData)
    if iRet == SKILLRET_SUCCESS and lstTriggerCache:
        TriggerCache(oAttack, dData['ActNum'], lstTriggerCache, 0, len(lstTriggerCache))
    return iRet


def TriggerCache(oAttack, iActNum, lstTriggerCache, iStartIndex, iLen):
    oSkill = oAttack.m_Game.m_SkillMgr.GetSkill(oAttack.m_ID, iActNum)
    if not oSkill:
        return None
    iStopIndex = iStartIndex + CACHE_SLICE
    if iStopIndex > iLen:
        iStopIndex = iLen
    for i in range(iStartIndex, iStopIndex):
        dTrigger = lstTriggerCache[i]
        if 'BulletChange' in dTrigger:
            TriggerBulletChange(oAttack, oSkill, dTrigger.pop('BulletChange'))
        oSkill.NetTriggerUpdate(dTrigger)

    if iStopIndex < iLen:
        oAttack.m_FramingSkill[iActNum] = 1
        func = Functor(TriggerCache, oAttack, iActNum, lstTriggerCache, iStopIndex, iLen)
        oAttack.Call_Out(func, 1, 'TriggerCacheSkill')
    elif iActNum in oAttack.m_FramingSkill and iActNum in oAttack.m_FramingCache:
        lstTriggerCache = oAttack.m_FramingCache.pop(iActNum, [])
        TriggerCache(oAttack, iActNum, lstTriggerCache, 0, len(lstTriggerCache))
    else:
        oAttack.m_FramingSkill.pop(iActNum, 0)


def TriggerBulletChange(oWarrior, oSkill, dData):
    if oWarrior.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    oWarrior.m_BulletChangeCon.TriggerBulletChange(oSkill, dData)


def TryFallBackBullet(oWarrior, iWeapon, oPerform):
    if oWarrior.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    if oPerform.m_PFType not in (PF_TYPE_CONSHOOT, PF_TYPE_SHOOT, PF_TYPE_CHARGE, PF_TYPE_FILLBULLET):
        return None
    if not iWeapon:
        return None
    oWeapon = oWarrior.m_WieldCon.GetItemByID(iWeapon)
    if not oWeapon:
        return None
    oBulletCom = oWeapon.GetComponent('Bullet')
    oBulletCom.RefreshCurBullet()
    iBulletSID = oBulletCom.BulletType()
    oBulletCon = oWarrior.m_BulletCon
    oBulletCon.GS2CRefreshBullet(iBulletSID)
    if oPerform.m_PFType != PF_TYPE_FILLBULLET:
        oPerform.RefreshCurPFBullet()


def SkillTryFallBackBullet(oSkill):
    if 'AID' not in oSkill.m_Base:
        return None
    if 'pfid' not in oSkill.m_Base:
        return None
    if 'Weapon' not in oSkill.m_Base:
        return None
    iAttack = oSkill.m_Base['AID']
    iWeapon = oSkill.m_Base['Weapon']
    pfid = oSkill.m_Base['pfid']
    oGame = oSkill.m_Game
    oAttacker = oGame.GetObject(iAttack)
    if not oAttacker:
        return None
    oPerform = oAttacker.GetPerform(pfid, iWeapon)
    if not oPerform:
        return None
    TryFallBackBullet(oAttacker, iWeapon, oPerform)
