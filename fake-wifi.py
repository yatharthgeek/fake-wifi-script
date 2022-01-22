
import os

#main menu
while 1==1:
    print("[-] MAIN MENU [-]")
    print("")

    print("[1] CREATE FAKE NETWORK ")
    print("[2] EXIT")
    print("[3] INSTALL PACKAGES REQUIRED")
    print("")


    bash = input("( fake-wifi/shell ) : ")
    if bash==1:
        os.system("ifconfig")
        print("")
        adap = input("( fake-wifi/shell/adpater ) : ")
        print("Network Saved")
        code = "airmon-ng start "+adap
        os.system(code)
        print("")
        adapfile= input("( fake-wifi/shell/adpater/file ) : ")
        code2 = "mdk3 "+adap+"mon b -c 1 -f "+adapfile
        print("Press Ctrl + C to Exit Brodcast")
        os.system(code2)
        code3 = "airmon-ng stop "+adap+"mon"
        os.system(code3)

    if bash == 2 :
        break


    if bash == 3:
        airmon = "apt install airmon-ng"
        mdk3 = "apt install mdk3"

        os.system(airmon)
        os.system(mdk3)

