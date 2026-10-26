def validate_student(name, email):
    if not name.strip():
        return False
    if "@" not in email or "." not in email:
        return False
    return True


def test_student_validation():
    assert validate_student("Akshita", "student@example.com")
    assert not validate_student("", "student@example.com")
    assert not validate_student("Akshita", "invalid-email")


if __name__ == "__main__":
    test_student_validation()
    print("All student validation tests passed!")
