import scapy.all as scapy
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Network Range")
	parser.add_argument("-r","--range",help="speficy a network range",dest="ip")
	args=parser.parse_args()

	if args.ip != None:
		print(args)
		arp_requestt= scapy.ARP(pdst=args.ip)
		broadcst = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
		arp_request = broadcst/arp_requestt
		#send and receive response
		answer=scapy.srp(arp_request,timeout=1,verbose=False)[0] # or answer,unnswer =
		print(__name__)
		print("-------------------------------------------")
		print("IPMAC\t\tMac address\t\tType")
		print("---------------------------------------------")
		clients_list = []
		for item in answer:
			client_dict = {'mac':item.answer.hwsrc,'ip':item.answer.psrc}
			clients_list.append(client_dict)
			print(item.answer.psrc,"\t\t",item.answer.hwsrc,"\t\t",item.answer.type)