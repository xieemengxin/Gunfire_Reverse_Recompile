# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_warmgr/testelement.pyc
# RelativePath: clientlogic/cl_warmgr/testelement.pyc
# Source Generated with Decompyle++
# File: testelement.pyc (Python 3.6)

from cl_warmgr.mobject import CBaseElement
from cl_commondefines import TESTELE_ACTION_WUDI, DEBUG_STATUS_WUDI
import cl_item
import cl_msgcenter
import cl_perform

class CTestElement(CBaseElement):
    
    def __init__(self, oGame, nid, oData):
        super(CTestElement, self).__init__(oGame, nid, oData)
        self.m_WarMgr = oGame.GetWarMgr()
        self.m_WeaponData = self.m_Data.m_Config.get('TESTWEAPON', [])
        self.m_BulletData = self.m_Data.m_Config.get('TESTBULLET', [])
        self.m_TalentData = self.m_Data.m_Config.get('TESTTALENT', [])
        self.m_PassiveData = self.m_Data.m_Config.get('TESTPASSIVE', [])

    
    def Init(self):
        oWarMgr = self.m_WarMgr
        cl_msgcenter.AddFunction(oWarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, self.InitPlayer, 'TestInit', -1, 0)

    
    def InitPlayer(self, oWarMgr, dInfo):
        iHero = dInfo['Hero']
        oHero = oWarMgr.m_Game.GetObject(iHero)
        if self.m_WeaponData:
            for lstWeapon in self.m_WeaponData:
                (iWeaponSID, iCurBullet) = lstWeapon
                TestArtWeapon(oHero, iWeaponSID, iCurBullet)
            
        if self.m_BulletData:
            for lstBullet in self.m_BulletData:
                (iBulletSID, iCnt) = lstBullet
                TestArtBullet(oHero, iBulletSID, iCnt)
            
        if self.m_TalentData:
            dCareerTalent = cl_perform.load.GetTalentLib().get(oHero.m_Career, { })
            for lstTalent in self.m_TalentData:
                (iTalentSID, iPos, iLevel) = lstTalent
                if iTalentSID in dCareerTalent:
                    TestArtTalent(oHero, iTalentSID, iLevel)
            
        if self.m_PassiveData:
            for iPerform, iLevel in self.m_PassiveData:
                TestArtPassive(oHero, iPerform, iLevel)
            
        dPlayerInfo = dInfo['CreateInfo']
        lstCustomAction = dPlayerInfo.get('LogicTestAction', [])
        for iCustomAction in lstCustomAction:
            if iCustomAction in g_CustonTestAction:
                g_CustonTestAction[iCustomAction](oHero)
        

    
    def Release(self):
        cl_msgcenter.DoneEvent(self.m_WarMgr, cl_msgcenter.MSG_WARMGR_ADDPLAYER, 'TestInit')
        self.m_WarMgr = None
        super(CTestElement, self).Release()



def TestArtWeapon(oHero, iWeapon, iCurBullet):
    oWeapon = cl_item.CreateEquip(oHero.m_Game, iWeapon)
    oWeapon.PutToContainer(oWeapon.GetTargetContainer(oHero), 'Init')
    oBulletCom = oWeapon.GetComponent('Bullet')
    if not oBulletCom:
        return None
    oBulletCom.BulletModify(iCurBullet)


def TestArtBullet(oHero, iBullet, iCnt):
    oHero.m_BulletCon.BulletModify(iBullet, iCnt, 'Init')


def TestArtTalent(oHero, iTalent, iLevel = 1):
    oTalentCon = oHero.m_TalentCon
    oTalentCon.AddTalent(iTalent, iLevel, 'Init')


def TestArtPassive(oHero, iPerform, iLevel = 1):
    oHero.AddPerform(iPerform, iLevel)


def CustomTestActionWudi(oHero):
    iStatus = oHero.Query('DebugStatus', 0)
    oHero.Set('DebugStatus', iStatus | DEBUG_STATUS_WUDI)
    oHero.ChangeBaseDamRatio('WUDI', 10000000, 0)
    oHero.GS2CPropChange('DebugStatus')

g_CustonTestAction = {
    TESTELE_ACTION_WUDI: CustomTestActionWudi }

def GetComponentClass(oMgrManager):
    return CTestElement

