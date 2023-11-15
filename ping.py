import os
import subprocess


def ping(target_host):
    ip_name_addressess = routers_ip(target_host)
    n = len(ip_name_addressess)
    for i in range (0, len(ip_name_addressess)):
        ip_name= ip_name_addressess[i][0]
        ip_address = ip_name_addressess[i][1]
        if (ip_name == '*'):
            print(i+1, '*', '*', '*')
            continue
        ping_command = f"ping -c 3 {ip_name}"
        ping_result = subprocess.run(ping_command, shell=True, stdout=subprocess.PIPE, text=True)
        ping_lines = ping_result.stdout.splitlines()
        # print("for ip = ", ip_address)
        if (i==n-1):
            print(ping_lines)
        if len(ping_lines)>=1 and ping_lines[1] == '':
            to_be_shown = f"{i+1} {ip_name} ({ip_address}) cant be determined"
            print(to_be_shown)
        else:
            
            time = []
            check = False
            for j in range (1, 4):
                if ping_lines[j] != []:
                    words = ping_lines[j].split()
                if words != []:
                    if len(words)<6:
                        pass
                    else:
                        if words[6] == 'exceeded':
                            check = True
                        if (i != n-1):
                            time.append(words[6][5:])
                        else:
                            time.append(words[6][4:])
            if len(time)<3:
                for k in range (0, 3-len(time)):
                    time.append('*')
            if check:
                to_be_shown = f"{i+1} {ip_name} ({ip_address}) ttl exceeded using ping"
            else:
                to_be_shown = f"{i+1} {ip_name} ({ip_address}) {time[0]}ms {time[1]}ms {time[2]}ms"
            print(to_be_shown)

    

def destination(host):
    command = f"ping -c 1 {host}"
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    if lines[0] != '':
        words = lines[0].split()
    destination_ip = words[2][1:-2]
    return destination_ip



def routers_ip(host, count=20):
    ip_name_addresses  = []
    destination_ip = destination(host)
    for i in range (1, count):
        # print("i = ", i)
        command = f"ping -c 1 -t {i} {host}"
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, text=True)
        lines = result.stdout.splitlines()
        if len(lines)>=1 and lines[1] != '':
            words = lines[1].split()
        else:
            ip_name_addresses.append(['*', '*'])
            continue
        if words == []:
            ip_name_addresses.append(['*', '*'])
        elif words[1] == 'bytes':
            ip_name_addresses.append([host, destination_ip])
            break
        else:
            show_name = words[1]
            if (i != 1):
                show_ip = words[2]
            else:
                show_ip = words[1]
            ip_name_addresses.append([show_name, show_ip])
    return ip_name_addresses

if __name__ == "__main__":
    # target_host = "google.com"  # Change this to the desired target host
    target_host = input("Enter your target host : ")
    # routers_ip(target_host)
    ping(target_host)
