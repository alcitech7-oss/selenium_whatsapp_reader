from core.login import login_whatsapp
from selenium.webdriver.common.by import By
import time

print("=" * 60)
print("🧪 TESTE DE SELETORES FIXOS")
print("📌 Vai tentar capturar remetente e mensagem pelos seletores")
print("=" * 60)

driver = login_whatsapp()

if driver:
    print("\n✅ LOGIN REALIZADO!")
    time.sleep(3)

    # Seletores fixos baseados no mapa
    seletor_remetente = "(//span[text()])[12]"
    seletor_mensagem = "(//span[text()])[14]"

    try:
        remetente = driver.find_element(By.XPATH, seletor_remetente).text
        print(f"📞 Remetente: {remetente}")
    except Exception as e:
        print(f"❌ Erro ao capturar remetente: {e}")

    try:
        mensagem = driver.find_element(By.XPATH, seletor_mensagem).text
        print(f"💬 Mensagem: {mensagem}")
    except Exception as e:
        print(f"❌ Erro ao capturar mensagem: {e}")

    driver.quit()
else:
    print("❌ Falha no login.")
