cd /sys/bus/pci/drivers/ehci-pci/
sudo sh -c 'echo -n "0000:00:1a.7">unbind'
sudo sh -c 'echo -n "0000:00:1d.7">unbind'
