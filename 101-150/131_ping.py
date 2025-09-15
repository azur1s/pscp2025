"""a"""

# 0 ping www.google.com
# 1 
# 2 Pinging www.google.com [2404:6800:4001:806::2004] with 32 bytes of data:
#   Reply from 2404:6800:4001:806::2004: time=27ms
#   Reply from 157.240.10.35: bytes=32 time=24ms TTL=51
#   Request timed out.
#   General failure.

s = [input() for _ in range(7)]
replies = s[2:7]

def parse_reply(str):
    """a"""
    parts = str.split()
    if "time=" in str:
        time_part = list(filter(lambda x: "time=" in x, parts))[0]
        time_value = time_part.split("=")[1]
        if time_value.endswith("ms"):
            time_value = time_value[:-2]
        return int(time_value)
    elif "time<" in str:
        return 0
    return None

ip = s[2].split()[2].strip("[]")
print(f"Ping statistics for {ip}:")

recv = list(filter(lambda x: "Reply from" in x, replies))
recv_ms = list(map(parse_reply, recv))
percent_loss = (4 - len(recv)) * 100 // 4
print(f"    Packets: Sent = 4, Received = {len(recv)}, Lost = {4 - len(recv)} ({percent_loss}% loss),")
if recv_ms:
    print("Approximate round trip times in milli-seconds:")
    min_ms = min(recv_ms)
    max_ms = max(recv_ms)
    avg_ms = sum(recv_ms) // len(recv_ms)
    print(f"    Minimum = {min_ms}ms, Maximum = {max_ms}ms, Average = {avg_ms}ms")
