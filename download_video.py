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
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': output_path + '%(title)s.%(ext)s',
    }
    
    if cookie_file:
        # 启用cookie支持以实现身份验证功能
        ydl_opts['cookiefile'] = cookie_file
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # 使用yt_dlp库创建下载管理器并开始下载视频
        ydl.download([url])


if __name__ == "__main__":
    video_url = "https://www.bilibili.com/video/BV1sg411Y7n7/?spm_id_from=333.337.search-card.all.click&vd_source=8d3ddbf2d0edec4feaea7e750337df94"
    output_directory = "./downloads/"
    cookie_file = "cookies.txt"  # 替换为你的cookie文件路径
    download_video(video_url, output_directory)