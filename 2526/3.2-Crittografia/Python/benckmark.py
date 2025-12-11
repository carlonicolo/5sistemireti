import time
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES, DES3, AES


def benchmark_cifrario(nome, cipher_func, key_size, data_size_mb):
    """
    Misura il tempo di cifratura di N megabyte
    """
    # Genera dati casuali
    data = get_random_bytes(data_size_mb * 1024 * 1024)
    key = get_random_bytes(key_size)
    # Cifra e misura il tempo
    start = time.time()
    cipher = cipher_func(key)
    ciphertext = cipher.encrypt(pad(data, cipher.block_size))
    elapsed = time.time() - start
    # Calcola throughput
    throughput = data_size_mb / elapsed
    print(f"{nome:12} | {elapsed:6.2f}s | {throughput:6.1f} MB/s")
    return throughput

# Test con 10 MB di dati
print("Benchmark su 10 MB di dati casuali:")
print("-" * 50)
print(f"{'Algoritmo':<12} | {'Tempo':<8} | {'Velocità':<12}")
print("-" * 50)
results = {}
results['DES'] = benchmark_cifrario(
    "DES",
    lambda k: DES.new(k, DES.MODE_ECB),
    8, 10
)
results['3DES'] = benchmark_cifrario(
    "3DES",
    lambda k: DES3.new(k, DES3.MODE_ECB),
    24, 10
)
results['AES-128'] = benchmark_cifrario(
    "AES-128",
    lambda k: AES.new(k, AES.MODE_ECB),
    16, 10
)
results['AES-256'] = benchmark_cifrario(
    "AES-256",
    lambda k: AES.new(k, AES.MODE_ECB),
    32, 10
)
print("-" * 50)
print(
    f"\nAES-128 è {results['AES-128']/results['3DES']:.1f}x più veloce di 3DES")
print(f"AES-128 è {results['AES-128']/results['DES']:.1f}x più veloce di DES")
