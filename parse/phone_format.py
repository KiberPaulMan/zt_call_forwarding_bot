def get_phone_format(phone: str) -> str:
    """
    Gets a phone number in the format: 7XXXXXXXXXX
    Returns in the format: +7 (XXX) XXX-XX-XX
    """
    return f'+{phone[0]} ({phone[1:4]}) {phone[4:7]}-{phone[7:9]}-{phone[9:]}'
