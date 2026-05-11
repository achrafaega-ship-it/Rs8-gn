import requests
import re

def get_clean_data():
    url = "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        links = re.findall(r'(http[s]?://[^\s]+?\.m3u8)', response.text)
        output = "#EXTM3U\n"
        for i, link in enumerate(links[:50]):
            output += f"#EXTINF:-1, AEGA Channel {i+1}\n{link}\n"
        return output
    except:
        return "#EXTM3U"

if __name__ == "__main__":
    content = get_clean_data()
    with open("net_link.txt", "w", encoding='utf-8') as f:
        f.write(content)

