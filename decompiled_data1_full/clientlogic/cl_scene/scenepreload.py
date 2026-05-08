# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_scene/scenepreload.pyc
# RelativePath: clientlogic/cl_scene/scenepreload.pyc
# Source Generated with Decompyle++
# File: scenepreload.pyc (Python 3.6)

import cl_minigame.choosepool as choosepool
import cl_item

class CScenePreLoad(object):
    
    def __init__(self, oGame):
        self.m_Game = oGame
        self.m_PreLoadData = {
            'Weapon': { },
            'Relic': { } }
        self.m_ChoosePool = { }

    
    def Release(self):
        for oChoosePool in self.m_ChoosePool.values():
            oChoosePool.Release()
        
        self.m_ChoosePool = { }
        self.m_Game = None

    
    def InitPreLoadData(self, dInfo):
        oGame = self.m_Game
        lstHero = oGame.GetWarMgr().GetRoomHero()
        dPreLoadWeapon = { }
        dChooseRemain = dInfo.get('ChoosePoolRemain', { })
        for iHero in lstHero:
            oChoosePool = choosepool.CChoosePoolMgr(oGame, iHero)
            oChoosePool.PreChoose(dChooseRemain.get(iHero, { }), dInfo)
            dPreLoadWeapon.update(oChoosePool.m_PreLoadData['Weapon'])
            self.m_ChoosePool[iHero] = oChoosePool
            oHero = oGame.GetObject(iHero)
            oWieldCon = oHero.m_WieldCon
            lstWeapon = oWieldCon.GetAllItem()
            for oWeapon in lstWeapon:
                dPreLoadWeapon[oWeapon.m_SID] = 1
            
        
        dWeaponShape = { }
        for iWeapon in dPreLoadWeapon:
            clsWeapon = cl_item.GetItemCls(iWeapon)
            dWeaponShape[clsWeapon.m_Shape] = 1
        
        self.m_PreLoadData = {
            'Weapon': list(dWeaponShape.keys()),
            'Relic': [] }

    
    def GetSceneChoosePool(self, pid):
        if pid in self.m_ChoosePool:
            return self.m_ChoosePool[pid]

    
    def GetPreLoadData(self):
        return self.m_PreLoadData

    
    def GetPassPreLoadData(self):
        dChoosePoolRemain = { }
        for pid, oChoosePool in self.m_ChoosePool.items():
            dChoosePoolRemain[pid] = oChoosePool.GetChoosePoolData()
        
        dData = {
            'ChoosePoolRemain': dChoosePoolRemain }
        return dData


