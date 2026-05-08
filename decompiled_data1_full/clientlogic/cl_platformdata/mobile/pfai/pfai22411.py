# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai22411.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai22411.pyc
# Source Generated with Decompyle++
# File: pfai22411.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 22411
    m_Name = '投射怪-投射法球怪'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                22411,
                1,
                1,
                0] },
        1004: {
            0: [
                22412,
                1,
                1,
                0] },
        1005: {
            0: [
                22413,
                1,
                1,
                0] },
        1006: {
            0: [
                38027,
                1,
                1,
                0] },
        1002: {
            0: [
                38025,
                1,
                1,
                0] },
        1003: {
            0: [
                38026,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        22411: [
            1001],
        22412: [
            1004],
        22413: [
            1005],
        38027: [
            1006],
        38025: [
            1002],
        38026: [
            1003] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 10 },
                    'angle': (0, 135) },
                {
                    'choose': {
                        1003: 10 },
                    'angle': (-135, 0) },
                {
                    'choose': {
                        1006: 10 },
                    'angle': (135, 180) },
                {
                    'choose': {
                        1006: 10 },
                    'angle': (-180, -135) }] },
        MONSTER_PFAI_CATCH: {
            (8, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1004: 10 } }],
            (3, 8, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1001: 10 } }],
            (0, 3, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1005: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST }

