# -*- coding: utf-8 -*-
"""Basic tests for tiny encryption algorithm encryption"""


import tea.encryption


def test_encryption(capsys):
    """Testing encryption algorithm"""

    tea.encryption.main('90001C55', '1234ABCD', 'FEDCBA98', 'E2468AC0',
                        'A0000009', '8000006B')
    out, err = capsys.readouterr()
    assert "DeltaOne = 0x11111111\n" in out
    assert "DeltaTwo = 0x22222222\n" in out
    assert "L[0] = 0xa0000009\n" in out
    assert "R[0] = 0x8000006b\n" in out
    assert "L[1] = 0x8000006b\n" in out
    assert "R[1] = 0xb72599b2\n" in out
    assert "L[2] = 0xb72599b2\n" in out
    assert "R[2] = 0xcf8e5a4c\n" in out
    assert err == ""
