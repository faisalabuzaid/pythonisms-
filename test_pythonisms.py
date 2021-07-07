from hashtable import HashMap
import pytest


def test_setitem():
    test = HashMap()
    test['Key']='Value'
    assert test == ['Key', 'Value']

def test_getitem():
    test = HashMap()
    test['Key']='Value'
    value = test['Key']
    assert value == 'Value'

def test_contains():
    test = HashMap()
    test['Key']='Value'
    if 'Key' in test:
        value = test['Key']
    assert value == 'Value'