# -*- coding: utf-8 -*-
"""
CS3750-001
Homework 2
Python
Larsen Close & Greg Dews

Decryption - TEA (Tiny Encryption Algorithm)
Input:  Keyboard (kb)
Output: Standard out (print)
        Will have system out dumped into text file via cs3750a server command

Todo: test, refactor
"""

from ctypes import c_uint32
import sys

DELTA_ONE = c_uint32(int("0x11111111", 16)).value
DELTA_TWO = c_uint32(int("0x22222222", 16)).value
SUM_DELTA = c_uint32(0).value
K = [0, 1, 2, 3]

L_LIST = [0, 1, 2]
R_LIST = [0, 1, 2]


def main(*kwargs):
    """Tiny encryption algorithm decrypt method"""
    _args = []
    if sys.argv:
        for arg in sys.argv:
            _args.append(str(arg).strip("'"))

    if kwargs is not None:
        for kwarg in kwargs:
            _args.append(str(kwarg).strip("'"))

    if len(_args) >= 7:
        k_zero = "0x" + _args[1]
        k_one = "0x" + _args[2]
        k_two = "0x" + _args[3]
        k_three = "0x" + _args[4]
        l_two = "0x" + _args[5]
        r_two = "0x" + _args[6]

    else:
        k_zero = "0x" + \
            input("Please input K[0] in Hex String (without “0x”): ")
        k_one = "0x" + input("Please input K[1] in Hex String (without “0x”): ")
        k_two = "0x" + input("Please input K[2] in Hex String (without “0x”): ")
        k_three = "0x" + \
            input("Please input K[3] in Hex String (without “0x”): ")
        l_two = "0x" + \
            input("\nPlease input L[2] in Hex String (without “0x”): ")
        r_two = "0x" + \
            input("Please input R[2] in Hex String (without “0x”): ")


    def convert_ctype():
        "converts inputed values into ctypes"
        K[0] = c_uint32(int(k_zero, 16)).value
        K[1] = c_uint32(int(k_one, 16)).value
        K[2] = c_uint32(int(k_two, 16)).value
        K[3] = c_uint32(int(k_three, 16)).value
        L_LIST[2] = c_uint32(int(l_two, 16)).value
        R_LIST[2] = c_uint32(int(r_two, 16)).value

    convert_ctype()

# Reverse from L[2] first
    def reverse_from_l2():
        reverse_one_left4 = c_uint32(L_LIST[2] << 4).value
        reverse_one_left4_add = c_uint32(reverse_one_left4 + K[2]).value

        reverse_one_right5 = c_uint32(L_LIST[2] >> 5).value
        reverse_one_right5_add = c_uint32(reverse_one_right5 + K[3]).value

        add_delta_two = c_uint32(SUM_DELTA + DELTA_TWO).value
        reverse_one_add_delta_two = c_uint32(L_LIST[2] + add_delta_two).value

        xor_first = c_uint32(reverse_one_left4_add ^ reverse_one_right5_add).value
        xor_second = c_uint32(xor_first ^ reverse_one_add_delta_two).value

        R_LIST[0] = c_uint32(R_LIST[2] - xor_second).value

    reverse_from_l2()


# second step from R[0] and L[2]
    def second_step_r0_l2():

        reverse_two_left4 = c_uint32(R_LIST[0] << 4).value
        reverse_two_left4_add = c_uint32(reverse_two_left4 + K[0]).value

        reverse_two_right5 = c_uint32(R_LIST[0] >> 5).value
        reverse_two_right5_add = c_uint32(reverse_two_right5 + K[1]).value

        add_delta_one = c_uint32(SUM_DELTA + DELTA_ONE).value
        reverse_two_add_delta_two = c_uint32(R_LIST[0] + add_delta_one).value

        reverse_two_xor_first = c_uint32(
            reverse_two_left4_add ^ reverse_two_right5_add).value
        reverse_two_xor_second = c_uint32(
            reverse_two_xor_first ^ reverse_two_add_delta_two).value

        L_LIST[0] = c_uint32(L_LIST[2] - reverse_two_xor_second).value

    second_step_r0_l2()

    def print_result_reverse():
        print("\nDeltaOne = " + hex(DELTA_ONE).rstrip("L"))
        print("DeltaTwo = " + hex(DELTA_TWO).rstrip("L"))

        print("\nL[2] = " + hex(L_LIST[2]).rstrip("L"))
        print("R[2] = " + hex(R_LIST[2]).rstrip("L"))

        print("\nL[1] = " + hex(R_LIST[0]).rstrip("L"))
        print("R[1] = " + hex(L_LIST[2]).rstrip("L"))

        print("\nL[0] = " + hex(L_LIST[0]).rstrip("L"))
        print("R[0] = " + hex(R_LIST[0]).rstrip("L"))

    print_result_reverse()

if __name__ == '__main__':
    main()
