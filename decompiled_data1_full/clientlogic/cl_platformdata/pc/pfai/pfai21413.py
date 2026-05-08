# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21413.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21413.pyc
# Source Generated with Decompyle++
# File: pfai21413.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21413
    m_Name = '<三周目>中型远程-基础远程怪'
    m_FillBulletData = (38012, 15, 3)
    m_UseBulletPF = (21411,)
    m_PFGroup = {
        1001: {
            0: [
                38021,
                1,
                1,
                0] },
        1002: {
            0: [
                38022,
                1,
                1,
                0] },
        1003: {
            0: [
                38012,
                1,
                1,
                0] },
        1101: {
            0: [
                21411,
                4,
                4,
                0] },
        1102: {
            0: [
                21411,
                4,
                4,
                0],
            1: [
                21411,
                2,
                4,
                25] },
        1103: {
            0: [
                21411,
                6,
                8,
                0] },
        1104: {
            0: [
                21411,
                4,
                6,
                0],
            1: [
                21411,
                4,
                6,
                25] },
        1105: {
            0: [
                21411,
                4,
                5,
                0],
            1: [
                21411,
                3,
                5,
                25],
            2: [
                21411,
                4,
                6,
                25] },
        1106: {
            0: [
                21411,
                8,
                11,
                0] },
        1201: {
            0: [
                21412,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        38021: [
            1001],
        38022: [
            1002],
        38012: [
            1003],
        21411: [
            1101,
            1102,
            1103,
            1104,
            1105,
            1106],
        21412: [
            1201] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 },
                    'angle': (0, 180) },
                {
                    'choose': {
                        1002: 10 },
                    'angle': (-180, 0) }] },
        MONSTER_PFAI_CATCH: {
            (12, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1104: 60,
                        1105: 20,
                        1106: 20 } }],
            (8, 12, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1102: 20,
                        1103: 50,
                        1104: 10 } }],
            (4, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1101: 75,
                        1102: 25 } }],
            (0, 4, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1201: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1101: PF_GROUP_CHECK_FIRST,
        1102: PF_GROUP_CHECK_FIRST,
        1103: PF_GROUP_CHECK_FIRST,
        1104: PF_GROUP_CHECK_FIRST,
        1105: PF_GROUP_CHECK_FIRST,
        1106: PF_GROUP_CHECK_FIRST,
        1201: PF_GROUP_CHECK_FIRST }

