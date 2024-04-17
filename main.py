import requests
from bs4 import BeautifulSoup
from datetime import datetime
import flet as ft


def get_video(e):
    req = requests.get(get_url.value)
    response = req.content

    soup = BeautifulSoup(response, 'html.parser')
    extract_url = soup.find("video", class_="hwa kVc MIw L4E")['src']
    convert_url = extract_url.replace("hls", "720p").replace("m3u8", "mp4")
    response = requests.get(convert_url, stream=True)
    with open(f'{datetime.now().strftime("%d_%m_%H_%M_%S_") + ".mp4"}', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)


get_url = ft.TextField(label='URL...', value='')
download_btn = ft.ElevatedButton(text='Download', on_click=get_video)


def main(page: ft.Page):
    page.title = 'Pinterest Downloader'
    page.theme_mode = 'dark'

    page.add(
        ft.Column(
            [
                get_url,
                download_btn
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(target=main)
