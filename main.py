"""Entry point."""

from controllers.base import Controller
from models.deck import Deck
from views.base import View


def main():
    deck = Deck()
    view = View()
    game = Controller(deck, view)
    game.run()

main()

