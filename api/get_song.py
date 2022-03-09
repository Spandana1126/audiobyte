from http.server import BaseHTTPRequestHandler
from urllib import parse
import youtube_dl
import json

class handler(BaseHTTPRequestHandler):
    ydl_opts = {
        'format': 'bestaudio',
        'noplaylist':'True'
    }
    BASE_URL="https://www.youtube.com/watch?v="
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        # q = dic.get("q",None)
        song_id=str(dic.get("song_id",None))
        # song_id=str((request.GET.get("song_id")))
        query_url=self.BASE_URL+song_id
        data={}
        try:
            info=True
            with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(query_url,download=False)
            data={"play_results":{"id":song_id,
                    "title":info["title"],
                    "play_url":info["formats"][0]['url'],
                    "description":info["description"]
                }}
        except:
            data={"error":"Something Went Wrong"}
        data = json.dumps(data)
        self.wfile.write(data.encode(encoding='utf_8'))
        return
