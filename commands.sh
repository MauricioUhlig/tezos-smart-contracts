# Create a new contract 
octez-client originate contract my-counter   transferring 0 from mauricio   running increment.tz  --init 10 --burn-cap 0.1

# get balance 
octez-client get balance for mauricio 
# 798.360242 ꜩ
# após entrar no jogo: 797.350555 ꜩ
# após empate: 798.350221 ꜩ
octez-client get balance for account1 
# 6.701624 ꜩ
# após entrar no jogo: 5.692305 ꜩ
# após empate: 6.692305 ꜩ

# Show addres details 
octez-client show address mauricio --show-secret

# Call a contract 
octez-client call my-counter from mauricio  --arg 7

# Running without deploy 
octez-client run script increment.tz on storage '6' and input '5'
octez-client run script helloTezos.tz on storage '""' and input '"Teste"'

# Type check
octez-client typecheck script helloTezos.tz --details 


# Create RPS contract 
octez-client originate contract rps-game transferring 0 from mauricio running ./RPS/step_001_cont_0_contract.tz  --init '(Pair "tz1MzBwYYBCtdL5ZFRYAeXPYHJjsXoh1sdFD" (Pair {Elt 0 {Elt 0 2; Elt 1 1; Elt 2 0}; Elt 1 {Elt 0 0; Elt 1 2; Elt 2 1}; Elt 2 {Elt 0 1; Elt 1 0; Elt 2 2}} (Pair 0 (Pair {} (Pair 0 -1)))))' --burn-cap 0.6

# created contract KT1KQ1y6v39bHdTetiFWA7Mt1WMweYroAFWc
# https://better-call.dev/ghostnet/KT1KQ1y6v39bHdTetiFWA7Mt1WMweYroAFWc/operations
# entrar no jogo - ambos com Rock (0)
octez-client transfer 1 from mauricio to rps-game --entrypoint add_player --arg '0' --burn-cap 0.00925
octez-client transfer 1 from account1 to rps-game --entrypoint add_player --arg '0' --burn-cap 0.00925

# Verificar quem ganhou
octez-client transfer 0 from mauricio to rps-game --entrypoint check --arg 'Unit'

octez-client transfer 0 from mauricio to rps-game --entrypoint reset --arg 'Unit'


octez-client transfer 1 from mauricio to rps-game --entrypoint add_player --arg '0' --burn-cap 0.00925
octez-client transfer 1 from account1 to rps-game --entrypoint add_player --arg '2' --burn-cap 0.00925

octez-client get balance for mauricio # 797.349587 ꜩ
octez-client get balance for account1 # 5.691986 ꜩ

octez-client transfer 0 from mauricio to rps-game --entrypoint check --arg 'Unit'
# mauricio 797.349263 ꜩ
# account1 7.691986 ꜩ
octez-client transfer 0 from mauricio to rps-game --entrypoint reset --arg 'Unit'