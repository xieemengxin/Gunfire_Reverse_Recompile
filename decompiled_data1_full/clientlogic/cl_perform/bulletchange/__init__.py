# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/bulletchange/__init__.pyc
# RelativePath: clientlogic/cl_perform/bulletchange/__init__.pyc
# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.6)

from cl_perform.mobject import CBasePerform as CCustomPerform
from cl_commondefines import PF_TYPE_BULLETCHANGE, BULLET_CBMETHOD_INFINITEFIRE, BULLET_CBMETHOD_SRVSTATE
from cl_only import Functor
from cl_item.defines import EQUIP_TYPE_MAINWEAPON
import cl_perform.net as net
import cl_msgcenter

class CBulletChange(CCustomPerform):
    m_Name = '子弹变更被动技能'
    m_PFType = PF_TYPE_BULLETCHANGE
    m_EnableActionInfo = { }
    m_DisableActionInfo = { }
    m_CanAddMsg = (cl_msgcenter.MSG_WAR_COSTBULLET, cl_msgcenter.MSG_WAR_ATTACK, cl_msgcenter.MSG_WAR_WEAPONPERFROM_COSTBULLET, cl_msgcenter.MSG_WAR_PERFORM_START)
    
    def __init__(self, oOwner, iLevel):
        super(CBulletChange, self).__init__(oOwner, iLevel)
        self.m_OwnPfid = 0
        self.m_CurGroup = 0
        self.m_Key = 'BC%d-%d' % (self.m_SID, self.m_ID)
        self.m_Func = { }
        if iLevel in self.m_EnableActionInfo:
            self.m_Func['Enable'] = self.m_EnableActionInfo[iLevel]
        if iLevel in self.m_DisableActionInfo:
            self.m_Func['Disable'] = self.m_DisableActionInfo[iLevel]
        self.m_Func['CBFunc'] = { }
        self.m_Func['ExtDisable'] = { }
        self.m_MsgTrigger = { }
        self.m_WaitEnable = 0

    
    def SetLevel(self, oOwner, iLevel):
        super().SetLevel(oOwner, iLevel)
        if iLevel in self.m_EnableActionInfo:
            self.m_Func['Enable'] = self.m_EnableActionInfo[iLevel]
        if iLevel in self.m_DisableActionInfo:
            self.m_Func['Disable'] = self.m_DisableActionInfo[iLevel]

    
    def SetOwnPerfom(self, iPfid):
        self.m_OwnPfid = iPfid

    
    def AttrCache(self):
        dData = super(CBulletChange, self).AttrCache()
        dData['OwnPfid'] = self.m_OwnPfid
        return dData

    
    def Enable(self, oHero, iNotify = 0):
        self.m_WaitEnable = 1
        net.GS2CAddBulletChangeRule(self.m_Game, self, [
            oHero.m_PlayerID])

    
    def Disable(self, oHero, iNotify = 1, iReleaseFlag = 0):
        self.m_WaitEnable = 0
        if iNotify:
            net.GS2CDelBulletChangeRule(self.m_Game, self, [
                oHero.m_PlayerID])
        else:
            self.TrueDisable(oHero)

    
    def TrueEnable(self, oHero):
        if self.m_Enable:
            return None
        self.m_WaitEnable = 0
        self.m_Enable = 1
        if 'Enable' in self.m_Func:
            func = self.m_Func['Enable']
            func(oHero, self)

    
    def TrueDisable(self, oHero):
        if not self.m_Enable:
            return None
        self.m_WaitEnable = 0
        self.m_Enable = 0
        if 'Disable' in self.m_Func:
            func = self.m_Func['Disable']
            func(oHero, self)
        dExtDisable = self.m_Func['ExtDisable']
        self.m_Func['ExtDisable'] = { }
        if BULLET_CBMETHOD_INFINITEFIRE in dExtDisable:
            lstWeapon = oHero.m_WieldCon.GetAllItemByType(EQUIP_TYPE_MAINWEAPON)
            for oWeapon in lstWeapon:
                oWeapon.RemoveTmp('InfiniteFire')
            
        if BULLET_CBMETHOD_SRVSTATE in dExtDisable:
            for iStateID in dExtDisable[BULLET_CBMETHOD_SRVSTATE]:
                oHero.m_State.RemoveItem(iStateID)
            
        self.m_Func['CBFunc'] = { }
        for dInfo in self.m_MsgTrigger.values():
            (iMsg, iSub) = dInfo['Msg']
            cl_msgcenter.DoneEvent(oHero, iMsg, self.m_Key, iSub)
        
        self.m_MsgTrigger = { }

    
    def Refresh(self):
        if not (self.m_Enable) and not (self.m_WaitEnable):
            return None
        oHero = self.m_Game.GetObject(self.m_Owner)
        net.GS2CAddBulletChangeRule(self.m_Game, self, [
            oHero.m_PlayerID])

    
    def AddCBGroupFunc(self, iMsg, iSub, iGroup):
        if iGroup in self.m_CBFuncAction:
            func = self.m_CBFuncAction[iGroup]
            self.m_Func['CBFunc'][iGroup] = func
        if iMsg in self.m_CanAddMsg:
            oHero = self.m_Game.GetObject(self.m_Owner)
            func = Functor(TriggerRuleMsgCB, self.m_SID, self.m_OwnPfid, iGroup)
            cl_msgcenter.AddFunction(oHero, iMsg, func, self.m_Key, iSub, 0, -1)
            self.m_MsgTrigger[iGroup] = {
                'Msg': (iMsg, iSub) }

    
    def AddExtDisableFunc(self, iType, *args):
        if iType == BULLET_CBMETHOD_INFINITEFIRE:
            self.m_Func['ExtDisable'][iType] = 1
        elif iType == BULLET_CBMETHOD_SRVSTATE:
            if iType not in self.m_Func['ExtDisable']:
                self.m_Func['ExtDisable'][iType] = { }
            self.m_Func['ExtDisable'][iType][args[0]] = 1

    
    def TriggerRule(self, oSkill, dClientInfo):
        if not self.m_Enable:
            return None
        oHero = self.m_Game.GetObject(self.m_Owner)
        lstGroup = []
        for (iGroup, _), _ in dClientInfo.items():
            if iGroup in lstGroup:
                continue
            lstGroup.append(iGroup)
        
        for iGroup in lstGroup:
            if iGroup not in self.m_Func['CBFunc']:
                continue
            if iGroup in self.m_MsgTrigger:
                self.m_MsgTrigger[iGroup]['Pfid'] = oSkill.m_Base['pfid']
                self.m_MsgTrigger[iGroup]['Client'] = dClientInfo
                continue
            self.m_CurGroup = iGroup
            func = self.m_Func['CBFunc'][iGroup]
            func(oHero, self, oSkill, dClientInfo)
        

    
    def TriggerRuleByMsg(self, oSkill, oHero, iGroup):
        if iGroup not in self.m_Func['CBFunc']:
            return None
        if iGroup not in self.m_MsgTrigger:
            return None
        dInfo = self.m_MsgTrigger[iGroup]
        if 'Pfid' not in dInfo or 'Client' not in dInfo:
            return None
        if dInfo['Pfid'] != oSkill.m_Base['pfid']:
            return None
        dInfo.pop('Pfid')
        dClientInfo = dInfo.pop('Client')
        self.m_CurGroup = iGroup
        func = self.m_Func['CBFunc'][iGroup]
        func(oHero, self, oSkill, dClientInfo)



def TriggerRuleMsgCB(iPerform, iOwnPfid, iGroup, oHero, dMsgInfo):
    oSkill = dMsgInfo['Skill']
    oBulletChange = oHero.GetPerform(iPerform, 0, iOwnPfid)
    if not oBulletChange:
        return None
    oBulletChange.TriggerRuleByMsg(oSkill, oHero, iGroup)

