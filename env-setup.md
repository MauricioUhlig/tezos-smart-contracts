# Preparando o Ambiente para Execução de *Smart Contracts* em *Tezos*

Guia de configuração inicial de ambiente Linux para desenvolvimento e execução de *smart contracts* na *Blockchain Tezos*.

---

## 📦 Instalação e Configuração das Ferramentas Essenciais

### 🧰 Octez Client

O `octez-client` é o CLI (*Command Line Interface*) utilizado para interagir com a rede Tezos.

#### 🔧 Instalação

Execute os comandos abaixo para adicionar o repositório e instalar o cliente:

```sh
REPO="ppa:serokell/tezos"
sudo add-apt-repository -y $REPO && sudo apt-get update
sudo apt-get install -y tezos-client
```

#### ✅ Verificação da Instalação

Para verificar se o `octez-client` foi instalado corretamente:

```sh
octez-client --version
```

Saída esperada:

```text
b8278e10 (2025-02-25 19:28:57 +0100) (Octez 21.4)
```

#### 🌐 Configuração do Endpoint

Configure o cliente para se conectar à rede de testes `ghostnet`:

```sh
octez-client --endpoint https://rpc.ghostnet.teztnets.com config update
```

📚 [Documentação oficial do Octez](https://docs.tezos.com/developing/octez-client/installing)

---

### 🧪 SmartPy

O *SmartPy* é uma linguagem e ferramenta para desenvolvimento de contratos inteligentes em Tezos utilizando Python.

#### 🔧 Instalação

Execute o comando abaixo para instalar o pacote:

```sh
pip install https://smartpy.io/static/tezos_smartpy-0.21.1-py3-none-any.whl
```

#### ✅ Verificação da Instalação

Teste a instalação com o seguinte exemplo:

```sh
wget https://smartpy.io/templates/welcome.py
python welcome.py
```

Isso irá gerar arquivos `.py`, `.json` e `.tz` dentro da pasta `welcome`.

Para visualizar os arquivos gerados:

```sh
ls welcome/
```

📚 [Documentação oficial do SmartPy](https://smartpy.tezos.com/manual/introduction/installation.html)

[<< Voltar](readme.md)