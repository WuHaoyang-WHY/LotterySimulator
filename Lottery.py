#!/usr/bin/python
# -*- coding:utf-8 -*-

import random


def lottery_generator():

    red_ball = random.sample(range(1, 34), 6)
    blue_ball = random.sample(range(1, 17), 1)

    return red_ball, blue_ball


def list_match(list1, list2):

    temp = [x for x in list1 if x in list2]

    return len(temp)


def game_rule(red, blue):

    if red == 6 and blue == 1:
        award = 5000000
        prize = 'first_prize'
    elif red == 6 and blue == 0:
        award = 1500000
        prize = 'second_prize'
    elif red == 5 and blue == 1:
        award = 3000
        prize = 'third_prize'
    elif (red == 5 and blue == 0) or (red == 4 and blue == 1):
        award = 200
        prize = 'fourth_prize'
    elif (red == 4 and blue ==0) or (red == 3 and blue == 1):
        award = 10
        prize = 'fifth_prize'
    elif blue == 1:
        award = 5
        prize = 'sixth_prize'
    else:
        award = 0
        prize = 'no_prize'

    return award, prize


def millionaire(init_money=1000000):

    track_record = [init_money]
    counter = {'first_prize': 0, 'second_prize': 0, 'third_prize': 0, 'fourth_prize': 0,
               'fifth_prize': 0, 'sixth_prize': 0, 'no_prize': 0, 'participation_times': 0}

    while init_money > 0:
        init_money -= 2
        prize_red, prize_blue = lottery_generator()
        guess_red, guess_blue = lottery_generator()

        match_red = list_match(prize_red, guess_red)
        match_blue = list_match(prize_blue, guess_blue)

        award, prize = game_rule(match_red, match_blue)
        init_money += award
        counter[prize] += 1
        counter['participation_times'] += 1

        track_record.append(init_money)

    print('The millionaire bought ' + str(counter['participation_times']) + ' lottery')
    print('He won ' + str(counter['first_prize']) + ' first prize')
    print(str(counter['second_prize']) + ' second prize')
    print(str(counter['third_prize']) + ' third prize')
    print(str(counter['fourth_prize']) + ' fourth prize')
    print(str(counter['fifth_prize']) + ' fifth prize')
    print(str(counter['sixth_prize']) + ' sixth prize')


