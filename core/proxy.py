from mitmproxy import http
from core.ui import TacticalHUD
from core.worker import AttackWorker
from core.brain import CerebroBrain
import re

class CerebroInterceptor:
    def __init__(self):
        self.ui = TacticalHUD()
        self.brain = CerebroBrain()
        self.active_worker = None
        self.ignore = ["google", "static", "facebook", "bing", "apple", "cloudflare", "ads", "clarity.ms"]

    def request(self, flow: http.HTTPFlow):
        domain = flow.request.host
        if any(x in domain for x in self.ignore): return
        if flow.request.path.lower().endswith(('.js', '.css', '.png', '.jpg', '.ico')): return

        q, post = dict(flow.request.query), flow.request.method == "POST"
        path_inj = bool(re.search(r'/\d+', flow.request.path))

        if q or post or path_inj:
            if self.active_worker and self.active_worker.is_alive(): return
            
            self.ui.show_intercept_notif(domain, flow.request.method)
            
            # FIXED: Mengirim TEPAT 3 argumen: flow, headers, dan tech
            worker = AttackWorker(
                flow, 
                dict(flow.request.headers), 
                self.brain.analyze_tech(flow.request.headers)
            )
            worker.start()
            self.active_worker = worker

addons = [CerebroInterceptor()]