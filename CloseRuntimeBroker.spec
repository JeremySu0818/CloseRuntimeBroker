# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['CloseRuntimeBroker.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icon.ico', '.'),      # 加入圖示
        ('lang.json', '.')      # 加入語系檔
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='CloseRuntimeBroker',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # 如果是 GUI 程式請設為 False
    icon='icon.ico',
    onefile=True
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CloseRuntimeBroker'
)
