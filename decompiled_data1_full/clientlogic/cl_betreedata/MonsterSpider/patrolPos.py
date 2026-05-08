# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSpider/patrolPos.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSpider/patrolPos.pyc
# Source Generated with Decompyle++
# File: patrolPos.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'patrolPos',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 16,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 10,
                    'Class': 'SelectorProbability',
                    'RandomGenerator': None,
                    'Node': [
                        {
                            'ID': 11,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 10,
                            'Node': [
                                {
                                    'ID': 14,
                                    'Class': 'Noop' }] },
                        {
                            'ID': 12,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 10,
                            'Node': [
                                {
                                    'ID': 15,
                                    'Class': 'WaitFrame',
                                    'Frames': 13 }] },
                        {
                            'ID': 13,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 10,
                            'Node': [
                                {
                                    'ID': 16,
                                    'Class': 'WaitFrame',
                                    'Frames': 25 }] }] },
                {
                    'ID': 9,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsWarning', 'false')),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetPatrolPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMPatrol, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 7,
                        'Class': 'Effector',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 3,
                        'Flag': 'effector' },),
                    'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'WaitFrame',
                    'Frames': 150 }] }] }
