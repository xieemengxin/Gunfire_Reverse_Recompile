# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai39092.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai39092.pyc
# Source Generated with Decompyle++
# File: pfai39092.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition39095(oOwner, dInfo):
    if not oOwner.Phase() == 2 or cl_condition.GetPerformRecord(oOwner, dInfo, {
        39093: 1 }) >= 2:
        if not oOwner.Phase() == 3 or cl_condition.GetPerformRecord(oOwner, dInfo, {
            39092: 1 }) >= 1 or cl_condition.GetPerformRecord(oOwner, dInfo, {
            39093: 1 }) >= 2:
            if not (oOwner.Phase() == 1 or cl_condition.GetPerformRecord(oOwner, dInfo, {
                39093: 1 }) >= 3) and oOwner.Phase() == 4 and cl_condition.GetPerformRecord(oOwner, dInfo, {
                39092: 1 }) >= 1:
                pass
    return cl_condition.GetPerformRecord(oOwner, dInfo, {
        39093: 1 }) >= 2


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39092
    m_Name = '<二周目>boss-石巨人'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                39091,
                1,
                1,
                0] },
        1002: {
            0: [
                39092,
                1,
                1,
                0] },
        1003: {
            0: [
                39093,
                1,
                1,
                0] },
        1004: {
            0: [
                39095,
                1,
                1,
                0] },
        1005: {
            0: [
                39096,
                1,
                1,
                0] },
        2001: {
            0: [
                39093,
                1,
                1,
                0],
            1: [
                39093,
                1,
                1,
                25] },
        2002: {
            0: [
                39093,
                1,
                1,
                0],
            1: [
                39092,
                1,
                1,
                25] },
        3001: {
            0: [
                39093,
                1,
                1,
                0],
            1: [
                39092,
                1,
                1,
                25],
            2: [
                39093,
                1,
                1,
                25] },
        3002: {
            0: [
                39092,
                1,
                1,
                0],
            1: [
                39093,
                1,
                1,
                25],
            2: [
                39093,
                1,
                1,
                25] },
        3003: {
            0: [
                39093,
                1,
                1,
                0],
            1: [
                39093,
                1,
                1,
                12],
            2: [
                39093,
                1,
                1,
                12] } }
    m_GroupOfPF = {
        39091: [
            1001],
        39092: [
            1002,
            2002,
            3001,
            3002],
        39093: [
            1003,
            2001,
            2002,
            3001,
            3002,
            3003],
        39095: [
            1004],
        39096: [
            1005] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 28, -1, 30, -1, 30, 0): [
                {
                    'choose': {
                        3003: 1,
                        1004: 100,
                        1005: 2 } }],
            (0, 28, 30, 60, 30, 60, 0): [
                {
                    'choose': {
                        1001: 5,
                        2002: 1,
                        1004: 100,
                        2001: 1 } }],
            (28, 100, -1, 30, -1, 30, 0): [
                {
                    'choose': {
                        3001: 1,
                        3002: 1,
                        1005: 3,
                        1004: 100,
                        1003: 1 } }],
            (28, 100, 30, 60, 30, 60, 0): [
                {
                    'choose': {
                        1005: 3,
                        2002: 1,
                        2001: 1,
                        1004: 100 } }],
            (0, 100, 60, 85, 60, 85, 0): [
                {
                    'choose': {
                        1001: 5,
                        1004: 100,
                        2001: 1,
                        2002: 1 } }],
            (0, 100, 85, 100, 85, 100, 0): [
                {
                    'choose': {
                        1003: 1,
                        1004: 100 } }] } }
    m_CheckPFCanUse = {
        39095: Condition39095 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        2001: PF_GROUP_CHECK_FIRST,
        2002: PF_GROUP_CHECK_FIRST,
        3001: PF_GROUP_CHECK_FIRST,
        3002: PF_GROUP_CHECK_FIRST,
        3003: PF_GROUP_CHECK_FIRST }

