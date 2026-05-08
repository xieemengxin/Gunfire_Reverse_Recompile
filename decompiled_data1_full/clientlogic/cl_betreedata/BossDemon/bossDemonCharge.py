# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossDemon/bossDemonCharge.pyc
# RelativePath: clientlogic/cl_betreedata/BossDemon/bossDemonCharge.pyc
# Source Generated with Decompyle++
# File: bossDemonCharge.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'bossDemonCharge',
    'ID': 0,
    'AgentType': '',
    'IsFSM': False,
    'Ver': 7,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseHateTarget, (10,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 24,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.ChooseCertainPF, (39246,)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 7,
                    'Class': 'Action',
                    'Attachment': ({
                        'ID': 8,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.StopMoving, ()),
                        'Phase': 1,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }, {
                        'ID': 25,
                        'Class': 'Precondition',
                        'Method': (cl_betree.monsteragent.CAgent.HateAllPlayer, ()),
                        'Phase': 3,
                        'Flag': 'precondition',
                        'BinaryOperator': 'And' }),
                    'Method': (cl_betree.monsteragent.CAgent.Attack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
