# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/skillcache.pyc
# RelativePath: clientlogic/cl_perform/skillcache.pyc
# Source Generated with Decompyle++
# File: skillcache.pyc (Python 3.6)

from cl_commondefines import ATTSTATUS_OPENSNIPE, WARRIOR_HERO, SNIPE_STATUS_OPEN, SKILLCACHE_PERFORMMODE
from cl_cscommondef.cs_perform import SKILLCACHE_CHARGELEVEL, SKILLCACHE_ELEMENTTYPE, SKILLCACHE_SIGNSPEED, SKILLCACHE_LIVEHEROCNT, SKILLCACHE_ATTPERFORMIDX, SKILLCACHE_INT, SKILLCACHE_EXTRATRAJECTORY, SKILLCACHE_RANDOM, SKILLCACHE_BALLISTICTYPE, SKILLCACHE_ATTACKSTATUS, SKILLCACHE_LSTPOS, SKILLCACHE_POS, SKILLCACHE_LSTINT, SKILLCACHE_LSTINTSPECIAL, SKILLCACHE_PARENTACTNUM, SKILLCACHE_BEACONCOUNT
from cl_duonet.netfunc import *
from cl_only import Functor
from cl_perform.cartoon.netdata import SkillUnpackInt, SkillUnpackFloat, SkillUnpackListInt
from cl_perform.cartoon.netdata import SkillPacketAddI, SkillPacketFloat, SkillPacketListInt, SkillPacketPos, SkillUnpacketPos, SkillPacketListPos, SkillUnpacketListPos
import cl_perform

class CSkillCacheData(object):
    
    def __init__(self):
        self.m_SkillCacheIndex = []
        self.m_IntPara = 0
        self.m_IntParaList = []
        self.m_PosTuple = ()
        self.m_PosList = []
        self.m_SpecialList = []
        self.m_AttackStatus = 0
        self.m_BallisticType = 0
        self.m_Random = 0
        self.m_ExtraTrajectory = 0
        self.m_SignSpeed = 0
        self.m_LiveHeroCnt = 0
        self.m_AttPerformIdx = 0
        self.m_PerformMode = 0
        self.m_ElementType = 0
        self.m_ChargeLevel = 0
        self.m_ParentActnum = 0
        self.m_BeaconCount = 0

    
    def TempChooseCtrlSend(self):
        if self.m_ExtraTrajectory == None:
            self.m_ExtraTrajectory = 0
        PacketAddI(self.m_ExtraTrajectory, 4)

    
    def GetSkillCache(self, sKey, default = None):
        if sKey not in self.__dict__:
            return default
        return self.__dict__[sKey]

    
    def SetSkillCache(self, sKey, objValue):
        self.__dict__[sKey] = objValue

    
    def IsOpenSnipe(self):
        if self.m_AttackStatus & ATTSTATUS_OPENSNIPE:
            return True
        return False

    
    def GetBallisticType(self):
        return self.m_BallisticType

    
    def SetBallisticType(self, iType):
        self.m_BallisticType = iType

    
    def SetRandom(self, iRandom):
        self.m_Random = iRandom

    
    def SetExtraTrajectory(self, iExtraTrajectory):
        self.m_ExtraTrajectory = iExtraTrajectory

    
    def GetExtraTrajectory(self):
        return self.m_ExtraTrajectory

    
    def GetPerformMode(self):
        return self.m_PerformMode

    
    def GetElementType(self):
        return self.m_ElementType

    
    def GetChargeLevel(self):
        return self.m_ChargeLevel

    
    def SetBeaconCount(self, iBeaconCount):
        self.m_BeaconCount = iBeaconCount

    
    def GetBeaconCount(self):
        return self.m_BeaconCount



def CacheInitAttackStatus(oSkill, oCacheData):
    oCacheData.m_AttackStatus = 0
    oAttack = oSkill.GetAttack()
    if oAttack.m_FightType & WARRIOR_HERO and oAttack.ShootStatus() == SNIPE_STATUS_OPEN:
        oCacheData.m_AttackStatus |= ATTSTATUS_OPENSNIPE


def CacheInitRandom(oSkill, oCacheData):
    oCacheData.m_Random = oSkill.m_Game.Random(100)


def CacheInitInt(oSkill, oCacheData):
    oCacheData.m_IntPara = 0


def CacheInitLstInt(oSkill, oCacheData):
    oCacheData.m_IntParaList = []


