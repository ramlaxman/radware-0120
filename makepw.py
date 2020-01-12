#!/usr/bin/env python3

import random


def make_password_generator(s):
    def make_password(n):
        output = ''
        for i in range(n):
            output += random.choice(s)
        return output
    return make_password


make_text_pw = make_password_generator('abcde')
make_stronger_pw = make_password_generator('abcde!@#$%')

short_bad_pw = make_text_pw(5)
long_better_pw = make_stronger_pw(20)

print(short_bad_pw)
print(long_better_pw)
