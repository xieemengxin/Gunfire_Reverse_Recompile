# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/pc/pfai/pfai21333.pyc
# RelativePath: clientlogic/cl_platformdata/pc/pfai/pfai21333.pyc
# Source Generated with Decompyle++
# File: pfai21333.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

def Condition21336(oOwner, dInfo):
    return cl_condition.AICheckHasState(oOwner, dInfo, 33586) == 0


class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 21333
    m_Name = '<三周目>【新三幕】鲨鱼怪浪鳍'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1002: {
            0: [
                21335,
                1,
                1,
                0] },
        1003: {
            0: [
                21336,
                1,
                1,
                0] },
        1004: {
            0: [
                21331,
                1,
                1,
                0] },
        1005: {
            0: [
                21332,
                1,
                1,
                0] },
        1006: {
            0: [
                21333,
                1,
                1,
                0] },
        1007: {
            0: [
                21334,
                1,
                1,
                0] },
        1008: {
            0: [
                21338,
                1,
                1,
                0],
            1: [
                21335,
                1,
                1,
                7] },
        1009: {
            0: [
                21337,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        21335: [
            1002,
            1008],
        21336: [
            1003],
        21331: [
            1004],
        21332: [
            1005],
        21333: [
            1006],
        21334: [
            1007],
        21338: [
            1008],
        21337: [
            1009] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 12, 0, 100, -1, 100, 2): [
                {
                    'choose': {
                        1009: 10 } }],
            (12, 99, 0, 100, -1, 100, 2): [
                {
                    'choose': {
                        1008: 10 } }],
            (12, 99, -1, 50, -1, 50, 1): [
                {
                    'choose': {
                        1002: 20,
                        1003: 80 } }],
            (8, 12, -1, 50, -1, 50, 1): [
                {
                    'choose': {
                        1002: 70,
                        1003: 20 } }],
            (0, 8, -1, 50, -1, 50, 1): [
                {
                    'choose': {
                        1002: 20,
                        1004: 30,
                        1005: 30 } }],
            (12, 99, 50, 100, 50, 100, 1): [
                {
                    'choose': {
                        1002: 20,
                        1003: 80,
                        1004: 5,
                        1005: 5,
                        1006: 5,
                        1007: 5 } }],
            (8, 12, 50, 100, 50, 100, 1): [
                {
                    'choose': {
                        1002: 60,
                        1003: 20,
                        1004: 5,
                        1005: 5,
                        1006: 5,
                        1007: 5 } }],
            (0, 8, 50, 100, 50, 100, 1): [
                {
                    'choose': {
                        1002: 10,
                        1004: 20,
                        1005: 20,
                        1006: 25,
                        1007: 25 } }] } }
    m_CheckPFCanUse = {
        21336: Condition21336 }
    m_PFGroupCheck = {
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST,
        1008: PF_GROUP_CHECK_FIRST,
        1009: PF_GROUP_CHECK_FIRST }

