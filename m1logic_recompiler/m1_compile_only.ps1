param(
    [Parameter(Mandatory = $true)]
    [string]$SourceDir,

    [Parameter(Mandatory = $true)]
    [string]$OutputDir,

    [string]$PythonExe = (Join-Path $PSScriptRoot "PCbuild\\amd64\\python.exe"),
    [string]$TempPythonHome = (Join-Path $PSScriptRoot "tmp_pyhome_compile"),
    [string]$DFilePrefix = "./",
    [switch]$UseAbsDFile
)

$ErrorActionPreference = "Stop"

$srcFull = (Resolve-Path $SourceDir).Path
if (-not (Test-Path $PythonExe)) {
    throw "python.exe not found: $PythonExe"
}
if (-not (Test-Path $srcFull)) {
    throw "source dir not found: $SourceDir"
}

$libSrc = Join-Path $PSScriptRoot "Lib"
if (-not (Test-Path $libSrc)) {
    throw "Lib dir not found: $libSrc"
}

New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
New-Item -ItemType Directory -Path $TempPythonHome -Force | Out-Null

$libDst = Join-Path $TempPythonHome "Lib"
robocopy $libSrc $libDst /E /XF *.pyc /XD __pycache__ /R:1 /W:1 | Out-Null
if ($LASTEXITCODE -ge 8) {
    throw "robocopy failed with exit code: $LASTEXITCODE"
}

$oldPythonHome = [Environment]::GetEnvironmentVariable("PYTHONHOME", "Process")
$oldPythonPath = [Environment]::GetEnvironmentVariable("PYTHONPATH", "Process")

$pyCode = @'
import os
import sys
import py_compile

src_root = os.path.abspath(sys.argv[1])
out_root = os.path.abspath(sys.argv[2])
dfile_prefix = sys.argv[3] if len(sys.argv) > 3 else "./"
use_abs_dfile = (len(sys.argv) > 4 and sys.argv[4] == "1")

dfile_prefix = dfile_prefix.replace("\\", "/")
if dfile_prefix and (not dfile_prefix.endswith("/")):
    dfile_prefix += "/"

compiled = 0
failed = 0

for root, _, files in os.walk(src_root):
    for name in files:
        if not name.endswith(".py"):
            continue
        src_path = os.path.join(root, name)
        rel = os.path.relpath(src_path, src_root)
        out_path = os.path.join(out_root, os.path.splitext(rel)[0] + ".pyc")
        out_dir = os.path.dirname(out_path)
        if out_dir and not os.path.isdir(out_dir):
            os.makedirs(out_dir)
        rel_norm = rel.replace("\\", "/")
        dfile = (dfile_prefix + rel_norm) if dfile_prefix else rel_norm
        try:
            if use_abs_dfile:
                py_compile.compile(src_path, cfile=out_path, doraise=True)
            else:
                py_compile.compile(src_path, cfile=out_path, dfile=dfile, doraise=True)
            compiled += 1
        except Exception as exc:
            failed += 1
            print("[fail]", src_path, exc)

print("[done] compiled=%d failed=%d" % (compiled, failed))
if failed:
    sys.exit(2)
'@

$tmpScript = Join-Path $TempPythonHome "m1_compile_only_tmp.py"
Set-Content -Path $tmpScript -Value $pyCode -Encoding ASCII

$useAbs = if ($UseAbsDFile) { "1" } else { "0" }
try {
    $env:PYTHONHOME = $TempPythonHome
    $env:PYTHONPATH = $libDst

    & $PythonExe -B -S $tmpScript $srcFull (Resolve-Path $OutputDir).Path $DFilePrefix $useAbs
    $code = $LASTEXITCODE
    if ($code -ne 0) {
        throw "compile failed, exit code: $code"
    }
}
finally {
    if ([string]::IsNullOrEmpty($oldPythonHome)) {
        Remove-Item Env:PYTHONHOME -ErrorAction SilentlyContinue
    }
    else {
        $env:PYTHONHOME = $oldPythonHome
    }

    if ([string]::IsNullOrEmpty($oldPythonPath)) {
        Remove-Item Env:PYTHONPATH -ErrorAction SilentlyContinue
    }
    else {
        $env:PYTHONPATH = $oldPythonPath
    }
}

Write-Host "[ok] custom pyc output:" (Resolve-Path $OutputDir).Path
