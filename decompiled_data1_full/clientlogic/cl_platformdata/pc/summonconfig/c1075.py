# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/summonconfig/c1075.pyc
# RelativePath: clientlogic/cl_platformdata/pc/summonconfig/c1075.pyc
# Source Generated with Decompyle++
# File: c1075.pyc (Python 3.6)

from cl_commondefines import WARRIOR_MOVEEFFECT
from cl_newformula import Func205
import cl_wardata.summonaction as summonaction
from . import summonconfigdata

def SummonAction1075(oSummon):
    summonaction.SummonSetDieWithOwner(oSummon, 0)


class CSummonData(summonconfigdata.CSummonData):
    m_DataSID = 1075
    m_Shape = 4266
    m_FightType = WARRIOR_MOVEEFFECT
    m_BodyPart = ()
    m_Action = SummonAction1075
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
        'Att': (lambda *a: 500 + (Func205(*a) - 1) * 100),
        'MoveSpeed': (lambda *a: (Func205(*a) - 1) * 75 + 550),
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
    m_PerformList = (4180, 4187, 14601)

