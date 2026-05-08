# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_abnormalconf.pyc
# RelativePath: clientlogic/cl_abnormalconf.pyc
# Source Generated with Decompyle++
# File: cl_abnormalconf.pyc (Python 3.6)

from cl_commondefines import *
from cl_only import Time2Frame
import cl_msgcenter
import cl_state
import itertools
g_AbnormalMap = {
    ABNORAML_THUNDER: {
        'Effect': (20028, 500),
        'Mixture': ((ABNORMAL_FIRE, ELEMENT_MIXTURE_VERTIGO, 1070, 500, 0), (ABNORAML_CORRISION, ELEMENT_MIXTURE_POISON, 20030, 500, 0)) },
    ABNORAML_CORRISION: {
        'Effect': (20027, 500),
        'Mixture': ((ABNORMAL_FIRE, ELEMENT_MIXTURE_EXPLOSION, 20031, 8, 12), (ABNORAML_THUNDER, ELEMENT_MIXTURE_POISON, 20030, 500, 0)) },
    ABNORMAL_FIRE: {
        'Effect': (20026, 500),
        'Mixture': ((ABNORAML_CORRISION, ELEMENT_MIXTURE_EXPLOSION, 20031, 8, 12), (ABNORAML_THUNDER, ELEMENT_MIXTURE_VERTIGO, 1070, 500, 0)) } }
g_AllEleAbnormalState = {
    20026: ABNORMAL_FIRE,
    20031: ELEMENT_MIXTURE_EXPLOSION,
    1070: ELEMENT_MIXTURE_VERTIGO,
    20027: ABNORAML_CORRISION,
    20030: ELEMENT_MIXTURE_POISON,
    20028: ABNORAML_THUNDER }
g_AbnormalCheck = {
    DAM_TYPE_THUNDER: (FIGHT3_KEY_IGNELETHUNDER, ABNORAML_THUNDER),
    DAM_TYPE_CORRISION: (FIGHT3_KEY_IGNELECORRISION, ABNORAML_CORRISION),
    DAM_TYPE_FIRE: (FIGHT3_KEY_IGNELEFIRE, ABNORMAL_FIRE) }
g_AbnormalDiectCheck = {
    ELEMENT_MIXTURE_POISON: FIGHT3_KEY_IGNOREPOISON,
    ELEMENT_MIXTURE_VERTIGO: FIGHT3_KEY_IGNOREVERTIGO,
    ABNORAML_THUNDER: FIGHT3_KEY_IGNELETHUNDER,
    ABNORAML_CORRISION: FIGHT3_KEY_IGNELECORRISION,
    ABNORMAL_FIRE: FIGHT3_KEY_IGNELEFIRE }
g_AbnormalString2Number = {
    'ABNORMAL_FIRE': 1,
    'ABNORAML_CORRISION': 2,
    'ABNORAML_THUNDER': 4 }
NO_MIXTURE_ABNORMAL_WARRIOR = WARRIOR_SERVANT | WARRIOR_PET

