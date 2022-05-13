#! /usr/bin/env python
#-*-coding:utf-8-*-
# Path: kylin-install\fonts-install.py
# 功能：安装字体
# 实现过程:把字体文件下载到缓存目录,统一拷贝到字体目录,给权限,删除缓存目录以及缓存文件,提示关闭WPS(可选)
import os

# 下载字体文件
font_url = {
    "仿宋Gb2312":"https://gitee.com/kliuoi/kylin-install/raw/master/fonts/%E4%BB%BF%E5%AE%8B_GB2312.ttf",
    "方正小标宋_GBK":"https://gitee.com/kliuoi/kylin-install/raw/master/fonts/%E6%96%B9%E6%AD%A3%E5%B0%8F%E6%A0%87%E5%AE%8B_GBK.ttf",
    "方正小标宋简体":"https://gitee.com/kliuoi/kylin-install/raw/master/fonts/%E6%96%B9%E6%AD%A3%E5%B0%8F%E6%A0%87%E5%AE%8B%E7%AE%80%E4%BD%93.ttf",
    "楷体_GB2312":"https://gitee.com/kliuoi/kylin-install/raw/master/fonts/%E6%A5%B7%E4%BD%93_GB2312.ttf",
    "黑体":"https://gitee.com/kliuoi/kylin-install/raw/master/fonts/%E9%BB%91%E4%BD%93.ttf"
}

def init():
    # 定义缓存文件路径,如果没有则创建
    global cache_path
    cache_path = '/tmp/fonts'
    os.system('mkdir -p %s' % cache_path)

    # 定义字体文件安装路径，如果没有则新建
    global font_path
    font_path = '/usr/share/fonts/myfonts'
    os.system('mkdir -p %s' % font_path)

# 下载字体文件
def download_font():
    global font_url
    for font_name,font_url in font_url.items():
        print('正在下载字体文件:%s' % font_name)
        os.system('wget -P %s %s' % (cache_path,font_url))
        print("下载%s完成" % font_name)

# 安装字体
def install_font():
    print('正在安装字体文件...')
    os.system('cp %s/* %s' % (cache_path,font_path))
    print('安装完成')

# 关闭WPS
def close_wps():
    input('请手动关闭WPS,按回车键继续...')
    os.system('killall -9 wps')

# 主函数
def main():
    init()
    download_font()
    install_font()
    close_wps()

main()