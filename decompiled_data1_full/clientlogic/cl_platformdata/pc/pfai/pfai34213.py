# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai34213.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai34213.pyc
# Source Generated with Decompyle++
# File: pfai34213.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition34214(oOwner, dInfo):
    return cl_condition.CheckTopObstacleDis(oOwner, 5)


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 34213
    m_Name = '<三周目>精英蜘蛛猎手'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                34211,
                1,
                1,
                0] },
        1002: {
            0: [
                34211,
                1,
                1,
                0],
            1: [
                34213,
                1,
                1,
                0] },
        1003: {
            0: [
                34212,
                1,
                1,
                0] },
        1004: {
            0: [
                34213,
                1,
                1,
                0] },
        1005: {
            0: [
                34214,
                1,
                1,
                0] },
        1006: {
            0: [
                34212,
                1,
                1,
                0],
            1: [
                34212,
                1,
                1,
                0] },
        1007: {
            0: [
                34214,
                1,
                1,
                0],
            1: [
                34212,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        34211: [
            1001,
            1002],
        34213: [
            1002,
            1004],
        34212: [
            1003,
            1006,
            1007],
        34214: [
            1005,
            1007] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (15, 99, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1007: 999,
                        1004: 10 } }],
            (10, 15, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1007: 999,
                        1004: 10 } }],
            (5, 10, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1005: 999,
                        1002: 10,
                        1004: 10 } }],
            (0, 5, -1, 100, -1, 50, 0): [
                {
                    'choose': {
                        1002: 100 } }],
            (15, 99, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1003: 70,
                        1004: 30,
                        1005: 100 } }],
            (10, 15, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1003: 50,
                        1004: 50,
                        1005: 100 } }],
            (5, 10, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1003: 50,
                        1004: 50,
                        1005: 100 } }],
            (0, 5, -1, 100, 50, 100, 0): [
                {
                    'choose': {
                        1001: 50,
                        1002: 50 } }] } }
    m_CheckPFCanUse = {
        34214: Condition34214 }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST }

