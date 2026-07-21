[app]

# (اسم التطبيق وحزمته)
title = Hisab Al Himayat
package.name = hisabalhimayat
package.domain = org.odey

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 1.0

# المكتبات المطلوبة (تم التأكد من وجود مكتبات العربية)[span_4](start_span)[span_4](end_span)
requirements = python3,kivy,arabic_reshaper,python-bidi

# مسارات الأيقونات
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

orientation = portrait
fullscreen = 0

# إعدادات الأندرويد (تمت إزالة سطر NDK ليتولى النظام إدارته تلقائياً)
android.api = 33
android.minapi = 21
# android.ndk = 25b  <-- تمت إزالته لتجنب أخطاء التوافق

# إضافة هذا السطر لحل مشكلة التراخيص
android.accept_sdk_license = True

log_level = 2

[buildozer]
warn_on_root = 1
