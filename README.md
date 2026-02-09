# 🖤 NoirRecon

NoirRecon é uma ferramenta de **reconhecimento automatizado** voltada para portfólio e aprendizado, focada em:

- Enumeração de subdomínios
- Detecção de hosts ativos
- Scan opcional com Nuclei (modo seguro)

⚠ **Uso permitido apenas em domínios próprios ou programas autorizados (Bug Bounty).**

---

## ✨ Features

✅ Subdomain Enumeration (subfinder)  
✅ Alive Hosts Detection (httpx)  
✅ Vulnerability Scan opcional (nuclei)  
✅ Report automático em `output/report.txt`  
✅ Fast Mode (critical-only templates)

---

## 🚀 Instalação

### Dependências externas:

```bash
sudo pacman -S subfinder httpx nuclei