class CBaseAbnormalEleDam(object):
    m_InitReceiveDebuff = 100
    
    def __init__(self, oOwner):
        self.m_OwnerObj = oOwner
        self.m_MixtureStatus = { }
        self.m_TempMistureSatus = 0
        self.m_ReceiveDebuffFactor = { }
        self.m_ReceiveDebuff = self.m_InitReceiveDebuff

    
    def Release(self):
        self.m_OwnerObj = None
        self.m_MixtureStatus = { }

    
    def TryTriggerEleAbnormal(self, oSkill, iDam, oReason, iAbnormalTime = 0):
        if not oSkill or not (self.m_OwnerObj):
            return 0
        iAllAbnormal = 0
        lstAbnormalDam = [
            [
                oSkill.m_Cache['DebuffProb'] if 'DebuffProb' in oSkill.m_Cache else 0,
                oReason.Query('DamType')]]
        lstExt = oReason.Query('ExtEleAbnormal', [])
        for dExt in lstExt:
            if dExt['Replace']:
                iDebuffProb = dExt['Prob']
                lstAbnormalDam[0][0] = iDebuffProb
                continue
            lstAbnormalDam.append([
                dExt['Prob'],
                dExt['DamType']])
        
        for iProb, iDamType in lstAbnormalDam:
            iAbnormal = self.CheckTriggerEleAbnormal(oSkill, oReason, iProb, iDamType)
            if not iAbnormal:
                continue
            iAllAbnormal |= self.TriggerEleAbnormal(oSkill, iDam, oReason, iAbnormal, iAbnormalTime)
        
        return iAllAbnormal

    
    def CheckTriggerEleAbnormal(self, oSkill, oReason, iProb, iDamType):
        iFactor = oSkill.m_Cache['DebuffFactor'] if 'DebuffFactor' in oSkill.m_Cache else 100
        iRatio = iProb * iFactor * self.m_ReceiveDebuff // 10000
        if not iRatio:
            return 0
        for iDamCheck, (iIgnoreKey, iAbnormal) in g_AbnormalCheck.items():
            if not (iDamType & iDamCheck) or self.m_OwnerObj.CheckLogicKey(iIgnoreKey):
                continue
            if oReason.Query('MustEleAbnormal'):
                return iAbnormal
            if oReason.Query('BanEleAbnormal'):
                continue
            if self.m_OwnerObj.m_Game.Random(10000) > iRatio:
                continue
            return iAbnormal
        
        return 0

    
    def CheckDirectAddEleAbnormal(self, iState):
        iAbnormal = g_AllEleAbnormalState[iState]
        if iAbnormal not in g_AbnormalDiectCheck:
            return True
        iIgnoreKey = g_AbnormalDiectCheck[iAbnormal]
        if self.m_OwnerObj.CheckLogicKey(iIgnoreKey):
            return False
        return True

    
    def TriggerEleAbnormal(self, oSkill, iDam, oReason, iAbnormal, iAbnormalTime):
        oOwner = self.m_OwnerObj
        dArgs = {
            'AbnormalSourceDam': iDam,
            'DamFactor': {
                OBJ_VICTIM: { },
                OBJ_ATTACK: { } } }
        dArgs['Cache'] = {
            'FireAbnormalFactor': oSkill.m_Cache['FireAbnormalFactor'],
            'ThunderAbnormalFactor': oSkill.m_Cache['ThunderAbnormalFactor'],
            'CorrisionAbnormalFactor': oSkill.m_Cache['CorrisionAbnormalFactor'] }
        if 'Att' in oSkill.m_Cache:
            dArgs['Cache']['Att'] = oSkill.m_Cache['Att']
        dState = {
            'AID': oSkill.m_Base['AID'],
            'RS': oReason.ExtInfo({
                'ActNum': 0 }),
            'pfid': oSkill.m_Base['pfid'],
            'PFLV': oSkill.m_Base['PFLV'],
            'arg': dArgs }
        iPeriod = oSkill.m_Cache['DebuffPeriod'] if 'DebuffPeriod' in oSkill.m_Cache else 100
        dInfo = g_AbnormalMap[iAbnormal]
        (iState, iTime) = dInfo['Effect']
        iTime = iAbnormalTime if iAbnormalTime else iTime
        iTime = iTime * iPeriod // 100
        dDebuffInfo = {
            'DebuffTime': iTime,
            'DebuffState': iState,
            'DebuffType': iAbnormal }
        dSendData = { }
        dSendData.update({
            'VID': oOwner.m_ID,
            'Debuff': dDebuffInfo,
            'StateInfo': dState,
            'Skill': oSkill,
            'StateSID': iState })
        oAttack = oSkill.GetAttack()
        if oAttack:
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSEDEBUFF, oAttack, dSendData, iSub = MAIN_DEBUFF)
        iFrame = Time2Frame(dDebuffInfo['DebuffTime'])
        if iFrame <= 0:
            return 0
        dState = dSendData['StateInfo']
        self.m_TempMistureSatus = 0
        oState = cl_state.AddState(oOwner, iState, STATE_TIME_LIMIT, iFrame, dState)
        if not oState or not (oState.m_LifeCycle):
            return 0
        oState.Enable(oOwner)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GOTDEBUFF, oOwner, {
            'StateSID': iState })
        if oAttack:
            dFinalSendData = {
                'VID': oOwner.m_ID,
                'StateSID': iState,
                'DebuffFrame': iFrame,
                'StateInfo': dState,
                'RS': oReason,
                'Skill': oSkill,
                'Debuff': dSendData['Debuff'] }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSEDFINALDEBUFF, oAttack, dFinalSendData, iSub = ACTIVE_SENDMESSAGE)
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_GOTDEFINALDEBUFF, oOwner, dFinalSendData, iSub = ACTIVE_SENDMESSAGE)
        iMixture = self.m_TempMistureSatus
        return iAbnormal | iMixture

    
    def TryTriggerMixtureStatus(self, iStateSid, dState):
        if iStateSid not in g_AllEleAbnormalState:
            return None
        iAbnormal = g_AllEleAbnormalState[iStateSid]
        if iAbnormal not in g_AbnormalMap:
            return None
        dStateArg = { }
        if 'arg' in dState:
            dStateArg.update(dState['arg'])
        dData = {
            'AID': dState['AID'],
            'RS': dState['RS'],
            'pfid': dState['pfid'] if 'pfid' in dState else 0,
            'arg': dStateArg }
        tMixture = g_AbnormalMap[iAbnormal]['Mixture']
        for iMatch, iMixStatus, iState, iTime, iCDTime in tMixture:
            (iMatchState, _) = g_AbnormalMap[iMatch]['Effect']
            if not self.HasState(iMatchState):
                continue
            if not self.CheckTriggerMixtureStatus(iMixStatus):
                continue
            self.m_TempMistureSatus |= iMixStatus
            self.TriggerMixtureStatus(iMixStatus, dData, iState, iTime, iCDTime)
        

    
    def CheckTriggerMixtureStatus(self, iMixStatus):
        iNowFrame = self.m_OwnerObj.m_Game.GetFrameNum()
        if iMixStatus not in self.m_MixtureStatus:
            return True
        iEffFrame = self.m_MixtureStatus[iMixStatus]
        if iEffFrame <= iNowFrame:
            return True
        return False

    
    def TriggerMixtureStatus(self, iMixStatus, dState, iState, iTime, iCDTime):
        oGame = self.m_OwnerObj.m_Game
        iNowFrame = oGame.GetFrameNum()
        iFrame = Time2Frame(iTime)
        if iFrame <= 0:
            return None
        oState = cl_state.AddState(self.m_OwnerObj, iState, STATE_TIME_LIMIT, iFrame, dState)
        if not oState:
            return None
        iAttack = dState['AID']
        oAttack = oGame.GetObject(iAttack)
        if oAttack and self.m_OwnerObj:
            dMsgInfo = {
                'VID': self.m_OwnerObj.m_ID,
                'StateSID': iState,
                'StateID': oState.m_ID }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_CAUSEMIXDEBUFF, oAttack, dMsgInfo)
        oState.Enable(self.m_OwnerObj)
        self.m_MixtureStatus[iMixStatus] = iNowFrame + Time2Frame(iCDTime)

    
    def HasState(self, iState):
        if self.m_OwnerObj.m_State.GetItemBySID(iState):
            return True
        return False

    
    def SetReceiveDebuff(self, iAdd, iMul, sKey):
        self.m_ReceiveDebuffFactor[sKey] = (iAdd, iMul)
        self.RefreshReceiveDebuff()

    
    def ClearReceiveDebuff(self, sKey):
        if sKey in self.m_ReceiveDebuffFactor:
            self.m_ReceiveDebuffFactor.pop(sKey)
        self.RefreshReceiveDebuff()

    
    def RefreshReceiveDebuff(self):
        iValue = self.m_InitReceiveDebuff
        lstMul = []
        for iAdd, iMul in self.m_ReceiveDebuffFactor.values():
            iValue += iAdd
            lstMul.append(iMul)
        
        for iOneMul in lstMul:
            iValue = iValue * (10000 + iOneMul) // 10000
        
        self.m_ReceiveDebuff = iValue



