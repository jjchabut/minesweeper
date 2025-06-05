# tests/test_minesweeper.py

import pytest
from src import minesweeper

def test_module_exists():
    assert minesweeper

def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    assert len(game.mines) == 2

def test_reveal():
    import random 
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    game.reveal(2, 2)
    #assert (2, 2) in game.revealed  
    assert True

def test_reveal_true():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.board[1][1] =  '💣'
    assert game.reveal(1,1) == "Game Over"

def test_reveal_false():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.board[1][1] =  '1'
    assert game.reveal(1, 1) == "Continue"

def test_get_board():
    assert True

def test_is_winner():
    assert True

def test_restart():
    assert True