def CacheInitExtraTrajectory(oSkill, oCacheData):
    oCacheData.m_ExtraTrajectory = 0


def CacheInitSignSpeed(oSkill, oCacheData):
    oCacheData.m_SignSpeed = 0


def CacheInitPerformMode(oSkill, oCacheData):
    oCacheData.m_PerformMode = 0


def CacheInitElementType(oSkill, oCacheData):
    oCacheData.m_ElementType = 0


def CacheInitChargeLevel(oSkill, oCacheData):
    oCacheData.m_ChargeLevel = 0


def CacheInitParentActnum(oSkill, oCacheData):
    oCacheData.m_ParentActnum = 0


def CacheInitLiveHeroCnt(oSkill, oCacheData):
    iCount = 0
    iScene = oSkill.m_Base['Scene']
    for iHero in oSkill.m_Game.m_WarMgr.GetLiveHero():
        oHero = oSkill.m_Game.GetObject(iHero)
        if not oHero or oHero.IsDead() or iScene != oHero.m_Scene:
            continue
        iCount += 1
    
    oCacheData.m_LiveHeroCnt = iCount


def CacheInitBallisticType(oSkill, oCacheData):
    oCacheData.m_BallisticType = oSkill.m_Custom['BallisticType'] if 'BallisticType' in oSkill.m_Custom else 1


def CacheInitAttPerformIdx(oSkill, oCacheData):
    oGame = oSkill.m_Game
    iAttack = oSkill.m_Base['AID']
    iItemID = oSkill.m_Base['Weapon']
    oAttack = oGame.GetObject(iAttack)
    oCacheData.m_AttPerformIdx = 0
    if not oAttack or oAttack.m_FightType & WARRIOR_HERO != WARRIOR_HERO:
        return None
    oWeapon = oAttack.m_WieldCon.GetItemByID(iItemID)
    if not oWeapon:
        return None
    oComPerform = oWeapon.GetComponent('Perform')
    oCacheData.m_AttPerformIdx = oComPerform.GetAttPerformIdx()


def CacheInitPos(oSkill, oCacheData):
    oCacheData.m_PosTuple = (0, 0, 0)


def CacheInitPosList(oSkill, oCacheData):
    oCacheData.m_PosList = []


def CacheInitSpecialList(oSkill, oCacheData):
    oCacheData.m_SpecialList = []


def CacheInitBeaconCount(oSkill, oCacheData):
    oCacheData.m_BeaconCount = 0

g_SkillCacheFunc = {
    SKILLCACHE_BEACONCOUNT: (SkillPacketAddI(2), SkillUnpackInt(2), 'm_BeaconCount', CacheInitBeaconCount),
    SKILLCACHE_PARENTACTNUM: (SkillPacketAddI(2), SkillUnpackInt(2), 'm_ParentActnum', CacheInitParentActnum),
    SKILLCACHE_CHARGELEVEL: (SkillPacketAddI(1), SkillUnpackInt(1), 'm_ChargeLevel', CacheInitChargeLevel),
    SKILLCACHE_ELEMENTTYPE: (SkillPacketAddI(2), SkillUnpackInt(2), 'm_ElementType', CacheInitElementType),
    SKILLCACHE_PERFORMMODE: (SkillPacketAddI(2), SkillUnpackInt(2), 'm_PerformMode', CacheInitPerformMode),
    SKILLCACHE_ATTPERFORMIDX: (SkillPacketAddI(1), SkillUnpackInt(1), 'm_AttPerformIdx', CacheInitAttPerformIdx),
    SKILLCACHE_LIVEHEROCNT: (SkillPacketAddI(1), SkillUnpackInt(1), 'm_LiveHeroCnt', CacheInitLiveHeroCnt),
    SKILLCACHE_SIGNSPEED: (SkillPacketFloat(4), SkillUnpackFloat(4), 'm_SignSpeed', CacheInitSignSpeed),
    SKILLCACHE_EXTRATRAJECTORY: (SkillPacketAddI(4), SkillUnpackInt(4), 'm_ExtraTrajectory', CacheInitExtraTrajectory),
    SKILLCACHE_RANDOM: (SkillPacketAddI(2), SkillUnpackInt(2), 'm_Random', CacheInitRandom),
    SKILLCACHE_BALLISTICTYPE: (SkillPacketAddI(1), SkillUnpackInt(1), 'm_BallisticType', CacheInitBallisticType),
    SKILLCACHE_ATTACKSTATUS: (SkillPacketAddI(1), SkillUnpackInt(1), 'm_AttackStatus', CacheInitAttackStatus),
    SKILLCACHE_LSTINTSPECIAL: (SkillPacketListInt(4), SkillUnpackListInt(4), 'm_SpecialList', CacheInitSpecialList),
    SKILLCACHE_LSTPOS: (SkillPacketListPos, SkillUnpacketListPos, 'm_PosList', CacheInitPosList),
    SKILLCACHE_POS: (SkillPacketPos, SkillUnpacketPos, 'm_PosTuple', CacheInitPos),
    SKILLCACHE_LSTINT: (SkillPacketListInt(4), SkillUnpackListInt(4), 'm_IntParaList', CacheInitLstInt),
    SKILLCACHE_INT: (SkillPacketAddI(4), SkillUnpackInt(4), 'm_IntPara', CacheInitInt) }

