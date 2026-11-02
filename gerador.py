import os
import sys
import shutil

CONFIG = {
    "site_url": "https://vittreseguros.com.br",
    "whatsapp": "5511978305192",
    "whatsapp_display": "(11) 97830-5192",
    "instagram": "vittreseguros",
    "formspree_endpoint": "https://formspree.io/f/mjyyakez",
    "cnpj": "",        
    "susep": "",       
    "ga4_id": ""       
}

cidades_sp = [
    {"slug": "franco-da-rocha", "nome": "Franco da Rocha", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Região Metropolitana de São Paulo", "hospitais": "Rede hospitalar credenciada, pronto-socorros, laboratórios de referência e centros de diagnóstico integrados na zona norte metropolitana.", "operadoras": ["Amil", "Hapvida GNDI", "Plena Saúde", "Unimed"], "principal_destaque": "Amplo suporte ambulatorial e hospitalar integrado na Grande São Paulo com fácil acesso a unidades de alta complexidade.", "cidades_vizinhas": ["francisco-morato", "mairipora", "cajamar", "caieiras"], "verificado": True, "publicar": True},
    {"slug": "francisco-morato", "nome": "Francisco Morato", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Região Metropolitana de São Paulo", "hospitais": "Unidades de pronto atendimento, postos de coleta laboratorial e rede credenciada de saúde local e regional.", "operadoras": ["Amil", "Hapvida GNDI", "Plena Saúde", "Unimed"], "principal_destaque": "Alternativas de assistência regional com foco em agilidade no atendimento de urgência e consultas eletivas.", "cidades_vizinhas": ["franco-da-rocha", "mairipora"], "verificado": True, "publicar": True},
    {"slug": "caieiras", "nome": "Caieiras", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Região Metropolitana de São Paulo", "hospitais": "Rede credenciada local e suporte integrado com Franco da Rocha, Francisco Morato e São Paulo.", "operadoras": ["Amil", "Hapvida GNDI", "Unimed", "Bradesco Saúde"], "principal_destaque": "Proximidade estratégica com a Grande São Paulo e excelente cobertura regional para famílias e empresas.", "cidades_vizinhas": ["franco-da-rocha", "sao-paulo"], "verificado": True, "publicar": True},
    {"slug": "mairipora", "nome": "Mairiporã", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Serra da Cantareira", "hospitais": "Hospital Maternidade local e suporte integrado em Franco da Rocha, Guarulhos e São Paulo.", "operadoras": ["Amil", "Bradesco Saúde", "Unimed", "Hapvida GNDI"], "principal_destaque": "Atendimento focado em qualidade de vida, bem-estar e proximidade estratégica com a capital.", "cidades_vizinhas": ["franco-da-rocha", "atibaia"], "verificado": True, "publicar": True},
    {"slug": "jundiai", "nome": "Jundiaí", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Aglomerado Urbano de Jundiaí", "hospitais": "Centros médicos especializados, hospitais gerais de grande porte e rede credenciada de excelência na região.", "operadoras": ["Unimed Jundiaí", "Amil", "Bradesco Saúde", "SulAmérica", "Hapvida GNDI"], "principal_destaque": "Polo regional consolidado com suporte médico de alta complexidade e hospitais premiados.", "cidades_vizinhas": ["cajamar", "varzea-paulista", "campo-limpo-paulista"], "verificado": True, "publicar": True},
    {"slug": "cajamar", "nome": "Cajamar", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Região Metropolitana", "hospitais": "Hospital Municipal de Cajamar e rede credenciada expandida em Jundiaí e Grande São Paulo.", "operadoras": ["Amil", "Hapvida GNDI", "Bradesco Saúde", "Unimed"], "principal_destaque": "Forte polo logístico e industrial com opções corporativas e PME altamente competitivas.", "cidades_vizinhas": ["jundiai", "santana-de-parnaiba", "barueri", "caieiras"], "verificado": True, "publicar": True},
    {"slug": "varzea-paulista", "nome": "Várzea Paulista", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Aglomerado Urbano de Jundiaí", "hospitais": "Unidades de saúde locais e rede hospitalar integrada com o polo de Jundiaí.", "operadoras": ["Unimed", "Amil", "Hapvida GNDI", "Bradesco Saúde"], "principal_destaque": "Acesso ágil aos melhores hospitais e laboratórios do aglomerado urbano de Jundiaí.", "cidades_vizinhas": ["jundiai", "campo-limpo-paulista"], "verificado": True, "publicar": True},
    {"slug": "campo-limpo-paulista", "nome": "Campo Limpo Paulista", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Aglomerado Urbano de Jundiaí", "hospitais": "Hospital de Clínicas local e rede referenciada de Jundiaí e região.", "operadoras": ["Unimed", "Amil", "Hapvida GNDI"], "principal_destaque": "Planos sob medida para moradores que buscam atendimento médico estruturado e preventivo.", "cidades_vizinhas": ["jundiai", "varzea-paulista", "jarinu"], "verificado": True, "publicar": True},
    {"slug": "santana-de-parnaiba", "nome": "Santana de Parnaíba", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Região Metropolitana Oeste", "hospitais": "Hospital Santa Ana e proximidade imediata com a rede de excelência de Alphaville e Barueri.", "operadoras": ["Amil", "Bradesco Saúde", "SulAmérica", "Omint", "Unimed"], "principal_destaque": "Cobertura executiva com acesso aos centros de referência e hospitais de ponta de Alphaville.", "cidades_vizinhas": ["cajamar", "barueri", "osasco"], "verificado": True, "publicar": True},
    {"slug": "barueri", "nome": "Barueri", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Região Metropolitana Oeste", "hospitais": "Hospital Municipal de Barueri Dr. Francisco Moran e rede de alto padrão em Alphaville.", "operadoras": ["Amil", "Bradesco Saúde", "SulAmérica", "Porto Seguro", "Unimed"], "principal_destaque": "Infraestrutura hospitalar de ponta ideal para planos corporativos, familiares e seniores.", "cidades_vizinhas": ["santana-de-parnaiba", "osasco", "cajamar"], "verificado": True, "publicar": True},
    {"slug": "osasco", "nome": "Osasco", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Região Metropolitana Oeste", "hospitais": "Hospital Antonio Giglio, Rede Amil Fácil e hospitais credenciados de referência na Zona Oeste.", "operadoras": ["Amil", "Bradesco Saúde", "SulAmérica", "Hapvida GNDI", "Porto Seguro"], "principal_destaque": "Alta densidade de laboratórios, clínicas especializadas e centros de alta complexidade integrados.", "cidades_vizinhas": ["barueri", "sao-paulo"], "verificado": True, "publicar": True},
    {"slug": "atibaia", "nome": "Atibaia", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Circuito das Frutas", "hospitais": "Hospital Albert Sabin e ampla rede credenciada local e regional.", "operadoras": ["Amil", "Unimed Atibaia", "Bradesco Saúde", "Hapvida GNDI"], "principal_destaque": "Opções de planos regionais e nacionais com excelente cobertura no interior paulista.", "cidades_vizinhas": ["mairipora", "jarinu"], "verificado": True, "publicar": True},
    {"slug": "itupeva", "nome": "Itupeva", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Aglomerado Urbano de Jundiaí", "hospitais": "Pronto Socorro Municipal e rede integrada de Jundiaí e Campinas.", "operadoras": ["Unimed", "Amil", "Bradesco Saúde", "Hapvida GNDI"], "principal_destaque": "Proximidade com polos industriais e facilidade de contratação familiar e PME.", "cidades_vizinhas": ["jundiai"], "verificado": True, "publicar": True},
    {"slug": "jarinu", "nome": "Jarinu", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Circuito das Frutas", "hospitais": "Unidade Básica de Saúde e atendimento médico integrado com Jundiaí e Atibaia.", "operadoras": ["Unimed", "Amil", "Hapvida GNDI"], "principal_destaque": "Tranquilidade no interior com suporte médico estruturado nas cidades vizinhas.", "cidades_vizinhas": ["jundiai", "campo-limpo-paulista", "atibaia"], "verificado": True, "publicar": True},
    {"slug": "sao-paulo", "nome": "São Paulo", "uf": "SP", "estado_slug": "sao-paulo", "regiao": "Capital Paulista", "hospitais": "A Beneficência Portuguesa, HCor, Hospital São Luiz, Oswaldo Cruz e rede hospitalar de excelência.", "operadoras": ["Amil", "Bradesco Saúde", "SulAmérica", "Omint", "Porto Seguro", "Hapvida GNDI"], "principal_destaque": "O principal polo de medicina avançada, cirurgias complexas e hospitais de referência do país.", "cidades_vizinhas": ["osasco", "barueri", "caieiras"], "verificado": True, "publicar": True}
]

cidades_ba = [
    {"slug": "barreiras", "nome": "Barreiras", "uf": "BA", "estado_slug": "bahia", "regiao": "Oeste Baiano", "hospitais": "Hospital do Oeste, Hospital Eurico Dutra, clínicas especializadas e centros de imagem de referência local.", "operadoras": ["Amil", "SulAmérica", "Bradesco Saúde", "Hapvida NotreDame"], "principal_destaque": "Principal polo médico, educacional e comercial do Oeste da Bahia, oferecendo cobertura robusta.", "cidades_vizinhas": ["luis-eduardo-magalhaes", "sao-desiderio"], "verificado": True, "publicar": True},
    {"slug": "luis-eduardo-magalhaes", "nome": "Luís Eduardo Magalhães", "uf": "BA", "estado_slug": "bahia", "regiao": "Oeste Baiano", "hospitais": "UPA 24h, Hospital Municipal e clínicas avançadas de diagnóstico por imagem.", "operadoras": ["Amil", "SulAmérica", "Bradesco Saúde", "Hapvida"], "principal_destaque": "Crescimento acelerado do agronegócio com alta demanda por planos familiares e PME.", "cidades_vizinhas": ["barreiras"], "verificado": True, "publicar": True},
    {"slug": "salvador", "nome": "Salvador", "uf": "BA", "estado_slug": "bahia", "regiao": "Região Metropolitana de Salvador", "hospitais": "Hospital Aliança, Hospital Português, Hospital da Bahia, Rede D'Or e hospitais especializados.", "operadoras": ["Amil", "Bradesco Saúde", "SulAmérica", "Hapvida GNDI", "Porto Seguro"], "principal_destaque": "Referência absoluta em saúde na Bahia com hospitais de excelência e corpo clínico renomado.", "cidades_vizinhas": ["lauro-de-freitas", "simoes-filho"], "verificado": True, "publicar": True},
    {"slug": "lauro-de-freitas", "nome": "Lauro de Freitas", "uf": "BA", "estado_slug": "bahia", "regiao": "Região Metropolitana de Salvador", "hospitais": "Hospital Menandro de Faria e rede credenciada expandida de Salvador.", "operadoras": ["Amil", "Bradesco Saúde", "SulAmérica", "Hapvida GNDI"], "principal_destaque": "Proximidade com os melhores hospitais da capital e forte expansão residencial e comercial.", "cidades_vizinhas": ["salvador"], "verificado": True, "publicar": True},
    {"slug": "camacari", "nome": "Camaçari", "uf": "BA", "estado_slug": "bahia", "regiao": "Região Metropolitana de Salvador", "hospitais": "Hospital Geral de Camaçari e clínicas integradas ao Polo Petroquímico.", "operadoras": ["Amil", "Bradesco Saúde", "SulAmérica", "Hapvida GNDI"], "principal_destaque": "Soluções corporativas robustas voltadas para colaboradores do Polo Industrial.", "cidades_vizinhas": ["salvador"], "verificado": True, "publicar": True},
    {"slug": "simoes-filho", "nome": "Simões Filho", "uf": "BA", "estado_slug": "bahia", "regiao": "Região Metropolitana de Salvador", "hospitais": "Hospital Municipal e suporte médico da RMS.", "operadoras": ["Amil", "Hapvida GNDI", "Bradesco Saúde"], "principal_destaque": "Logística e indústria com facilidade de contratação de convênios médicos empresariais.", "cidades_vizinhas": ["salvador"], "verificado": True, "publicar": True},
    {"slug": "candeias", "nome": "Candeias", "uf": "BA", "estado_slug": "bahia", "regiao": "Recôncavo Baiano", "hospitais": "Hospital Ouro Negro e rede credenciada metropolitana.", "operadoras": ["Amil", "Hapvida GNDI", "SulAmérica"], "principal_destaque": "Atendimento regional com foco em planos familiares e empresariais seguros.", "cidades_vizinhas": ["salvador"], "verificado": True, "publicar": True},
    {"slug": "dias-d-avila", "nome": "Dias d'Ávila", "uf": "BA", "estado_slug": "bahia", "regiao": "Região Metropolitana de Salvador", "hospitais": "Hospital Municipal e rede integrada de Camaçari e Salvador.", "operadoras": ["Amil", "Hapvida GNDI", "Bradesco Saúde"], "principal_destaque": "Assistência médica acessível e de qualidade para moradores e empresas locais.", "cidades_vizinhas": ["camacari"], "verificado": True, "publicar": True},
    {"slug": "feira-de-santana", "nome": "Feira de Santana", "uf": "BA", "estado_slug": "bahia", "regiao": "Portal do Sertão", "hospitais": "Hospital da Mulher, Hospital Emec, COTF e rede Unimed Feira.", "operadoras": ["Unimed Feira", "Amil", "Bradesco Saúde", "SulAmérica", "Hapvida GNDI"], "principal_destaque": "O maior entroncamento rodoviário do Nordeste com excelente estrutura hospitalar própria.", "cidades_vizinhas": [], "verificado": True, "publicar": True},
    {"slug": "santo-amaro", "nome": "Santo Amaro", "uf": "BA", "estado_slug": "bahia", "regiao": "Recôncavo Baiano", "hospitais": "Santa Casa de Misericórdia e rede de suporte em Salvador.", "operadoras": ["Amil", "Hapvida GNDI", "SulAmérica"], "principal_destaque": "Tradição histórica unida a planos de saúde com cobertura regional garantida.", "cidades_vizinhas": [], "verificado": True, "publicar": True},
    {"slug": "mata-de-sao-joao", "nome": "Mata de São João", "uf": "BA", "estado_slug": "bahia", "regiao": "Litoral Norte Baiano", "hospitais": "Unidades de saúde locais e proximidade com a rede de Praia do Forte e Salvador.", "operadoras": ["Amil", "Bradesco Saúde", "SulAmérica"], "principal_destaque": "Cobertura voltada para moradores, comércios e condomínios do litoral norte.", "cidades_vizinhas": ["lauro-de-freitas"], "verificado": True, "publicar": True},
    {"slug": "saubara", "nome": "Saubara", "uf": "BA", "estado_slug": "bahia", "regiao": "Recôncavo Baiano", "hospitais": "Atendimento local e suporte avançado em Feira de Santana e Salvador.", "operadoras": ["Amil", "Hapvida GNDI"], "principal_destaque": "Planos com suporte em urgência para moradores da região do recôncavo.", "cidades_vizinhas": [], "verificado": True, "publicar": True},
    {"slug": "sao-desiderio", "nome": "São Desidério", "uf": "BA", "estado_slug": "bahia", "regiao": "Oeste Baiano", "hospitais": "Suporte hospitalar integrado com o polo de Barreiras.", "operadoras": ["Amil", "SulAmérica", "Hapvida GNDI"], "principal_destaque": "Foco no setor agrícola, fazendas e produtores rurais com facilidade de adesão.", "cidades_vizinhas": ["barreiras"], "verificado": True, "publicar": True},
    {"slug": "riachao-das-neves", "nome": "Riachão das Neves", "uf": "BA", "estado_slug": "bahia", "regiao": "Oeste Baiano", "hospitais": "Rede de atendimento integrada com Barreiras.", "operadoras": ["Amil", "Hapvida GNDI"], "principal_destaque": "Cobertura essencial com suporte rápido no polo médico de Barreiras.", "cidades_vizinhas": ["barreiras"], "verificado": True, "publicar": True},
    {"slug": "formosa-do-rio-preto", "nome": "Formosa do Rio Preto", "uf": "BA", "estado_slug": "bahia", "regiao": "Extremo Oeste Baiano", "hospitais": "Unidade municipal e rede credenciada regional.", "operadoras": ["Amil", "SulAmérica", "Hapvida GNDI"], "principal_destaque": "Extremo norte do agronegócio baiano com opções de atendimento flexíveis.", "cidades_vizinhas": [], "verificado": True, "publicar": True}
]

cidades_outros = [
    {"slug": "sorriso", "nome": "Sorriso", "uf": "MT", "estado_slug": "mato-grosso", "regiao": "Norte de Mato Grosso", "hospitais": "Hospital Regional de Sorriso, Hospital 13 de Maio e clínicas avançadas.", "operadoras": ["Unimed Norte Mato Grosso", "Amil", "Bradesco Saúde", "Hapvida"], "principal_destaque": "Capital nacional do agronegócio com infraestrutura hospitalar moderna.", "cidades_vizinhas": [], "verificado": True, "publicar": True},
    {"slug": "lucas-do-rio-verde", "nome": "Lucas do Rio Verde", "uf": "MT", "estado_slug": "mato-grosso", "regiao": "Centro-Norte Mato-grossense", "hospitais": "Hospital São Lucas e rede credenciada local.", "operadoras": ["Unimed", "Amil", "Bradesco Saúde"], "principal_destaque": "Economia dinâmica com alta procura por planos empresariais e familiares.", "cidades_vizinhas": ["sorriso"], "verificado": True, "publicar": True},
    {"slug": "sinop", "nome": "Sinop", "uf": "MT", "estado_slug": "mato-grosso", "regiao": "Polo Nortista de Mato Grosso", "hospitais": "Hospital Regional de Sinop e Hospital Santo Antônio.", "operadoras": ["Unimed", "Amil", "Bradesco Saúde", "SulAmérica"], "principal_destaque": "Polo educacional e médico do norte mato-grossense.", "cidades_vizinhas": ["sorriso"], "verificado": True, "publicar": True},
    {"slug": "rio-verde", "nome": "Rio Verde", "uf": "GO", "estado_slug": "goias", "regiao": "Sudoeste Goiano", "hospitais": "Hospital Universitário, Hospital Santa Doroteia e Unimed Sudoeste.", "operadoras": ["Unimed", "Amil", "Bradesco Saúde", "SulAmérica"], "principal_destaque": "Referência industrial e agrícola em Goiás com excelente oferta de convênios.", "cidades_vizinhas": [], "verificado": True, "publicar": True},
    {"slug": "jatai", "nome": "Jataí", "uf": "GO", "estado_slug": "goias", "regiao": "Sudoeste Goiano", "hospitais": "Hospital das Clínicas e rede credenciada local.", "operadoras": ["Unimed", "Amil", "Bradesco Saúde"], "principal_destaque": "Assistência médica de qualidade estruturada para famílias e empresas locais.", "cidades_vizinhas": ["rio-verde"], "verificado": True, "publicar": True},
    {"slug": "gurupi", "nome": "Gurupi", "uf": "TO", "estado_slug": "tocantins", "regiao": "Sul do Tocantins", "hospitais": "Hospital Regional de Gurupi e clínicas privadas.", "operadoras": ["Unimed", "Amil", "Hapvida GNDI"], "principal_destaque": "Polo do sul do Tocantins com atendimento médico regionalizado.", "cidades_vizinhas": [], "verificado": True, "publicar": True},
    {"slug": "araguaina", "nome": "Araguaína", "uf": "TO", "estado_slug": "tocantins", "regiao": "Norte do Tocantins", "hospitais": "Hospital Regional de Araguaína e hospitais particulares.", "operadoras": ["Unimed", "Amil", "Bradesco Saúde", "Hapvida"], "principal_destaque": "Principal polo econômico e de saúde do norte tocantinense.", "cidades_vizinhas": [], "verificado": True, "publicar": True},
    {"slug": "balsas", "nome": "Balsas", "uf": "MA", "estado_slug": "maranhao", "regiao": "Sul do Maranhão", "hospitais": "Hospital Regional de Balsas e clínicas integradas.", "operadoras": ["Amil", "Hapvida GNDI", "SulAmérica"], "principal_destaque": "Centro produtivo do sul maranhense com forte demanda por planos de saúde.", "cidades_vizinhas": [], "verificado": True, "publicar": True},
    {"slug": "petrolina", "nome": "Petrolina", "uf": "PE", "estado_slug": "pernambuco", "regiao": "Vale do São Francisco", "hospitais": "Hospital Dom Malan, Hospital Memorial Petrolina e Unimed Vale.", "operadoras": ["Unimed Vale do São Francisco", "Amil", "Bradesco Saúde", "SulAmérica"], "principal_destaque": "Polo médico do Vale do São Francisco com infraestrutura qualificada.", "cidades_vizinhas": [], "verificado": True, "publicar": True},
    {"slug": "juazeiro", "nome": "Juazeiro", "uf": "BA", "estado_slug": "bahia", "regiao": "Norte Baiano", "hospitais": "Hospital Regional do Norte Baiano e rede integrada com Petrolina.", "operadoras": ["Amil", "Unimed", "Bradesco Saúde", "Hapvida GNDI"], "principal_destaque": "Integração total com o polo médico do Vale do São Francisco.", "cidades_vizinhas": ["petrolina"], "verificado": True, "publicar": True}
]

cidades_db = cidades_sp + cidades_ba + cidades_outros

def validar_dados(modo_preview=False):
    print("=== EXECUTANDO QUALITY GATE E VALIDAÇÕES ===")
    cidades_validas = []
    for c in cidades_db:
        if modo_preview:
            c["_preview"] = True
            cidades_validas.append(c)
            continue
        if not c.get("publicar", False):
            continue
        if not c.get("verificado", False):
            raise ValueError(f"ERRO QUALITY GATE: A cidade '{c['nome']}' está marcada para publicar (True), mas seus dados não foram confirmados (verificado=False).")
        cidades_validas.append(c)

    print(f"✅ Validação concluída. {len(cidades_validas)} cidade(s) aprovada(s) para publicação.")
    return cidades_validas

def gerar_carrossel(operadoras):
    itens = ""
    for op in operadoras:
        itens += f'''
        <div class="flex items-center gap-2 bg-slate-50 px-5 py-2.5 rounded-xl border border-slate-100 shadow-sm flex-shrink-0">
            <span class="font-black text-slate-800 tracking-wider text-sm">{op.upper()}</span>
        </div>'''
    return itens

def gerar_faq(nome, operadoras):
    ops = ", ".join(operadoras)
    return f'''
    <div class="space-y-4">
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
            <h3 class="font-bold text-slate-900 mb-2">Como escolher o plano de saúde ideal em {nome}?</h3>
            <p class="text-slate-600 text-sm leading-relaxed">A escolha depende do seu perfil (individual, familiar, MEI ou adesão), orçamento e rede de preferência. Nossa equipe monta um comparativo gratuito enviado diretamente para você.</p>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
            <h3 class="font-bold text-slate-900 mb-2">Quais operadoras atendem em {nome}?</h3>
            <p class="text-slate-600 text-sm leading-relaxed">As principais operadoras mapeadas para esta praça incluem: {ops}.</p>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
            <h3 class="font-bold text-slate-900 mb-2">Existe fidelidade em planos Pessoa Física?</h3>
            <p class="text-slate-600 text-sm leading-relaxed">Não há fidelidade abusiva ou multa rescisória em planos individuais/familiares regulamentados. Os prazos existentes referem-se estritamente às carências assistenciais reguladas.</p>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
            <h3 class="font-bold text-slate-900 mb-2">Quais documentos são exigidos para contratação MEI / PME?</h3>
            <p class="text-slate-600 text-sm leading-relaxed">Para planos empresariais e MEI, é necessário apresentar o cartão CNPJ ativo (com pelo menos 6 meses de abertura), documento de identidade dos sócios/beneficiários e comprovante de endereço.</p>
        </div>
    </div>'''

def gerar_links_vizinhas_e_hub(cidade, cidades_validas, estado_slug, estado_nome):
    vizinhos = [c for c in cidades_validas if c["slug"] in cidade.get("cidades_vizinhas", []) and c.get("publicar", False)]
    html_vizinhos = ""
    if vizinhos:
        html_vizinhos += '<div class="mt-6 pt-4 border-t border-slate-200"><h4 class="text-xs font-bold text-slate-500 uppercase mb-2">Cidades Vizinhas Atendidas:</h4><div class="flex flex-wrap gap-2">'
        for v in vizinhos:
            html_vizinhos += f'<a href="/{v["slug"]}" class="bg-slate-100 hover:bg-blue-50 text-slate-700 px-3 py-1 rounded text-xs font-semibold">{v["nome"]} ({v["uf"]})</a>'
        html_vizinhos += '</div></div>'
    html_hub = f'<div class="mt-4"><a href="/{estado_slug}" class="text-blue-600 font-bold text-sm hover:underline">&larr; Ver todas as cidades atendidas no estado de {estado_nome}</a></div>'
    return html_vizinhos + html_hub

def gerar_html_cidade(cidade, cidades_validas):
    nome = cidade["nome"]
    slug = cidade["slug"]
    regiao = cidade["regiao"]
    uf = cidade["uf"]
    estado_slug = cidade["estado_slug"]
    hospitais = cidade["hospitais"]
    operadoras_lista = ", ".join(cidade["operadoras"])
    destaque = cidade["principal_destaque"]
    is_preview = cidade.get("_preview", False)
    
    canonical_url = f"{CONFIG['site_url']}/{slug}"
    carrossel_html = gerar_carrossel(cidade["operadoras"])
    faq_html = gerar_faq(nome, cidade["operadoras"])
    
    estado_nomes = {"bahia": "Bahia", "sao-paulo": "São Paulo", "mato-grosso": "Mato Grosso", "goias": "Goiás", "tocantins": "Tocantins", "maranhao": "Maranhão", "pernambuco": "Pernambuco"}
    estado_nome = estado_nomes.get(estado_slug, "Região")
    
    links_extras = gerar_links_vizinhas_e_hub(cidade, cidades_validas, estado_slug, estado_nome)
    
    bloco_institucional = ""
    if CONFIG["cnpj"] or CONFIG["susep"]:
        bloco_institucional = f'''
        <div class="mt-4 pt-4 border-t border-slate-800 text-xs text-slate-400">
            {f"<strong>CNPJ:</strong> {CONFIG['cnpj']}<br>" if CONFIG["cnpj"] else ""}
            {f"<strong>SUSEP:</strong> {CONFIG['susep']}" if CONFIG["susep"] else ""}
        </div>'''

    ga4_head = ""
    if CONFIG["ga4_id"]:
        ga4_head = f'''
        <script async src="https://www.googletagmanager.com/gtag/js?id={CONFIG["ga4_id"]}"></script>
        <script>
          window.dataLayer = window.dataLayer || [];
          function gtag(){{dataLayer.push(arguments);}}
          gtag('js', new Date());
          gtag('config', '{CONFIG["ga4_id"]}');
        </script>'''

    robots_content = "noindex, follow" if is_preview else "index, follow"

    return f'''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    {ga4_head}
    <title>Plano de Saúde em {nome} ({uf}) | Tabelas de Preços e Cotação - Vittre</title>
    <meta name="description" content="Simule plano de saúde em {nome} ({uf}). Tabelas completas para pessoa física, familiar, PME, MEI e adesão. Confira redes credenciadas, carências e regras da ANS.">
    <meta name="robots" content="{robots_content}">
    <link rel="canonical" href="{canonical_url}">
    
    <meta property="og:title" content="Plano de Saúde em {nome} ({uf}) | Tabelas e Redes Credenciadas - Vittre Seguros">
    <meta property="og:description" content="Compare tabelas, preços e redes de hospitais e laboratórios para planos de saúde em {nome} e região.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">

    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="stylesheet" href="/styles.css">

    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@graph": [
        {{
          "@type": "InsuranceAgency",
          "@id": "{CONFIG['site_url']}/#organization",
          "name": "Vittre Seguros",
          "url": "{CONFIG['site_url']}",
          "telephone": "+{CONFIG['whatsapp']}"
        }},
        {{
          "@type": "Service",
          "name": "Planos de Saúde em {nome}",
          "provider": {{ "@id": "{CONFIG['site_url']}/#organization" }},
          "areaServed": {{ "@type": "City", "name": "{nome}", "addressRegion": "{uf}" }}
        }}
      ]
    }}
    </script>
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased">

    <header class="bg-white backdrop-blur-md border-b border-slate-200 sticky top-0 z-50 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex justify-between items-center">
            <a href="/" class="text-2xl font-black text-blue-950 tracking-tight">VITTRE<span class="text-blue-600">SEGUROS</span></a>
            <div class="flex items-center gap-4">
                <a href="https://wa.me/{CONFIG['whatsapp']}?text=Olá,%20quero%20simular%20plano%20em%20{nome}" target="_blank" rel="noopener" class="hidden md:block text-sm font-bold text-slate-700 hover:text-green-600 transition">
                    {CONFIG['whatsapp_display']}
                </a>
                <a href="#cotacao" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-5 rounded-lg text-sm transition">
                    Cotar Online
                </a>
            </div>
        </div>
    </header>

    <section class="bg-gradient-to-br from-blue-950 via-blue-900 to-indigo-950 text-white py-16 md:py-24">
        <div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12 items-center">
            <div>
                <span class="inline-block bg-blue-800 text-blue-200 text-xs font-semibold px-3.5 py-1.5 rounded-full mb-4 tracking-wide uppercase border border-blue-700">Atendimento em {regiao}</span>
                <h1 class="text-3xl md:text-5xl font-extrabold leading-tight mb-6 tracking-tight text-white">
                    Plano de Saúde em {nome} ({uf})
                </h1>
                <p class="text-blue-100 text-lg mb-8 leading-relaxed">
                    Compare tabelas, preços atualizados e redes credenciadas para planos de saúde individuais, familiares, PME, MEI e adesão em {nome}.
                </p>
            </div>

            <div id="cotacao" class="bg-white text-slate-900 p-6 md:p-8 rounded-2xl shadow-2xl border border-slate-100">
                <h2 class="text-2xl font-bold text-slate-900 mb-1">Simular Preços em {nome}</h2>
                <p class="text-slate-600 text-sm mb-6">Preencha para receber o comparativo detalhado. Entraremos em contato em breve.</p>

                <form id="form-lead" onsubmit="enviarLead(event)" class="space-y-4">
                    <input type="hidden" name="_subject" value="Nova cotação - {nome} ({uf})">
                    <input type="text" name="_gotcha" class="hidden">
                    <input type="hidden" name="cidade" id="origem_cidade" value="{nome} ({uf})">
                    
                    <div>
                        <label for="lead-nome" class="block text-sm font-semibold text-slate-700 mb-1">Seu Nome</label>
                        <input type="text" id="lead-nome" name="nome" required placeholder="Digite seu nome" class="w-full">
                    </div>
                    <div>
                        <label for="lead-email" class="block text-sm font-semibold text-slate-700 mb-1">E-mail (Opcional)</label>
                        <input type="email" id="lead-email" name="email" placeholder="seu@email.com" class="w-full">
                    </div>
                    <div>
                        <label for="lead-whatsapp" class="block text-sm font-semibold text-slate-700 mb-1">WhatsApp (com DDD)</label>
                        <input type="tel" id="lead-whatsapp" name="whatsapp" required placeholder="(11) 90000-0000" class="w-full">
                    </div>
                    <div>
                        <label for="lead-tipo" class="block text-sm font-semibold text-slate-700 mb-1">Tipo de Plano</label>
                        <select id="lead-tipo" name="tipo_plano" class="w-full">
                            <option value="individual">Individual (Pessoa Física)</option>
                            <option value="familiar">Familiar</option>
                            <option value="pme">Empresarial / MEI / PME</option>
                            <option value="adesao">Por Adesão</option>
                            <option value="infantil">Infantil</option>
                            <option value="gestante">Gestante</option>
                        </select>
                    </div>
                    <button type="submit" id="btn-submit" class="w-full bg-green-600 hover:bg-green-700 text-white font-black text-lg py-4 rounded-xl shadow-lg hover:shadow-xl hover:-translate-y-0.5 transition-all duration-200 cursor-pointer">
                        Solicitar cotação
                    </button>
                </form>
                
                <div id="sucesso-msg" class="hidden text-center py-8">
                    <div class="text-green-600 font-bold text-lg mb-2">✅ Solicitação Enviada com Sucesso!</div>
                    <p class="text-sm text-slate-600">Entraremos em contato em breve.</p>
                </div>
                <div id="erro-msg" class="hidden text-center py-4 text-red-600 text-sm">
                    ❌ Erro ao enviar. Se preferir, fale conosco direto pelo <a href="https://wa.me/{CONFIG['whatsapp']}" class="underline font-bold">WhatsApp</a>.
                </div>
            </div>
        </div>
    </section>

    <section class="py-10 bg-white border-b border-slate-200 overflow-hidden">
        <div class="max-w-6xl mx-auto px-4 mb-6 text-center">
            <p class="text-xs font-bold uppercase tracking-widest text-slate-400">Operadoras com Atendimento em {nome}</p>
        </div>
        <div class="relative w-full overflow-hidden">
            <div class="animate-scroll flex gap-12 items-center">
                <div class="flex items-center gap-12 px-6">{carrossel_html}</div>
                <div class="flex items-center gap-12 px-6" aria-hidden="true">{carrossel_html}</div>
            </div>
        </div>
    </section>

    <section class="py-16 max-w-5xl mx-auto px-4">
        <div class="bg-white p-8 md:p-12 rounded-2xl shadow-sm border border-slate-200 space-y-6">
            <h2 class="text-2xl md:text-3xl font-extrabold text-slate-900 leading-tight">Guia Definitivo de Planos de Saúde em {nome} ({uf})</h2>
            
            <p class="text-slate-700 leading-relaxed">
                Procurar por tabelas de preços e opções de convênios médicos em <strong>{nome}</strong> exige análise detalhada da rede credenciada, abrangência geográfica, prazos de carência e regras de contratação reguladas pela ANS. Na <strong>Vittre Seguros</strong>, reunimos as melhores alternativas do mercado para atender moradores, famílias, profissionais autônomos e empresas de todos os portes localizadas no {regiao}.
            </p>

            <p class="text-slate-700 leading-relaxed">
                {destaque} Nosso compromisso é fornecer uma consultoria 100% transparente, ajudando você a entender quais hospitais, clínicas e laboratórios estão disponíveis no seu plano, além de orientar sobre os critérios de elegibilidade para planos individuais, coletivos por adesão e corporativos PME/MEI.
            </p>

            <div class="grid md:grid-cols-2 gap-6 bg-blue-50 p-6 rounded-xl border border-blue-100 my-6">
                <div>
                    <h3 class="font-bold text-blue-950 mb-2 text-base">Hospitais e Rede Credenciada</h3>
                    <p class="text-sm text-slate-700 leading-relaxed">{hospitais}</p>
                </div>
                <div>
                    <h3 class="font-bold text-blue-950 mb-2 text-base">Principais Operadoras Disponíveis</h3>
                    <p class="text-sm text-slate-700 leading-relaxed">{operadoras_lista}</p>
                </div>
            </div>

            <h3 class="text-xl font-bold text-slate-900 pt-2">Como Escolher o Convênio Médico Ideal em {nome}?</h3>
            <p class="text-slate-700 leading-relaxed">
                A escolha de um plano de saúde envolve ponderar três pilares fundamentais: <strong>rede de atendimento</strong> (se você prefere hospitais locais ou abrangência nacional), <strong>tipo de acomodação</strong> (enfermaria em quarto coletivo ou apartamento privativo) e <strong>modelo de coparticipação</strong> (onde o plano possui mensalidades menores e uma taxa moderada por consulta/exame realizado).
            </p>

            <h4 class="font-bold text-slate-900 text-lg pt-1">Critérios e Regras por Categoria:</h4>
            <ul class="list-disc pl-5 space-y-2 text-slate-700">
                <li><strong>Planos Individuais e Familiares:</strong> Contratos voltados para pessoas físicas com total estabilidade regulatória, reajustes anuais definidos pelo teto da ANS e sem cláusulas de fidelidade abusiva após o período inicial.</li>
                <li><strong>Planos Empresariais (PME e MEI):</strong> Excelente alternativa para reduzir custos. Disponíveis para empresas com CNPJ ativo (incluindo MEI com mais de 6 meses) a partir de 2 vidas, oferecendo tabelas de preços consideravelmente mais econômicas.</li>
                <li><strong>Planos por Adesão:</strong> Destinados a beneficiários vinculados a entidades de classe, sindicatos ou associações profissionais conforme a profissão ou ramo de atuação.</li>
            </ul>

            <p class="text-slate-700 leading-relaxed pt-2">
                Preencha o nosso formulário de cotação ou entre em contato diretamente pelo WhatsApp para receber a tabela detalhada com valores por faixa etária, redes de laboratórios e condições especiais vigentes em {nome}.
            </p>

            {links_extras}
        </div>
    </section>

    <section class="py-12 max-w-6xl mx-auto px-4">
        <div class="text-center mb-12">
            <h2 class="text-3xl font-extrabold text-slate-900 mb-3">O Que Você Precisa Saber Antes de Contratar</h2>
            <p class="text-slate-600 max-w-2xl mx-auto">Regras essenciais sobre documentação, portabilidade de carências e funcionamento da assistência.</p>
        </div>
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-white p-8 rounded-xl border border-slate-200 shadow-sm space-y-3">
                <div class="bg-blue-50 w-12 h-12 rounded-lg flex items-center justify-center text-blue-600 mb-4 font-bold text-xl">01</div>
                <h3 class="font-bold text-xl text-blue-950">Documentação Necessária</h3>
                <p class="text-slate-600 text-sm leading-relaxed">
                    Para Pessoa Física: RG, CPF e Comprovante de Residência. Para PME/MEI: Cartão CNPJ ativo, Contrato Social / Requerimento de Empresário, documentos dos sócios e funcionários inclusos.
                </p>
            </div>
            <div class="bg-white p-8 rounded-xl border border-slate-200 shadow-sm space-y-3">
                <div class="bg-blue-50 w-12 h-12 rounded-lg flex items-center justify-center text-blue-600 mb-4 font-bold text-xl">02</div>
                <h3 class="font-bold text-xl text-blue-950">Portabilidade de Carências</h3>
                <p class="text-slate-600 text-sm leading-relaxed">
                    Caso você já possua um plano de saúde anterior e cumpra os requisitos da ANS, é possível trocar de operadora aproveitando todo ou parte do tempo de carência já cumprido, sem precisar esperar novos prazos.
                </p>
            </div>
            <div class="bg-white p-8 rounded-xl border border-slate-200 shadow-sm space-y-3">
                <div class="bg-blue-50 w-12 h-12 rounded-lg flex items-center justify-center text-blue-600 mb-4 font-bold text-xl">03</div>
                <h3 class="font-bold text-xl text-blue-950">Abrangência e Reembolso</h3>
                <p class="text-slate-600 text-sm leading-relaxed">
                    Planos podem ter cobertura municipal, regional, estadual ou nacional. Algumas linhas executivas também contam com sistema de livre escolha e reembolso para médicos fora da rede credenciada.
                </p>
            </div>
        </div>
    </section>

    <section class="bg-slate-100 py-16 border-y border-slate-200">
        <div class="max-w-4xl mx-auto px-4">
            <div class="text-center mb-10">
                <h2 class="text-3xl font-extrabold text-slate-900 mb-2">Prazos de Carência Regulados pela ANS</h2>
                <p class="text-slate-600 text-sm">Prazos máximos legais aplicados aos contratos de assistência médica suplementar.</p>
            </div>
            <div class="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden divide-y divide-slate-100">
                <div class="p-4 sm:p-6 flex justify-between items-center"><span class="font-semibold text-slate-800">Urgência e Emergência (Atendimento 24h)</span><span class="bg-green-100 text-green-800 font-bold px-3 py-1 rounded-full text-sm">24 horas</span></div>
                <div class="p-4 sm:p-6 flex justify-between items-center"><span class="font-semibold text-slate-800">Consultas Médicas e Exames Simples</span><span class="bg-blue-100 text-blue-800 font-bold px-3 py-1 rounded-full text-sm">30 dias</span></div>
                <div class="p-4 sm:p-6 flex justify-between items-center"><span class="font-semibold text-slate-800">Exames Complexos, Terapias e Cirurgias</span><span class="bg-blue-100 text-blue-800 font-bold px-3 py-1 rounded-full text-sm">180 dias</span></div>
                <div class="p-4 sm:p-6 flex justify-between items-center"><span class="font-semibold text-slate-800">Parto a Termo (Obstetrícia)</span><span class="bg-blue-100 text-blue-800 font-bold px-3 py-1 rounded-full text-sm">300 dias</span></div>
                <div class="p-4 sm:p-6 flex justify-between items-center"><span class="font-semibold text-slate-800">Doenças e Lesões Preexistentes (DLP)</span><span class="bg-amber-100 text-amber-800 font-bold px-3 py-1 rounded-full text-sm">720 dias</span></div>
            </div>
            <p class="text-xs text-slate-500 mt-4 text-center">*Prazos sujeitos à redução ou eliminação mediante portabilidade de carências, conforme regras da operadora escolhida.</p>
        </div>
    </section>

    <section class="py-16 max-w-4xl mx-auto px-4">
        <div class="text-center mb-10"><h2 class="text-3xl font-extrabold text-slate-900 mb-2">Dúvidas Frequentes Sobre Planos em {nome}</h2></div>
        {faq_html}
    </section>

    <footer class="bg-slate-950 text-slate-400 py-12 border-t border-slate-800 text-sm">
        <div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-8 items-center text-center md:text-left">
            <div>
                <a href="/" class="text-2xl font-black text-white tracking-tight">VITTRE<span class="text-blue-500">SEGUROS</span></a>
                <p class="text-xs text-slate-500 mt-2">Corretora especializada em planos de saúde regionais. WhatsApp: {CONFIG['whatsapp_display']}</p>
                <div class="mt-3 flex gap-4 text-xs justify-center md:justify-start">
                    <a href="/quem-somos.html" class="hover:text-white underline">Quem Somos</a>
                    <a href="/contato.html" class="hover:text-white underline">Contato</a>
                    <a href="/politica-de-privacidade.html" class="hover:text-white underline">Política de Privacidade</a>
                </div>
                {bloco_institucional}
            </div>
            <div class="text-md md:text-right text-xs text-slate-600">
                <p>&copy; 2026 Vittre Seguros (@{CONFIG['instagram']}). Todos os direitos reservados.</p>
            </div>
        </div>
    </footer>

    <script src="/form.js" data-ga4="{CONFIG['ga4_id']}" data-endpoint="{CONFIG['formspree_endpoint']}"></script>
</body>
</html>'''

def gerar_pagina_principal(cidades_validas):
    cards_cidades = ""
    for c in sorted(cidades_validas, key=lambda x: x["nome"]):
        cards_cidades += f'''
        <a href="/{c["slug"]}" class="group p-4 rounded-xl border border-slate-200 hover:border-blue-600 hover:bg-blue-50 transition duration-200 flex justify-between items-center shadow-sm">
            <span class="font-bold text-slate-700 group-hover:text-blue-900">{c["nome"]} <span class="text-slate-400 font-normal">({c["uf"]})</span></span>
            <span class="text-blue-600 opacity-0 group-hover:opacity-100 transition duration-200">&rarr;</span>
        </a>'''

    operadoras_cards = [
        {"nome": "Amil", "cobertura": "COBERTURA NACIONAL", "cor": "bg-indigo-600"},
        {"nome": "Bradesco Saúde", "cobertura": "COBERTURA NACIONAL", "cor": "bg-red-600"},
        {"nome": "SulAmérica", "cobertura": "COBERTURA NACIONAL", "cor": "bg-blue-600"},
        {"nome": "Hapvida GNDI", "cobertura": "COBERTURA NACIONAL", "cor": "bg-blue-800"},
        {"nome": "Porto Seguro", "cobertura": "COBERTURA NACIONAL", "cor": "bg-blue-900"},
        {"nome": "Omint", "cobertura": "COBERTURA NACIONAL", "cor": "bg-slate-800"},
        {"nome": "Unimed", "cobertura": "COBERTURA REGIONAL", "cor": "bg-green-600"},
        {"nome": "Plena Saúde", "cobertura": "COBERTURA REGIONAL SP", "cor": "bg-teal-600"},
        {"nome": "Alice Saúde", "cobertura": "COBERTURA NACIONAL", "cor": "bg-blue-500"},
        {"nome": "Samoc", "cobertura": "COBERTURA REGIONAL SP", "cor": "bg-orange-600"}
    ]

    html_operadoras = ""
    for op in operadoras_cards:
        html_operadoras += f'''
        <div class="bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm hover:shadow-md transition group">
            <div class="{op['cor']} h-24 flex items-center justify-center p-4">
                <span class="text-white font-black text-2xl tracking-wider">{op['nome']}</span>
            </div>
            <div class="p-4 text-center">
                <p class="text-xs font-bold text-slate-500 tracking-widest mb-2">{op['cobertura']}</p>
                <a href="#cotacao" class="text-sm font-bold text-blue-600 hover:text-blue-800 group-hover:underline">Ver Tabelas e Preços &rarr;</a>
            </div>
        </div>'''

    faq_home = '''
    <div class="space-y-4 max-w-3xl mx-auto">
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
            <h3 class="font-bold text-slate-900 mb-2">Qual o melhor plano de saúde do mercado?</h3>
            <p class="text-slate-600 text-sm leading-relaxed">Não existe um "melhor" universal. O plano ideal depende do seu perfil (individual, familiar, MEI), da sua região e do seu orçamento. A Vittre Seguros analisa a sua necessidade e encontra a melhor relação custo-benefício entre Amil, Bradesco, SulAmérica e outras.</p>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
            <h3 class="font-bold text-slate-900 mb-2">Posso contratar um plano PME mesmo sendo MEI?</h3>
            <p class="text-slate-600 text-sm leading-relaxed">Sim! O plano PME (ou Empresarial) é a melhor opção para MEIs e microempresas. Basta ter o CNPJ ativo e cumprir os requisitos mínimos da operadora (geralmente a partir de 2 vidas e CNPJ com mais de 6 meses).</p>
        </div>
        <div class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
            <h3 class="font-bold text-slate-900 mb-2">Como funciona a portabilidade de carências?</h3>
            <p class="text-slate-600 text-sm leading-relaxed">Se você já tem um plano de saúde e está em dia com as mensalidades, pode trocar para outra operadora aproveitando o tempo de carência que já cumpriu. A Vittre cuida de toda a papelada e regras da ANS para você.</p>
        </div>
    </div>'''

    return f'''<!DOCTYPE html>
<html lang="pt-BR" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vittre Seguros | Tabelas de Planos de Saúde e Cotações Online</title>
    <meta name="description" content="Compare tabelas de preços e redes credenciadas dos principais planos de saúde (Amil, Bradesco, SulAmérica, Hapvida). Cotação gratuita para Individual, Familiar, PME e MEI.">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{CONFIG['site_url']}/">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="stylesheet" href="/styles.css">
</head>
<body class="bg-slate-50 text-slate-800 font-sans antialiased">

    <header class="bg-white backdrop-blur-md border-b border-slate-200 sticky top-0 z-50 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex justify-between items-center">
            <a href="/" class="text-2xl font-black text-blue-950 tracking-tight">VITTRE<span class="text-blue-600">SEGUROS</span></a>
            <div class="flex items-center gap-4">
                <a href="https://wa.me/{CONFIG['whatsapp']}" target="_blank" rel="noopener" class="hidden md:block text-sm font-bold text-slate-700 hover:text-green-600 transition">
                    {CONFIG['whatsapp_display']}
                </a>
                <a href="#cotacao" class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-5 rounded-lg text-sm transition">
                    Cotar Online
                </a>
            </div>
        </div>
    </header>

    <section class="bg-gradient-to-br from-blue-950 via-blue-900 to-indigo-950 text-white py-16 md:py-24">
        <div class="max-w-6xl mx-auto px-4 grid md:grid-cols-2 gap-12 items-center">
            <div>
                <span class="inline-block bg-blue-800 text-blue-200 text-xs font-semibold px-3.5 py-1.5 rounded-full mb-4 tracking-wide uppercase border border-blue-700">Referência em Planos de Saúde</span>
                <h1 class="text-4xl md:text-5xl font-extrabold leading-tight mb-6 tracking-tight text-white">
                    Tabelas de Planos de Saúde e Cotações Online
                </h1>
                <p class="text-blue-100 text-lg mb-8 leading-relaxed">
                    Simule seu plano de saúde Individual, Familiar, Empresarial ou por Adesão gratuitamente. Encontre as melhores operadoras do mercado com preços atualizados.
                </p>
                <div class="flex gap-4 text-sm font-medium text-blue-200">
                    <span class="flex items-center gap-2">✓ Cotação Gratuita</span>
                    <span class="flex items-center gap-2">✓ Sem Compromisso</span>
                </div>
            </div>

            <div id="cotacao" class="bg-white text-slate-900 p-6 md:p-8 rounded-2xl shadow-2xl border border-slate-100">
                <h2 class="text-2xl font-bold text-slate-900 mb-1">Simule seu Plano</h2>
                <p class="text-slate-600 text-sm mb-6">Preencha para receber o comparativo detalhado. Entraremos em contato em breve.</p>

                <form id="form-lead" onsubmit="enviarLead(event)" class="space-y-4">
                    <input type="hidden" name="_subject" value="Nova cotação - Home">
                    <input type="text" name="_gotcha" class="hidden">
                    <input type="hidden" name="cidade" id="origem_cidade" value="Home">
                    
                    <div>
                        <label for="lead-nome" class="block text-sm font-semibold text-slate-700 mb-1">Seu Nome</label>
                        <input type="text" id="lead-nome" name="nome" required placeholder="Digite seu nome" class="w-full">
                    </div>
                    <div>
                        <label for="lead-email" class="block text-sm font-semibold text-slate-700 mb-1">E-mail (Opcional)</label>
                        <input type="email" id="lead-email" name="email" placeholder="seu@email.com" class="w-full">
                    </div>
                    <div>
                        <label for="lead-whatsapp" class="block text-sm font-semibold text-slate-700 mb-1">WhatsApp (com DDD)</label>
                        <input type="tel" id="lead-whatsapp" name="whatsapp" required placeholder="(11) 90000-0000" class="w-full">
                    </div>
                    <div>
                        <label for="lead-tipo" class="block text-sm font-semibold text-slate-700 mb-1">Tipo de Plano</label>
                        <select id="lead-tipo" name="tipo_plano" class="w-full">
                            <option value="individual">Individual (Pessoa Física)</option>
                            <option value="familiar">Familiar</option>
                            <option value="pme">Empresarial / MEI / PME</option>
                            <option value="adesao">Por Adesão</option>
                        </select>
                    </div>
                    <button type="submit" id="btn-submit" class="w-full bg-green-600 text-white font-black text-base py-3.5 rounded-lg shadow-md transition">
                        Solicitar cotação
                    </button>
                </form>
                
                <div id="sucesso-msg" class="hidden text-center py-8">
                    <div class="text-green-600 font-bold text-lg mb-2">✅ Solicitação Enviada com Sucesso!</div>
                    <p class="text-sm text-slate-600">Entraremos em contato em breve.</p>
                </div>
                <div id="erro-msg" class="hidden text-center py-4 text-red-600 text-sm">
                    ❌ Erro ao enviar. Se preferir, fale conosco direto pelo <a href="https://wa.me/{CONFIG['whatsapp']}" class="underline font-bold">WhatsApp</a>.
                </div>
            </div>
        </div>
    </section>

    <section class="py-10 bg-white border-b border-slate-200 overflow-hidden">
        <div class="max-w-6xl mx-auto px-4 mb-6 text-center">
            <p class="text-xs font-bold uppercase tracking-widest text-slate-400">As melhores operadoras e seguradoras do mercado</p>
        </div>
        <div class="relative w-full overflow-hidden">
            <div class="animate-scroll flex gap-12 items-center">
                <div class="flex items-center gap-12 px-6">
                    {gerar_carrossel(["Amil", "Hapvida GNDI", "Unimed", "Bradesco Saúde", "SulAmérica", "Porto Seguro", "Omint", "Alice Saúde"])}
                </div>
                <div class="flex items-center gap-12 px-6" aria-hidden="true">
                    {gerar_carrossel(["Amil", "Hapvida GNDI", "Unimed", "Bradesco Saúde", "SulAmérica", "Porto Seguro", "Omint", "Alice Saúde"])}
                </div>
            </div>
        </div>
    </section>

    <section class="py-16 bg-slate-50">
        <div class="max-w-6xl mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-extrabold text-slate-900 mb-3">Planos de Saúde</h2>
                <p class="text-slate-600 max-w-2xl mx-auto">Trabalhamos com os melhores planos de saúde do mercado! Confira abaixo algumas das principais operadoras e seguradoras de saúde.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
                {html_operadoras}
            </div>
            <div class="text-center mt-10">
                <a href="#cotacao" class="inline-block bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-lg shadow-md transition">Simular Meu Plano Agora</a>
            </div>
        </div>
    </section>

    <section class="py-16 bg-white border-t border-slate-200">
        <div class="max-w-6xl mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-extrabold text-slate-900 mb-3">Por que escolher a Vittre Seguros?</h2>
                <p class="text-slate-600 max-w-2xl mx-auto">Nossa consultoria ajuda você a economizar tempo e dinheiro na escolha do seu convênio médico.</p>
            </div>
            <div class="grid md:grid-cols-3 gap-8">
                <div class="p-8 rounded-xl border border-slate-200 bg-slate-50 text-center">
                    <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center text-blue-600 mx-auto mb-6 text-2xl">💰</div>
                    <h3 class="font-bold text-xl text-blue-950 mb-3">Economia Real</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">Comparamos as principais operadoras do país para encontrar o plano que cabe no seu bolso, seja individual ou PME.</p>
                </div>
                <div class="p-8 rounded-xl border border-slate-200 bg-slate-50 text-center">
                    <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center text-blue-600 mx-auto mb-6 text-2xl">🤝</div>
                    <h3 class="font-bold text-xl text-blue-950 mb-3">Atendimento Humano</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">Sem robôs. Você fala com consultores reais que entendem de ANS, carências e redes credenciadas.</p>
                </div>
                <div class="p-8 rounded-xl border border-slate-200 bg-slate-50 text-center">
                    <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center text-blue-600 mx-auto mb-6 text-2xl">⚡</div>
                    <h3 class="font-bold text-xl text-blue-950 mb-3">Agilidade na Cotação</h3>
                    <p class="text-slate-600 text-sm leading-relaxed">Nossa tecnologia gera o comparativo em poucos minutos e envia direto para o seu WhatsApp.</p>
                </div>
            </div>
        </div>
    </section>

    <main class="py-16 max-w-5xl mx-auto px-4">
        <div class="bg-white p-8 md:p-12 rounded-2xl shadow-sm border border-slate-200 space-y-6">
            <div class="text-center mb-8">
                <h2 class="text-3xl font-bold text-slate-900 mb-2">Atendimento em todo o Brasil</h2>
                <p class="text-slate-600 text-sm max-w-2xl mx-auto">Aceda à página dedicada à sua região para consultar operadoras, hospitais e solicitar uma cotação personalizada.</p>
            </div>
            
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 pt-4">
                {cards_cidades}
            </div>
        </div>
    </main>

    <section class="py-16 bg-slate-50 border-t border-slate-200">
        <div class="max-w-6xl mx-auto px-4">
            <div class="text-center mb-12">
                <h2 class="text-3xl font-extrabold text-slate-900 mb-3">Dúvidas Frequentes</h2>
                <p class="text-slate-600">Tire suas dúvidas antes de contratar o seu plano.</p>
            </div>
            {faq_home}
        </div>
    </section>

    <footer class="bg-slate-950 text-slate-400 py-12 border-t border-slate-800 text-sm">
        <div class="max-w-6xl mx-auto px-4 text-center">
            <a href="/" class="text-2xl font-black text-white tracking-tight inline-block mb-4">VITTRE<span class="text-blue-500">SEGUROS</span></a>
            <p class="mb-4">Corretora especializada em planos de saúde regionais e nacionais.</p>
            <div class="flex flex-wrap justify-center gap-6 mb-8 text-xs">
                <a href="/quem-somos.html" class="hover:text-white underline">Quem Somos</a>
                <a href="/contato.html" class="hover:text-white underline">Contato</a>
                <a href="/politica-de-privacidade.html" class="hover:text-white underline">Política de Privacidade</a>
            </div>
            <p class="text-xs text-slate-600">&copy; 2026 Vittre Seguros (@{CONFIG['instagram']}). Todos os direitos reservados.</p>
        </div>
    </footer>

    <script src="/form.js" data-ga4="{CONFIG['ga4_id']}" data-endpoint="{CONFIG['formspree_endpoint']}"></script>
</body>
</html>'''

def gerar_pagina_institucional(titulo, slug, conteudo_html):
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{titulo} | Vittre Seguros</title>
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{CONFIG['site_url']}/{slug}">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="stylesheet" href="/styles.css">
</head>
<body class="bg-slate-50 text-slate-800 font-sans">
    <header class="bg-white border-b border-slate-200 p-4 text-center"><a href="/" class="text-2xl font-black text-blue-950">VITTRE<span class="text-blue-600">SEGUROS</span></a></header>
    <main class="max-w-3xl mx-auto my-12 bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
        <h1 class="text-3xl font-extrabold text-slate-900 mb-6">{titulo}</h1>
        {conteudo_html}
        <p class="mt-8"><a href="/" class="text-blue-600 font-bold hover:underline">&larr; Voltar para a página inicial</a></p>
    </main>
    <footer class="text-center py-8 text-slate-500 text-xs">&copy; 2026 Vittre Seguros | WhatsApp: {CONFIG['whatsapp_display']}</footer>
</body>
</html>'''

def gerar_hub_estado(uf_sigla, uf_nome, cidades_estado, modo_preview=False):
    meta_robots = "index, follow" if (len(cidades_estado) >= 3 and not modo_preview) else "noindex, follow"
    lista_links = ""
    for c in cidades_estado:
        lista_links += f'<li><a href="/{c["slug"]}" class="text-blue-600 font-bold hover:underline">Plano de Saúde em {c["nome"]} ({c["uf"]})</a></li>'
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Planos de Saúde em {uf_nome} | Vittre Seguros</title>
    <meta name="robots" content="{meta_robots}">
    <link rel="canonical" href="{CONFIG['site_url']}/{uf_sigla.lower()}.html">
    <link rel="icon" type="image/x-icon" href="/favicon.ico">
    <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
    <link rel="stylesheet" href="/styles.css">
</head>
<body class="bg-slate-50 text-slate-800 font-sans">
    <header class="bg-white border-b border-slate-200 p-4 text-center"><a href="/" class="text-2xl font-black text-blue-950">VITTRE<span class="text-blue-600">SEGUROS</span></a></header>
    <main class="max-w-3xl mx-auto my-12 bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
        <h1 class="text-3xl font-extrabold text-slate-900 mb-4">Planos de Saúde no Estado de {uf_nome}</h1>
        <p class="text-slate-600 mb-6">Selecione abaixo a cidade desejada para ver cotações e tabelas atualizadas:</p>
        <ul class="space-y-2 pl-5 list-disc">{lista_links}</ul>
        <p class="mt-8"><a href="/" class="text-blue-600 font-bold hover:underline">&larr; Voltar para a página inicial</a></p>
    </main>
    <footer class="text-center py-8 text-slate-500 text-xs">&copy; 2026 Vittre Seguros | WhatsApp: {CONFIG['whatsapp_display']}</footer>
</body>
</html>'''

if __name__ == "__main__":
    modo_preview = "--preview" in sys.argv
    if modo_preview:
        print("🔍 MODO PREVIEW ATIVADO: Gerando arquivos com noindex para revisão visual.")

    cidades_validas = validar_dados(modo_preview)
    os.makedirs("public", exist_ok=True)
    
    css_content = """
    *, ::before, ::after { box-sizing: border-box; border-width: 0; border-style: solid; border-color: #e2e8f0; }
    html { line-height: 1.5; font-family: system-ui, -apple-system, sans-serif; }
    body { margin: 0; background-color: #f8fafc; color: #1e293b; }
    a { color: inherit; text-decoration: none; }
    .bg-white { background-color: #fff; } .bg-slate-50 { background-color: #f8fafc; } .bg-slate-100 { background-color: #f1f5f9; }
    .bg-blue-950 { background-color: #020617; } .bg-blue-900 { background-color: #1e3a8a; } .bg-green-600 { background-color: #16a34a; }
    .bg-green-700:hover { background-color: #15803d; } .text-white { color: #fff; } .text-slate-800 { color: #1e293b; }
    .text-slate-900 { color: #0f172a; } .text-slate-700 { color: #334155; } .text-slate-600 { color: #475569; }
    .text-slate-500 { color: #64748b; } .text-slate-400 { color: #94a3b8; } .text-blue-600 { color: #2563eb; }
    .text-blue-950 { color: #172554; } .text-blue-200 { color: #bfdbfe; } .text-green-600 { color: #16a34a; }
    .text-red-600 { color: #dc2626; } .bg-blue-800 { background-color: #1e40af; } .bg-blue-50 { background-color: #eff6ff; }
    .bg-green-100 { background-color: #dcfce7; } .text-green-800 { color: #166534; }
    .bg-blue-100 { background-color: #dbeafe; } .text-blue-800 { color: #1e40af; }
    .bg-amber-100 { background-color: #fef3c7; } .text-amber-800 { color: #92400e; }
    .font-black { font-weight: 900; } .font-bold { font-weight: 700; } .font-semibold { font-weight: 600; }
    .max-w-6xl { max-width: 72rem; } .max-w-4xl { max-width: 56rem; } .max-w-5xl { max-width: 64rem; } .max-w-3xl { max-width: 48rem; }
    .mx-auto { margin-left: auto; margin-right: auto; }
    .px-4 { padding-left: 1rem; padding-right: 1rem; } .py-16 { padding-top: 4rem; padding-bottom: 4rem; }
    .py-8 { padding-top: 2rem; padding-bottom: 2rem; } .py-10 { padding-top: 2.5rem; padding-bottom: 2.5rem; }
    .py-12 { padding-top: 3rem; padding-bottom: 3rem; } .py-2 { padding-top: 0.5rem; padding-bottom: 0.5rem; }
    .px-5 { padding-left: 1.25rem; padding-right: 1.25rem; } .py-2.5 { padding-top: 0.625rem; padding-bottom: 0.625rem; }
    .p-6 { padding: 1.5rem; } .p-8 { padding: 2rem; } .p-4 { padding: 1rem; } .p-12 { padding: 3rem; }
    .my-12 { margin-top: 3rem; margin-bottom: 3rem; } .mb-6 { margin-bottom: 1.5rem; } .mb-4 { margin-bottom: 1rem; }
    .mb-2 { margin-bottom: 0.5rem; } .mb-1 { margin-bottom: 0.25rem; } .mt-8 { margin-top: 2rem; }
    .mt-6 { margin-top: 1.5rem; } .mt-4 { margin-top: 1rem; } .mt-2 { margin-top: 0.5rem; }
    .flex { display: flex; } .items-center { align-items: center; } .justify-between { justify-content: space-between; }
    .justify-center { justify-content: center; } .flex-shrink-0 { flex-shrink: 0; } .flex-wrap { flex-wrap: wrap; }
    .grid { display: grid; } .gap-8 { gap: 2rem; } .gap-6 { gap: 1.5rem; } .gap-4 { gap: 1rem; } .gap-12 { gap: 3rem; } .space-y-4 > * + * { margin-top: 1rem; } .space-y-3 > * + * { margin-top: 0.75rem; } .space-y-2 > * + * { margin-top: 0.5rem; }
    @media(min-width: 768px) { .md\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); } .md\\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); } .md\\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); } .md\\:text-left { text-align: left; } }
    @media(min-width: 640px) { .sm\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    @media(min-width: 1024px) { .lg\\:grid-cols-5 { grid-template-columns: repeat(5, minmax(0, 1fr)); } }
    .rounded-xl { border-radius: 0.75rem; } .rounded-2xl { border-radius: 1rem; } .rounded-lg { border-radius: 0.5rem; } .rounded-full { border-radius: 9999px; }
    .shadow-sm { box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05); } .shadow-2xl { box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25); }
    .border { border-width: 1px; } .border-slate-200 { border-color: #e2e8f0; } .border-blue-700 { border-color: #1d4ed8; } .border-blue-100 { border-color: #dbeafe; } .border-slate-800 { border-color: #1e293b; }
    .sticky { position: sticky; } .top-0 { top: 0; } .z-50 { z-index: 50; }
    .w-full { width: 100%; } input, select { width: 100%; padding: 0.75rem 1rem; border: 1px solid #cbd5e1; border-radius: 0.5rem; font-size: 0.875rem; background: #fff; color: #0f172a; }
    @keyframes scroll { 0% { transform: translateX(0); } 100% { transform: translateX(-50%); } }
    .animate-scroll { display: flex; width: max-content; animation: scroll 35s linear infinite; }
    .hidden { display: none; }
    .bg-gradient-to-br { background-image: linear-gradient(to bottom right, var(--tw-gradient-stops)); }
    .from-blue-950 { --tw-gradient-from: #020617; --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-to); }
    .via-blue-900 { --tw-gradient-via: #1e3a8a; --tw-gradient-stops: var(--tw-gradient-from), var(--tw-gradient-via), var(--tw-gradient-to); }
    .to-indigo-950 { --tw-gradient-to: #172554; }
    .overflow-hidden { overflow: hidden; }
    .text-center { text-align: center; }
    .underline { text-decoration: underline; }
    .list-disc { list-style-type: disc; }
    .pl-5 { padding-left: 1.25rem; }
    .text-xs { font-size: 0.75rem; line-height: 1rem; }
    .text-sm { font-size: 0.875rem; line-height: 1.25rem; }
    .text-lg { font-size: 1.125rem; line-height: 1.75rem; }
    .text-xl { font-size: 1.25rem; line-height: 1.75rem; }
    .text-2xl { font-size: 1.5rem; line-height: 2rem; }
    .text-3xl { font-size: 1.875rem; line-height: 2.25rem; }
    .text-5xl { font-size: 3rem; line-height: 1; }
    .tracking-tight { letter-spacing: -0.025em; }
    .tracking-wider { letter-spacing: 0.05em; }
    .tracking-widest { letter-spacing: 0.1em; }
    .uppercase { text-transform: uppercase; }
    .inline-block { display: inline-block; }
    .bg-slate-950 { background-color: #020617; }
    .transition { transition-property: color, background-color, border-color, text-decoration-color, fill, stroke, opacity, box-shadow, transform; transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1); transition-duration: 150ms; }
    """
    with open(os.path.join("public", "styles.css"), "w", encoding="utf-8") as f:
        f.write(css_content.strip())

    js_content = """
    async function enviarLead(e) {
        e.preventDefault();
        const form = e.target;
        const btn = document.getElementById('btn-submit');
        const sucesso = document.getElementById('sucesso-msg');
        const erro = document.getElementById('erro-msg');
        
        const scriptTag = document.currentScript || document.querySelector('script[data-endpoint]');
        const endpoint = scriptTag ? scriptTag.getAttribute('data-endpoint') : '';
        const ga4Id = scriptTag ? scriptTag.getAttribute('data-ga4') : '';

        btn.disabled = true;
        btn.textContent = 'Enviando...';
        erro.classList.add('hidden');

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch(endpoint, {
                method: 'POST',
                headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            if (response.ok) {
                form.classList.add('hidden');
                sucesso.classList.remove('hidden');

                if (ga4Id && typeof gtag === 'function') {
                    gtag('event', 'generate_lead', {
                        'event_category': 'Conversao',
                        'event_label': data.cidade || 'Landing Page',
                        'tipo_plano': data.tipo_plano
                    });
                }
            } else {
                throw new Error('Falha no envio');
            }
        } catch (err) {
            console.error(err);
            erro.classList.remove('hidden');
            btn.disabled = false;
            btn.textContent = 'Solicitar cotação';
        }
    }
    """
    with open(os.path.join("public", "form.js"), "w", encoding="utf-8") as f:
        f.write(js_content.strip())

    count = 0
    sitemap_urls = [f"{CONFIG['site_url']}/"]
    
    index_html = gerar_pagina_principal(cidades_validas)
    with open(os.path.join("public", "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)

    for cidade in cidades_validas:
        html = gerar_html_cidade(cidade, cidades_validas)
        caminho = os.path.join("public", f"{cidade['slug']}.html")
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(html)
        if not cidade.get("_preview", False):
            sitemap_urls.append(f"{CONFIG['site_url']}/{cidade['slug']}")
        count += 1

    estados = {
        "bahia": ("bahia", "Bahia"),
        "sao-paulo": ("sao-paulo", "São Paulo"),
        "mato-grosso": ("mato-grosso", "Mato Grosso"),
        "goias": ("goias", "Goiás"),
        "tocantins": ("tocantins", "Tocantins"),
        "maranhao": ("maranhao", "Maranhão"),
        "pernambuco": ("pernambuco", "Pernambuco")
    }
    for slug_estado, (sigla, nome_est) in estados.items():
        cidades_do_estado = [c for c in cidades_validas if c["estado_slug"] == slug_estado and c.get("publicar", False)]
        if len(cidades_do_estado) < 3 and not modo_preview:
            continue
            
        hub_html = gerar_hub_estado(sigla, nome_est, cidades_do_estado, modo_preview)
        with open(os.path.join("public", f"{slug_estado}.html"), "w", encoding="utf-8") as f:
            f.write(hub_html)
        if len(cidades_do_estado) >= 3 and not modo_preview:
            sitemap_urls.append(f"{CONFIG['site_url']}/{slug_estado}")

    inst_pages = {
        "quem-somos.html": ("Quem Somos", "<p>A <strong>Vittre Seguros</strong> é uma corretora especializada em soluções de assistência médica e planos de saúde.</p>"),
        "contato.html": ("Contato", "<p>Fale diretamente com nossa equipe comercial especializada.</p><p><strong>WhatsApp:</strong> (11) 97830-5192</p>"),
        "politica-de-privacidade.html": ("Política de Privacidade", "<p>A Vittre Seguros respeita a sua privacidade em conformidade com a LGPD.</p>")
    }
    for filename, (title, content) in inst_pages.items():
        page_html = gerar_pagina_institucional(title, filename.replace(".html", ""), content)
        with open(os.path.join("public", filename), "w", encoding="utf-8") as f:
            f.write(page_html)
        sitemap_urls.append(f"{CONFIG['site_url']}/{filename.replace('.html', '')}")

    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in sorted(list(set(sitemap_urls))):
        sitemap_xml += f'  <url>\n    <loc>{url}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n'
    sitemap_xml += '</urlset>'
    with open(os.path.join("public", "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)

    robots_txt = f"User-agent: *\nAllow: /\nSitemap: {CONFIG['site_url']}/sitemap.xml\n"
    with open(os.path.join("public", "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_txt)

    for fav in ["favicon.ico", "favicon-32x32.png", "favicon-16x16.png"]:
        if os.path.exists(fav):
            shutil.copy(fav, os.path.join("public", fav))

    print(f"\n🎉 Sucesso! {count} página(s) densas de nível corporativo e o index.html principal foram compilados na pasta 'public'.")