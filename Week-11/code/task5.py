# Write a function called 'GetIpAddress' that will keep asking the user to enter an IPv4 Address until it is valid. The function will then return the IPv4 address as a string.

def GetIpAddress():
    while True:
        ip = input("Enter an IPv4 Address: ")
        if len(ip.split(".")) == 4:
            ipParts = ip.split(".")
            for i in ipParts:
                if (len(i) in range(1, 4)) and (int(i) in range(0, 256)):
                    continue
            if not((int(ipParts[0]) == 0) or (int(ipParts[3]) == 255)):
                return ip


print(GetIpAddress())