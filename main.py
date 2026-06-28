from core.login import login_whatsapp
from core.escritor_master import escrever_master
import time

print("=" * 60)
print("🍞 BOT DO PÃO - MODO SELETORES POR CLASSE")
print("📌 Lendo a cada 3 segundos")
print("=" * 60)

driver = login_whatsapp()

if driver:
    print("\n✅ LOGIN REALIZADO!")
    print("🔄 Iniciando loop...\n")
    try:
        while True:
            escrever_master(driver)
            time.sleep(3)
    except KeyboardInterrupt:
        driver.quit()
        print("\n👋 Bot encerrado.")
else:
    print("❌ Falha no login.")
