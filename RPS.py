import smartpy as sp

@sp.module
def main():
    class RockPaperScissors(sp.Contract):
        def __init__(self, admin):
            self.data.reward = sp.tez(0)
            self.data.players = {}
            self.data.num_players=0
            self.data.check_winner={
                    0: {0: 2, 1: 1, 2: 0},   # Rock rules
                    1: {0: 0, 1: 2, 2: 1},   # Paper rules
                    2: {0: 1, 1: 0, 2: 2}    # Scissors rules
                }
            self.data.winner = -1
            self.data.admin = admin
            
        
        @sp.entrypoint
        def add_player(self, params):
            assert self.data.num_players < 2
            assert sp.amount == sp.tez(1)
            
            self.data.reward += sp.amount
            self.data.players[self.data.num_players] = sp.record(
                address=sp.sender,
                choice=params.choice
            )
            self.data.num_players += 1
        
        @sp.entrypoint
        def check(self):
            assert sp.sender == self.data.admin, "Only admin can check"
            assert self.data.num_players == 2, "You can only check if all have played"
            
            p0_choice = self.data.players[0].choice
            p1_choice = self.data.players[1].choice
            self.data.winner = self.data.check_winner[p0_choice][p1_choice]
            
            if self.data.winner  == 0:  # Player 0 wins
                sp.send(self.data.players[0].address, self.data.reward)
            else: 
                if self.data.winner  == 1:  # Player 1 wins
                    sp.send(self.data.players[1].address, self.data.reward)
                else:  # Tie
                    # half_reward = self.data.reward / sp.tez(2) # changed to integer division
                    sp.send(self.data.players[0].address, sp.tez(1)) 
                    sp.send(self.data.players[1].address, sp.tez(1)) 

            
        @sp.entrypoint
        def reset(self):
            assert sp.sender == self.data.admin
            # Reset game state
            self.data.players = {}
            self.data.num_players = 0
            self.data.reward = sp.tez(0)

@sp.add_test()
def test():
    scenario = sp.test_scenario("RPS", main)
    
    # Test accounts
    admin = sp.test_account("Admin")
    player1 = sp.test_account("Player1")
    player2 = sp.test_account("Player2")
    
    # Initialize contract
    rps = main.RockPaperScissors(admin.address)
    scenario += rps
    
    # Helper function to print choices
    def choice_to_str(choice):
        if choice == 0:
            return "Rock"
        elif choice == 1:
            return "Paper"
        else:
            return "Scissors"
    
    # Test case 1: Player 1 (Scissors) vs Player 2 (Paper) - Player 1 wins
    scenario.h1("Test 1: Scissors vs Paper - Scissors wins")
    rps.add_player(choice=sp.int(2), _sender=player1, _amount=sp.tez(1))
    rps.add_player(choice=sp.int(1), _sender=player2, _amount=sp.tez(1))
    rps.check(_sender=admin.address)
    scenario.verify(rps.data.winner == 0) # first player is the winner
    rps.reset(_sender=admin.address)
    
    # Test case 2: Player 1 (Paper) vs Player 2 (Scissors) - Player 2 wins
    scenario.h1("Test 2: Paper vs Scissors - Scissors wins")
    rps.add_player(choice=sp.int(1), _sender=player1, _amount=sp.tez(1))
    rps.add_player(choice=sp.int(2), _sender=player2, _amount=sp.tez(1))
    rps.check(_sender=admin.address)
    scenario.verify(rps.data.winner == 1) # second player is the winner
    rps.reset(_sender=admin.address)

    # Test case 3: Check with only one player - should fail
    scenario.h1("Test 3: Check with one player - should fail")
    rps.add_player(choice=sp.int(1), _sender=player1, _amount=sp.tez(1))
    rps.check(_sender=admin, _valid=False)
    rps.reset(_sender=admin.address)
    
    # Test case 4: Both choose Paper - Tie
    scenario.h1("Test 4: Paper vs Paper - Tie")
    rps.add_player(choice=sp.int(1), _sender=player1, _amount=sp.tez(1))
    rps.add_player(choice=sp.int(1), _sender=player2, _amount=sp.tez(1))
    rps.check(_sender=admin.address)
    scenario.verify(rps.data.winner == 2) # tie
    rps.reset(_sender=admin.address)
    
    # Test case 5: Player 1 (Rock) vs Player 2 (Paper) - Player 2 wins
    scenario.h1("Test 5: Rock vs Paper - Paper wins")
    rps.add_player(choice=sp.int(0), _sender=player1, _amount=sp.tez(1))
    rps.add_player(choice=sp.int(1), _sender=player2, _amount=sp.tez(1))
    rps.check(_sender=admin.address)
    scenario.verify(rps.data.winner == 1) # second player wins
    rps.reset(_sender=admin.address)
    
    # Test case 6: Player 1 (Rock) vs Player 2 (Scissors) - Player 1 wins
    scenario.h1("Test 6: Rock vs Scissors - Rock wins")
    rps.add_player(choice=sp.int(0), _sender=player1, _amount=sp.tez(1))
    rps.add_player(choice=sp.int(2), _sender=player2, _amount=sp.tez(1))
    rps.check(_sender=admin.address)
    scenario.verify(rps.data.winner == 0) # first player wins
    rps.reset(_sender=admin.address)
    
    # # Test case 7: Both choose Rock - Tie
    scenario.h1("Test 7: Rock vs Rock - Tie")
    rps.add_player(choice=sp.int(0), _sender=player1, _amount=sp.tez(1))
    rps.add_player(choice=sp.int(0), _sender=player2, _amount=sp.tez(1))
    rps.check(_sender=admin.address)
    scenario.verify(rps.data.winner == 2) # tie
    rps.reset(_sender=admin.address)
    
    # Test case 8: Both choose Scissors - Tie
    scenario.h1("Test 8: Scissors vs Scissors - Tie")
    rps.add_player(choice=sp.int(2), _sender=player1, _amount=sp.tez(1))
    rps.add_player(choice=sp.int(2), _sender=player2, _amount=sp.tez(1))
    rps.check(_sender=admin.address)
    scenario.verify(rps.data.winner == 2) # tie
    rps.reset(_sender=admin.address)
    
    # Test case 9: Try to add third player - should fail
    scenario.h1("Test 9: Add third player - should fail")
    rps.add_player(choice=sp.int(0), _sender=player1, _amount=sp.tez(1))
    rps.add_player(choice=sp.int(1), _sender=player2, _amount=sp.tez(1))
    rps.add_player(choice=sp.int(2), _sender=admin, _amount=sp.tez(1), _valid=False)
    rps.reset(_sender=admin.address)
    
    # Test case 10: Try to play without sending tez - should fail
    scenario.h1("Test 10: Play without tez - should fail")
    rps.add_player(choice=sp.int(0), _sender=player1, _amount=sp.tez(0), _valid=False)
    
    # Test case 11: Non-admin tries to check - should fail
    scenario.h1("Test 11: Non-admin check - should fail")
    rps.add_player(choice=sp.int(0), _sender=player1, _amount=sp.tez(1))
    rps.add_player(choice=sp.int(1), _sender=player2, _amount=sp.tez(1))
    rps.check(_sender=player1, _valid=False)
    rps.reset(_sender=admin.address)
    
    # Test case 12: Non-admin tries to reset - should fail
    scenario.h1("Test 12: Non-admin reset - should fail")
    rps.add_player(choice=sp.int(0), _sender=player1, _amount=sp.tez(1))
    rps.reset(_sender=player1, _valid=False)
    rps.reset(_sender=admin.address)