# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_hero/load.pyc
# RelativePath: clientlogic/cl_hero/load.pyc
# Source Generated with Decompyle++
# File: load.pyc (Python 3.6)

from cllib.lib_only import RunMobileData
from . import pc
from . import mobile
import cl_dlcdata

def GetDefaultHero():
    if RunMobileData():
        return mobile.GetDefaultHero()
    return pc.GetDefaultHero()


def GetHeroPut():
    if RunMobileData():
        return mobile.GetHeroPut()
    return pc.GetHeroPut()


def GetCareer2Hero():
    if RunMobileData():
        return mobile.GetCareer2Hero()
    return pc.GetCareer2Hero()


def GetAllLoadHero():
    if RunMobileData():
        return mobile.GetAllLoadHero()
    return pc.GetAllLoadHero()


def GetInternalPutHero():
    if RunMobileData():
        return mobile.GetInternalPutHero()
    return pc.GetInternalPutHero()


def GetHero2Dlc():
    return cl_dlcdata.GetHero2Dlc()


def GetHero2HeroCareer():
    if RunMobileData():
        return mobile.GetHero2HeroCareer()
    return pc.GetHero2HeroCareer()


def GetHero2HeroThrow():
    if RunMobileData():
        return mobile.GetHero2HeroThrow()
    return pc.GetHero2HeroThrow()


def GetHero2SpecialCareer():
    if RunMobileData():
        return mobile.GetHero2SpecialCareer()
    return pc.GetHero2SpecialCareer()

