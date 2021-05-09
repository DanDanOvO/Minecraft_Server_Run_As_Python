sudo apt update
sudo apt install -y openjdk-11 git htop screen
sudo apt install -y wget software-properties-common build-essential libnss3-dev zlib1g-dev libgdbm-dev libncurses5-dev   libssl-dev libffi-dev libreadline-dev libsqlite3-dev libbz2-dev
tar xvf Python-3.9.2.tgz
cd Python-3.9.2/
./configure --enable-optimizations
sudo make altinstall
pip3.9 install requests
pip3.9 install subprocess.run




