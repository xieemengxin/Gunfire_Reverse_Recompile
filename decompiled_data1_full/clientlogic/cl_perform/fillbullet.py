# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/fillbullet.pyc
# RelativePath: clientlogic/cl_perform/fillbullet.pyc
# Source Generated with Decompyle++
# File: fillbullet.pyc (Python 3.6)

from cl_commondefines import PF_TYPE_FILLBULLET, PF_SUBMSG_FILLBULLET, FORBID_FILLBULLET
from cl_perform.mobject import CPerform as CCustomPerform

class CPerform(CCustomPerform):
    m_PFType = PF_TYPE_FILLBULLET
    m_SubMsg = PF_SUBMSG_FILLBULLET
    m_CheckForbid = FORBID_FILLBULLET
    
    def CanUse(self, oWarrior, dInfo):
        if not super(CPerform, self).CanUse(oWarrior, dInfo):
            return 0
        oWeapon = self.GetMyItem()
        if not oWeapon:
            return 0
        oBulletCom = oWeapon.GetComponent('Bullet')
        if not oBulletCom:
            return 0
        if oBulletCom.Bullet() >= oBulletCom.MaxBullet():
            return 0
        iBulletSID = oBulletCom.BulletType()
        if not iBulletSID:
            return 0
        iBagBullet = oWarrior.m_BulletCon.Bullet(iBulletSID)
        bIsInitWeapon = oWeapon.IsInitWeapon()
        if not iBagBullet and not bIsInitWeapon:
            return 0
        return 1

    
    def AttrCache(self):
        dData = { }
        for sAttr in self.m_Attr:
            dData[sAttr] = self.CalAttr(sAttr)
        
        return dData


