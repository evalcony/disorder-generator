# disorder-generator
中文乱序生成器

### 功能

将中文字符顺序打乱。

可接受一句话，或者一个文件。

对数字、英文，不影响。例如
```
输入 hello, world. 你好,世界
输出 hello, world. 好你,界世
```

### 特点

本生成器特别区分了一般的符号，不对符号进行乱序，以保证语句的间隔完整性，不影响阅读。

举个例子，`你好，世界`，输出的结果不会是 `好你世界，` 这种，而依然保留原文的结构。

### 使用方法

- python3 main.py -s '你好，世界'

- python3 main.py -f '/your/file/path/name'

### 其他

想要调整乱序区块长度，修改 main.py 中的 seg_len 值即可。默认是5。