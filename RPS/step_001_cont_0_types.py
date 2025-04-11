import smartpy as sp

tstorage = sp.record(admin = sp.address, check_winner = sp.map(sp.int, sp.map(sp.int, sp.int)), num_players = sp.int, players = sp.map(sp.int, sp.record(address = sp.address, choice = sp.int).layout(("address", "choice"))), reward = sp.mutez, winner = sp.int).layout(("admin", ("check_winner", ("num_players", ("players", ("reward", "winner"))))))
tparameter = sp.variant(add_player = sp.record(choice = sp.int).layout("choice"), check = sp.unit, reset = sp.unit).layout(("add_player", ("check", "reset")))
tprivates = { }
tviews = { }
