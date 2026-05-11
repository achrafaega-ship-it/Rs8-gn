from flask import Flask, Response
import requests

app = Flask(__name__)

def aega_ai_sniper():
    sources = [
        "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u",
        "https://raw.githubusercontent.com/MoiraSama/IPTV-Arabic/main/Arabic.m3u",
        "https://raw.githubusercontent.com/tarekzort/IPTV-Daily/main/arabic.m3u",
        "https://raw.githubusercontent.com/FazzRazz/IPTV/master/Arabic.m3u",
        "https://raw.githubusercontent.com/byte-capsule/Fan_IPTV/main/IPTV_Arabic.m3u"
    ]
    headers = {'User-Agent': 'Mozilla/5.0'}
    targets = ['beIN', 'OSN', 'بين', 'أوزن', 'alkass', 'ssc', 'الجزيرة']
    output = "#EXTM3U\n"
    
     
    output += "#EXTINF:-1, beIN SPORTS News Live\nhttps://www.youtube.com/watch?v=X_shN9F90vY\n"
    output += "#EXTINF:-1, Al Jazeera Arabic Live\nhttps://www.youtube.com/watch?v=bNyUCPDXtgE\n"

    added_links = set()
    for url in sources:
        try:
            r = requests.get(url, headers=headers, timeout=15)
            if r.status_code == 200:
                for line in r.text.splitlines():
                    if line.startswith("#EXTINF") and any(t.lower() in line.lower() for t in targets):
                        idx = r.text.splitlines().index(line)
                        link = r.text.splitlines()[idx+1].strip()
                        if link.startswith("http") and link not in added_links:
                            output += f"{line}\n{link}\n"
                            added_links.add(link)
        except: continue
    return output

@app.route('/')
def home(): return "AEGA AI Sniper is Active"

@app.route('/playlist.m3u')
def get_playlist():
    return Response(aega_ai_sniper(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
    
