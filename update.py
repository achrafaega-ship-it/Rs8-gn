import requests

def aega_ultra_sniper():
    sources = [
        "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u",
        "https://raw.githubusercontent.com/MoiraSama/IPTV-Arabic/main/Arabic.m3u",
        "https://raw.githubusercontent.com/tarekzort/IPTV-Daily/main/arabic.m3u",
        "https://raw.githubusercontent.com/FazzRazz/IPTV/master/Arabic.m3u",
        "https://raw.githubusercontent.com/byte-capsule/Fan_IPTV/main/IPTV_Arabic.m3u",
        "https://raw.githubusercontent.com/Yan-S-S/IPTV/main/Arabic.m3u",
        "https://raw.githubusercontent.com/ZonS-S/IPTV/main/Arabic.m3u",
        "https://raw.githubusercontent.com/M3U-Daily/M3U-Daily/main/Arabic.m3u",
        "https://raw.githubusercontent.com/LITUAN-IPTV/IPTV/main/Arabic.m3u",
        "https://raw.githubusercontent.com/sam-iptv/arabic/main/ar.m3u",
        "https://raw.githubusercontent.com/iptv-restream/iptv/master/arabic.m3u",
        "https://raw.githubusercontent.com/K-Maina/IPTV_Auto/main/Arabic.m3u",
        "https://raw.githubusercontent.com/Global-IPTV/IPTV-Lists/master/Arabic.m3u",
        "https://raw.githubusercontent.com/m3u8playlist/free-iptv-m3u8-list/master/arabic.m3u",
        "https://raw.githubusercontent.com/skatv/skatv/master/arabic.m3u",
        "https://raw.githubusercontent.com/duztin-s/iptv-arabic/main/list.m3u",
        "https://raw.githubusercontent.com/mahdidz1/iptv/main/arabic.m3u"
    ]
    
    targets = ['beIN', 'OSN', 'بين', 'أوزن', 'alkass', 'ssc']
    output = "#EXTM3U\n"
    added_links = set()

    for url in sources:
        try:
            r = requests.get(url, timeout=35)
            if r.status_code == 200:
                lines = r.text.splitlines()
                for i in range(len(lines)):
                    if lines[i].startswith("#EXTINF"):
                        if any(t.lower() in lines[i].lower() for t in targets):
                            if i + 1 < len(lines):
                                link = lines[i+1].strip()
                                if link.startswith("http") and link not in added_links:
                                    name = lines[i].split(',')[-1]
                                    output += f"#EXTINF:-1, {name}\n{link}\n"
                                    added_links.add(link)
        except:
            continue
    return output

if __name__ == "__main__":
    with open("tvlist.m3u", "w", encoding='utf-8') as f:
        f.write(aega_ultra_sniper())
