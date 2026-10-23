import datetime
import requests

def obter_dolar_bcb():
    hoje = datetime.date.today().strftime('%m-%d-%Y')
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(data=@data)?@data='{hoje}'&\$format=json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if data.get('value'):
                cotacao = data['value'][0]['cotacaoVenda']
                return f"R$ {cotacao:.2f}".replace('.', ',')
    except Exception:
        pass
    return "R$ 5,03"

def gerar_html_painel():
    data_atual = datetime.datetime.now().strftime('%d/%m/%Y')
    dolar_val = obter_dolar_bcb()
    
    html_content = f"""<div style="background: #ffffff;border: 1px solid #e2e8f0;padding: 12px;border-radius: 12px;max-width: 100%;margin: 5px auto;font-family: Arial, sans-serif">

<!-- Cabeçalho -->
<div style="display: flex;flex-direction: column;border-bottom: 2px solid #0f172a;padding-bottom: 10px;margin-bottom: 10px">
<div style="display: flex;justify-content: space-between;align-items: center;flex-wrap: wrap;gap: 6px">
<h2 style="color: #0f172a;margin: 0;font-size: 14px;font-weight: bold;line-height: 1.3">☕ Agro Frequência | Painel do Café & Mercado</h2>
<span style="background: #0f172a;color: #ffffff;font-size: 9px;padding: 3px 8px;border-radius: 20px;font-weight: 600;white-space: nowrap">Atualizado: {data_atual}</span>
</div>
<span style="background: #f1f5f9;color: #334155;font-size: 10px;padding: 3px 8px;border-radius: 20px;font-weight: 600;width: fit-content;margin-top: 6px">Foco: Rondônia (RO) & Mato Grosso (MT) | Cepea / ICE</span>
</div>

<!-- Destaques em Cartões (Café em 1º Lugar) -->
<div style="display: grid;grid-template-columns: repeat(2, 1fr);gap: 6px;margin-bottom: 12px">
<div style="background: #fffbeb;border: 1px solid #fde68a;padding: 8px;border-radius: 8px">
<div style="font-size: 9px;color: #b45309;font-weight: bold;text-transform: uppercase">☕ Café Arábica Futuro (ICE)</div>
<div style="font-size: 13px;font-weight: bold;color: #0f172a;margin-top: 2px">US$ 285,40 <span style="color: #16a34a;font-size: 10px">▲ +1,15%</span></div>
</div>
<div style="background: #fffbeb;border: 1px solid #fde68a;padding: 8px;border-radius: 8px">
<div style="font-size: 9px;color: #b45309;font-weight: bold;text-transform: uppercase">☕ Conilon Físico (RO)</div>
<div style="font-size: 13px;font-weight: bold;color: #0f172a;margin-top: 2px">R$ 882,00 <span style="color: #16a34a;font-size: 10px">▲ +0,45%</span></div>
</div>
<div style="background: #f8fafc;border: 1px solid #e2e8f0;padding: 8px;border-radius: 8px">
<div style="font-size: 9px;color: #64748b;font-weight: 600;text-transform: uppercase">Dólar (USD - PTAX)</div>
<div style="font-size: 13px;font-weight: bold;color: #0f172a;margin-top: 2px">{dolar_val} <span style="color: #16a34a;font-size: 10px">▲ +0,11%</span></div>
</div>
<div style="background: #f8fafc;border: 1px solid #e2e8f0;padding: 8px;border-radius: 8px">
<div style="font-size: 9px;color: #64748b;font-weight: 600;text-transform: uppercase">Funrural (Retenção Lei)</div>
<div style="font-size: 13px;font-weight: bold;color: #0f172a;margin-top: 2px">1,2% <span style="color: #64748b;font-size: 10px">(Físico/Jurídico)</span></div>
</div>
</div>

<!-- TABELA 1: CAFÉ EM DESTAQUE ABSOLUTO -->
<h3 style="color: #0f172a;font-size: 12px;margin: 8px 0 4px 0;border-left: 3px solid #d97706;padding-left: 6px">☕ Cotações do Café (Físico & Futuros)</h3>
<div class="agro-tabela-responsiva" style="margin-bottom: 10px">
<table style="width: 100%;border-collapse: collapse;font-size: 11px">
<thead>
<tr style="background: #f1f5f9;border-bottom: 2px solid #cbd5e1;text-align: left">
<th style="padding: 6px 4px;color: #1e293b;width: 34%">Produto / Contrato</th>
<th style="padding: 6px 4px;color: #1e293b;width: 26%">Bolsa / Praça</th>
<th style="padding: 6px 4px;color: #1e293b;width: 20%">Valor</th>
<th style="padding: 6px 4px;color: #1e293b;width: 20%">Líq. Funrural</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #f1f5f9;background: #fffbeb">
<td style="padding: 6px 4px;font-weight: 600;color: #0f172a">☕ Conilon (RO)</td>
<td style="padding: 6px 4px;color: #64748b">Cacoal / RO</td>
<td style="padding: 6px 4px;font-weight: bold;color: #d97706">R$ 882,00</td>
<td style="padding: 6px 4px;color: #0f172a">R$ 871,42</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9">
<td style="padding: 6px 4px;font-weight: 600;color: #0f172a">☕ Conilon (ES)</td>
<td style="padding: 6px 4px;color: #64748b">Vitória / ES</td>
<td style="padding: 6px 4px;font-weight: bold;color: #d97706">R$ 910,00</td>
<td style="padding: 6px 4px;color: #0f172a">R$ 899,08</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9;background: #fffbeb">
<td style="padding: 6px 4px;font-weight: 600;color: #0f172a">☕ Arábica Futuro</td>
<td style="padding: 6px 4px;color: #64748b">ICE NY (KC)</td>
<td style="padding: 6px 4px;font-weight: bold;color: #d97706">US$ 285,40</td>
<td style="padding: 6px 4px;color: #64748b">-</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9">
<td style="padding: 6px 4px;font-weight: 600;color: #0f172a">☕ Conilon Futuro</td>
<td style="padding: 6px 4px;color: #64748b">ICE Londres (RM)</td>
<td style="padding: 6px 4px;font-weight: bold;color: #d97706">US$ 3.420/t</td>
<td style="padding: 6px 4px;color: #64748b">-</td>
</tr>
</tbody>
</table>
</div>

<!-- TABELA 2: DEMAIS COMMODITIES -->
<h3 style="color: #0f172a;font-size: 12px;margin: 8px 0 4px 0;border-left: 3px solid #0f172a;padding-left: 6px">📈 Demais Commodities (MT / RO)</h3>
<div class="agro-tabela-responsiva">
<table style="width: 100%;border-collapse: collapse;font-size: 11px">
<thead>
<tr style="background: #f1f5f9;border-bottom: 2px solid #cbd5e1;text-align: left">
<th style="padding: 6px 4px;color: #1e293b;width: 34%">Produto</th>
<th style="padding: 6px 4px;color: #1e293b;width: 26%">Região</th>
<th style="padding: 6px 4px;color: #1e293b;width: 20%">Valor</th>
<th style="padding: 6px 4px;color: #1e293b;width: 20%">Líq. Funrural</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #f1f5f9">
<td style="padding: 6px 4px;font-weight: 600;color: #0f172a">🐂 Boi Gordo</td>
<td style="padding: 6px 4px;color: #64748b">MT / RO</td>
<td style="padding: 6px 4px;font-weight: bold;color: #d97706">R$ 340,20</td>
<td style="padding: 6px 4px;color: #0f172a">R$ 336,12</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9;background: #fffbeb">
<td style="padding: 6px 4px;font-weight: 600;color: #0f172a">🌱 Soja</td>
<td style="padding: 6px 4px;color: #64748b">MT / RO</td>
<td style="padding: 6px 4px;font-weight: bold;color: #d97706">R$ 138,50</td>
<td style="padding: 6px 4px;color: #0f172a">R$ 136,84</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9">
<td style="padding: 6px 4px;font-weight: 600;color: #0f172a">🌽 Milho</td>
<td style="padding: 6px 4px;color: #64748b">MT / RO</td>
<td style="padding: 6px 4px;font-weight: bold;color: #d97706">R$ 46,00</td>
<td style="padding: 6px 4px;color: #0f172a">R$ 45,45</td>
</tr>
</tbody>
</table>
</div>

<div style="background: #f8fafc;border-left: 3px solid #3b82f6;padding: 6px;font-size: 9px;color: #475569;border-radius: 0 4px 4px 0;margin-top: 8px"><strong>Nota:</strong> Painel focado no mercado de Café (RO/ES e Futuros ICE). Atualizado em {data_atual}.</div>
</div>"""
    
    with open("painel-agro.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Painel HTML gerado com sucesso!")

if __name__ == "__main__":
    gerar_html_painel()
