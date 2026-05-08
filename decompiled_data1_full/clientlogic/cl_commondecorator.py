# Path: /Users//个人空间/04 Gunfire/converted/converted_data1/clientlogic/cl_commondecorator.pyc
# RelativePath: clientlogic/cl_commondecorator.pyc
# Source Generated with Decompyle++
# File: cl_commondecorator.pyc (Python 3.6)


def ChooseRewardEnd(func):
    
    def _ChooseRewardEnd(*args):
        oHero = args[1]
        r = func(*args)
        if r:
            oHero.DoNextMapLoadOKCbFun()
        return r

    return _ChooseRewardEnd


def CheckFaultToleranceWithDefault(Default = None):
    
    def _CheckFaultToleranceWithDefault(func):
        
        def _ExcuteFunc(*args, **kwargs):
            
            try:
                r = func(*args, **kwargs)
            except:
                from cl_only import PythonError
                PythonError()
                return Default

            return r

        return _ExcuteFunc

    return _CheckFaultToleranceWithDefault


def CheckFaultTolerance(func):
    
    def _CheckFaultTolerance(*args, **kwargs):
        
        try:
            return func(*args, **kwargs)
        except:
            from cl_only import PythonError
            PythonError()


    return _CheckFaultTolerance

