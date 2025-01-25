def verify_aotp(user_input, expected_aotp):
    return user_input == expected_aotp

if __name__ == "__main__":
    expected_aotp = "AbCdEf"
    user_input = input("Enter AOTP: ")
    if verify_aotp(user_input, expected_aotp):
        print("AOTP Verified!")
    else:
        print("Invalid AOTP.")
