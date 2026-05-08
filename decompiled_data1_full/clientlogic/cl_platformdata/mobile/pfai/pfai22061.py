# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai22061.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai22061.pyc
# Source Generated with Decompyle++
# File: pfai22061.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 22061
    m_Name = '<一周目>重型远程-激光怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                22061,
                1,
                1,
                0] },
        1002: {
            0: [
                22062,
                1,
                1,
                0] },
        1003: {
            0: [
                22063,
                1,
                1,
                0] },
        1004: {
            0: [
                22061,
                1,
                1,
                0],
            1: [
                22062,
                1,
                1,
                37] } }
    m_GroupOfPF = {
        22061: [
            1001,
            1004],
        22062: [
            1002,
            1004],
        22063: [
            1003] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 5, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10 } }],
            (5, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 10,
                        1001: 40 } }],
            (10, 15, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 30,
                        1002: 10 } }],
            (15, 20, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 20,
                        1002: 10,
                        1004: 5 } }],
            (20, 30, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 30,
                        1001: 10 } }],
            (30, 80, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST }

