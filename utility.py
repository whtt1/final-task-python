def is_valid_phone(phone):
    return phone.startswith('+370') and len(phone) == 12 and phone[4:].isdigit()