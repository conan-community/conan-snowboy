from conans.model.conan_file import ConanFile

import os


class DefaultNameConan(ConanFile):
    name = "DefaultName"
    version = "0.1"
    settings = "os", "arch"

    def configure(self):
        if self.settings.os == "Android":
            del self.settings.os.api_level

        if self.settings.os == "iOS":
            del self.settings.os.version

    def test(self):
        lib = os.path.join(self.deps_cpp_info["snowboy"].rootpath, "lib", "libsnowboy-detect.a")
        if not os.path.exists(lib):
            raise Exception("Invalid package, not found library at: %s" % lib)
        if not self.deps_cpp_info["snowboy"].libs == ["snowboy-detect"]:
            raise Exception("Invalid package cpp_info.libs: %s" % self.deps_cpp_info["snowboy"].libs)

        header = os.path.join(self.deps_cpp_info["snowboy"].rootpath, "include", "snowboy-detect.h")
        if not os.path.exists(header):
            raise Exception("Invalid package, not found header at: %s" % header)

