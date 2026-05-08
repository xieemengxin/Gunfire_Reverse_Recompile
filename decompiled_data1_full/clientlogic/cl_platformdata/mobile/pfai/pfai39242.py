# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_platformdata/mobile/pfai/pfai39242.pyc
# RelativePath: clientlogic/cl_platformdata/mobile/pfai/pfai39242.pyc
# Source Generated with Decompyle++
# File: pfai39242.pyc (Python 3.6)

import cl_betree.pfai.mobject as pfaiobj
import cl_condition
from cl_commondefines import MONSTER_PFAI_CATCH, MONSTER_PFAI_DODGE, PF_GROUP_CHECK_ALL, PF_GROUP_CHECK_ALLCD

class CPerformAI(pfaiobj.CBasePerformAI):
    m_SID = 39242
    m_Name = '<二周目>boss-妖王'
    m_FillBulletData = ()
    m_UseBulletPF = ()
    m_PFGroup = {
        1001: {
            0: [
                39244,
                1,
                1,
                0] },
        1002: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39244,
                1,
                1,
                0] },
        1101: {
            0: [
                39242,
                1,
                1,
                0] },
        1201: {
            0: [
                39243,
                1,
                1,
                0] },
        1202: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39243,
                1,
                1,
                0] },
        1203: {
            0: [
                39243,
                1,
                1,
                0],
            1: [
                39244,
                1,
                1,
                0] },
        1204: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39243,
                1,
                1,
                0],
            2: [
                39244,
                1,
                1,
                0] },
        2001: {
            0: [
                39244,
                1,
                1,
                0] },
        2002: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39244,
                1,
                1,
                0] },
        2003: {
            0: [
                39244,
                1,
                1,
                0],
            1: [
                39245,
                1,
                1,
                0],
            2: [
                39242,
                1,
                1,
                0] },
        2101: {
            0: [
                39242,
                1,
                1,
                0] },
        2102: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39242,
                1,
                1,
                0] },
        2103: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39242,
                1,
                1,
                0],
            2: [
                39244,
                1,
                1,
                0] },
        2104: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39242,
                1,
                1,
                0],
            2: [
                39245,
                1,
                1,
                0],
            3: [
                39242,
                1,
                1,
                0] },
        2201: {
            0: [
                39243,
                1,
                1,
                0] },
        2202: {
            0: [
                39243,
                1,
                1,
                0],
            1: [
                39245,
                1,
                1,
                0],
            2: [
                39242,
                1,
                1,
                0] },
        2203: {
            0: [
                39243,
                1,
                1,
                0],
            1: [
                39244,
                1,
                1,
                0] },
        2204: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39243,
                1,
                1,
                0],
            2: [
                39245,
                1,
                1,
                0],
            3: [
                39242,
                1,
                1,
                0] },
        3001: {
            0: [
                39244,
                1,
                1,
                0],
            1: [
                39245,
                1,
                1,
                0],
            2: [
                39244,
                1,
                1,
                0] },
        3002: {
            0: [
                39244,
                1,
                1,
                0],
            1: [
                39245,
                1,
                1,
                0],
            2: [
                39241,
                1,
                1,
                0] },
        3101: {
            0: [
                39243,
                1,
                1,
                0],
            1: [
                39244,
                1,
                1,
                0] },
        3201: {
            0: [
                39241,
                1,
                1,
                0] },
        3202: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39241,
                1,
                1,
                0] },
        3203: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39241,
                1,
                1,
                0],
            2: [
                39245,
                1,
                1,
                0],
            3: [
                39244,
                1,
                1,
                0] },
        3204: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39241,
                1,
                1,
                0],
            2: [
                39245,
                1,
                1,
                0],
            3: [
                39243,
                1,
                1,
                0] },
        3301: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39247,
                1,
                1,
                0] },
        4001: {
            0: [
                39241,
                1,
                1,
                0] },
        4002: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39241,
                1,
                1,
                0] },
        4003: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39242,
                1,
                1,
                0],
            2: [
                39245,
                1,
                1,
                0],
            3: [
                39242,
                1,
                1,
                0],
            4: [
                39245,
                1,
                1,
                0],
            5: [
                39242,
                1,
                1,
                0] },
        4101: {
            0: [
                39244,
                1,
                1,
                0],
            1: [
                39245,
                1,
                1,
                0],
            2: [
                39241,
                1,
                1,
                0] },
        4102: {
            0: [
                39244,
                1,
                1,
                0],
            1: [
                39245,
                1,
                1,
                0],
            2: [
                39244,
                1,
                1,
                0] },
        5101: {
            0: [
                39243,
                1,
                1,
                0],
            1: [
                39245,
                1,
                1,
                0],
            2: [
                39243,
                1,
                1,
                0],
            3: [
                39245,
                1,
                1,
                0],
            4: [
                39243,
                1,
                1,
                0] },
        5102: {
            0: [
                39245,
                1,
                1,
                0],
            1: [
                39243,
                1,
                1,
                0],
            2: [
                39245,
                1,
                1,
                0],
            3: [
                39243,
                1,
                1,
                0],
            4: [
                39245,
                1,
                1,
                0],
            5: [
                39243,
                1,
                1,
                0] } }
    m_GroupOfPF = {
        39244: [
            1001,
            1002,
            1203,
            1204,
            2001,
            2002,
            2003,
            2103,
            2203,
            3001,
            3002,
            3101,
            3203,
            4101,
            4102],
        39245: [
            1002,
            1202,
            1204,
            2002,
            2003,
            2102,
            2103,
            2104,
            2202,
            2204,
            3001,
            3002,
            3202,
            3203,
            3204,
            3301,
            4002,
            4003,
            4101,
            4102,
            5101,
            5102],
        39242: [
            1101,
            2003,
            2101,
            2102,
            2103,
            2104,
            2202,
            2204,
            4003],
        39243: [
            1201,
            1202,
            1203,
            1204,
            2201,
            2202,
            2203,
            2204,
            3101,
            3204,
            5101,
            5102],
        39241: [
            3002,
            3201,
            3202,
            3203,
            3204,
            4001,
            4002,
            4101],
        39247: [
            3301] }
    m_ChoosePFInfo = {
        MONSTER_PFAI_DODGE: { },
        MONSTER_PFAI_CATCH: {
            (0, 6, -1, 100, -1, 100, 6): [
                {
                    'choose': {
                        4001: 10 } }],
            (6, 12, -1, 100, -1, 100, 6): [
                {
                    'choose': {
                        4002: 10,
                        4003: 12,
                        5101: 6 } }],
            (12, 18, -1, 100, -1, 100, 6): [
                {
                    'choose': {
                        4002: 12,
                        4003: 6,
                        5102: 12 } }],
            (18, 99, -1, 100, -1, 100, 6): [
                {
                    'choose': {
                        4002: 16,
                        4003: 6,
                        5102: 6 } }],
            (0, 6, -1, 100, -1, 100, 4): [
                {
                    'choose': {
                        4001: 10 } }],
            (6, 12, -1, 100, -1, 100, 4): [
                {
                    'choose': {
                        4001: 10,
                        4101: 10 } }],
            (12, 18, -1, 100, -1, 100, 4): [
                {
                    'choose': {
                        4002: 10,
                        4003: 12,
                        4101: 10 } }],
            (18, 99, -1, 100, -1, 100, 4): [
                {
                    'choose': {
                        4002: 10,
                        4003: 12,
                        4101: 12,
                        4102: 6 } }],
            (0, 6, -1, 100, -1, 100, 3): [
                {
                    'choose': {
                        1201: 10 } }],
            (6, 12, -1, 100, -1, 100, 3): [
                {
                    'choose': {
                        3201: 10,
                        3002: 10,
                        3301: 1000 } }],
            (12, 18, -1, 100, -1, 100, 3): [
                {
                    'choose': {
                        3001: 6,
                        3002: 10,
                        3101: 12,
                        3202: 8,
                        3203: 7,
                        3204: 7,
                        3301: 1000 } }],
            (18, 99, -1, 100, -1, 100, 3): [
                {
                    'choose': {
                        3001: 7,
                        3002: 9,
                        3202: 8,
                        3203: 7,
                        3204: 6,
                        3301: 1000 } }],
            (0, 6, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        2101: 10 } }],
            (6, 12, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        2101: 8,
                        2201: 8,
                        2202: 8,
                        2203: 8,
                        2002: 5 } }],
            (12, 18, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        2102: 9,
                        2103: 9,
                        2104: 6,
                        2201: 6,
                        2202: 9,
                        2203: 9,
                        2002: 5,
                        2003: 10 } }],
            (18, 99, -1, 100, -1, 100, 2): [
                {
                    'choose': {
                        2001: 8,
                        2002: 5,
                        2003: 12,
                        2102: 8,
                        2104: 6,
                        2204: 11 } }],
            (0, 6, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1101: 10 } }],
            (6, 18, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1002: 10,
                        1201: 15,
                        1203: 15 } }],
            (18, 99, -1, 100, -1, 100, 1): [
                {
                    'choose': {
                        1001: 10,
                        1002: 7,
                        1202: 10,
                        1204: 10 } }] } }
    m_CheckPFCanUse = { }
    m_PFGroupCheck = {
        1001: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1002: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1101: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1201: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1202: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1203: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        1204: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2001: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2002: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2003: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2101: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2102: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2103: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2104: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2201: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2202: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2203: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        2204: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        3001: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        3002: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        3101: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        3201: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        3202: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        3203: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        3204: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        3301: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        4001: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        4002: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        4003: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        4101: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        4102: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        5101: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD,
        5102: PF_GROUP_CHECK_ALL | PF_GROUP_CHECK_ALLCD }

