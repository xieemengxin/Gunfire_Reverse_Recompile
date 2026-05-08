# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_perform/cartoon/crt_scantarget.pyc
# RelativePath: clientlogic/cl_perform/cartoon/crt_scantarget.pyc
# Source Generated with Decompyle++
# File: crt_scantarget.pyc (Python 3.6)

from cl_commondefines import PF_TYPE_CHARGE, DEBUG_STATUS_NOCOSTBULLET
from .mobject import CBaseCartoon

class ScanTargetCartoon(CBaseCartoon):
    m_NeedCtrlNet = 0
    
    def IsOver(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if 'Over' in dCartoon:
            oSkill.Send(iNodeID, {
                'Over': 1 })
            return 1
        return 0

    IsOver = classmethod(IsOver)
    
    def InitTraceClient(cls, oSkill, dCartoon, *args, **kwargs):
        pass

    InitTraceClient = classmethod(InitTraceClient)
    
    def HitTargetClient(cls, oSkill, dCartoon):
        iNodeID = dCartoon['ID']
        if iNodeID not in oSkill.m_NetReceive:
            return -1
        dClient = oSkill.m_NetReceive[iNodeID]
        if 'Dict' in dClient:
            dCartoon['Dict'] = dClient['Dict']
            oAttack = oSkill.GetAttack()
            pfobj = oAttack.GetPerform(oSkill.m_Base['pfid'], oSkill.m_Base['Weapon'])
            oSkill.m_Collect['BaseBullet'] = pfobj.m_CurBulletUse
            if pfobj.m_PFType == PF_TYPE_CHARGE:
                pfobj.TrueUsePerform(oAttack, oSkill)
                if oAttack.Query('DebugStatus', 0) & DEBUG_STATUS_NOCOSTBULLET != DEBUG_STATUS_NOCOSTBULLET:
                    pfobj.CostBullet(oAttack, oSkill)
                pfobj.WeaponFire(oAttack, oSkill)
        if 'Over' in dClient:
            dCartoon['Over'] = 1
        dNet = { }
        if 'Trigger' in dClient:
            cls.Trigger(oSkill)
            dNet['Trigger'] = dClient['Trigger']
            oSkill.Send(dCartoon['ID'], dNet)
        return 0

    HitTargetClient = classmethod(HitTargetClient)
    
    def HitTargetServer(cls, oSkill, dCartoon):
        pass

    HitTargetServer = classmethod(HitTargetServer)

