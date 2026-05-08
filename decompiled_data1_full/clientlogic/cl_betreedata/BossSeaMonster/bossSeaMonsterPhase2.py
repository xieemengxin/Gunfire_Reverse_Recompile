# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossSeaMonster/bossSeaMonsterPhase2.pyc
# RelativePath: clientlogic/cl_betreedata/BossSeaMonster/bossSeaMonsterPhase2.pyc
# Source Generated with Decompyle++
# File: bossSeaMonsterPhase2.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'bossSeaMonsterPhase2',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 22,
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
                    'ID': 34,
                    'Class': 'SelectorProbability',
                    'RandomGenerator': None,
                    'Node': [
                        {
                            'ID': 43,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 30,
                            'Node': [
                                {
                                    'ID': 44,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.AbsoluteArcMove, (60, 10, 60, 130)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 35,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 30,
                            'Node': [
                                {
                                    'ID': 37,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.AbsoluteArcMove, (60, 10, 60, 120)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 36,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 20,
                            'Node': [
                                {
                                    'ID': 42,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ArcMove, (60, 10, 60, 50)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 20,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' },),
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 45,
                    'Class': 'WaitFrame',
                    'Frames': 10 },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.TurnToLockEnemy, (0, 1)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 10,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.UsePerformGroup, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
