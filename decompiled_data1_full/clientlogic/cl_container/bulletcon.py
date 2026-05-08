# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_container/bulletcon.pyc
# RelativePath: clientlogic/cl_container/bulletcon.pyc
# Source Generated with Decompyle++
# File: bulletcon.pyc (Python 3.6)

from cl_object.baseattr import NewAttr
from cl_commondefines import BASEATTR_REFRESH, DROP_BULLETPICK_NORMAL
import cl_msgcenter
import cl_item.load
import cl_notify
import cl_duonet.dn_cl_item_cnet
import math

def GS2CRefreshBullet(oGame, iWarrior, iBulletSID, iAmount, iMaxAmount, dPlayer):
    netData = {
        'iBulletSID': iBulletSID,
        'iAmount': iAmount,
        'iMaxAmount': iMaxAmount,
        'iWarrior': iWarrior,
        'oGame': oGame,
        'dPlayer': dPlayer }
    cl_duonet.dn_cl_item_cnet.DN_GS2CBulletRefresh(netData)


class CBulletContainer(object):
    m_CostBulletSubMsg = cl_item.load.GetBulletSubMsg()
    
    def __init__(self, oGame, iOwner, iPlayer):
        self.m_Game = oGame
        self.m_Owner = iOwner
        self.m_PlayerID = iPlayer
        self.m_Bullet = { }
        self.m_BulletMul = { }
        self.m_DropModule = DROP_BULLETPICK_NORMAL
        lstAllBullet = cl_item.load.GetAllBulletType()
        for iSID in lstAllBullet:
            self.m_Bullet[iSID] = 0
        

    
    def Release(self):
        self.m_Game = None

    
    def Save(self):
        dData = { }
        for iSID, iAmount in self.m_Bullet.items():
            if iAmount:
                dData[iSID] = iAmount
        
        return dData

    
    def Load(self, dData):
        self.m_Bullet.update(dData)

    
    def AddInBulletMul(self, iSid, iMul, iAdd, sKey):
        if not self.m_Game:
            return None
        if iSid not in self.m_Bullet:
            return None
        if iSid in self.m_BulletMul:
            self.m_BulletMul[iSid].AddValue(None, iMul, iAdd, sKey)
        else:
            oBulletItem = cl_item.GetTemp(iSid)
            self.m_BulletMul[iSid] = NewAttr(oBulletItem, 'MaxBullet', oBulletItem.m_MaxAmount, BASEATTR_REFRESH)
            self.m_BulletMul[iSid].AddValue(None, iMul, iAdd, sKey)
        iAmount = self.m_Bullet[iSid]
        if iAmount > self.GetMaxBullet(iSid):
            self.SetBullet(iSid, iAmount)
        self.GS2CRefreshBullet(iSid)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MAXBAGBULLETCHANGE, self.GetOwner(), {
            'SID': iSid }, iSub = self.m_CostBulletSubMsg[iSid])

    
    def RemoveBulletMul(self, iSid, sKey):
        if not self.m_Game:
            return None
        if iSid not in self.m_BulletMul or iSid not in self.m_Bullet:
            return None
        self.m_BulletMul[iSid].ClearValue(None, sKey)
        self.SetBullet(iSid, self.m_Bullet[iSid])
        self.GS2CRefreshBullet(iSid)
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_MAXBAGBULLETCHANGE, self.GetOwner(), {
            'SID': iSid }, iSub = self.m_CostBulletSubMsg[iSid])

    
    def ReturnMaxBullet(self, iSid):
        if iSid in self.m_BulletMul:
            return self.m_BulletMul[iSid].GetValue(None)
        oBulletItem = cl_item.GetTemp(iSid)
        iMaxMount = oBulletItem.m_MaxAmount
        return iMaxMount

    
    def Refresh(self, dPlayer = None):
        for iSID in self.m_Bullet:
            self.GS2CRefreshBullet(iSID, dPlayer)
        

    
    def GetOwner(self):
        if not self.m_Game:
            return None
        return self.m_Game.GetObject(self.m_Owner)

    
    def GetMaxBullet(self, iBulletSID):
        if not cl_item.load.HasBulletType(iBulletSID):
            return 9999
        return self.ReturnMaxBullet(iBulletSID)

    
    def Bullet(self, iBulletSID):
        if iBulletSID not in self.m_Bullet:
            return 0
        return self.m_Bullet[iBulletSID]

    
    def SetBullet(self, iBulletSID, iAmount, iSync = 1):
        if not self.m_Game:
            return None
        if not cl_item.load.HasBulletType(iBulletSID):
            oOwner = self.GetOwner()
            cl_notify.GS2CDebugMsg(self.m_Game, oOwner.m_PlayerID, '不存在的子弹类型%d' % iBulletSID)
            return None
        iMaxAmount = self.GetMaxBullet(iBulletSID)
        if iAmount > iMaxAmount:
            iAmount = iMaxAmount
        self.m_Bullet[iBulletSID] = iAmount
        if iSync:
            self.GS2CRefreshBullet(iBulletSID)

    
    def BulletModify(self, iBulletSID, iCnt, sReason, iSendMsg = 1, iSync = 1, bNotTrueModify = False, iActNum = 0):
        if not self.m_Game:
            return 0
        if not cl_item.load.HasBulletType(iBulletSID):
            oOwner = self.GetOwner()
            cl_notify.GS2CDebugMsg(self.m_Game, oOwner.m_PlayerID, '不存在的子弹类型%d' % iBulletSID)
            return 0
        iCnt = math.ceil(iCnt) if iCnt > 0 else math.floor(iCnt)
        if not iCnt:
            return 0
        oOwner = self.m_Game.GetObject(self.m_Owner)
        dInfo = {
            'SID': iBulletSID,
            'Amount': iCnt }
        cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BAGBULLETCHANGE_BEFOR, oOwner, dInfo)
        iCnt = dInfo['Amount']
        if bNotTrueModify:
            iAddAmount = iCnt
        elif iBulletSID not in self.m_Bullet:
            self.m_Bullet[iBulletSID] = 0
        iMaxBullet = self.GetMaxBullet(iBulletSID)
        iHasBullet = self.m_Bullet[iBulletSID]
        if iHasBullet >= iMaxBullet and iCnt > 0:
            return 0
        iNewBullet = iHasBullet + iCnt
        if iNewBullet < 0:
            iNewBullet = 0
        elif iNewBullet > iMaxBullet:
            iNewBullet = iMaxBullet
        iAddAmount = iNewBullet - iHasBullet
        self.m_Bullet[iBulletSID] = iNewBullet
        if iSync:
            self.GS2CRefreshBullet(iBulletSID)
        if iSendMsg:
            iSubMsg = self.m_CostBulletSubMsg[iBulletSID]
            dMsgInfo = {
                'SID': iBulletSID,
                'Amount': iAddAmount,
                'TotalAddAmount': iCnt,
                'Reason': sReason,
                'ActNum': iActNum }
            cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_BULLETCHANGE, oOwner, dMsgInfo, iSub = iSubMsg)
            if iAddAmount < 0:
                cl_msgcenter.SendMsg(cl_msgcenter.MSG_WAR_COMCOSTBAGBULLET, oOwner, dMsgInfo, iSub = iSubMsg)
        return iAddAmount

    
    def GS2CRefreshBullet(self, iBulletSID, dPlayer = None):
        if iBulletSID not in self.m_Bullet:
            return None
        if not dPlayer:
            dPlayer = {
                self.m_PlayerID: 1 }
        iAmount = self.m_Bullet[iBulletSID]
        iMaxAmount = self.GetMaxBullet(iBulletSID)
        GS2CRefreshBullet(self.m_Game, self.m_Owner, iBulletSID, iAmount, iMaxAmount, dPlayer)


