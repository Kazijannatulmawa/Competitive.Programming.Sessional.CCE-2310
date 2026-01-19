import sys

# Set a large prime number for the modulus (M) to reduce collisions
MODULUS = 10**9 + 7
# Set a prime number for the base (P)
BASE_P = 31

def custom_string_hash(input_string):
    """
    Generates a simple hash value for a given string using a weighted sum method.
    """
    hash_value = 0
    power = 1
    for char in input_string:
        # Get the Unicode value of the character and add to the sum
        hash_value = (hash_value + (ord(char) * power)) % MODULUS
        # Update the power for the next character
        power = (power * BASE_P) % MODULUS
    return hash_value

# --- Example Usage and Output ---
# You would use a hash table size for practical application
hash_table_size = 100

data_items = ["apple", "banana", "cherry", "date", "apple"]

print(f"Hash Table Size: {hash_table_size}\n")
print(f"{'String':<10} | {'Raw Hash':<20} | {'Table Index':<15}")
print("-" * 50)

for item in data_items:
    raw_hash = custom_string_hash(item)
    # The final index in a specific-sized hash table is modulo of the table size
    table_index = raw_hash % hash_table_size
    print(f"{item:<10} | {raw_hash:<20} | {table_index:<15}")

# Example output to demonstrate collision for "date" and a hypothetical input
# (Note: actual collisions will depend on the input set and hash function)
print("\nExample of a potential collision (different inputs might have same index):")
item1 = "date"
item2 = "earl" # Fictional collision example
index1 = custom_string_hash(item1) % hash_table_size
index2 = custom_string_hash(item2) % hash_table_size
print(f"'{item1}' index: {index1}, '{item2}' index: {index2}")
