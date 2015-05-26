# keystone-dropbearauth-backend
Backend for keystone to verify passwords with dropbear ssh connection.  

# Dependencies

dropbear:

sudo yum install dropbear

or

sudo apt-get install dropbear


# Installation instructions (approximate)

git clone https://github.com/UPPMAX/keystone-dropbearauth-backend.git
cd keystone-dropbearauth-backend
sudo cp dropbearauth.py /usr/lib/python2.7/site-packages/keystone/identity/backends/


