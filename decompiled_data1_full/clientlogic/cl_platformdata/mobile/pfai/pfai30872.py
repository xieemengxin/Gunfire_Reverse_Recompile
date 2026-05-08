# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai30872.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai30872.pyc
# Source Generated with Decompyle++
# File: pfai30872.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 30872
    m_Name = '【第三幕】精英小型近战（迭代）'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                38031,
                1,
                1,
                0] },
        1002: {
            0: [
                38032,
                1,
                1,
                0] },
        1003: {
            0: [
                38035,
                1,
                1,
                0] },
        1101: {
            0: [
                30876,
                1,
                1,
                0] },
        1102: {
            0: [
                30876,
                1,
                1,
                0],
            1: [
                30874,
                1,
                1,
                0] },
        1201: {
            0: [
                30872,
                1,
                1,
                0] },
        1301: {
            0: [
                30875,
                10,
                15,
                0] },
        1302: {
            0: [
                30875,
                10,
                15,
                0],
            1: [
                30874,
                1,
                1,
                0] },
        1303: {
            0: [
                30875,
                10,
                15,
                0],
            1: [
                30874,
                1,
                1,
                0],
            2: [
                30876,
                1,
                1,
                0] },
        1401: {
            0: [
                30874,
                1,
                1,
                0] },
        1402: {
            0: [
                30874,
                1,
                1,
                0],
            1: [
                30876,
                1,
                1,
                0] },
        1403: {
            0: [
                30874,
                1,
                1,
                0],
            1: [
                30876,
                1,
                1,
                0],
            2: [
                30874,
                1,
                1,
                0] },
        1404: {
            0: [
                30874,
                1,
                1,
                0],
            1: [
                30876,
                1,
                1,
                0],
            2: [
                30875,
                10,
                15,
                0] } }
    m_GroupOfPF = {
        38031: [
            1001],
        38032: [
            1002],
        38035: [
            1003],
        30876: [
            1101,
            1102,
            1303,
            1402,
            1403,
            1404],
        30874: [
            1102,
            1302,
            1303,
            1401,
            1402,
            1403,
            1404],
        30872: [
            1201],
        30875: [
            1301,
            1302,
            1303,
            1404] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 },
                    'angle': (0, 135) },
                {
                    'choose': {
                        1002: 10 },
                    'angle': (-135, 0) },
                {
                    'choose': {
                        1003: 10 },
                    'angle': (135, 180) },
                {
                    'choose': {
                        1003: 10 },
                    'angle': (-180, -135) }] },
        MONSTER_PFAI_CATCH: {
            (16, 99, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1402: 10,
                        1303: 60,
                        1403: 10,
                        1404: 10 } }],
            (8, 16, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1303: 30,
                        1402: 20,
                        1403: 20,
                        1404: 20 } }],
            (4, 8, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1102: 10 } }],
            (0, 4, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1201: 10 } }],
            (16, 99, -1, 100, 50, 80, 0): [
                {
                    'choose': {
                        1401: 10,
                        1302: 10 } }],
            (8, 16, -1, 100, 50, 80, 0): [
                {
                    'choose': {
                        1401: 10 } }],
            (4, 8, -1, 100, 50, 80, 0): [
                {
                    'choose': {
                        1102: 10 } }],
            (0, 4, -1, 100, 50, 80, 0): [
                {
                    'choose': {
                        1201: 10 } }],
            (8, 99, -1, 100, 80, 100, 0): [
                {
                    'choose': {
                        1301: 75,
                        1101: 25 } }],
            (4, 8, -1, 100, 80, 100, 0): [
                {
                    'choose': {
                        1101: 10 } }],
            (0, 4, -1, 100, 80, 100, 0): [
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
        1201: PF_GROUP_CHECK_FIRST,
        1301: PF_GROUP_CHECK_FIRST,
        1302: PF_GROUP_CHECK_FIRST,
        1303: PF_GROUP_CHECK_FIRST,
        1401: PF_GROUP_CHECK_FIRST,
        1402: PF_GROUP_CHECK_FIRST,
        1403: PF_GROUP_CHECK_FIRST,
        1404: PF_GROUP_CHECK_FIRST }

