[app]

title = حساب الحمايات
package.name = hisabalhimayat
package.domain = org.odey

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 1.0

# تم إضافة المكتبات الخاصة بدعم اللغة العربية هنا
requirements = python3,kivy,arabic_reshaper,python-bidi

# تم إضافة مسارات الأيقونة وشاشة البداية هنا
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

orientation = portrait

fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b

log_level = 2

[buildozer]

warn_on_root = 1
