import time
import sqlite3
import socket
import csv
from general import *
from networking.ethernet import Ethernet
from networking.ipv4 import IPv4
from networking.icmp import ICMP
from networking.tcp import TCP
from networking.udp import UDP
from networking.pcap import Pcap
from networking.http import HTTP
import pandas as pd


db = sqlite3.connect('packet.db')
c = db.cursor()


def main():
    pcap = Pcap('capture.pcap')
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    
    t_end = time.time() + 2
    c.execute('''CREATE TABLE IF NOT EXISTS packets (sip,dip,tcp,tcp_sport,tcp_dport,tcp_fin,tcp_syn,tcp_push,tcp_ack,tcp_urg,udp,udp_sport,udp_dport,icmp)''')
    while time.time() < t_end:
        raw_data, addr = conn.recvfrom(65535)
        pcap.write(raw_data)
        eth = Ethernet(raw_data)


        if eth.proto == 8:
            ipv4 = IPv4(eth.data)

            if ipv4.target == "192.168.44.129":

                if ipv4.proto == 1:
                    icmp = ICMP(ipv4.data)
                    c.execute('''INSERT INTO packets (sip,dip,icmp) VALUES (?,?,?)''',(ipv4.src,ipv4.target,1))
                    db.commit()

                # TCP
                elif ipv4.proto == 6:
                    tcp = TCP(ipv4.data)
                    c.execute('''INSERT INTO packets (sip,dip,tcp,tcp_sport,tcp_dport,tcp_fin,tcp_syn,tcp_push,tcp_ack,tcp_urg) VALUES (?,?,?,?,?,?,?,?,?,?)''',(ipv4.src,ipv4.target,1,tcp.src_port,tcp.dest_port,tcp.flag_fin,tcp.flag_syn,tcp.flag_psh,tcp.flag_ack,tcp.flag_urg))
                    db.commit()

                # UDP
                elif ipv4.proto == 17:
                    udp = UDP(ipv4.data)
                    c.execute('''INSERT INTO packets (sip,dip,udp,udp_sport,udp_dport) VALUES (?,?,?,?,?)''',(ipv4.src,ipv4.target,1,udp.src_port, udp.dest_port))
                    db.commit()

    pcap.close()

def sniff():
    main()
    print('Staring sniffer')
    """
    c.execute('SELECT sip,dip,sum(tcp),count(DISTINCT tcp_sport),count(DISTINCT tcp_dport), sum(tcp_fin), sum(tcp_syn), sum(tcp_push), sum(tcp_ack), sum(tcp_urg), sum(udp), count(DISTINCT udp_sport), count(DISTINCT udp_dport), sum(icmp) FROM packets GROUP BY sip, dip;')
    r = c.fetchall()
    for i in r:
        j = list(i)
        cfile = "current.csv"
        with open(cfile, 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(j)
    print("completed csv")
    """

    query=pd.read_sql_query('''SELECT sip,dip,sum(tcp),count(DISTINCT tcp_sport),count(DISTINCT tcp_dport), sum(tcp_fin), sum(tcp_syn), sum(tcp_push), sum(tcp_ack), sum(tcp_urg), sum(udp), count(DISTINCT udp_sport), count(DISTINCT udp_dport), sum(icmp) FROM packets GROUP BY sip, dip;''',db)

    df=pd.DataFrame(query)
    #print(df)

    c.execute('DROP TABLE packets')
    db.commit()

    return df

#sniff()