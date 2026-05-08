# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterCannon/CannonpatrolPos.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterCannon/CannonpatrolPos.pyc
# Source Generated with Decompyle++
# File: CannonpatrolPos.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'CannonpatrolPos',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 2,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 8,
                    'Class': 'SelectorProbability',
                    'RandomGenerator': None,
                    'Node': [
                        {
                            'ID': 2,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 10,
                            'Node': [
                                {
                                    'ID': 5,
                                    'Class': 'Noop' }] },
                        {
                            'ID': 3,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 10,
                            'Node': [
                                {
                                    'ID': 6,
                                    'Class': 'WaitFrame',
                                    'Frames': 13 }] },
                        {
                            'ID': 4,
                            'Class': 'DecoratorWeight',
                            'DecorateWhenChildEnds': False,
                            'Weight': 10,
                            'Node': [
                                {
                                    'ID': 7,
                                    'Class': 'WaitFrame',
                                    'Frames': 25 }] }] }] }] }
