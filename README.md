# JarPatcher
通过jar包快速生成patch模版

## Patch方法

1. 修改`config.py`
```python
javaPath = "*/bin/java.exe"    #请填写java绝对路径
jarPath = "design-cms.jar"     #如果使用的是war包请先将后缀改为jar
copyConfig=True                #是否将IDEA配置进行复制
```
2. src目录下存放对应的jar包
3. 运行程序`main.py`
```shell
python3 main.py
```
4. 可以在./target下找到经过反编译的jar包, ./project下找到相应的IDEA工程

5. 打开IDEA项目完成手动配置（手动配置说明见后）

## 程序逻辑

1. 使用java-decompiler.jar反编译

2. 将对应Java文件和依赖jar包拷贝到project下（这里以jar包为实例）

## 手动配置

1. 打开项目，此时IDEA会自动做好默认配置
2. 设置SDK和class输出，在***文件-项目结构-项目设置-项目-SDK***中更改项目SDK，将编译器输出改为当前项目目录下的out文件夹
3. 设置源代码，在***文件-项目结构-项目设置-模块-当前项目***中将**src/main/java**标记为源代码
4. 设置依赖库，在***文件-项目结构-项目设置-库***中将lib文件夹添加为库文件夹
5. 设置jar包或war包打包，在***文件-项目结构-项目设置-工件***中添加jar或者Web应用程序，将清单文件设置为**META-INF/MANIFEST.MF**，将可用元素全部拖入即可

## 最后

个人推荐的用法是不进行jar包或war包的打包，只需要获取对应patch的class文件，然后通过压缩软件对编译好的class文件直接进行替换，目前测试Bandizip可以保证替换前后jar包和war包的可用性

有部分的jar包war包反编译的class是经过编译器优化的，这也导致反编译后生成的Java文件会有奇怪的语法错误，这时候对症下药即可，也可以直接删除所有java文件只保留你需要进行patch的java文件



















