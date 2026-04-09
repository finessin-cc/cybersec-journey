import hashlib

def identify_hash(hash_string):
    length = len(hash_string)
    
    if length == 32:
        return "MD5"
    elif length == 40:
        return "SHA1"
    elif length == 64:
        return "SHA256"
    elif length == 128:
        return "SHA512"
    else:
        return "Unknown"

def crack_hash(target_hash, wordlist):
    print(f"\nTarget hash: {target_hash}")
    print(f"Trying {len(wordlist)} passwords...")
    print("─" * 40)
    
    hash_type = identify_hash(target_hash)
    print(f"Detected: {hash_type}")
    print("─" * 40)
    
    for password in wordlist:
        # Try MD5
        md5 = hashlib.md5(password.encode()).hexdigest()
        if md5 == target_hash:
            print(f"[CRACKED] {target_hash} → {password}")
            return password
            
        # Try SHA1
        sha1 = hashlib.sha1(password.encode()).hexdigest()
        if sha1 == target_hash:
            print(f"[CRACKED] {target_hash} → {password}")
            return password
            
        # Try SHA256
        sha256 = hashlib.sha256(password.encode()).hexdigest()
        if sha256 == target_hash:
            print(f"[CRACKED] {target_hash} → {password}")
            return password
    
    print(f"[FAILED]  Hash not found in wordlist")
    return None

# Common passwords wordlist
wordlist = [
    "password", "123456", "password123",
    "admin", "letmein", "qwerty",
    "monkey", "dragon", "master",
    "sunshine", "princess", "welcome",
    "shadow", "superman", "michael"
]

# Test hashes — try to crack these:
test_hashes = [
    "482c811da5d5b4bc6d497ffa98491e38",
    "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8",
    "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
]

for hash_val in test_hashes:
    crack_hash(hash_val, wordlist)
    print()