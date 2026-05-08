# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cs_propdata.pyc
# RelativePath: clientlogic/cs_propdata.pyc
# Source Generated with Decompyle++
# File: cs_propdata.pyc (Python 3.6)

QUERY_GET = 0
ATTR_GET = 1
FUNC_GET = 2
QUERYATTR_GET = 3
OTHER_GET = 4
ATTRBASE_GET = 5
QUERYATTR_NETGET = 6
QUERYATTR_FORECAST = 7
CLASS_GET = 8
SPECIALATTR_GET = 9
TYPE_INTEGER = 0
TYPE_VARCHAR = 1
TYPE_VECTOR = 2
TYPE_FLOAT = 3
TYPE_INT100 = 4
TYPE_FORECASTATTR = 5
TYPE_FORECASTVAR = 6
TYPE_ENHANCE = 7
TYPE_INTD100 = 8
TYPE_LONG = 9
TYPE_NEWVECTOR = 10
TYPE_LONGD100 = 11
BASIC_PROP_LIST = ([
    1,
    'ID',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    2,
    'Sex',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    3,
    'Photo',
    TYPE_INTEGER,
    2,
    ATTR_GET], [
    4,
    'Shape',
    TYPE_INTEGER,
    2,
    FUNC_GET], [
    5,
    'Name',
    TYPE_VARCHAR,
    28,
    FUNC_GET], [
    6,
    'Exp',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    7,
    'ExpNext',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    8,
    'Cash',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    9,
    'Grade',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    10,
    'NameIdx',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    11,
    'GetGold',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    12,
    'Switch',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    13,
    'SID',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    14,
    'Side',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    15,
    'Speed',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    16,
    'AttSpeed',
    TYPE_INTEGER,
    4,
    QUERYATTR_GET], [
    17,
    'BAttSpeed',
    TYPE_INTEGER,
    4,
    ATTRBASE_GET], [
    18,
    'HP',
    TYPE_LONGD100,
    5,
    FUNC_GET], [
    19,
    'HPMax',
    TYPE_LONGD100,
    5,
    QUERYATTR_GET], [
    20,
    'RHP',
    TYPE_INT100,
    4,
    QUERYATTR_GET], [
    21,
    'Armor',
    TYPE_LONGD100,
    5,
    FUNC_GET], [
    22,
    'ArmorMax',
    TYPE_LONGD100,
    5,
    QUERYATTR_GET], [
    23,
    'Att',
    TYPE_INT100,
    4,
    QUERYATTR_GET], [
    24,
    'FightMark',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    25,
    'MoveStatus',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    26,
    'ShootStatus',
    TYPE_FORECASTVAR,
    4,
    QUERYATTR_FORECAST], [
    27,
    'FightStatus',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    28,
    'CurWeapon',
    TYPE_VECTOR,
    16,
    FUNC_GET], [
    29,
    'Desc',
    TYPE_VECTOR,
    12,
    FUNC_GET], [
    30,
    'SnipeShape',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    31,
    'LifeTime',
    TYPE_INTEGER,
    2,
    FUNC_GET], [
    32,
    'Shield',
    TYPE_LONGD100,
    5,
    FUNC_GET], [
    33,
    'RShield',
    TYPE_INT100,
    4,
    FUNC_GET], [
    34,
    'ShieldMax',
    TYPE_LONGD100,
    5,
    FUNC_GET], [
    35,
    'DefPhysical',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    36,
    'DefFire',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    37,
    'DefThunder',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    38,
    'DefCorrision',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    39,
    'DeputyWeapon',
    TYPE_VECTOR,
    16,
    FUNC_GET], [
    40,
    'ShieldStatus',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    41,
    'ActionType',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    42,
    'CrazyEff',
    TYPE_INTEGER,
    4,
    QUERYATTR_GET], [
    43,
    'AdsorbDis',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    44,
    'WarCash',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    45,
    'WarGrade',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    46,
    'Abandoner',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    47,
    'ShieldRecoverTime',
    TYPE_INT100,
    4,
    QUERYATTR_GET], [
    48,
    'InteractStatus',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    50,
    'LockEnemy',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    51,
    'Dead',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    52,
    'ClientOwner',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    53,
    'ClientSummonID',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    54,
    'Phase',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    55,
    'Owner',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    56,
    'SrcWeapon',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    57,
    'SrcPerform',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    58,
    'AttachPart',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    59,
    'AttachTarget',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    60,
    'RollTime',
    TYPE_INTEGER,
    2,
    FUNC_GET], [
    61,
    'SuperLevel',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    62,
    'WarGSCash',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    63,
    'Scene',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    64,
    'TeamPos',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    65,
    'Online',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    66,
    'TurnThresholdAngle',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    67,
    'TurnInterval',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    68,
    'SaveTime',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    69,
    'RandomSeed',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    70,
    'DebugStatus',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    71,
    'DropReason',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    72,
    'MonsterDrop',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    73,
    'DyingTimes',
    TYPE_INTEGER,
    1,
    OTHER_GET], [
    74,
    'MaxRelicNum',
    TYPE_INTEGER,
    2,
    FUNC_GET], [
    75,
    'Energy',
    TYPE_INT100,
    4,
    FUNC_GET], [
    76,
    'REnergy',
    TYPE_INT100,
    4,
    FUNC_GET], [
    77,
    'EnergyMax',
    TYPE_INT100,
    4,
    FUNC_GET], [
    78,
    'EnergyStatus',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    79,
    'EnergyCost',
    TYPE_INT100,
    4,
    QUERY_GET], [
    80,
    'DeadPunishmentTimes',
    TYPE_INTEGER,
    1,
    OTHER_GET], [
    81,
    'RestDyingSecond',
    TYPE_INTEGER,
    1,
    OTHER_GET], [
    82,
    'Source',
    TYPE_LONG,
    8,
    ATTR_GET], [
    83,
    'InteractDis',
    TYPE_FLOAT,
    2,
    ATTR_GET], [
    84,
    'RollLineID',
    TYPE_INTEGER,
    2,
    ATTR_GET], [
    85,
    'CurseRelic',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    86,
    'HitRange',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    87,
    'Scale',
    TYPE_INT100,
    4,
    QUERY_GET], [
    88,
    'FightIndex',
    TYPE_INTEGER,
    4,
    QUERY_GET], [
    89,
    'MaxGrade',
    TYPE_INTEGER,
    2,
    ATTR_GET], [
    90,
    'RollRelicCnt',
    TYPE_INTEGER,
    1,
    OTHER_GET], [
    91,
    'MaxRelicRollNum',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    92,
    'Resistance',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    93,
    'ActionSpeed',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    94,
    'MagicPower',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    95,
    'RelicChooseAllCnt',
    TYPE_INTEGER,
    1,
    OTHER_GET], [
    96,
    'Share',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    97,
    'DeviceEnergy',
    TYPE_INT100,
    4,
    FUNC_GET], [
    98,
    'MaxDeviceEnergy',
    TYPE_INT100,
    4,
    QUERYATTR_GET], [
    99,
    'RDeviceEnergy',
    TYPE_INT100,
    4,
    QUERYATTR_GET], [
    100,
    'DeployStatus',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    101,
    'ActiveStatus',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    102,
    'ModelScale',
    TYPE_VECTOR,
    12,
    ATTR_GET], [
    103,
    'DeviceEnergyStatus',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    104,
    'ConquerStatus',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    105,
    'RelifeTime',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    106,
    'SkillInterval',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    107,
    'SpecialMHPWeight',
    TYPE_INTEGER,
    2,
    QUERYATTR_GET], [
    108,
    'MaxCloneNum',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    109,
    'SublimeCash',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    110,
    'ExcessHP',
    TYPE_LONGD100,
    5,
    FUNC_GET], [
    111,
    'ExcessShield',
    TYPE_LONGD100,
    5,
    FUNC_GET], [
    112,
    'ExcessArmor',
    TYPE_LONGD100,
    5,
    FUNC_GET], [
    113,
    'ExtendBag',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    114,
    'DisableTalent',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    115,
    'ComAtt',
    TYPE_INT100,
    4,
    QUERYATTR_GET], [
    116,
    'DebuffFactor',
    TYPE_INT100,
    4,
    QUERYATTR_GET], [
    117,
    'BurstCount',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    118,
    'ChargeSpeed',
    TYPE_INTEGER,
    4,
    QUERYATTR_GET], [
    119,
    'JumpHeight',
    TYPE_INT100,
    4,
    QUERYATTR_GET], [
    120,
    'AllLifeTime',
    TYPE_INTEGER,
    4,
    FUNC_GET])
