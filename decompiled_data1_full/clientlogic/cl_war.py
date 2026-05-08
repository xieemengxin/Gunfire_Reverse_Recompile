# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_war.pyc
# RelativePath: clientlogic/cl_war.pyc
# Source Generated with Decompyle++
# File: cl_war.pyc (Python 3.6)

from cl_commondefines import SKILLRET_SUCCESS, SKILLRET_FAIL, PF_TYPE_FILLBULLET
from cl_commondefines import PF_TYPE_CONSHOOT, PF_TYPE_SHOOT, PF_TYPE_CHARGE, WARRIOR_HERO
from cl_only import Functor
CACHE_SLICE = 5

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

