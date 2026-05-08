# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/MonsterSpider/dashToShowPos.pyc
# RelativePath: clientlogic/cl_betreedata/MonsterSpider/dashToShowPos.pyc
# Source Generated with Decompyle++
# File: dashToShowPos.pyc (Python 3.6)

import cl_betree.monsteragent

def Func0(oAgent):
    return cl_betree.monsteragent.CAgent.CheckHasState(8094, oAgent) == False

data = {
    'Name': 'dashToShowPos',
    'ID': 0,
    'AgentType': 'cl_betree.monsteragent',
    'IsFSM': False,
    'Ver': 70,
    'Node': [
        {
            'ID': 41,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 42,
                    'Class': 'IfElse',
                    'Node': [
                        {
                            'ID': 45,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 43,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 47,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.AddState, (8094, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 38,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.ChooseShowPos, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 30,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.SetActionSMSprint, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 37,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.FacePath, ()),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 48,
                                    'Class': 'Action',
                                    'Method': (cl_betree.monsteragent.CAgent.DashToPos, (24222,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None }] },
                        {
                            'ID': 46,
                            'Class': 'Noop' }] }] }] }
