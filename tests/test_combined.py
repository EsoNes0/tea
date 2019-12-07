# -*- coding: utf-8 -*-
"""Basic tests for tiny encryption algorithm encryption"""


import tea.combined


def test_encryption(capsys):
    """Testing encryption algorithm"""

    tea.combined.main('encrypt', '90001C55', '1234ABCD', 'FEDCBA98',
                      'E2468AC0', 'A0000009', '8000006B')
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


def test_decryption(capsys):
    """Testing decryption algorithm"""

    tea.combined.main("decrypt", "90001C55", "1234ABCD", "FEDCBA98",
                      "E2468AC0", "B72599B2", "CF8E5A4C")
    out, err = capsys.readouterr()

    assert "DeltaOne = 0x11111111\n" in out
    assert "DeltaTwo = 0x22222222\n" in out
    assert "L[2] = 0xb72599b2\n" in out
    assert "R[2] = 0xcf8e5a4c\n" in out
    assert "L[1] = 0x8000006b\n" in out
    assert "R[1] = 0xb72599b2\n" in out
    assert "L[0] = 0xa0000009\n" in out
    assert "R[0] = 0x8000006b\n" in out
    assert err == ""
