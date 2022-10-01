import random
import string
import asyncio

def get_pass(letters_count, digits_count, sym_count):
    letters = ''.join(random.choice(string.ascii_letters) for _ in range(letters_count))
    digits = ''.join(random.choice(string.digits) for _ in range(digits_count))
    sym = ''.join(random.choice(string.punctuation) for _ in range(sym_count))
    sample_list = list(letters + digits + sym)
    random.shuffle(sample_list)
    return ''.join(sample_list)

async def main():
    lt = int(input("Enter the number of letters: "))
    dt = int(input("Enter the number of digits: "))
    sy = int(input("Enter the number of symbols: "))
    password = get_pass(lt, dt, sy)
    print("Generated Password:", password)

asyncio.run(main())