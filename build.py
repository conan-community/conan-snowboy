
from conan.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add(settings={"os": "Linux", "arch": "x86_64"})
    builder.add(settings={"os": "Linux", "arch": "armv7hf"})
    builder.add(settings={"os": "Android", "arch": "armv7hf"})
    builder.add(settings={"os": "Android", "arch": "armv8"})
    builder.add(settings={"os": "iOS"})
    builder.add(settings={"os": "Macos"})
    builder.run()
