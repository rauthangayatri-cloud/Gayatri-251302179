import secrets
import string


# ---------------- PASSWORD GENERATOR ----------------
def generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_similar):
    if length < 8:
        raise ValueError("Password length should be at least 8.")

    characters = ""
    guaranteed_chars = []

    # Similar characters to exclude
    similar_chars = "l1I0O"

    def filter_chars(char_set):
        if exclude_similar:
            return ''.join(c for c in char_set if c not in similar_chars)
        return char_set

    if use_upper:
        upper = filter_chars(string.ascii_uppercase)
        characters += upper
        guaranteed_chars.append(secrets.choice(upper))

    if use_lower:
        lower = filter_chars(string.ascii_lowercase)
        characters += lower
        guaranteed_chars.append(secrets.choice(lower))

    if use_digits:
        digits = filter_chars(string.digits)
        characters += digits
        guaranteed_chars.append(secrets.choice(digits))

    if use_symbols:
        symbols = string.punctuation
        characters += symbols
        guaranteed_chars.append(secrets.choice(symbols))

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Fill remaining characters
    remaining_length = length - len(guaranteed_chars)
    password_chars = guaranteed_chars + [
        secrets.choice(characters) for _ in range(remaining_length)
    ]

    # Shuffle securely
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)


# ---------------- PASSWORD STRENGTH CHECK ----------------
def check_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (min 8 recommended)")

    # Character variety
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Pattern checks
    if password.lower() in ["password", "123456", "qwerty"]:
        score = 0
        feedback.append("Very common password (extremely unsafe)")

    if len(set(password)) < len(password) / 2:
        feedback.append("Too many repeated characters")

    if password.isdigit() or password.isalpha():
        feedback.append("Use a mix of letters, numbers, and symbols")

    # Final rating
    if score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback

def generate_multiple(count, *args):
    passwords = set()

    while len(passwords) < count:
        pwd = generate_password(*args)
        passwords.add(pwd)

    return list(passwords)
# ---------------- MAIN PROGRAM ----------------
def main():
    print("\n=== Secure Password Generator ===\n")

    try:
        length = int(input("Enter password length (min 8): "))
        count = int(input("How many passwords to generate: "))

        if count <= 0:
            raise ValueError("Count must be greater than 0.")

        upper = input("Include uppercase? (y/n): ").lower() == 'y'
        lower = input("Include lowercase? (y/n): ").lower() == 'y'
        digits = input("Include numbers? (y/n): ").lower() == 'y'
        symbols = input("Include symbols? (y/n): ").lower() == 'y'
        exclude_similar = input("Exclude similar characters (l,1,O,0)? (y/n): ").lower() == 'y'

        passwords = generate_multiple(
            count,
            length,
            upper,
            lower,
            digits,
            symbols,
            exclude_similar
        )

        print("\nGenerated Passwords:\n")

        for i, pwd in enumerate(passwords, 1):
            strength, feedback = check_strength(pwd)

            print(f"{i}. {pwd}")
            print(f"   Strength: {strength}")

            if feedback:
                print("   Suggestions:")
                for f in feedback:
                    print(f"   - {f}")
            print()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
