# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/farareamove.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/farareamove.pyc
# Source Generated with Decompyle++
# File: farareamove.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.GetArrivePosDis(oAgent) >= 3

data = {
    'Name': 'farareamove',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 54,
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
                    'ID': 17,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetMoveStatusRun, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 39,
                    'Class': 'Action',
                    'Method': (cl_betree.monsteragent.CAgent.SetFightStatusAttack, ()),
                    'ResultOption': 0,
                    'ResultFunctor': None },
                {
                    'ID': 108,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 22,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 109,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 147,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 148,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 149,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] }] },
                {
                    'ID': 150,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 151,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedAreaPos, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 152,
                            'Class': 'IfElse',
                            'Node': [
                                {
                                    'ID': 154,
                                    'Class': 'Condition',
                                    'Method': (Func0, ()) },
                                {
                                    'ID': 155,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 157,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 158,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 165,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 166,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 167,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 159,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '0')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 160,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] },
                                {
                                    'ID': 156,
                                    'Class': 'Sequence',
                                    'Node': [
                                        {
                                            'ID': 161,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 162,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 168,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 169,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'true')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 170,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'false')),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 163,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'IsSquat', '0')),
                                            'ResultOption': 0,
                                            'ResultFunctor': None },
                                        {
                                            'ID': 164,
                                            'Class': 'Action',
                                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, ()),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] },
                        {
                            'ID': 153,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FaceLockEnemy, (1,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
