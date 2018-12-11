# -*- mode: python -*-

block_cipher = None


a = Analysis(['main_author.py'],
             pathex=['C:\\Users\\Johnny\\OneDrive\\School - suny poly\\Fall 2018\\CS 370 - software engineering\\Code\\cs370-Text_Adventure_Engine_Final'],
             binaries=[],
             datas=[('./sounds', 'sounds')],
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
          name='main_author',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
