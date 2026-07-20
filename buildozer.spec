[app]

# تم تغيير الاسم للإنجليزية لتجنب أخطاء الترميز
title = Hisab Al Himayat
package.name = hisabalhimayat
package.domain = org.odey

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 1.0

# المكتبات المطلوبة
requirements = python3,kivy,arabic_reshaper,python-bidi

# مسارات الصور
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 23b

# إضافة هذا السطر لحل مشكلة التراخيص
android.accept_sdk_license = True

log_level = 2

[buildozer]
warn_on_root = 1
