## test pokedex.py
import pypokedex 
import pytest 

def test_get_pokemon():
    # get the pokemon from the pokedex
    assert pypokedex.get(name = "bulbasaur").name == "bulbasaur"
    assert pypokedex.get(name = "ivysaur").name == "ivysaur"
    assert pypokedex.get(name = "venusaur").name == "venusaur"
    assert pypokedex.get(name = "charmander").name == "charmander"
    assert pypokedex.get(name = "charmeleon").name == "charmeleon"
    assert pypokedex.get(name = "charizard").name == "charizard"
    assert pypokedex.get(name = "squirtle").name == "squirtle"
    assert pypokedex.get(name = "wartortle").name == "wartortle"
    assert pypokedex.get(name = "blastoise").name == "blastoise"
    assert pypokedex.get(name = "caterpie").name == "caterpie"
    assert pypokedex.get(name = "metapod").name == "metapod"
    assert pypokedex.get(name = "butterfree").name == "butterfree"
    print("test_get_pokemon passed")


pytest.main([ __file__])

