"""Base view."""


class View:
    """Card game view."""

    def prompt_for_player(self):
        """Prompt for a name."""
        name = input("Tapez le nom du joueur : ")
        if not name:
            return None
        return name

    def show_player_hand(self, name, hand):
        """Show the plyer hand."""
        print(f"[Joueur {name}]")
        for card in hand:
            if card.is_face_up:
                print(card)
            else:
                print("(carte face cachée)")

    def prompt_for_flip_cards(self):
        """Request to return the cards."""
        print()
        input("Prêt à retourner les cartes?")
        return True

    def show_winner(self, name):
        """Show the winner."""
        print(f"Bravo {name} !")

    def prompt_for_new_game(self):
        """Reqiest to replay."""
        print("Souhaitez vous refaire une partie?")
        choice = input("Y/N: ")
        if choice == "N":
            return False
        return True
