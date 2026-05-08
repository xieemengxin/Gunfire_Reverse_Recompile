# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_betreedata/Spare/SpareAttack.pyc
# RelativePath: clientlogic/cl_betreedata/Spare/SpareAttack.pyc
# Source Generated with Decompyle++
# File: SpareAttack.pyc (Python 3.6)

import cl_betree.servantagent

def Func0(oAgent):
    return cl_betree.servantagent.CAgent.CheckCanSeeLock(oAgent) == True


def Func1(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) <= 12


def Func2(oAgent):
    return cl_betree.servantagent.CAgent.GetHeroDis(oAgent) >= 12

data = {
    'Name': 'SpareAttack',
    'ID': 0,
    'AgentType': 'cl_betree.servantagent',
    'IsFSM': False,
    'Ver': 109,
    'Node': [
        {
            'ID': 1,
            'Class': 'Sequence',
            'Node': [
                {
                    'ID': 50,
                    'Class': 'Parallel',
                    'FailurePolicy': 1,
                    'SuccessPolicy': 1,
                    'ExitPolicy': 1,
                    'ChildFinishPolicy': 1,
                    'Node': [
                        {
                            'ID': 51,
                            'Class': 'Sequence',
                            'Node': [
                                {
                                    'ID': 62,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.ChooseHateTarget, (1, 0)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 54,
                                    'Class': 'Action',
                                    'Method': (cl_betree.servantagent.CAgent.FaceLockEnemy, (0,)),
                                    'ResultOption': 0,
                                    'ResultFunctor': None },
                                {
                                    'ID': 111,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 80,
                                            'Class': 'Condition',
                                            'Method': (Func0, ()) },
                                        {
                                            'ID': 123,
                                            'Class': 'Sequence',
                                            'Node': [
                                                {
                                                    'ID': 122,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.ChoosePF, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None },
                                                {
                                                    'ID': 121,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.Attack, (1,)),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] },
                                        {
                                            'ID': 113,
                                            'Class': 'DecoratorAlwaysFailure',
                                            'DecorateWhenChildEnds': False,
                                            'Node': [
                                                {
                                                    'ID': 114,
                                                    'Class': 'Action',
                                                    'Method': (cl_betree.servantagent.CAgent.ClearHateTarget, ()),
                                                    'ResultOption': 0,
                                                    'ResultFunctor': None }] }] }] },
                        {
                            'ID': 82,
                            'Class': 'DecoratorAlwaysRunning',
                            'DecorateWhenChildEnds': False,
                            'Node': [
                                {
                                    'ID': 89,
                                    'Class': 'IfElse',
                                    'Node': [
                                        {
                                            'ID': 90,
                                            'Class': 'Condition',
                                            'Method': (Func1, ()) },
                                        {
                                            'ID': 93,
                                            'Class': 'SelectorProbability',
                                            'RandomGenerator': None,
                                            'Node': [
                                                {
                                                    'ID': 94,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 25,
                                                    'Node': [
                                                        {
                                                            'ID': 96,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 50 }] },
                                                {
                                                    'ID': 95,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 25,
                                                    'Node': [
                                                        {
                                                            'ID': 100,
                                                            'Class': 'WaitFrame',
                                                            'Frames': 25 }] },
                                                {
                                                    'ID': 98,
                                                    'Class': 'DecoratorWeight',
                                                    'DecorateWhenChildEnds': False,
                                                    'Weight': 50,
                                                    'Node': [
                                                        {
                                                            'ID': 101,
                                                            'Class': 'Sequence',
                                                            'Node': [
                                                                {
                                                                    'ID': 102,
                                                                    'Class': 'Action',
                                                                    'Method': (cl_betree.servantagent.CAgent.ChooseEnemyAroundPos, (10, 15, 0)),
                                                                    'ResultOption': 0,
                                                                    'ResultFunctor': None },
                                                                {
                                                                    'ID': 115,
                                                                    'Class': 'Parallel',
                                                                    'FailurePolicy': 0,
                                                                    'SuccessPolicy': 1,
                                                                    'ExitPolicy': 0,
                                                                    'ChildFinishPolicy': 1,
                                                                    'Node': [
                                                                        {
                                                                            'ID': 103,
                                                                            'Class': 'Action',
                                                                            'Method': (cl_betree.servantagent.CAgent.MoveToPos, (2,)),
                                                                            'ResultOption': 0,
                                                                            'ResultFunctor': None },
                                                                        {
                                                                            'ID': 116,
                                                                            'Class': 'Condition',
                                                                            'Method': (Func2, ()) }] }] }] }] },
                                        {
                                            'ID': 69,
                                            'Class': 'Action',
                                            'Method': (cl_betree.servantagent.CAgent.MoveToHeroPos, (3,)),
                                            'ResultOption': 0,
                                            'ResultFunctor': None }] }] }] }] }] }