class CNoMixtureAbnoramEleDam(CBaseAbnormalEleDam):
    
    def CheckTriggerMixtureStatus(self, tKey):
        return False



class CNoAbnormalEleDam(CBaseAbnormalEleDam):
    
    def TryTriggerEleAbnormal(self, oSkill, iDam, oReason, iAbnormalTime = 0):
        return 0

    
    def TryTriggerMixtureStatus(self, iStateSid, dState):
        pass

    
    def CheckDirectAddEleAbnormal(self, iState):
        return False



def GetAbnormalEleDam(oWarrior, iFightType):
    if iFightType in (WARRIOR_HERO, WARRIOR_PROTEGE_NORMAL) or iFightType & NO_MIXTURE_ABNORMAL_WARRIOR:
        return CNoMixtureAbnoramEleDam(oWarrior)
    return CBaseAbnormalEleDam(oWarrior)


def GetNoAbnormalEleDam(oWarrior):
    return CNoAbnormalEleDam(oWarrior)


def GetAbnormalEleTime(sAbnormalType):
    iEleAbnormalType = g_AbnormalString2Number[sAbnormalType]
    iTime = g_AbnormalMap[iEleAbnormalType]['Effect'][1]
    return iTime


def GetAbnormalState(iAbnormalType):
    if iAbnormalType not in g_AbnormalMap:
        return 0
    return g_AbnormalMap[iAbnormalType]['Effect'][0]

g_AllAbnormalStateSID = set()

def Init():
    global g_AllAbnormalStateSID
    g_AllAbnormalStateSID = set((dConfig['Effect'][0] for dConfig in g_AbnormalMap.values()))

Init()
