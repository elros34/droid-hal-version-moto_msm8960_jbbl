# rpm_device is in 99% cases $DEVICE
%define rpm_device moto_msm8960_jbbl
# rpm_vendor is in 99% cases $VENDOR
%define rpm_vendor motorola

# Manufacturer and device name to be shown in UI
%define vendor_pretty Motorola
%define device_pretty Photon Q

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 1
%define have_led 1

%include droid-hal-version/droid-hal-version.inc