PLAYER_PROP_INIT = ('Name', 'Cash', 'GetGold', 'Grade', 'FightIndex', 'MaxGrade', 'SublimeCash')
HERO_PROP_INIT = ('SID', 'Shape', 'Name', 'Side', 'Speed', 'Scene', 'HP', 'HPMax', 'RHP', 'Armor', 'ArmorMax', 'Shield', 'ShieldMax', 'RShield', 'ShootStatus', 'ShieldStatus', 'CurWeapon', 'DeputyWeapon', 'Dead', 'TeamPos', 'Desc', 'Online', 'SaveTime', 'DyingTimes', 'MaxRelicNum', 'DeadPunishmentTimes', 'RestDyingSecond', 'FightMark', 'ExcessHP', 'ExcessShield', 'ExcessArmor')
HERO_PROP_EXT = ('DefPhysical', 'DefFire', 'DefThunder', 'DefCorrision', 'AdsorbDis', 'WarCash', 'WarGrade', 'ClientSummonID', 'WarGSCash', 'RandomSeed', 'DebugStatus', 'Energy', 'REnergy', 'EnergyMax', 'EnergyStatus', 'EnergyCost', 'CurseRelic', 'RollRelicCnt', 'MaxRelicRollNum', 'Resistance', 'MagicPower', 'RelicChooseAllCnt', 'DeviceEnergy', 'MaxDeviceEnergy', 'RDeviceEnergy', 'DeviceEnergyStatus', 'ExtendBag', 'DisableTalent', 'DebuffFactor', 'BurstCount', 'ChargeSpeed', 'JumpHeight')
NPC_PROP_INIT = ('Shape', 'SID', 'ActionType', 'Side', 'InteractDis', 'Share')
CARNPC_PROP_INIT = ('Shape', 'SID', 'ActionType', 'Side', 'Speed', 'Phase', 'InteractDis', 'Share')
GOLDENCUP_PROP_INIT = ('Shape', 'SID', 'ActionType', 'Side', 'Abandoner', 'InteractDis', 'Share')
HOOKROPE_PROP_INIT = ('Shape', 'SID', 'ActionType', 'Side', 'AttachTarget', 'InteractDis')
BUILD_PROP_INIT = ('SID', 'HP', 'Shape', 'Side', 'HPMax')
STONE_BUILD_PROP_INIT = ('SID', 'HP', 'Shape', 'Side', 'RollTime', 'RollLineID')
SUMMON_PROP_INIT = ('Shape', 'SID', 'Speed', 'LifeTime', 'Side', 'ClientOwner', 'Owner', 'HP', 'HPMax', 'Shield', 'ShieldMax', 'Armor', 'ArmorMax', 'AttachTarget', 'ClientSummonID', 'Scale')
BEACON_SUMMON_PROP_INIT = ('Shape', 'SID', 'Speed', 'LifeTime', 'Side', 'Owner', 'SrcWeapon', 'SrcPerform', 'AttachPart', 'AttachTarget')
AIRFOLLOWEFFECT_SUMMON_PROP_INIT = ('Shape', 'SID', 'Speed', 'Side', 'ClientOwner', 'Owner', 'HP', 'HPMax', 'Scale')
AIRFOLLOWEFFECT_SUMMON_PROP_EXT = ('LifeTime', 'AllLifeTime')
MONSTER_PROP_INIT = ('Shape', 'SID', 'Side', 'HP', 'HPMax', 'AttSpeed', 'Speed', 'RHP', 'Armor', 'ArmorMax', 'Att', 'FightMark', 'MoveStatus', 'FightStatus', 'LockEnemy', 'ShieldStatus', 'Shield', 'RShield', 'ShieldMax', 'Grade', 'Phase', 'SuperLevel', 'Dead', 'TurnThresholdAngle', 'TurnInterval', 'Owner', 'Energy', 'EnergyMax', 'ActionSpeed', 'ConquerStatus', 'Scale', 'ExcessHP', 'ExcessShield', 'ExcessArmor')
DROPS_PROP_INIT = ('SID', 'Shape', 'Abandoner', 'DropReason', 'Source')
EQUIPDROPS_PROP_INIT = ('SID', 'Shape', 'Abandoner', 'DropReason', 'MonsterDrop', 'Source')
SERVANT_PROP_INIT = ('Shape', 'SID', 'Side', 'HP', 'HPMax', 'AttSpeed', 'Speed', 'RHP', 'Armor', 'ArmorMax', 'LockEnemy', 'ShieldStatus', 'Shield', 'RShield', 'ShieldMax', 'Dead', 'RestDyingSecond', 'Phase', 'Scale')
DEVICE_PROP_INIT = ('Shape', 'SID', 'Side', 'Owner', 'Scene', 'DeployStatus', 'ActiveStatus', 'Phase', 'Speed', 'AttSpeed')
POISON_DEVICE_PROP_INIT = ('Shape', 'SID', 'Side', 'Owner', 'Scene', 'DeployStatus', 'ActiveStatus', 'AttachPart', 'AttachTarget')
BARRIER_DEVICE_PROP_INIT = ('Shape', 'SID', 'Side', 'Owner', 'Scene', 'DeployStatus', 'ActiveStatus', 'ModelScale', 'Phase')
PET_PROP_SHOW = ('SID', 'HPMax', 'Att', 'Speed', 'AttSpeed', 'RelifeTime', 'SkillInterval', 'HP', 'RHP', 'Dead')
PET_PROP_INIT = ('Shape', 'SID', 'Side', 'HP', 'HPMax', 'AttSpeed', 'Speed', 'RHP', 'Dead', 'RestDyingSecond', 'LockEnemy', 'MoveStatus', 'Att', 'FightStatus', 'Phase', 'Owner', 'RelifeTime', 'SkillInterval', 'Scale', 'MaxCloneNum')
PET_PROP_FINISHWAR = ('HPMax', 'AttSpeed', 'Speed', 'Att', 'RelifeTime', 'SkillInterval')
PLANT_PROP_INIT = ('Shape', 'SID', 'Side', 'HP', 'HPMax', 'AttSpeed', 'LockEnemy', 'Dead', 'Phase', 'HitRange', 'Scale')
INFO_PROP_LIST = ([
    1,
    'SID',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    2,
    'Shape',
    TYPE_INTEGER,
    2,
    FUNC_GET], [
    3,
    'Amount',
    TYPE_INTEGER,
    4,
    FUNC_GET], [
    4,
    'Grade',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    5,
    'AttSpeed',
    TYPE_FORECASTATTR,
    4,
    QUERYATTR_FORECAST], [
    6,
    'Att',
    TYPE_INT100,
    4,
    QUERYATTR_NETGET], [
    7,
    'ElementType',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    8,
    'Accuracy',
    TYPE_FORECASTATTR,
    4,
    QUERYATTR_FORECAST], [
    9,
    'Stability',
    TYPE_FORECASTATTR,
    4,
    QUERYATTR_FORECAST], [
    10,
    'CrazyEff',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    11,
    'CurBullet',
    TYPE_INTEGER,
    2,
    OTHER_GET], [
    12,
    'MaxBullet',
    TYPE_INTEGER,
    2,
    QUERYATTR_NETGET], [
    13,
    'FillTime',
    TYPE_FORECASTATTR,
    4,
    QUERYATTR_FORECAST], [
    14,
    'FillPerform',
    TYPE_INTEGER,
    2,
    OTHER_GET], [
    15,
    'Radius',
    TYPE_FLOAT,
    2,
    QUERYATTR_NETGET], [
    16,
    'Quality',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    17,
    'UnwieldTime',
    TYPE_INTEGER,
    2,
    QUERYATTR_NETGET], [
    18,
    'WieldTime',
    TYPE_INTEGER,
    2,
    QUERYATTR_NETGET], [
    19,
    'AttDis',
    TYPE_FLOAT,
    4,
    QUERYATTR_NETGET], [
    20,
    'BulletSpeed',
    TYPE_FLOAT,
    4,
    QUERYATTR_NETGET], [
    21,
    'RShield',
    TYPE_INT100,
    4,
    FUNC_GET], [
    22,
    'ShieldMax',
    TYPE_INT100,
    4,
    FUNC_GET], [
    23,
    'ShieldStatus',
    TYPE_INTEGER,
    1,
    QUERY_GET], [
    24,
    'ThrowInterval',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    25,
    'ExplodeDelay',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    26,
    'SnipeFov',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    27,
    'SnipeTime',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    28,
    'Trajectory',
    TYPE_INTEGER,
    2,
    QUERYATTR_NETGET], [
    29,
    'BulletVerticalAcc',
    TYPE_FLOAT,
    4,
    QUERYATTR_NETGET], [
    30,
    'ShieldRecoverTime',
    TYPE_INT100,
    4,
    QUERYATTR_NETGET], [
    31,
    'ColdTime',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    32,
    'Pierce',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    33,
    'BulletUse',
    TYPE_INTEGER,
    1,
    FUNC_GET], [
    34,
    'BulletSID',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    35,
    'AddStateTime',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    36,
    'MaxCover',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    37,
    'BallisticType',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    38,
    'Inscription',
    TYPE_VECTOR,
    24,
    OTHER_GET], [
    39,
    'MaxGrade',
    TYPE_INTEGER,
    4,
    ATTR_GET], [
    40,
    'AttDistance',
    TYPE_FLOAT,
    2,
    QUERYATTR_NETGET], [
    41,
    'AttPerformIdx',
    TYPE_INTEGER,
    1,
    OTHER_GET], [
    42,
    'HPConsumption',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    43,
    'FillPerformID',
    TYPE_INTEGER,
    4,
    OTHER_GET], [
    44,
    'DebuffProb',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    45,
    'ChargeTime',
    TYPE_FORECASTATTR,
    4,
    QUERYATTR_FORECAST], [
    46,
    'BulletState',
    TYPE_INTEGER,
    1,
    OTHER_GET], [
    47,
    'Enable',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    48,
    'Pos',
    TYPE_INTEGER,
    1,
    OTHER_GET], [
    49,
    'Target',
    TYPE_INTEGER,
    4,
    OTHER_GET], [
    50,
    'LuckyHit',
    TYPE_INTEGER,
    2,
    QUERYATTR_NETGET], [
    51,
    'PFBulletUse',
    TYPE_INTEGER,
    2,
    QUERYATTR_NETGET], [
    52,
    'CurPFBullet',
    TYPE_INTEGER,
    2,
    FUNC_GET], [
    53,
    'MaxPFBullet',
    TYPE_INTEGER,
    2,
    FUNC_GET], [
    54,
    'KeepTime',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    55,
    'DamInterval',
    TYPE_INTEGER,
    4,
    QUERYATTR_NETGET], [
    56,
    'AddInscriptionTimes',
    TYPE_INTEGER,
    1,
    OTHER_GET], [
    57,
    'Level',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    58,
    'Enhance',
    TYPE_ENHANCE,
    1,
    OTHER_GET], [
    59,
    'SealedInscription',
    TYPE_VECTOR,
    12,
    OTHER_GET], [
    60,
    'ExtGradeGroup',
    TYPE_ENHANCE,
    1,
    OTHER_GET], [
    61,
    'RollNum',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    62,
    'EnergyBar',
    TYPE_INTEGER,
    2,
    SPECIALATTR_GET], [
    63,
    'ExplodeControl',
    TYPE_INT100,
    4,
    SPECIALATTR_GET], [
    64,
    'DisableInscription',
    TYPE_NEWVECTOR,
    1,
    OTHER_GET], [
    65,
    'CanUseCount',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    66,
    'MultipleExplodeCnt',
    TYPE_INTEGER,
    1,
    QUERYATTR_NETGET], [
    67,
    'Share',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    68,
    'EnergyCost',
    TYPE_INT100,
    2,
    QUERYATTR_NETGET], [
    69,
    'TriggerTimes',
    TYPE_INTEGER,
    1,
    QUERYATTR_NETGET], [
    70,
    'StartUpControl',
    TYPE_INTEGER,
    2,
    SPECIALATTR_GET], [
    71,
    'CommonMaxCount',
    TYPE_INTEGER,
    2,
    QUERYATTR_NETGET], [
    72,
    'PFBulletRecover',
    TYPE_INTEGER,
    2,
    QUERYATTR_NETGET], [
    73,
    'PFBulletRecoverMul',
    TYPE_INTEGER,
    2,
    QUERYATTR_NETGET], [
    74,
    'PFBulletCostMul',
    TYPE_INTEGER,
    2,
    QUERYATTR_NETGET], [
    75,
    'BulletSize',
    TYPE_INT100,
    2,
    SPECIALATTR_GET], [
    76,
    'CliModeIdx',
    TYPE_INTEGER,
    1,
    OTHER_GET], [
    77,
    'MaxTarget',
    TYPE_INTEGER,
    2,
    OTHER_GET], [
    78,
    'ShareInscription',
    TYPE_NEWVECTOR,
    1,
    OTHER_GET], [
    79,
    'PointRange',
    TYPE_NEWVECTOR,
    1,
    ATTR_GET], [
    80,
    'RollPoint',
    TYPE_INTEGER,
    1,
    ATTR_GET], [
    81,
    'MinUseEnergy',
    TYPE_INT100,
    2,
    QUERYATTR_NETGET], [
    82,
    'FillBulletCnt',
    TYPE_INTEGER,
    1,
    QUERYATTR_GET], [
    83,
    'DefaultPoint',
    TYPE_INTEGER,
    1,
    ATTR_GET])
