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


def test_encryption_2(capsys):
    """Testing encryption algorithm"""

    tea.combined.main('encrypt', '9ff579e5', 'fd720aac', '36629fc9',
                      '64a74968', '6d792074', '6578740a')
    out, err = capsys.readouterr()
    assert "DeltaOne = 0x11111111\n" in out
    assert "DeltaTwo = 0x22222222\n" in out
    assert "L[0] = 0x6d792074\n" in out
    assert "R[0] = 0x6578740a\n" in out
    assert "L[1] = 0x6578740a\n" in out
    assert "R[1] = 0xeee21246\n" in out
    assert "L[2] = 0xeee21246\n" in out
    assert "R[2] = 0xbf121dc5\n" in out
    assert err == ""


def test_decryption_2(capsys):
    """Testing decryption algorithm"""

    tea.combined.main("decrypt", "9ff579e5", "fd720aac", "36629fc9",
                      "64a74968", "eee21246", "bf121dc5")
    out, err = capsys.readouterr()

    assert "DeltaOne = 0x11111111\n" in out
    assert "DeltaTwo = 0x22222222\n" in out
    assert "L[2] = 0xeee21246\n" in out
    assert "R[2] = 0xbf121dc5\n" in out
    assert "L[1] = 0x6578740a\n" in out
    assert "R[1] = 0xeee21246\n" in out
    assert "L[0] = 0x6d792074\n" in out
    assert "R[0] = 0x6578740a\n" in out
    assert err == ""


def test_set_variables_encrypt_with_input(capsys, mocker):
    """Testing set variables method encrypt"""
    _args = []
    mocked_input = mocker.patch('builtins.input')
    mocked_input.side_effect = [1, '90001C55', '1234ABCD', 'FEDCBA98',
                                'E2468AC0', 'A0000009', '8000006B']
    tea.combined.set_variables(_args)
    captured = capsys.readouterr()
    assert "DeltaOne = 0x11111111\n" in captured.out
    assert "DeltaTwo = 0x22222222\n" in captured.out
    assert "L[0] = 0xa0000009\n" in captured.out
    assert "R[0] = 0x8000006b\n" in captured.out
    assert "L[1] = 0x8000006b\n" in captured.out
    assert "R[1] = 0xb72599b2\n" in captured.out
    assert "L[2] = 0xb72599b2\n" in captured.out
    assert "R[2] = 0xcf8e5a4c\n" in captured.out
    assert captured.err == ""
    assert mocked_input.call_count == 7


def test_set_variables_decrypt_with_input(capsys, mocker):
    """Testing set variables method decrypt"""
    _args = []
    mocked_input = mocker.patch('builtins.input')
    mocked_input.side_effect = [0, "9ff579e5", "fd720aac", "36629fc9",
                                "64a74968", "eee21246", "bf121dc5"]
    tea.combined.set_variables(_args)
    captured = capsys.readouterr()
    assert "DeltaOne = 0x11111111\n" in captured.out
    assert "DeltaTwo = 0x22222222\n" in captured.out
    assert "L[2] = 0xeee21246\n" in captured.out
    assert "R[2] = 0xbf121dc5\n" in captured.out
    assert "L[1] = 0x6578740a\n" in captured.out
    assert "R[1] = 0xeee21246\n" in captured.out
    assert "L[0] = 0x6d792074\n" in captured.out
    assert "R[0] = 0x6578740a\n" in captured.out
    assert captured.err == ""
    assert mocked_input.call_count == 7


def test_set_variables_encrypt_with_args(capsys):
    """Testing set variables method encrypt with args"""
    _args = ["encrypt", '90001C55', '1234ABCD', 'FEDCBA98',
             'E2468AC0', 'A0000009', '8000006B']
    tea.combined.set_variables(_args)
    captured = capsys.readouterr()
    assert "DeltaOne = 0x11111111\n" in captured.out
    assert "DeltaTwo = 0x22222222\n" in captured.out
    assert "L[0] = 0xa0000009\n" in captured.out
    assert "R[0] = 0x8000006b\n" in captured.out
    assert "L[1] = 0x8000006b\n" in captured.out
    assert "R[1] = 0xb72599b2\n" in captured.out
    assert "L[2] = 0xb72599b2\n" in captured.out
    assert "R[2] = 0xcf8e5a4c\n" in captured.out
    assert captured.err == ""


def test_set_variables_decrypt_with_args(capsys):
    """Testing set variables method decrypt with args"""
    _args = ["decrypt", "9ff579e5", "fd720aac", "36629fc9",
             "64a74968", "eee21246", "bf121dc5"]
    tea.combined.set_variables(_args)
    captured = capsys.readouterr()
    assert "DeltaOne = 0x11111111\n" in captured.out
    assert "DeltaTwo = 0x22222222\n" in captured.out
    assert "L[2] = 0xeee21246\n" in captured.out
    assert "R[2] = 0xbf121dc5\n" in captured.out
    assert "L[1] = 0x6578740a\n" in captured.out
    assert "R[1] = 0xeee21246\n" in captured.out
    assert "L[0] = 0x6d792074\n" in captured.out
    assert "R[0] = 0x6578740a\n" in captured.out
    assert captured.err == ""
