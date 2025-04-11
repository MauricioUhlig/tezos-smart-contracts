# Guia Completo das Operações de Pilha do Michelson

Michelson é uma linguagem baseada em pilha onde todas as operações manipulam uma pilha do tipo LIFO (*Last-In-First-Out*). Este documento fornece uma referência completa de todas as operações de pilha.

## 1. Operações de Manipulação de Pilha

| Operação   | Pilha Antes         | Pilha Depois         | Descrição                            |
|------------|---------------------|----------------------|--------------------------------------|
| `DROP`     | `a : s`             | `s`                  | Remove o elemento do topo            |
| `DUP`      | `a : s`             | `a : a : s`          | Duplica o elemento do topo           |
| `SWAP`     | `a : b : s`         | `b : a : s`          | Troca os dois elementos do topo      |
| `DIG n`    | `xₙ : ... : x₁ : s` | `x₁ : xₙ : ... : s`  | Move o n-ésimo elemento para o topo  |
| `DUG n`    | `x₁ : ... : xₙ : s` | `xₙ : x₁ : ... : s`  | Enterra o topo na profundidade n     |
| `PUSH tipo valor` | `s`         | `valor : s`          | Empilha um valor                     |
| `UNIT`     | `s`                 | `unit : s`           | Empilha o valor `unit`               |

## 2. Operações com Pares e Tuplas

| Operação   | Pilha Antes     | Pilha Depois     | Descrição                            |
|------------|-----------------|------------------|--------------------------------------|
| `PAIR`     | `a : b : s`     | `(a, b) : s`     | Combina dois valores em um par       |
| `UNPAIR`   | `(a, b) : s`    | `a : b : s`      | Divide o par em dois valores         |
| `CAR`      | `(a, b) : s`    | `a : s`          | Obtém o primeiro elemento do par     |
| `CDR`      | `(a, b) : s`    | `b : s`          | Obtém o segundo elemento do par      |

## 3. Operações Aritméticas

| Operação   | Pilha Antes     | Pilha Depois     | Descrição                                  |
|------------|-----------------|------------------|--------------------------------------------|
| `ADD`      | `a : b : s`     | `(a + b) : s`    | Soma (int/nat/tez)                         |
| `SUB`      | `a : b : s`     | `(a - b) : s`    | Subtração (int/nat/tez)                    |
| `MUL`      | `a : b : s`     | `(a * b) : s`    | Multiplicação                              |
| `EDIV`     | `a : b : s`     | `Some (a / b) : s` | Divisão euclidiana                       |
| `ABS`      | `a : s`         | `abs(a) : s`     | Valor absoluto (int → nat)                 |
| `NEG`      | `a : s`         | `-a : s`         | Negação (int → int)                        |

## 4. Operações Booleanas e Lógicas

| Operação   | Pilha Antes     | Pilha Depois     | Descrição                              |
|------------|-----------------|------------------|----------------------------------------|
| `OR`       | `a : b : s`     | `(a ∨ b) : s`    | OU lógico                              |
| `AND`      | `a : b : s`     | `(a ∧ b) : s`    | E lógico                               |
| `XOR`      | `a : b : s`     | `(a ⊕ b) : s`    | XOR lógico                             |
| `NOT`      | `a : s`         | `¬a : s`         | Negação lógica                         |
| `COMPARE`  | `a : b : s`     | `cmp(a,b) : s`   | Retorna -1 (LT), 0 (EQ), ou 1 (GT)     |

## 5. Operações de Controle de Fluxo

| Operação               | Pilha Antes   | Pilha Depois     | Descrição                                    |
|------------------------|---------------|------------------|----------------------------------------------|
| `IF { bt } { bf }`     | `cond : s`    | Executa `bt` se `cond=True` | Ramificação condicional          |
| `LOOP { corpo }`       | `cond : s`    | Repete enquanto `cond=True` | Laço tipo while                 |
| `ITER { corpo }`       | `lista : s`   | Aplica `corpo` a cada elemento | Iteração sobre lista         |
| `DIP { código }`       | `a : s`       | Executa `código` abaixo do topo | Preserva o item superior  |

## 6. Operações com Listas e Mapas

| Operação   | Pilha Antes         | Pilha Depois       | Descrição                           |
|------------|---------------------|--------------------|-------------------------------------|
| `CONS`     | `x : lista : s`     | `{x; lista} : s`   | Adiciona elemento na lista          |
| `NIL tipo` | `s`                 | `{} : s`           | Cria lista vazia                    |
| `SIZE`     | `lista : s`         | `tamanho(lista) : s` | Retorna o tamanho                 |
| `GET`      | `chave : mapa : s`  | `Some valor : s`   | Recupera valor do mapa              |
| `UPDATE`   | `chave : option valor : mapa : s` | `novo_mapa : s` | Atualiza o mapa          |

## 7. Operações Criptográficas

| Operação            | Pilha Antes              | Pilha Depois      | Descrição                        |
|---------------------|--------------------------|-------------------|----------------------------------|
| `HASH_KEY`          | `chave : s`              | `hash : s`        | Hash da chave pública            |
| `BLAKE2B`           | `bytes : s`              | `hash : s`        | Hash Blake2b                     |
| `CHECK_SIGNATURE`   | `chave : assinatura : bytes : s` | `bool : s` | Verifica assinatura      |

## 8. Operações de Contrato

| Operação           | Pilha Antes                     | Pilha Depois         | Descrição                                |
|--------------------|----------------------------------|----------------------|------------------------------------------|
| `CONTRACT tipo`    | `endereço : s`                  | `Some contrato : s`  | Faz cast para contrato                   |
| `TRANSFER_TOKENS`  | `param : quantia : contrato : s` | `operação : s`      | Cria uma transferência                   |
| `CREATE_CONTRACT`  | `{ armazenamento; código } : s` | `(op, endereço) : s` | Origina novo contrato                    |

## 9. Conversão de Tipos

| Operação   | Pilha Antes     | Pilha Depois     | Descrição                          |
|------------|-----------------|------------------|------------------------------------|
| `PACK`     | `a : s`         | `bytes : s`      | Serializa                          |
| `UNPACK tipo` | `bytes : s` | `Some a : s`     | Desserializa                       |
| `ISNAT`    | `int : s`       | `Some nat : s`   | Converte para nat                  |

## 10. Operações Especiais

| Operação               | Pilha Antes    | Pilha Depois     | Descrição                             |
|------------------------|----------------|------------------|---------------------------------------|
| `FAILWITH`             | `a : s`        | (termina execução) | Aborta a execução                     |
| `NEVER`                | `never : s`    | (inacessível)     | Lida com casos impossíveis            |
| `LAMBDA tipo1 tipo2 código` | `s`     | `lambda : s`     | Cria uma função                       |

## Exemplo de Contrato

&&michelson
parameter int;
storage int;
code {
  UNPAIR ;       # Pilha: input : storage
  ADD ;          # Pilha: (input + storage)
  DUP ;          # Pilha: soma : soma
  PUSH int 10 ;  # Pilha: 10 : soma : soma
  COMPARE ;      # Pilha: (10 > soma?) : soma
  IF { FAILWITH } {} ;  # Falha se soma > 10
  NIL operation ;
  PAIR
}
&&
