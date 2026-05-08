# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterLargeSummon/LargeSummonMove.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterLargeSummon/LargeSummonMove.pyc
# Source Generated with Decompyle++
# File: LargeSummonMove.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'LargeSummonMove',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 23,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseAreaConfigPos, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FlyToPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 23,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 24,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (24011,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 25,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 12,
                    'Class': 'SelectorProbability',
                    'RandomGenerator': None,
                    'Node': [
                        {
                            'ID': 19,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 10,
                            'Node': [
                                {
                                    'ID': 20,
                                    'Class': 'WaitFrame',
                                    'Frames': 0 }] },
                        {
                            'ID': 14,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 12,
                            'Node': [
                                {
                                    'ID': 17,
                                    'Class': 'WaitFrame',
                                    'Frames': 13 }] },
                        {
                            'ID': 15,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 6,
                            'Node': [
                                {
                                    'ID': 18,
                                    'Class': 'WaitFrame',
                                    'Frames': 25 }] }] }] }] }
