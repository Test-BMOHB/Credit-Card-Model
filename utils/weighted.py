import random

from constants.constants import WEIGHTED_OPTIONS


def weighted_options(opt):
    choices = WEIGHTED_OPTIONS.get(opt, None)
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    up_to = 0
    for c, w in choices:
        if up_to + w >= r:
            return c
        up_to += w
    assert False, "Shouldn't get here."
