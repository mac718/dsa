def canConstruct(ransomNote: str, magazine: str) -> bool:
    mag_hash = {}
    ran_hash = {}

    for c in magazine:
        if c in mag_hash:
            mag_hash[c] += 1
        else:
            mag_hash[c] = 1

    for c in ransomNote:
        if c in ran_hash:
            ran_hash[c] += 1
        else:
            ran_hash[c] = 1

    for c in ran_hash:
        if c not in mag_hash or mag_hash[c] < ran_hash[c]:
            return False

    return True