from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import json

SEARCH_URL = "https://suggestqueries-clients6.youtube.com/complete/search?client=youtube&q="

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        dic = dict(parse.parse_qsl(parse.urlsplit(s).query))
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        r=dic.get("data",None)
        print(r)
        res=str(requests.get(SEARCH_URL+r).text)[19:-1]
        data = {}
        if r:
            data=json.dumps({"results":res})
        self.wfile.write(data.encode(encoding='utf_8'))
        return
