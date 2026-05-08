# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/summonconfig/c1059.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/summonconfig/c1059.pyc
# Source Generated with Decompyle++
# File: c1059.pyc (Python 3.6)

from cl_commondefines import WARRIOR_ENTITYEFFECT
from cl_newformula import Func205
import cl_wardata.summonaction as summonaction
from . import summonconfigdata

class CSummonData(summonconfigdata.CSummonData):
    m_DataSID = 1059
    m_Shape = 4253
    m_FightType = WARRIOR_ENTITYEFFECT
    m_BodyPart = ()
    m_Action = None
    m_BaseAttr = {
        'HPMax': (lambda *a: Func205(*a) * 20000 + 40000),
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
        'Att': 6000,
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
    m_PerformList = (4255,)

