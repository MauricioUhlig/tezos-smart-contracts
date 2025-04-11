# Comandos Úteis com `octez-client`

Guia prático com comandos essenciais para configurar contas, testar e interagir com *smart contracts* na blockchain Tezos, utilizando a ferramenta `octez-client`.

---

## 🧾 Configuração de Contas

### ➕ Criar nova conta
Cria uma nova conta com o nome `account`:

```sh
octez-client gen keys account
```

---

### 🔍 Ver endereço da conta
Exibe o endereço (hash) e a chave pública da conta criada:

```sh
octez-client show address account
```

Saída esperada:

```
txt
Hash: tz1VZw1oeUuyZM4xi7yYPZSYQtrBKjvAcAA7
Public Key: edpkvB22Vg9FbJ7Fokn934u1d8HNnKovhQge9sdnR3vxAqBxzpXvFT
```

---

## 💰 Adicionando Fundos à Conta

Toda operação na blockchain tem um custo. Para usar sua conta, você precisa de fundos.

1. Copie o `Hash` da conta criada.
2. Acesse [https://faucet.ghostnet.teztnets.com](https://faucet.ghostnet.teztnets.com).
3. Cole o endereço no campo **_Fund any address_**, escolha um valor e clique em **_Request_**.

> ⚠️ Este processo pode levar alguns minutos.

---

## 💳 Verificar Saldo da Conta

Use o comando abaixo para ver o saldo atual da conta:

```sh
octez-client get balance for account
```

Exemplo de saída: `5.692305 ꜩ`


---

## 🧪 Execução Avulsa de Smart Contracts

Permite testar contratos *Michelson* localmente, sem publicá-los na blockchain.

### 📌 Formato do comando

```sh
octez-client run script <caminho/arquivo.tz> on storage '<valor inicial storage>' and input '<valor de entrada>' [--entrypoint <método>]
```

### 🧷 Exemplos

```sh
octez-client run script ./examples/increment.tz on storage '6' and input '5'

octez-client run script ./examples/helloTezos.tz on storage '""' and input '"Mauricio"' --entrypoint name
```

---

## 🚀 Publicação de Smart Contracts

Para publicar (originar) um contrato na rede:

### 📌 Formato do comando

```sh
octez-client originate contract <nome_do_contrato> transferring 0 from <conta> running <arquivo.tz> --init <valor_storage> --burn-cap <limite_taxa>
```

> A publicação irá retornar um hash  do endereço do contrato e este pode ser usado para consultar o contrato na `ghostnet` pelo site [https://better-call.dev/](https://better-call.dev/)

### 🧷 Exemplo

```sh
octez-client originate contract my-counter transferring 0 from account running ./examples/increment.tz --init 10 --burn-cap 0.1
```

---

## ⚙️ Invocação de Smart Contracts

Executa uma chamada a um contrato já publicado na blockchain.

### 📌 Formato do comando

```sh
octez-client call <nome_do_contrato> from <conta> --arg <parametros> [--entrypoint <método>]
```

### 🧷 Exemplo

```sh
octez-client call my-counter from account --arg 7
```

---

📚 Para mais informações, consulte a [documentação oficial do Octez](https://octez.tezos.com/docs/introduction/tezos.html).

