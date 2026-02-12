def get_external_ips(data):
    external_ip_list = [line[1] for line in data
                        if not (line[1].startswith('192.168') or line[1].startswith('10.'))]
    return external_ip_list
