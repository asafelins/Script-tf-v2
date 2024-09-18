import platform
import hashlib
from datetime import datetime, timedelta, timezone
import pyperclip
import requests

class Licenca:
    def __init__(self, hwid_esperado, data_criacao_licenca):
        self.hwid_esperado = hwid_esperado
        self.data_criacao_licenca = data_criacao_licenca

    def obter_hwid(self):
        system_info = platform.uname()
        hwid_data = f"{system_info.node}{system_info.processor}{system_info.system}"
        return hashlib.sha256(hwid_data.encode()).hexdigest()

    def copiar_hwid(self):
        hwid_atual = self.obter_hwid()
        pyperclip.copy(hwid_atual)

    def obter_data_remota(self):
        url = "https://worldtimeapi.org/api/timezone/America/Sao_Paulo"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data_json = response.json()
                data_str = data_json["datetime"]
                data_atual = datetime.fromisoformat(data_str)
                data_atual = data_atual.replace(tzinfo=timezone.utc)
                return data_atual
        except requests.exceptions.RequestException as e:
            print(f"Erro de conexão: {e}")
        return None

    def verificar_licenca(self):
        hwid_atual = self.obter_hwid()
        if hwid_atual != self.hwid_esperado:
            return False
        data_atual = self.obter_data_remota()
        if data_atual and data_atual > self.data_criacao_licenca.replace(tzinfo=timezone.utc) + timedelta(days=300):
            return False
        return True
