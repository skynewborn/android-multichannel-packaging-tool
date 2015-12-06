Android多渠道打包工具
==================

多渠道打包工具使用Python编写，可用于Android应用的渠道包生成，特点是可直接针对apk进行处理，打包速度快，无需重新签名。此工具的思路来源于[美团][1]，特此声明并感谢。

使用方法
-------------------------

在脚本所在目录下：

	python pack.py [path_to_apk] [path_to_config]

即可。

要打包的渠道号需要写在配置文件中，支持同时生成多个渠道包，不同渠道号之间以逗号分隔。具体可参考`config_sample`文件。

生成的所有渠道包会打包为一个output.zip文件，便于下载和传输。

TODO
-----------

增加更多参数控制的支持，如生成的文件名、是否生成zip文件等。

Acknowledge
-----------

[美团Android自动化之旅—生成渠道包][1]

License
-----------

    MIT
    
    Copyright (c) 2015 skynewborn@github.com

	Permission is hereby granted, free of charge, to any person obtaining a copy
	of this software and associated documentation files (the "Software"), to deal
	in the Software without restriction, including without limitation the rights
	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
	copies of the Software, and to permit persons to whom the Software is
	furnished to do so, subject to the following conditions:
	
	The above copyright notice and this permission notice shall be included in
	all copies or substantial portions of the Software.
	
	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
	THE SOFTWARE.


 [1]: http://tech.meituan.com/mt-apk-packaging.html