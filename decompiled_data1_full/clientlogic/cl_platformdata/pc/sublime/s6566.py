# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/sublime/s6566.pyc
# RelativePath: clientlogic/cl_platformdata/pc/sublime/s6566.pyc
# Source Generated with Decompyle++
# File: s6566.pyc (Python 3.6)

from cl_commondefines import VIRTUAL_UNLOCK_INITWEAPONDROP
from cl_sublimation.mobject import CSublimation as CCustom

class CSublimation(CCustom):
    m_SID = 6566
    m_Name = '军火支援'
    m_LimitHero = 0
    m_MaxLevel = 3
    m_LevelInfo = {
        1: {
            'NeedPlayerGrade': 10,
            'CashCost': 20,
            'Depend': {
                6551: 1 },
            'TotalDependLevel': 0,
            'Reward': [],
            'WarReward': [
                {
                    'item': VIRTUAL_UNLOCK_INITWEAPONDROP,
                    'info': {
                        'bullettype': 4502 } }] },
        2: {
            'NeedPlayerGrade': 10,
            'CashCost': 35,
            'Depend': { },
            'TotalDependLevel': 0,
            'Reward': [],
            'WarReward': [
                {
                    'item': VIRTUAL_UNLOCK_INITWEAPONDROP,
                    'info': {
                        'bullettype': 4502 } },
                {
                    'item': VIRTUAL_UNLOCK_INITWEAPONDROP,
                    'info': {
                        'bullettype': 4503 } }] },
        3: {
            'NeedPlayerGrade': 10,
            'CashCost': 55,
            'Depend': { },
            'TotalDependLevel': 0,
            'Reward': [],
            'WarReward': [
                {
                    'item': VIRTUAL_UNLOCK_INITWEAPONDROP,
                    'info': {
                        'bullettype': 4504 } },
                {
                    'item': VIRTUAL_UNLOCK_INITWEAPONDROP,
                    'info': {
                        'bullettype': 4503 } },
                {
                    'item': VIRTUAL_UNLOCK_INITWEAPONDROP,
                    'info': {
                        'bullettype': 4502 } }] } }

