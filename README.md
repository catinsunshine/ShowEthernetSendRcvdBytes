# ShowEthernetSendRcvdBytes

Store on Amazon EC2 covering:

    apt update/upgrade/autoremove

    show current Rcvd/Sent Bytes used till login


Files:

    update

    rt.py

    wl.txt (Generate & overide when login)



Setup & Usages:

    chmod u+x update (one-time setup)

    ./update

    Remarks for update:
        ifconfig wlp3s0 > wl.txt | python3 rt.py
        replace wlp3s0 with your own Enther card name. You can use ifconfig command to clarify it.
