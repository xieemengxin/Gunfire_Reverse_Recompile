# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/condition.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/condition.pyc
# Source Generated with Decompyle++
# File: condition.pyc (Python 3.6)

from cl_commondefines import BULLET_CBCHECK_CONSUME, BULLET_CBCHECK_WEAPON_BULLETCNT, BULLET_CBCHECK_STA_GREATERCNT, BULLET_CBCHECK_SKILL_LEVEL, BULLET_CBCHECK_HASSTA, BULLET_CBCHECK_STACNT, BULLET_CBCHECK_HASSERVERSTA, BULLET_CBCHECK_RANDOM, BULLET_CBCHECK_FROM_PERFORM, BULLET_CBCHECK_FROM_PERFORMS, BULLET_CBCHECK_BAGBULLET, BULLET_CBCHECK_SERVERSTA_GREATERCNT

def CheckdClientInfo(dClientInfo, tkey):
    if tkey not in dClientInfo:
        return False
    if dClientInfo[tkey]['Result'] == 0:
        return False
    return True


def CheckFromSameItem(oWarrior, pfBulletChange, oSkill, dClientInfo):
    return True


def CheckShootStatus(oWarrior, pfBulletChange, oSkill, dClientInfo):
    return True


def CheckRandom(oWarrior, pfBulletChange, oSkill, dClientInfo, iRange, iProb):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_RANDOM)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckOwnClientState(oWarrior, pfBulletChange, oSkill, dClientInfo, iStateSID):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_HASSTA)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckWeaponBulletCnt(oWarrior, pfBulletChange, oSkill, dClientInfo, iCnt):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_WEAPON_BULLETCNT)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckTargetStateGreaterCount(oWarrior, pfBulletChange, oSkill, dClientInfo):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_STA_GREATERCNT)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckSkillLevel(oWarrior, pfBulletChange, oSkill, dClientInfo):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_SKILL_LEVEL)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckTargetStateCount(oWarrior, pfBulletChange, oSkill, dClientInfo, iState, iCnt):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_STACNT)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckOpenDual(oWarrior, pfBulletChange, oSkill, dClientInfo):
    return True


def CheckPerformTriggerType(oWarrior, pfBulletChange, oSkill, dClientInfo):
    return True


def CheckFireStatus(oWarrior, pfBulletChange, oSkill, dClientInfo):
    return True


def CheckSkillFireUnAllHit(oWarrior, pfBulletChange, oSkill, dClientInfo):
    return True


def CheckSkillFireHit(oWarrior, pfBulletChange, oSkill, dClientInfo):
    return True


def CheckOwnServerState(oWarrior, pfBulletChange, oSkill, dClientInfo, iStateSID):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_HASSERVERSTA)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckTargetServerStateGreaterCount(oWarrior, pfBulletChange, oSkill, dClientInfo, iState, iCnt):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_SERVERSTA_GREATERCNT)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckSkillMainPF(oWarrior, pfBulletChange):
    return True


def CheckWeaponUnFundamental(oWarrior, pfBulletChange):
    return True


def CheckBulletConsume(oWarrior, pfBulletChange, oSkill, dClientInfo):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_CONSUME)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckNoBulletConsume(oWarrior, pfBulletChange):
    return True


def CheckFromPointPerform(oWarrior, pfBulletChange, dClientInfo, iPerformSID):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_FROM_PERFORM)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckFromPointPerforms(oWarrior, pfBulletChange, dClientInfo, dPerform):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_FROM_PERFORMS)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckWeaponBulletCntOnPre(oWarrior, pfBulletChange, dClientInfo, dPerform):
    tkey = (pfBulletChange.m_CurGroup, BULLET_CBCHECK_BAGBULLET)
    return CheckdClientInfo(dClientInfo, tkey)


def CheckHitWeakness(oWarrior, pfBulletChange):
    return True


def CheckSkillMinorPF(oWarrior, pfBulletChange):
    return True


def CheckSkillMinorType(oWarrior, pfBulletChange, iType):
    return True


def CheckWeaponResourceLessPercent(oWarrior, pfBulletChange, iPercent):
    return True


def CheckThrowMaxUpperLimit(oWarrior, pfBulletChange, iCheckValues):
    oPerform = oWarrior.GetThrowPerform()
    if not oPerform:
        return False
    iBullet = oPerform.CalAttr('BulletSID')
    iBagBulletMax = oWarrior.m_BulletCon.GetMaxBullet(iBullet)
    return iBagBulletMax >= iCheckValues


def CheckThrowBulletCntUpperLimit(oWarrior, pfBulletChange, iCheckValues):
    oPerform = oWarrior.GetThrowPerform()
    if not oPerform:
        return False
    iBullet = oPerform.CalAttr('BulletSID')
    return oWarrior.m_BulletCon.Bullet(iBullet) >= iCheckValues

