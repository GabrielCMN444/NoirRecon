# 🖤 NoirRecon

**NoirRecon** é uma ferramenta automatizada de **Reconhecimento (Recon)** para Pentest e Bug Bounty, criada para facilitar o processo de:

- Enumeração de subdomínios
- Detecção de hosts ativos
- Scan automatizado com Nuclei
- Geração de relatórios organizados

Projeto desenvolvido para portfólio e aprendizado em Cybersecurity.

---

## ⚡ Funcionalidades

✅ Subdomain Enumeration (Subfinder)  
✅ Alive Hosts Detection (Httpx)  
✅ Vulnerability Scan (Nuclei)  
✅ Modo rápido com menos templates  
✅ Barra de progresso e saída organizada  
✅ Relatório salvo automaticamente  

---

## 🛠️ Requisitos

Antes de usar, você precisa ter instalado:

- Python 3
- Subfinder
- Httpx
- Nuclei
- Nuclei Templates

No Linux:

```bash
sudo pacman -S python git
sudo pacman -S subfinder httpx nuclei
  


📦 Instalação

Clone o repositório

git clone https://github.com/GabrielCMN444/NoirRecon.git
cd NoirRecon




Crie um ambiente virtual:

python -m venv venv
source venv/bin/activat




Instale as dependências:

pip install -r requirements.txt





Como Usar

Scan padrão:
python noirrecon.py -d example.com


Scan com limite de subdomínios:
python noirrecon.py -d hackerone.com --limit 200


Scan com mais threads (mais rápido):
python noirrecon.py -d hackerone.com --threads 80


Modo rápido (menos templates do nuclei):
python noirrecon.py -d hackerone.com --fast




output/
 ├── subs.txt        → subdomínios encontrados
 ├── alive.txt       → hosts ativos
 ├── nuclei.txt      → vulnerabilidades detectadas
 └── report.txt      → relatório final completo




🧪 Teste Seguro (Recomendado)

Use domínios autorizados para prática:

Nmap Scanme (oficial)
python noirrecon.py -d scanme.nmap.org --fast

Example Domain
python noirrecon.py -d example.com --fast



⚠️ Aviso Legal

Esta ferramenta foi criada apenas para:


Estudo

Portfólio

Bug Bounty autorizado

Pentest com permissão

❌ Não use em sites aleatórios sem autorização.
O uso indevido pode ser considerado atividade ilegal.




👤 Autor

 Desenvolvido por Gabriel Campos

 Estudante de Cybersecurity | Pentest | Front-end Dev

GitHub: https://github.com/GabrielCMN444
