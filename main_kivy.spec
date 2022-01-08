from kivy_deps import sdl2, glew, angle
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main_kivy.py'],
             pathex=[],
             binaries=[],
             datas=[('C:/Users/send2_19iz6ad/PycharmProjects/FaceRecognitionProject/ImagesBasic', 'ImagesBasic/'), ('C:/Users/send2_19iz6ad/PycharmProjects/FaceRecognitionProject/adduser.png', '.'), ('C:/Users/send2_19iz6ad/PycharmProjects/FaceRecognitionProject/Attendance.csv', '.'), ('C:/Users/send2_19iz6ad/PycharmProjects/FaceRecognitionProject/fr123.png', '.'), ('C:/Users/send2_19iz6ad/PycharmProjects/FaceRecognitionProject/ICON.ico', '.'), ('C:/Users/send2_19iz6ad/PycharmProjects/FaceRecognitionProject/Main_Att.csv', '.'), ('C:/Users/send2_19iz6ad/PycharmProjects/FaceRecognitionProject/SidePic.png', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          [],
          exclude_binaries=True,
          name='main_kivy',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='C:\\Users\\send2_19iz6ad\\PycharmProjects\\FaceRecognitionProject\\ICON.ico')
coll = COLLECT(exe,
Tree('C:\\Users\\send2_19iz6ad\\PycharmProjects\\FaceRecognitionProject\\'),
               a.binaries,
               a.zipfiles,
               a.datas, 
 	       *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + angle.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main_kivy')
