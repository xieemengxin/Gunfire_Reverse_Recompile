# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/weaponskincon.pyc
# RelativePath: clientlogic/cl_container/weaponskincon.pyc
# Source Generated with Decompyle++
# File: weaponskincon.pyc (Python 3.6)

import cl_msgcenter
import cllib.lib_flag

class CWeaponSkinContainer(object):
    
    def __init__(self, oGame, iOwner, iPlayerID):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_PlayerID = iPlayerID
        self.CurWeaponSkin = { }
        self.InitListen()

    
    def Save(self):
        if not cllib.lib_flag.g_OpenSeason:
            return { }
        dData = { }
        dData['CWK'] = self.CurWeaponSkin
        return dData

    
    def Load(self, dData):
        if not dData:
            return None
        self.CurWeaponSkin = dData['CWK']

    
    def InitListen(self):
        if not cllib.lib_flag.g_OpenSeason:
            return None
        oHero = self.GetOwner()
        if oHero:
            cl_msgcenter.AddFunction(oHero, cl_msgcenter.MSG_WAR_GREATEWEAPON, self.OnGreateWeapon, 'WeaponSkinInit', -1, 0)

    
    def Release(self):
        if not cllib.lib_flag.g_OpenSeason:
            return None
        oHero = self.GetOwner()
        if oHero:
            cl_msgcenter.DoneEvent(oHero, cl_msgcenter.MSG_WAR_GREATEWEAPON, 'WeaponSkinInit')

    
    def OnGreateWeapon(self, oWarMgr, dInfo):
        oWeapon = dInfo['Weapon']
        self.SetWeaponShapBySkin(oWeapon)

    
    def LoadWeaponSkin(self, dWeaponSkin):
        for iWeaponSID, iSkin in dWeaponSkin.items():
            self.CurWeaponSkin[iWeaponSID] = iSkin
        

    
    def GetSkinByWeaponSID(self, iWeaponSID):
        if iWeaponSID in self.CurWeaponSkin:
            return self.CurWeaponSkin[iWeaponSID]
        return 0

    
    def GetOwner(self):
        return self.m_Game.GetObject(self.m_Owner)

    
    def SetWeaponShapBySkin(self, oWeapon):
        iWeaponSkin = self.GetSkinByWeaponSID(oWeapon.m_SID)
        if not iWeaponSkin:
            return None
        oWeapon.m_Shape = iWeaponSkin


