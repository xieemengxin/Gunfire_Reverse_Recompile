# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/summonconfig/c1028.pyc
# RelativePath: clientlogic/cl_platformdata/pc/summonconfig/c1028.pyc
# Source Generated with Decompyle++
# File: c1028.pyc (Python 3.6)

from cl_commondefines import WARRIOR_PHYSXENTITYEFFECT
from cl_newformula import Func205
import cl_wardata.summonaction as summonaction
from . import summonconfigdata

def SummonAction1028(oSummon):
    summonaction.SummonSetDieWithOwner(oSummon, 0)


class CSummonData(summonconfigdata.CSummonData):
    m_DataSID = 1028
    m_Shape = 4241
    m_FightType = WARRIOR_PHYSXENTITYEFFECT
    m_BodyPart = ()
    m_Action = SummonAction1028
    m_BaseAttr = {
        'HPMax': 1,
        'RHP': 0,
        'ArmorMax': 0,
        'ShieldMax': 0,
        'RShield': 0,
        'ShieldRecoverTime': 0,
        'DefPhysical': 0,
        'DefThunder': 0,
        'DefCorrision': 0,
        'DefFire': 0,
        'AccuracyProb': 0,
        'StruckIgnoreFrame': 0,
        'DefKnockBack': 0,
        'KnockBackFrame': 0,
        'DefThump': 0,
        'ThumpFrame': 0,
        'Att': (lambda *a: 400 + (Func205(*a) - 1) * 100),
        'MoveSpeed': 0,
        'AttSpeed': 0,
        'Toughness': 0,
        'TurnSpeed': 0,
        'TurnThresholdAngle': 0,
        'TurnInterval': 0,
        'AdsorbDis': 0,
        'HardEff': 0,
        'SaveTime': 0,
        'DodgeProb': 0,
        'IntervalTime': 0,
        'EnergyMax': 0,
        'REnergy': 0,
        'SpecialMHPWeight': 0,
        'HitRange': 0,
        'Scale': 100 }
    m_PerformList = (4118, 4186)

