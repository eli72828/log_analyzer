def get_external_ips(data):
    external_ip_list = [line[1] for line in data
                        if not (line[1].startswith('192.168') or line[1].startswith('10.'))]
    return external_ip_list

def filter_sensitive_ports(data):
    sensitive_ports = ('22', '23', '3389')
    sensitive_ports_list = filter(lambda line: line[3] in sensitive_ports, data)
    return list(sensitive_ports_list)
