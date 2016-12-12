def test_balance0(chain):
    gnt = chain.get_contract('TestGNT')

    b = gnt.call().balanceOf('0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    assert b == 0
