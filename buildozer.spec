[app]
title = Calora AI
package.name = caloraai
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Kitabxanaları dəqiq belə yaz:
requirements = python3,kivy==2.2.1,groq,requests,certifi,urllib3,idna,charset-normalizer

orientation = portrait
fullscreen = 0

# Android tənzimləmələri (BU HİSSƏ ÇOX VACİBDİR)
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25c
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
