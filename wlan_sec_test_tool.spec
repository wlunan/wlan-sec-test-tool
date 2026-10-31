# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller 打包配置（Windows / Linux 的 GUI 版本）。

用法：
    python -m PyInstaller wlan_sec_test_tool.spec --noconfirm

产物：dist/wlan-sec-test-tool/ 目录，压缩该目录即为便携版分发包。
如需图标，把 .ico 放到项目根目录并改下面的 icon 参数。
"""
import sys

from PyInstaller.utils.hooks import collect_dynamic_libs

# PySide6 的 DLL 由内置 hook 收集；这里额外显式收集一次，避免自定义安装路径下漏文件
binaries = collect_dynamic_libs("PySide6")

a = Analysis(
    ["wlan_sec_test_tool.py"],
    pathex=[],
    binaries=binaries,
    datas=[],
    hiddenimports=[
        "pywifi",
        "pywifi.iface",
        "win32api",
        "win32security",
        "win32event",
    ] if sys.platform == "win32" else ["pywifi", "pywifi.iface"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "tkinter",
        "PyQt5",
        "PyQt6",
        "pytest",
        "unittest",
        "pydoc_data",
    ],
    noarchive=False,
    optimize=1,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="wlan-sec-test-tool",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,          # Qt 的 DLL 经 UPX 压缩后容易被杀软误报或加载失败，务必保持 False
    console=False,
    disable_windowed_traceback=False,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    name="wlan-sec-test-tool",
)
