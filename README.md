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

### 使用方法

- python3 main.py -s '你好，世界'

- python3 main.py -f '/your/file/path/name'

### 其他

想要调整乱序区块长度，修改 main.py 中的 seg_len 值即可。默认是5。