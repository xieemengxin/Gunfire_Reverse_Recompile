# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_monster/monsterpart.pyc
# RelativePath: clientlogic/cl_monster/monsterpart.pyc
# Source Generated with Decompyle++
# File: monsterpart.pyc (Python 3.6)

from cl_formula import g_DamTypeSequence
import cl_netattr
import cl_monster.mobject
import cl_world
import cl_msgcenter

class CMonsterPart(cl_monster.mobject.CMonster):
    m_Delete = 0
    m_DiePhase = 0
    
    def NetAddTo(self, dPlayer):
        pass

    
    def GetPos(self):
        oOwner = self.m_Game.GetObject(self.m_Owner)
        if oOwner:
            return oOwner.GetPos()
        return super().GetPos()

    
    def OnGoto(self):
        oScene = self.m_Game.m_SceneMgr.GetScene(self.m_Scene)
        dPlayer = oScene.GetPlayers()
        if dPlayer:
            self.PartNetAddTo(dPlayer)

    
    def PartNetAddTo(self, dPlayer):
        cl_netattr.MapMonsterAndPart(self, dPlayer)
        cl_world.CSceneObject.NetAddTo(self, dPlayer)

    
    def Release(self):
        cl_msgcenter.DoneEvent(self, cl_msgcenter.MSG_WAR_DIE, 'CMonsterPart_OnPartDie')
        super().Release()

    
    def InitMonster(self, clsData, dAddData):
        super().InitMonster(clsData, dAddData)
        cl_msgcenter.AddFunction(self, cl_msgcenter.MSG_WAR_DIE, self.OnPartDie, 'CMonsterPart_OnPartDie')

    
    def OnPartDie(self, oPart, dMsgInfo):
        if self.m_DiePhase:
            oOwner = self.m_Game.GetObject(self.m_Owner)
            if oOwner and oOwner.HP() > 0:
                oOwner.SetPhase(self.m_DiePhase)

    
    def OnPartDamage(self, oOwner, dMsgInfo):
        if self.IsDead():
            return None
        oReason = dMsgInfo['RS']
        iAttack = dMsgInfo['AID']
        oAttack = self.m_Game.GetObject(iAttack)
        iPartRatio = dMsgInfo['PartRatio'] if 'PartRatio' in dMsgInfo else 10000
        iBodyRatio = dMsgInfo['BodyRatio'] if 'BodyRatio' in dMsgInfo else 10000
        lstPredictChange = dMsgInfo['PredictChange']
        iExcessChange = dMsgInfo['ExcessChange']
        lstPartChange = dMsgInfo['PartTotalChange']
        iPartExcessChange = dMsgInfo['PartExcessChange']
        iRealChange = 0
        for idx, sAttr, _ in g_DamTypeSequence:
            iPredictChange = lstPredictChange[idx]
            if not iPredictChange:
                continue
            if iPartRatio:
                iPartChage = max(100, iPredictChange * iPartRatio // 10000)
                iTrueChange = -self.TrueModify(sAttr, oAttack, -iPartChage)
                iPartExcessChange += iPartChage - iTrueChange
                lstPartChange[idx] = iTrueChange
                iRealChange += iTrueChange
            iPredictChange = iPredictChange * iBodyRatio // 10000
            lstPredictChange[idx] = max(100, iPredictChange) if iBodyRatio else iPredictChange
        
        dMsgInfo['PartTotalChange'] = lstPartChange
        dMsgInfo['PartExcessChange'] = iPartExcessChange
        dMsgInfo['ExcessChange'] = iExcessChange * iBodyRatio // 10000
        if self.m_HP <= 0:
            self.SetDieFinalInfo(iRealChange, iAttack)
            self.Die(iAttack, oReason)

    
    def MonsterSuper(self, iSuperLevel, iPlusPF, iAfPF):
        pass


