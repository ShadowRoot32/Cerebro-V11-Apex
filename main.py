from core.proxy import CerebroInterceptor
from core.ui import TacticalHUD

# Inisialisasi UI untuk banner
ui = TacticalHUD()
ui.show_banner()

# Load addon untuk mitmproxy
addons = [CerebroInterceptor()]