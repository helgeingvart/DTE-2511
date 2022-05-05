from del3 import SecondOrderPolynomal

def test_me() :
    polynom = SecondOrderPolynomal(1,0,-1)
    root1, root2 = polynom.findRoots()
    assert root1 == 1, "Should find positive root first"
    assert root2 == -1, "Should find negative root second"