# 使用视频下载器yt-dlp下载全网视频

> 仓库地址

::github{repo="yt-dlp/yt-dlp"}

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714115009549.png)

点击右下角的release

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714120445194.png)

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714120602322.png)

除此之外，还需下载[ffmpeg](https://www.ffmpeg.org/)插件

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714120923322.png)

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714121038636.png)

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714121100059.png)

解压出来后，需要这两个文件

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714121210274.png)

随后，新建一个文件夹，文件夹下有这三个文件`yt-dlp` `ffprobe` `ffmpeg`

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714134815964.png)

然后设置下这个文件夹的环境变量`path`，这样的话我们在哪里都能通过命令运行`yt-dlp`

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714140252807.png)

## 测试下载bilibili视频	

在你想放置下载视频的文件夹下打开cmd，输入命令`yt-dlp`+`想下载的视频链接`

```cmd
yt-dlp https://www.bilibili.com/video/BV1sg411Y7n7/?spm_id_from=333.337.search-card.all.click&vd_source=8d3ddbf2d0edec4feaea7e750337df94
```

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714140804599.png)

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/image-20250714141104780.png)

> 可以看到视频已经下载下来了,但是4k的视频下载下来只有`2k`，yt-dlp还可以传一个cookie参数，用来提取用户登录cookie，从而下载最高清晰度的视频

## 测试下载油管视频

```cmd
yt-dlp https://www.youtube.com/watch?v=5LxsViMm25o&list=PLTtnfaUimdLgRaBMnVe7iyctHbMTA4RGg
```

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714143523960.png)

也是可以下载下来并正常播放的

## 传入cookie参数来下载

在传入之前我们需要安装一个`浏览器插件`

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/image-20250714144530716.png)

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/image-20250714144653999.png)

然后我们测试，把b站网页上所有的`cookie`下载下来

cookie在这里可以理解为`下载高清视频的凭证`

```cmd
yt-dlp --cookies cookies.txt https://www.bilibili.com/video/BV1sg411Y7n7/?spm_id_from=333.337.search-card.all.click&vd_source=8d3ddbf2d0edec4feaea7e750337df94
```

> 这里注意，把cookies.txt文件放在运行cmd的当前目录下

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714145919037.png)

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714145949678.png)

> 也是可以看到视频帧率变成了4k

## 自定义输出文件名

```
-o "%(title)s.%(ext)s"
```

上面的代码表示的是用`视频标题名`.`视频文件类型名`的形式保存,现在测试一下

![](https://cdn.jsdelivr.net/gh/YAO-JIAYE/my_imgs_repo@main/imgs/20250714153634943.png)

## 用python脚本下载

```python
import yt_dlp


def download_video(url, output_path, cookie_file=None):
    """
    下载指定URL的视频并保存到指定目录

    参数:
        url (str): 视频页面的URL地址
        output_path (str): 用于存储下载视频的本地路径
        cookie_file (str, optional): 包含cookies信息的文件路径，用于需要登录验证的网站. 默认为None.

    返回:
        None: 函数不返回任何值
    """
    ydl_opts = {
        # 'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_path + '%(title)s.%(ext)s',
    }
    
    if cookie_file:
        # 启用cookie支持以实现身份验证功能
        ydl_opts['cookiefile'] = cookie_file
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # 使用yt_dlp库创建下载管理器并开始下载视频
        ydl.download([url])


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=36LsS8T5RHE"
    output_directory = "./downloads/"
    cookie_file = ""  # 替换为你的cookie文件路径
    download_video(video_url, output_directory)
```

用python脚本也能下载，不过有个很大的问题

:::note

下载多了，会被视频网站阻止，得过一段时间才能恢复

:::