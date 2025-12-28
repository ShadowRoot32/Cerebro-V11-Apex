import sqlite3, os
from datetime import datetime

class CerebroStorage:
    def __init__(self):
        self.db_path = "cerebro.db"
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS vulns 
            (id INTEGER PRIMARY KEY, timestamp TEXT, url_target TEXT, type TEXT, payload TEXT)''')
        self.conn.commit()
        if not os.path.exists("reports"): os.makedirs("reports")

    def add_vuln(self, url, t, p):
        ts = datetime.now().strftime("%H:%M:%S")
        self.cursor.execute('INSERT INTO vulns (timestamp, url_target, type, payload) VALUES (?,?,?,?)', (url, t, p))
        self.conn.commit()

    def generate_html_report(self, filter_url):
        self.cursor.execute('SELECT * FROM vulns WHERE url_target = ?', (filter_url,))
        rows = self.cursor.fetchall()
        if not rows: return None
        fname = f"reports/BUG_{datetime.now().strftime('%H%M%S')}.html"
        html = f"<html><body style='font-family:monospace;background:#0d1117;color:#0f0;padding:20px;'><h1>CEREBRO V11 REPORT</h1><hr><table>"
        for r in rows:
            html += f"<tr><td>{r[1]}</td><td>{r[3]}</td><td><code>{r[4]}</code></td></tr>"
        html += "</table></body></html>"
        with open(fname, "w") as f: f.write(html)
        return fname