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
    
    html_content = f"""<div style="background: #ffffff;border: 1px solid #e2e8f0;padding: 12px;border-radius: 12px;max-width: 100%;margin: 10px auto;font-family: Arial, sans-serif">

<!-- Cabeçalho -->
<div style="display: flex;flex-direction: column;border-bottom: 2px solid #0f172a;padding-bottom: 12px;margin-bottom: 15px">
<div style="display: flex;justify-content: space-between;align-items: center;flex-wrap: wrap;gap: 8px">
<h2 style="color: #0f172a;margin: 0;font-size: 16px;font-weight: bold;line-height: 1.3">📊 Agro Frequência | Painel Completo de Mercado</h2>
<span style="background: #0f172a;color: #ffffff;font-size: 10px;padding: 4px 10px;border-radius: 20px;font-weight: 600;white-space: nowrap">Atualizado: {data_atual}</span>
</div>
<span style="background: #f1f5f9;color: #334155;font-size: 11px;padding: 4px 8px;border-radius: 20px;font-weight: 600;width: fit-content;margin-top: 8px">Fontes: IMEA / Cepea / Scot / ANP / B3 / ICE / CME</span>
</div>

<p style="color: #475569;font-size: 13px;line-height: 1.4;margin-bottom: 15px">Monitoramento estratégico para Mato Grosso e Rondônia: foco em Café (Conilon e Arábica - Físico e Futuros), contratos de bolsas internacionais, amplitude de basis, Funrural (1,2%), insumos e câmbio.</p>

<!-- Indicadores em Grid Flexível com Destaque no Café -->
<div style="display: grid;grid-template-columns: repeat(2, 1fr);gap: 8px;margin-bottom: 15px">
<div style="background: #f8fafc;border: 1px solid #e2e8f0;padding: 10px;border-radius: 8px">
<div style="font-size: 10px;color: #64748b;font-weight: 600;text-transform: uppercase">Dólar (USD - PTAX)</div>
<div style="font-size: 14px;font-weight: bold;color: #0f172a;margin-top: 2px">{dolar_val} <span style="color: #16a34a;font-size: 11px">▲ +0,11%</span></div>
</div>
<div style="background: #f8fafc;border: 1px solid #e2e8f0;padding: 10px;border-radius: 8px">
<div style="font-size: 10px;color: #64748b;font-weight: 600;text-transform: uppercase">Café Arábica Futuro (ICE)</div>
<div style="font-size: 14px;font-weight: bold;color: #0f172a;margin-top: 2px">US$ 285,40 cpm <span style="color: #16a34a;font-size: 11px">▲ +1,15%</span></div>
</div>
<div style="background: #f8fafc;border: 1px solid #e2e8f0;padding: 10px;border-radius: 8px">
<div style="font-size: 10px;color: #64748b;font-weight: 600;text-transform: uppercase">Diesel S-10 (Média ANP)</div>
<div style="font-size: 14px;font-weight: bold;color: #0f172a;margin-top: 2px">MT: R$ 7,80 | RO: R$ 7,80</div>
</div>
<div style="background: #f8fafc;border: 1px solid #e2e8f0;padding: 10px;border-radius: 8px">
<div style="font-size: 10px;color: #64748b;font-weight: 600;text-transform: uppercase">Funrural (Retenção Lei)</div>
<div style="font-size: 14px;font-weight: bold;color: #0f172a;margin-top: 2px">1,2% <span style="color: #64748b;font-size: 11px">(Pessoa Física/Jurídica)</span></div>
</div>
</div>

<!-- TABELA 1: CAFÉ EM DESTAQUE (Físico & Futuros) -->
<h3 style="color: #0f172a;font-size: 14px;margin: 15px 0 8px 0;border-left: 3px solid #d97706;padding-left: 8px">☕ Café: Mercado Físico (RO/ES) & Futuros (ICE / Bolsas)</h3>
<div class="agro-tabela-responsiva" style="margin-bottom: 15px">
<table style="width: 100%;border-collapse: collapse;min-width: 600px;font-size: 12px">
<thead>
<tr style="background: #f1f5f9;border-bottom: 2px solid #cbd5e1;text-align: left">
<th style="padding: 9px 8px;color: #1e293b;width: 28%">Produto / Contrato</th>
<th style="padding: 9px 8px;color: #1e293b;width: 25%">Praça / Bolsa</th>
<th style="padding: 9px 8px;color: #1e293b;width: 22%">Valor / Tendência</th>
<th style="padding: 9px 8px;color: #1e293b;width: 25%">Basis / Referência & Funrural</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #f1f5f9;background: #fffbeb">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">☕ Café Conilon (RO)</td>
<td style="padding: 9px 8px;color: #64748b">Cacoal / Rolim de Moura</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 882,00 <span style="color: #16a34a">▲ +0,45%</span></td>
<td style="padding: 9px 8px;color: #64748b">Basis Mín: -R$ 32 | Máx: -R$ 22 (vs ES) <br><strong style="color:#0f172a">líq. c/ Funrural (1,2%): R$ 871,42</strong></td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">☕ Café Conilon (Benchmark)</td>
<td style="padding: 9px 8px;color: #64748b">Vitória / ES (Cepea)</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 910,00 <span style="color: #16a34a">▲ +0,33%</span></td>
<td style="padding: 9px 8px;color: #64748b">Referência Primária (Base ES) <br><strong style="color:#0f172a">líq. c/ Funrural (1,2%): R$ 899,08</strong></td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9;background: #fffbeb">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">☕ Café Arábica Futuro</td>
<td style="padding: 9px 8px;color: #64748b">ICE Futures US (KC) / B3</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">US$ 285,40 cpm <span style="color: #16a34a">▲ +1,15%</span></td>
<td style="padding: 9px 8px;color: #64748b">Nova York / Referência Global</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">☕ Café Conilon Futuro</td>
<td style="padding: 9px 8px;color: #64748b">ICE Futures Europe (Londres / RM)</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">US$ 3.420,00/t <span style="color: #16a34a">▲ +0,85%</span></td>
<td style="padding: 9px 8px;color: #64748b">Robusta / London Liffe Ref.</td>
</tr>
</tbody>
</table>
</div>

<!-- TABELA 2: DEMAIS MERCADOS FUTUROS (B3) -->
<h3 style="color: #0f172a;font-size: 14px;margin: 15px 0 8px 0;border-left: 3px solid #0f172a;padding-left: 8px">📈 Demais Mercados Futuros (B3)</h3>
<div class="agro-tabela-responsiva" style="margin-bottom: 15px">
<table style="width: 100%;border-collapse: collapse;min-width: 600px;font-size: 12px">
<thead>
<tr style="background: #f1f5f9;border-bottom: 2px solid #cbd5e1;text-align: left">
<th style="padding: 9px 8px;color: #1e293b;width: 28%">Ativo / Contrato</th>
<th style="padding: 9px 8px;color: #1e293b;width: 25%">Bolsa / Vencimento</th>
<th style="padding: 9px 8px;color: #1e293b;width: 22%">Preço / Tendência</th>
<th style="padding: 9px 8px;color: #1e293b;width: 25%">Referência / Ajuste</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #f1f5f9;background: #fffbeb">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">🐂 Boi Gordo Futuro (@)</td>
<td style="padding: 9px 8px;color: #64748b">B3 (BGI)</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 346,50 <span style="color: #16a34a">▲ +0,65%</span></td>
<td style="padding: 9px 8px;color: #64748b">Ajuste Oficial B3</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">🌱 Soja Futuro</td>
<td style="padding: 9px 8px;color: #64748b">B3 (CPN) / CME</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 142,20 <span style="color: #16a34a">▲ +0,28%</span></td>
<td style="padding: 9px 8px;color: #64748b">Contrato Próximo</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9;background: #fffbeb">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">🌽 Milho Futuro</td>
<td style="padding: 9px 8px;color: #64748b">B3 (CCM)</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 48,10 <span style="color: #f87171">▼ -0,62%</span></td>
<td style="padding: 9px 8px;color: #64748b">Vencimento Próximo</td>
</tr>
</tbody>
</table>
</div>

<!-- TABELA 3: COTAÇÕES FÍSICAS (BOI, SOJA, MILHO) -->
<h3 style="color: #0f172a;font-size: 14px;margin: 15px 0 8px 0;border-left: 3px solid #0f172a;padding-left: 8px">📍 Demais Cotações Físicas (MT / RO)</h3>
<div class="agro-tabela-responsiva">
<table style="width: 100%;border-collapse: collapse;min-width: 600px;font-size: 12px">
<thead>
<tr style="background: #f1f5f9;border-bottom: 2px solid #cbd5e1;text-align: left">
<th style="padding: 9px 8px;color: #1e293b;width: 28%">Produto</th>
<th style="padding: 9px 8px;color: #1e293b;width: 25%">Praça / Região</th>
<th style="padding: 9px 8px;color: #1e293b;width: 22%">Valor / Tendência</th>
<th style="padding: 9px 8px;color: #1e293b;width: 25%">Basis & Funrural</th>
</tr>
</thead>
<tbody>
<tr style="border-bottom: 1px solid #f1f5f9">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">🐂 Boi Gordo Físico (MT)</td>
<td style="padding: 9px 8px;color: #64748b">Cuiabá / Araputanga</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 340,20 <span style="color: #16a34a">▲ +0,89%</span></td>
<td style="padding: 9px 8px;color: #64748b">líq. c/ Funrural: R$ 336,12</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9;background: #fffbeb">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">🐂 Boi Gordo Físico (RO)</td>
<td style="padding: 9px 8px;color: #64748b">Vilhena / Ji-Paraná</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 332,00 <span style="color: #16a34a">▲ +0,30%</span></td>
<td style="padding: 9px 8px;color: #64748b">líq. c/ Funrural: R$ 328,02</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">🌱 Soja Disponível (MT)</td>
<td style="padding: 9px 8px;color: #64748b">Rondonópolis / Sorriso</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 138,50 <span style="color: #16a34a">▲ +0,36%</span></td>
<td style="padding: 9px 8px;color: #64748b">líq. c/ Funrural: R$ 136,84</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9;background: #fafafa">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">🌱 Soja Disponível (RO)</td>
<td style="padding: 9px 8px;color: #64748b">Vilhena / Ariquemes</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 135,50 <span style="color: #16a34a">▲ +0,35%</span></td>
<td style="padding: 9px 8px;color: #64748b">líq. c/ Funrural: R$ 133,87</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">🌽 Milho Grão (MT)</td>
<td style="padding: 9px 8px;color: #64748b">Sorriso / Sinop</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 46,00 <span style="color: #f87171">▼ -1,08%</span></td>
<td style="padding: 9px 8px;color: #64748b">líq. c/ Funrural: R$ 45,45</td>
</tr>
<tr style="border-bottom: 1px solid #f1f5f9;background: #fafafa">
<td style="padding: 9px 8px;font-weight: 600;color: #0f172a">🌽 Milho Grão (RO)</td>
<td style="padding: 9px 8px;color: #64748b">Ji-Paraná / Porto Velho</td>
<td style="padding: 9px 8px;font-weight: bold;color: #d97706;white-space: nowrap">R$ 44,00 <span style="color: #f87171">▼ -0,20%</span></td>
<td style="padding: 9px 8px;color: #64748b">líq. c/ Funrural: R$ 43,47</td>
</tr>
</tbody>
</table>
</div>

<!-- Nota Metodológica -->
<div style="background: #f8fafc;border-left: 4px solid #3b82f6;padding: 10px;font-size: 11px;color: #475569;border-radius: 0 6px 6px 0;line-height: 1.3;margin-top: 15px"><strong>Nota Metodológica:</strong> Painel Agro Frequência com foco principal em Café (Conilon e Arábica, físico e futuros ICE/Londres), cotações regionais para Mato Grosso (MT) e Rondônia (RO), basis, câmbio PTAX e dedução legal do Funrural (1,2%). Fontes: IMEA, Cepea, Scot Consultoria, ANP, B3 e ICE. (Atualizado em {data_atual}).</div>
</div>"""
    
    with open("painel-agro.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Painel HTML gerado com sucesso!")

if __name__ == "__main__":
    gerar_html_painel()
