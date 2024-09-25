import multiprocessing

def is_prime(n):
    """Returns True if the number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime_chunk(numbers):
    """Checks a chunk of numbers for primes."""
    return [n for n in numbers if is_prime(n)]

def find_primes_in_range(numbers, chunk_size):
    """Splits numbers into chunks and checks for primes using multiprocessing."""
    chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]
    with multiprocessing.Pool() as pool:
        result_chunks = pool.map(check_prime_chunk, chunks)
    
    primes = [prime for chunk in result_chunks for prime in chunk]  # Flatten the list
    return primes
