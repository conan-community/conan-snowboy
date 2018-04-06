# conan-snowboy

![conan-snowboy image](conan_snowboy.png)

[Conan.io](https://conan.io) package for [snowboy](https://snowboy.kitt.ai) project.

The packages generated with this *conanfile.py* can be found in [Bintray](https://bintray.com/conan-community/conan/snowboy%3Aconan).

## Basic setup

    $ conan install snowboy/1.3.0@conan/stable

## Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*:

    [requires]
    snowboy/1.3.0@conan/stable

    [generators]
    cmake
    
    
## License

Current repo is [MIT License](LICENSE)
Check the specific license for the library being packaged.