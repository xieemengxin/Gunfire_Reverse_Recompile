# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai20891.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai20891.pyc
# Source Generated with Decompyle++
# File: pfai20891.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_FIRST

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 20891
    m_Name = '【第四幕】小型近战'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                20891,
                1,
                1,
                0] },
        1002: {
            0: [
                20892,
                1,
                1,
                0] },
        1003: {
            0: [
                20893,
                1,
                1,
                0],
            1: [
                20891,
                1,
                1,
                0] },
        1004: {
            0: [
                20893,
                1,
                1,
                0] },
        2001: {
            0: [
                38036,
                1,
                1,
                0] },
        2002: {
            0: [
                38037,
                1,
                1,
                0] },
        1005: {
            0: [
                20897,
                1,
                1,
                0] },
        1006: {
            0: [
                20898,
                1,
                1,
                0] },
        1007: {
            0: [
                20899,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        20891: [
            1001,
            1003],
        20892: [
            1002],
        20893: [
            1003,
            1004],
        38036: [
            2001],
        38037: [
            2002],
        20897: [
            1005],
        20898: [
            1006],
        20899: [
            1007] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: {
            (0, 99, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        2001: 10 },
                    'angle': (0, 135) },
                {
                    'choose': {
                        2002: 10 },
                    'angle': (-135, 0) }] },
        MONSTER_PFAI_CATCH: {
            (12, 50, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1004: 0,
                        1006: 20 } }],
            (7, 10, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1003: 100 } }],
            (0, 3, -1, 100, -1, 100, 0): [
                {
                    'choose': {
                        1002: 15,
                        1001: 20 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_FIRST,
        1002: PF_GROUP_CHECK_FIRST,
        1003: PF_GROUP_CHECK_FIRST,
        1004: PF_GROUP_CHECK_FIRST,
        2001: PF_GROUP_CHECK_FIRST,
        2002: PF_GROUP_CHECK_FIRST,
        1005: PF_GROUP_CHECK_FIRST,
        1006: PF_GROUP_CHECK_FIRST,
        1007: PF_GROUP_CHECK_FIRST }