ITEM_PROP_INIT = ('Grade', 'SID', 'Shape', 'Amount')
WEAPON_PROP_INIT = ('Grade', 'SID', 'Shape')
MAINWEAPON_PROP_INIT = ('Grade', 'SID', 'Shape', 'Quality', 'CurBullet', 'Att', 'AttSpeed', 'MaxBullet', 'FillTime', 'FillPerform', 'ElementType', 'Accuracy', 'Stability', 'UnwieldTime', 'WieldTime', 'AttDis', 'BulletSpeed', 'SnipeFov', 'SnipeTime', 'Trajectory', 'Pierce', 'BulletVerticalAcc', 'BulletState', 'ExtGradeGroup', 'BallisticType', 'Inscription', 'MaxGrade', 'AttPerformIdx', 'FillPerformID', 'DebuffProb', 'CrazyEff', 'Radius', 'LuckyHit', 'AddInscriptionTimes', 'Enhance', 'SealedInscription', 'DisableInscription', 'MultipleExplodeCnt', 'ShareInscription', 'CliModeIdx')
SHIELD_PROP_INIT = ('Grade', 'SID', 'Shape', 'ShieldStatus', 'ShieldMax', 'RShield', 'ShieldRecoverTime')
DROPITEM_MAINWEAPON_PROP_INIT = ('SID', 'Shape', 'Grade', 'Quality', 'Att', 'AttSpeed', 'MaxBullet', 'Accuracy', 'Inscription', 'MaxGrade', 'DebuffProb', 'CrazyEff', 'Trajectory', 'FillTime', 'ElementType', 'LuckyHit', 'Enhance', 'SealedInscription', 'ExtGradeGroup', 'DisableInscription', 'Radius', 'ShareInscription')
DROPITEM_RELIC_PROP_INIT = ('SID', 'Level', 'RollNum', 'Share')
DROPITEM_DEMON_PROP_INIT = ('SID', 'Quality')
DROPITEM_MAGICPOWER_PROP_INIT = ('SID', 'Shape')
DROPITEM_DEVICECOMP_PROP_INIT = ('SID',)
RELIC_PROP_INIT = ('SID', 'Level', 'RollNum')
TALENT_PROP_INIT = ('SID', 'Level')
PERFORM_PROP_INIT = ('SID', 'Enable')
SHOOTPERFORM_PROP_INIT = ('SID', 'Enable', 'BulletUse', 'ChargeTime', 'PFBulletUse', 'CurPFBullet', 'MaxPFBullet', 'TriggerTimes', 'CommonMaxCount')
THROWPERFORM_PROP_INIT = ('SID', 'Enable', 'Att', 'BulletSpeed', 'ExplodeDelay', 'ThrowInterval', 'Radius', 'ElementType', 'BulletVerticalAcc', 'ColdTime', 'BulletSID', 'AddStateTime', 'KeepTime', 'DamInterval', 'BulletUse', 'Pierce', 'TriggerTimes', 'MinUseEnergy')
CAREERPERFORM_PROP_INIT = ('SID', 'Enable', 'Att', 'BulletSpeed', 'ExplodeDelay', 'ThrowInterval', 'Radius', 'ElementType', 'BulletVerticalAcc', 'ColdTime', 'MaxCover', 'AttDistance', 'AddStateTime', 'DamInterval', 'Pierce', 'PFBulletUse', 'CurPFBullet', 'MaxPFBullet', 'MinUseEnergy')
FILLPERFORM_PROP_INIT = ('SID', 'Enable', 'HPConsumption')
CLIENTACTIVE_PROP_INIT = ('SID', 'Enable', 'CanUseCount', 'AttDistance', 'MaxCover')
COMMONACTIVE_PROP_INIT = ('SID', 'Enable', 'Radius')
DEVICEACTIVE_PROP_INIT = ('SID', 'Enable', 'Radius', 'EnergyCost', 'TriggerTimes')
PETACTIVE_PROP_INIT = ('SID', 'Enable', 'Radius')
SUITACTIVE_PROP_INIT = ('SID', 'Enable', 'ColdTime', 'MaxCover')
WATCHACTIVE_PROP_INIT = ('SID', 'Enable', 'ColdTime', 'MaxCover')
S8THIRDACTIVE_PROP_INIT = ('SID', 'Enable', 'Radius', 'ColdTime')
ITEM_BROADCAST_PROP = ('Grade',)
WEAPON_SHARE_PROP = ('Inscription', 'Grade', 'Att', 'CrazyEff', 'MaxBullet', 'DisableInscription', 'ShareInscription')
WANDCOMP_PROP_INIT = ('SID', 'Level')
DICE_PROP_INIT = ('SID', 'Quality', 'PointRange', 'RollPoint')
DICESPECIALITEM_PROP_INIT = ('SID',)
S7MODULE_PROP_INIT = ('SID', 'Quality', 'DefaultPoint')
S7CRYSTAL_PROP_INIT = ('SID',)
S8THIRDPFITEM_PROP_INIT = ('SID', 'Quality')
S8GEMITEM_PROP_INIT = ('SID', 'Quality')
BASIC_PROP_NAME = { }
INFO_PROP_NAME = { }
BASIC_PROP_DICT = { }
INFO_PROP_DICT = { }
PC_SEND_BC = 1
PC_SEND_SBC = 2
PC_SEND_SELF = 4
PROP_NONE = 0
PROP_HERO = 1
PROP_MONSTER = 2
PROP_SUMMON = 3
PROP_NPC = 4
PROP_DROPS = 5
PROP_BUILD = 6
PROP_BEACONSUMMON = 7
PROP_STONEBUILD = 8
PROP_CARNPC = 9
PROP_GOLDENCUP = 10
PROP_EQUIPDROPS = 11
PROP_TALENT = 12
PROP_SERVANT = 13
PROP_RELIC = 14
PROP_DEVICE = 15
PROP_POISON_DEVICE = 16
PROP_BARRIER_DEVICE = 17
PROP_PET = 19
PROP_HOOKROPECUP = 20
PROP_PET_FINISHWAR = 21
PROP_PLANT = 22
PROP_AIRFOLLOWEFFECT = 23
PROP_ITEM = 15
PROP_MAINWEAPON = 16
PROP_DICE = 17
PROP_PET_SHOW = 18
PROP_WANDCOMP = 19
PROP_PERFORM = 20
PROP_THROWPERFORM = 21
PROP_SHOOTPERFORM = 22
PROP_CAREERPERFORM = 23
PROP_FILLPERFORM = 24
PROP_CLIENTACTIVEPERFORM = 25
PROP_COMMONACTIVEPERFORM = 26
PROP_DEVICEACTIVEPERFORM = 27
PROP_PETACTIVEPERFORM = 28
PROP_SUITACTIVEPERFORM = 29
PROP_DROPITEM_MAINWEAPON = 30
PROP_DROPITEM_RELIC = 33
PROP_DROPITEM_DEMON = 34
PROP_DROPITEM_MAGICPOWER = 35
PROP_DROPITEM_DEVICECOMP = 36
PROP_DROPITEM_DICESPECIALITEM = 38
PROP_DROPITEM_S7MODULE = 39
PROP_DROPITEM_S7CRYSTAL = 40
PROP_DROPITEM_S8THITDPFITEM = 42
PROP_DROPITEM_S8GEMITEM = 43
PROP_WATCHACTIVEPERFORM = 37
PROP_S8THIRDACTIVEPERFORM = 41
PROP_PLAYER = 50
PROP_BASIC_SINGLE = 100
PROP_INFO_SINGLE = 101
BASIC_OBJECT_INIT = {
    PROP_AIRFOLLOWEFFECT: AIRFOLLOWEFFECT_SUMMON_PROP_INIT,
    PROP_PLANT: PLANT_PROP_INIT,
    PROP_PET: PET_PROP_INIT,
    PROP_BARRIER_DEVICE: BARRIER_DEVICE_PROP_INIT,
    PROP_POISON_DEVICE: POISON_DEVICE_PROP_INIT,
    PROP_DEVICE: DEVICE_PROP_INIT,
    PROP_SERVANT: SERVANT_PROP_INIT,
    PROP_STONEBUILD: STONE_BUILD_PROP_INIT,
    PROP_BUILD: BUILD_PROP_INIT,
    PROP_EQUIPDROPS: EQUIPDROPS_PROP_INIT,
    PROP_DROPS: DROPS_PROP_INIT,
    PROP_HOOKROPECUP: HOOKROPE_PROP_INIT,
    PROP_GOLDENCUP: GOLDENCUP_PROP_INIT,
    PROP_CARNPC: CARNPC_PROP_INIT,
    PROP_NPC: NPC_PROP_INIT,
    PROP_BEACONSUMMON: BEACON_SUMMON_PROP_INIT,
    PROP_SUMMON: SUMMON_PROP_INIT,
    PROP_MONSTER: MONSTER_PROP_INIT,
    PROP_HERO: HERO_PROP_INIT,
    PROP_PLAYER: PLAYER_PROP_INIT }
