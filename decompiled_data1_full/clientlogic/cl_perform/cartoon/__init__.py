# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/__init__.pyc
# RelativePath: clientlogic/cl_perform/cartoon/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_commondefines import DEBUG_STATUS_NOCOSTBULLET

def ContinuousCostBullet(oSkill, iNodeID):
    if 'BulletCrt' in oSkill.m_Base or iNodeID != oSkill.m_Base['BulletCrt']:
        return 1
    oSkill.m_Base['BulletCrt'] = iNodeID
    oAttack = oSkill.m_Game.GetObject(oSkill.m_Base['AID'])
    if not oAttack:
        return 0
    oPerform = oAttack.GetPerform(oSkill.m_Base['pfid'], oSkill.m_Base['Weapon'])
    if not oPerform:
        return 0
    oWeapon = oPerform.GetMyItem()
    if not oWeapon:
        return 0
    oBulletCom = oWeapon.GetComponent('Bullet')
    if oBulletCom and oAttack.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET != DEBUG_STATUS_NOCOSTBULLET:
        iNowTotalBulletUse = oSkill.m_Collect['TotalBullet']
        oSkill.m_Collect['TotalBullet'] = 0
        oSkill.m_Collect.pop('OtherBulletUse', { })
        oSkill.m_Collect.pop('ExtShootBulletUse', 0)
        oPerform.CostBullet(oAttack, oSkill)
        oSkill.m_Collect['RealBullet'] = oSkill.m_Collect['TotalBullet']
        oSkill.m_Collect['TotalBullet'] += iNowTotalBulletUse
        oSkill.m_Collect.pop('ExtBulletUse', 0)
        oSkill.m_Collect.pop('NoBulletUse', 0)
    if 'CopyWeapon' in oSkill.m_Collect:
        dCopyWeapon = oSkill.m_Collect['CopyWeapon']
        dCopyCartoon = dCopyWeapon['CopyCartoon']
        dCopyCartoon.pop(iNodeID, None)
    oPerform.WeaponFire(oAttack, oSkill)
    return 1

