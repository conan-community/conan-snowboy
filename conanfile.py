import os

from conans import ConanFile


class SnowboyConan(ConanFile):
    name = "snowboy"
    license = " Apache License Version 2.0"
    url = "https://github.com/conan-community/conan-snowboy"
    description = "DNN based hotword and wake word detection toolkit"
    website = "https://snowboy.kitt.ai"
    settings = "os", "arch"
    no_copy_sources = True

    def configure(self):
        if False and not self._get_src_to_package():
            raise Exception("""
Invalid settings, snowboy provides prebuilt binaries for:
    aarch64-ubuntu1604 => "os=Linux, arch=armv8"
    android =>  "os=Android, arch=armv8" and "os=Android, arch=armv7a"
    ios => "os=iOS"
    osx => "os=Macos"
    rpi => "os=Linux, arch=armv6", "os=Linux, arch=armv7", "os=Linux, arch=armv7hf", "os=Linux, arch=armv8"
    ubuntu64 => "os=Linux, arch=x86_64"
""")

        if self.settings.os == "Android":
            del self.settings.os.api_level

        if self.settings.os == "iOS":
            del self.settings.os.version

    def _get_src_to_package(self):
        if self.settings.os == "Macos":
            return "osx"
        if self.settings.os == "iOS":
            return "ios"
        elif self.settings.os == "Linux" and self.settings.arch == "x86_64":
            return "ubuntu64"
        elif self.settings.os == "Linux" and "arm" in self.settings.arch:
            return "rpi"
        elif self.settings.os == "Android" and "armv7" in self.settings.arch:
            return "android/armv7a"
        elif self.settings.os == "Android" and "armv8" in self.settings.arch:
            return "android/armv8-aarch64"

    def source(self):
        self.run("git clone https://github.com/Kitt-AI/snowboy.git")
        self.run("cd snowboy && git checkout tags/v%s" % self.version)

    def package(self):
        lib_path = os.path.join(self.source_folder, "snowboy", "lib", self._get_src_to_package())
        self.output.warn(lib_path)
        self.copy("*.h", dst="include", src=os.path.join(self.source_folder, "snowboy", "include"))
        self.copy("libsnowboy-detect.a", dst="lib", src=lib_path, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["snowboy-detect"]

    def package_id(self):
        if self.settings.os == "iOS" or self.settings.os == "Macos" or \
                (self.settings.os == "Linux" and "arm" in self.settings.arch):
            del self.info.settings.arch




