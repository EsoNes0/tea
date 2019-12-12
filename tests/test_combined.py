# -*- coding: utf-8 -*-
"""Basic tests for tiny encryption algorithm encryption"""


import tea.combined

DELTA_ONE = "DeltaOne = 0x11111111\n"
DELTA_TWO = "DeltaTwo = 0x22222222\n"
L_0 = "L[0] = 0xa0000009\n"
R_0 = "R[0] = 0x8000006b\n"
L_1 = "L[1] = 0x8000006b\n"
R_1 = "R[1] = 0xb72599b2\n"
L_2 = "L[2] = 0xb72599b2\n"
R_2 = "R[2] = 0xcf8e5a4c\n"

L_0_2 = "L[0] = 0x6d792074\n"
R_0_2 = "R[0] = 0x6578740a\n"
L_1_2 = "L[1] = 0x6578740a\n"
R_1_2 = "R[1] = 0xeee21246\n"
L_2_2 = "L[2] = 0xeee21246\n"
R_2_2 = "R[2] = 0xbf121dc5\n"


def test_encryption(capsys):
    """Testing encryption algorithm"""

    tea.combined.main('encrypt', '90001C55', '1234ABCD', 'FEDCBA98',
                      'E2468AC0', 'A0000009', '8000006B')
    out, err = capsys.readouterr()
    assert DELTA_ONE in out
    assert DELTA_TWO in out
    assert L_0 in out
    assert R_0 in out
    assert L_1 in out
    assert R_1 in out
    assert L_2 in out
    assert R_2 in out
    assert err == ""


def test_decryption(capsys):
    """Testing decryption algorithm"""

    tea.combined.main("decrypt", "90001C55", "1234ABCD", "FEDCBA98",
                      "E2468AC0", "B72599B2", "CF8E5A4C")
    out, err = capsys.readouterr()

    assert DELTA_ONE in out
    assert DELTA_TWO in out
    assert L_2 in out
    assert R_2 in out
    assert L_1 in out
    assert R_1 in out
    assert L_0 in out
    assert R_0 in out
    assert err == ""


def test_encryption_2(capsys):
    """Testing encryption algorithm"""

    tea.combined.main('encrypt', '9ff579e5', 'fd720aac', '36629fc9',
                      '64a74968', '6d792074', '6578740a')
    out, err = capsys.readouterr()
    assert DELTA_ONE in out
    assert DELTA_TWO in out
    assert L_0_2 in out
    assert R_0_2 in out
    assert L_1_2 in out
    assert R_1_2 in out
    assert L_2_2 in out
    assert R_2_2 in out
    assert err == ""


def test_decryption_2(capsys):
    """Testing decryption algorithm"""

    tea.combined.main("decrypt", "9ff579e5", "fd720aac", "36629fc9",
                      "64a74968", "eee21246", "bf121dc5")
    out, err = capsys.readouterr()

    assert DELTA_ONE in out
    assert DELTA_TWO in out
    assert L_2_2 in out
    assert R_2_2 in out
    assert L_1_2 in out
    assert R_1_2 in out
    assert L_0_2 in out
    assert R_0_2 in out
    assert err == ""


def test_set_variables_encrypt_with_input(capsys, mocker):
    """Testing set variables method encrypt"""
    _args = []
    mocked_input = mocker.patch('builtins.input')
    mocked_input.side_effect = [1, '90001C55', '1234ABCD', 'FEDCBA98',
                                'E2468AC0', 'A0000009', '8000006B']
    tea.combined.set_variables(_args)
    captured = capsys.readouterr()
    assert DELTA_ONE in captured.out
    assert DELTA_TWO in captured.out
    assert L_0 in captured.out
    assert R_0 in captured.out
    assert L_1 in captured.out
    assert R_1 in captured.out
    assert R_2 in captured.out
    assert R_2 in captured.out
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
    assert DELTA_ONE in captured.out
    assert DELTA_TWO in captured.out
    assert L_2_2 in captured.out
    assert R_2_2 in captured.out
    assert L_1_2 in captured.out
    assert R_1_2 in captured.out
    assert L_0_2 in captured.out
    assert R_0_2 in captured.out
    assert captured.err == ""
    assert mocked_input.call_count == 7


def test_set_variables_encrypt_with_args(capsys):
    """Testing set variables method encrypt with args"""
    _args = ["encrypt", '90001C55', '1234ABCD', 'FEDCBA98',
             'E2468AC0', 'A0000009', '8000006B']
    tea.combined.set_variables(_args)
    captured = capsys.readouterr()
    assert DELTA_ONE in captured.out
    assert DELTA_TWO in captured.out
    assert L_0 in captured.out
    assert R_0 in captured.out
    assert L_1 in captured.out
    assert R_1 in captured.out
    assert L_2 in captured.out
    assert R_2 in captured.out
    assert captured.err == ""


def test_set_variables_decrypt_with_args(capsys):
    """Testing set variables method decrypt with args"""
    _args = ["decrypt", "9ff579e5", "fd720aac", "36629fc9",
             "64a74968", "eee21246", "bf121dc5"]
    tea.combined.set_variables(_args)
    captured = capsys.readouterr()
    assert DELTA_ONE in captured.out
    assert DELTA_TWO in captured.out
    assert L_2_2 in captured.out
    assert R_2_2 in captured.out
    assert L_1_2 in captured.out
    assert R_1_2 in captured.out
    assert L_0_2 in captured.out
    assert R_0_2 in captured.out
    assert captured.err == ""
