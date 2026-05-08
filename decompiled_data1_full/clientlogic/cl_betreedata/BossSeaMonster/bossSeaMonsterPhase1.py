# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossSeaMonster/bossSeaMonsterPhase1.pyc
# RelativePath: clientlogic/cl_betreedata/BossSeaMonster/bossSeaMonsterPhase1.pyc
# Source Generated with Decompyle++
# File: bossSeaMonsterPhase1.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'bossSeaMonsterPhase1',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 52,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 14,
                    'Class': 'SelectorProbability',
                    'RandomGenerator': None,
                    'Node': [
                        {
                            'ID': 15,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 35,
                            'Node': [
                                {
                                    'ID': 12,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.AbsoluteArcMove, (60, 10, 60, 180)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 22,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 35,
                            'Node': [
                                {
                                    'ID': 23,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.AbsoluteArcMove, (60, 10, 60, 170)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 25,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 10,
                            'Node': [
                                {
                                    'ID': 17,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ArcMove, (60, 10, 60, 50)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 13,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 24,
                    'Class': 'WaitFrame',
                    'Frames': 10 },
                {
                    'ID': 11,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
