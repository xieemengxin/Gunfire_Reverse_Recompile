# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/MovingAttack.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/MovingAttack.pyc
# Source Generated with Decompyle++
# File: MovingAttack.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'MovingAttack',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 36,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 63,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChoosePF, (1,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 65,
                    'Class': 'SelectorProbability',
                    'RandomGenerator': None,
                    'Node': [
                        {
                            'ID': 66,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 20,
                            'Node': [
                                {
                                    'ID': 71,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 0,
                                    'Node': [
                                        {
                                            'ID': 72,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 75,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 76,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (12, 4, 6, 60, 90)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 77,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 67,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 10,
                            'Node': [
                                {
                                    'ID': 68,
                                    'Class': 'Parallel',
                                    'FailurePolicy': 1,
                                    'SuccessPolicy': 0,
                                    'ExitPolicy': 1,
                                    'ChildFinishPolicy': 0,
                                    'Node': [
                                        {
                                            'ID': 69,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 70,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToLockEnemy, (10,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 73,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 5,
                            'Node': [
                                {
                                    'ID': 74,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] }] }] }
