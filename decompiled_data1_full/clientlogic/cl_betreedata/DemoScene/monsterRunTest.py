# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/DemoScene/monsterRunTest.pyc
# RelativePath: clientlogic/cl_betreedata/DemoScene/monsterRunTest.pyc
# Source Generated with Decompyle++
# File: monsterRunTest.pyc (Python 3.6)

import cl_betree.monsteragent
data = {
    'Name': 'monsterRunTest',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 41,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 2,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 3,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (10, 5, 7, 80, 100)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 4,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 9,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 10,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 11,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 5,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 6,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, (0,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 12,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 13,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (10, 5, 7, 80, 100)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 14,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 17,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 18,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 19,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 15,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 16,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, (0,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 20,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 21,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.ChooseRangedPos, (10, 5, 7, 80, 100)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 22,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 25,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Patrol', 'false')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 26,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Run', 'false')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 27,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMArgs, (2, 'Sprint', 'true')),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 23,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 24,
                            'Class': 'Action',
                            'Method': (cl_betree.monsteragent.CAgent.MoveToPos, (0,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] }] }] }
