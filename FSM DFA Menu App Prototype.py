# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 19:42:17 2021

@author: ASUS
"""

from automata.fa.dfa import DFA
dfa = DFA(
    states={'isClose', 'offlineMenu', 'onlineMenu', 'otherDeliveryOptions', 'onSpot', 'book', 'pickUp', 'delivery', 'processFoodBefore', 'processFoodAfter', 'offlinePaymentAfter', 'onlinePaymentBefore', 'onlinePaymentAfter', 'done'},
    input_symbols={'0', '1'},
    transitions={
        'isClose': {'0': 'onlineMenu', '1': 'offlineMenu'},
        'offlineMenu': {'0': 'onSpot', '1': 'otherDeliveryOptions'},
        'onlineMenu': {'0': 'book', '1': 'otherDeliveryOptions'},
        'otherDeliveryOptions' : {'0': 'pickUp', '1': 'delivery'},
        'onSpot': {'0': 'processFoodBefore', '1': 'processFoodBefore'},
        'book': {'0': 'onlinePaymentBefore', '1': 'onlinePaymentBefore'},
        'pickUp': {'0': 'onlinePaymentBefore', '1': 'onlinePaymentBefore'},
        'delivery': {'0': 'onlinePaymentBefore', '1': 'onlinePaymentBefore'},
        'processFoodBefore': {'0': 'offlinePaymentAfter', '1': 'onlinePaymentAfter'},
        'processFoodAfter': {'0': 'done', '1': 'done'},
        'offlinePaymentAfter': {'0': 'done', '1': 'done'},
        'onlinePaymentBefore': {'0': 'processFoodAfter', '1': 'processFoodAfter'},
        'onlinePaymentAfter': {'0': 'done', '1': 'done'},
        'done' : {'0': 'done', '1': 'done'}
    },
    initial_state='isClose',
    final_states={'done'}
)

input = '10000'

if dfa.accepts_input(input):
    for i in dfa.read_input_stepwise(input):
        print(i)
    print('Input accepted')
else:
    try:
        for i in dfa.read_input_stepwise(input):
            print(i)
    except:
        print('Input rejected')