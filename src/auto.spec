# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['auto.py'],
             pathex=['C:\\Users\\vikkh\\Downloads\\000767ad0ee278ec8bc2381a42e86b15-0619dcb143414418f9ae87462a0d8ee3fef37c89\\000767ad0ee278ec8bc2381a42e86b15-0619dcb143414418f9ae87462a0d8ee3fef37c89'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='auto',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