INFO_OBJECT_INIT = {
    PROP_DROPITEM_S8GEMITEM: S8GEMITEM_PROP_INIT,
    PROP_DROPITEM_S8THITDPFITEM: S8THIRDPFITEM_PROP_INIT,
    PROP_DROPITEM_S7CRYSTAL: S7CRYSTAL_PROP_INIT,
    PROP_DROPITEM_S7MODULE: S7MODULE_PROP_INIT,
    PROP_DROPITEM_DICESPECIALITEM: DICESPECIALITEM_PROP_INIT,
    PROP_DROPITEM_DEVICECOMP: DROPITEM_DEVICECOMP_PROP_INIT,
    PROP_DROPITEM_MAGICPOWER: DROPITEM_MAGICPOWER_PROP_INIT,
    PROP_DROPITEM_DEMON: DROPITEM_DEMON_PROP_INIT,
    PROP_DROPITEM_RELIC: DROPITEM_RELIC_PROP_INIT,
    PROP_DROPITEM_MAINWEAPON: DROPITEM_MAINWEAPON_PROP_INIT,
    PROP_DICE: DICE_PROP_INIT,
    PROP_WANDCOMP: WANDCOMP_PROP_INIT,
    PROP_S8THIRDACTIVEPERFORM: S8THIRDACTIVE_PROP_INIT,
    PROP_WATCHACTIVEPERFORM: WATCHACTIVE_PROP_INIT,
    PROP_SUITACTIVEPERFORM: SUITACTIVE_PROP_INIT,
    PROP_PETACTIVEPERFORM: PETACTIVE_PROP_INIT,
    PROP_DEVICEACTIVEPERFORM: DEVICEACTIVE_PROP_INIT,
    PROP_COMMONACTIVEPERFORM: COMMONACTIVE_PROP_INIT,
    PROP_CLIENTACTIVEPERFORM: CLIENTACTIVE_PROP_INIT,
    PROP_FILLPERFORM: FILLPERFORM_PROP_INIT,
    PROP_CAREERPERFORM: CAREERPERFORM_PROP_INIT,
    PROP_THROWPERFORM: THROWPERFORM_PROP_INIT,
    PROP_SHOOTPERFORM: SHOOTPERFORM_PROP_INIT,
    PROP_PERFORM: PERFORM_PROP_INIT,
    PROP_PET_SHOW: PET_PROP_SHOW,
    PROP_RELIC: RELIC_PROP_INIT,
    PROP_TALENT: TALENT_PROP_INIT,
    PROP_MAINWEAPON: MAINWEAPON_PROP_INIT,
    PROP_ITEM: ITEM_PROP_INIT }
INFO_OBJECT_FINISHWAR = {
    PROP_PET_FINISHWAR: PET_PROP_FINISHWAR }
BASIC_OBJECT_EXT = {
    PROP_AIRFOLLOWEFFECT: AIRFOLLOWEFFECT_SUMMON_PROP_EXT,
    PROP_HERO: HERO_PROP_EXT }

def MyInit():
    for idx, info in enumerate(BASIC_PROP_LIST):
        BASIC_PROP_NAME[info[1]] = info
    
    BASIC_PROP_NAME['MoveSpeed'] = BASIC_PROP_NAME['Speed']
    for idx, info in enumerate(INFO_PROP_LIST):
        INFO_PROP_NAME[info[1]] = info
    
    for info in BASIC_PROP_LIST:
        BASIC_PROP_DICT[info[1]] = (info[2], info[4])
    
    for info in INFO_PROP_LIST:
        INFO_PROP_DICT[info[1]] = (info[2], info[4])
    

MyInit()
