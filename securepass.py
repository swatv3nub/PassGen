import random
import string
import asyncio

def get_pass(letters_count, digits_count, sym_count):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))
    sym = ''.join((random.choice(string.punctuation) for i in range(sym_count)))
    sample_list = list(letters + digits + sym)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    print("Password: ", final_string)

async def main():
    lt = int(input("Enter the number of letters: "))
    dt = int(input("Enter the number of digits: "))
    sy = int(input("Enter the number of symbols: "))
    get_pass(lt, dt, sy)

asyncio.run(main())