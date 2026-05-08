# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/BossTornado/bossTornadoAttackmsg.pyc
# RelativePath: clientlogic/cl_betreedata/BossTornado/bossTornadoAttackmsg.pyc
# Source Generated with Decompyle++
# File: bossTornadoAttackmsg.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'bossTornadoAttackmsg',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 14,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddAttackEvents, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 5,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddEventDamBlinkVal, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 6,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.AddState, (7109, 0)),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 3,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 4,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
