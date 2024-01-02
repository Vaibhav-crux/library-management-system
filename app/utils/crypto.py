import string, random, hashlib


def otp6():
    return random.randint(100000, 999999)


def token_alphanum(size):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))


def token_alphanum8():
    return token_alphanum(8)


def token_alphanum16():
    return token_alphanum(16)


def token_alphanum36():
    return token_alphanum(36)


def create_hash(token: str):
    salt = 'ps:'
    token = (salt+token).encode('utf-8')
    return hashlib.md5(token).hexdigest()
