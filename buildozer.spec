[app]
title = Test APK
package.name = testapk
package.domain = org.test
source.dir = .
source.include_exts = py
requirements = python3,kivy
orientation = portrait
version = 1.0
android.api = 31
android.minapi = 21
android.sdk = 34
android.build_tools_version = 34.0.0
android.ndk = 25b
android.archs = arm64-v8a
android.permissions = android.permission.INTERNET
android.accept_sdk_license = True

[buildozer]
log_level = 2