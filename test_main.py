from main import gen_expiry
from datetime import datetime, timedelta, time


def inc(x):
    return x + 1

# sample test
def test_answer():
    assert inc(3) == 5

def test_gen_expiry(req_exp):
  now = datetime.now()
  assert gen_expiry(now) == (now + timedelta(minutes=req_exp)).timestamp()