#register & login
import os
from getpass import getpass
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

pepper=os.environ.get("App_PEPPER","change_this_to_a_secret")

ph=PasswordHasher(
    time_cost=3,
    memory_cost=64*1024,
    parallelism=4,
    hash_len=32,
    salt_len=16

)

users={}

def strongpass(p):
    if len(p)<12:return False
    has_u=any(c.isupper() for c in p)
    has_l=any(c.islower() for c in p)
    has_d=any(c.isdigit() for c in p)
    has_s=any(not c.isalnum() for c in p) # has special char
    return has_u and has_l and has_d and has_s

def hash_pwd(p):
    return ph.hash(p+pepper)

def verify_pass(stored_hash,p):
    try:
        ph.verify(stored_hash,p+pepper)
        return True
    except VerifyMismatchError:
        return False

def register(username,password):
    if username in users:
        return False,"user exists"
    if not strongpass(password):
        return False, "weak password"
    users[username]=hash_pwd(password)
    return True,"registered"

def login(username,password):
    h=users.get(username)
    if h is None:
        fake=ph.hash('x'+ pepper)
        try:
            ph.verify(fake,password+pepper)
        except:
            pass
        return False, "Invalid"
    if verify_pass(h,password):
        return True,"logged in"
    return False,"invalid"


if __name__=="__main__":
    u=input("username:")
    p=getpass("password:")
    ok,msg=register(u,p)
    print(msg)
    
    print("\nlogin")
    u2=input("username:")
    p2=getpass("password:")
    ok,msg=login(u2,p2)
    print(msg)