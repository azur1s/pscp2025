"""a"""
def validate_octet(octet):
    """a"""
    if " " in octet or not octet.isdigit():
        return False
    if not 0 <= int(octet) <= 255:
        return False
    return True

def validate_ip(ip):
    """a"""
    if len(ip) != 4:
        return False
    for octet in ip:
        if not validate_octet(octet):
            return False
    return True

input_ip = list(input().split("."))

if validate_ip(input_ip):
    print(".".join(map(lambda x: str(int(x)), input_ip)))
else:
    print("Invalid IPv4 address")
