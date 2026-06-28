from core.login import login_whatsapp
from testes.mapping import mapear_spans
import time

print("=" * 60)
print("🗺️  MAPEADOR DE SPANS")
print("📌 Gera um mapa completo de todos os spans na tela")
print("=" * 60)

driver = login_whatsapp()

if driver:
    print("\n✅ LOGIN REALIZADO!")
    time.sleep(3)
    arquivo = mapear_spans(driver)
    print(f"📂 Mapa salvo em: {arquivo}")
    driver.quit()
else:
    print("❌ Falha no login.")