def CacheInitData(oSkill):
    iPerform = oSkill.m_Base['pfid']
    funSkillCacheIndex = cl_perform.GetPerformModuleAttr(iPerform, 'GetSkillCacheIndex')
    if funSkillCacheIndex:
        lstChoose = funSkillCacheIndex()
    else:
        lstChoose = [ _ for _ in range(SKILLCACHE_ATTACKSTATUS, SKILLCACHE_ATTPERFORMIDX + 1) ]
    oCacheData = oSkill.m_CacheData
    for iChooseIndex in lstChoose:
        funcInit = g_SkillCacheFunc[iChooseIndex][3]
        if funcInit:
            funcInit(oSkill, oCacheData)
    
    oCacheData.m_SkillCacheIndex = lstChoose


def CacheInitSend(oSkill):
    lstChoose = oSkill.m_CacheData.m_SkillCacheIndex
    CacheChooseSend(oSkill, lstChoose)


def CacheChooseSend(oSkill, lstChoose):
    oCacheData = oSkill.m_CacheData
    iLen = len(lstChoose)
    PacketAddI(iLen, 1)
    if not iLen:
        oCacheData.TempChooseCtrlSend()
    else:
        for iChooseIndex in lstChoose:
            PacketAddI(iChooseIndex, 1)
            funcSend = g_SkillCacheFunc[iChooseIndex][0]
            sAttrName = g_SkillCacheFunc[iChooseIndex][2]
            if funcSend:
                objValue = oCacheData.GetSkillCache(sAttrName)
                funcSend(objValue)
        


def SyncClientCacheData(oSkill):
    iLen = UnpackInt(1)
    oCacheData = oSkill.m_CacheData
    lstChoose = []
    for _ in range(iLen):
        iChooseIndex = UnpackInt(1)
        lstChoose.append(iChooseIndex)
        funcUnpack = g_SkillCacheFunc[iChooseIndex][1]
        sAttrName = g_SkillCacheFunc[iChooseIndex][2]
        objValue = funcUnpack()
        oCacheData.SetSkillCache(sAttrName, objValue)
    
    return lstChoose


def CacheInitPacket():
    lstChoose = []
    oCacheData = CSkillCacheData()
    for _ in range(UnpackInt(1)):
        iChooseIndex = UnpackInt(1)
        funcRecv = g_SkillCacheFunc[iChooseIndex][1]
        sAttrName = g_SkillCacheFunc[iChooseIndex][2]
        objValue = funcRecv()
        oCacheData.SetSkillCache(sAttrName, objValue)
        lstChoose.append(iChooseIndex)
    
    oCacheData.m_SkillCacheIndex = lstChoose
    return oCacheData


def GetSkillCacheByIndex(oSkill, iChooseIndex):
    sAttrName = g_SkillCacheFunc[iChooseIndex][2]
    oCacheData = oSkill.m_CacheData
    return oCacheData.GetSkillCache(sAttrName)


def SetSkillCacheByIndex(oSkill, iChooseIndex, objValue):
    sAttrName = g_SkillCacheFunc[iChooseIndex][2]
    oCacheData = oSkill.m_CacheData
    oCacheData.SetSkillCache(sAttrName, objValue)


def GetSkillCacheAttrNameByIndex(iChooseIndex):
    return g_SkillCacheFunc[iChooseIndex][2]

