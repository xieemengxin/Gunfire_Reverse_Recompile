# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Servant/ServantOperate.pyc
# RelativePath: clientlogic/cl_betreedata/Servant/ServantOperate.pyc
# Source Generated with Decompyle++
# File: ServantOperate.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.IsEnterFight(oAgent) == False


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.GetChoosePF(oAgent) == 7153


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.GetChoosePF(oAgent) == 7154

data = {
    'Name': 'ServantOperate',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 4,
    'Node': [
        {
            'ID': 3,
            'Class': 'IfElse',
            'Node': [
                {
                    'ID': 4,
                    'Class': 'And',
                    'Node': [
                        {
                            'ID': 5,
                            'Class': 'Condition',
                            'Method': (Func0, ()) },
                        {
                            'ID': 6,
                            'Class': 'Or',
                            'Node': [
                                {
                                    'ID': 7,
                                    'Class': 'Condition',
                                    'Method': (Func1, ()) },
                                {
                                    'ID': 9,
                                    'Class': 'Condition',
                                    'Method': (Func2, ()) }] }] },
                {
                    'ID': 2,
                    'Class': 'Sequence',
                    'Node': [
                        {
                            'ID': 1,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.Attack, (0,)),
                            'ResultOption': 0,
                            'ResultFunctor': None },
                        {
                            'ID': 10,
                            'Class': 'Action',
                            'Method': (cl_betree.servantagent.CAgent.HateRangeMonster, (20,)),
                            'ResultOption': 0,
                            'ResultFunctor': None }] },
                {
                    'ID': 8,
                    'Class': 'Action',
                    'Method': (cl_betree.servantagent.CAgent.Attack, (0,)),
                    'ResultOption': 0,
                    'ResultFunctor': None }] }] }
