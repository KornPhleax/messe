from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError


class LDAP:

	def __init__(server_addr, root_dn, test_user=admin, pw=admin):
		self.ldap_server = server_addr
		self.root_dn = root_dn
		self.test_user = user
		self.test_user_pw = pw

	def 

ldap_server = f"ldap://127.0.0.1:389"
 
# dn
root_dn = "dc=ffh,dc=de"
 
# ldap user and password
ldap_user_name = 'admin'
ldap_password = 'admin'
 
# user
user = f'cn={ldap_user_name},ou=users,{root_dn}'

server = Server(ldap_server, get_info=ALL)

connection = Connection(server,
                        user=user,
                        password=ldap_password,
                        auto_bind=True)

print(f" *** Response from the ldap bind is \n{connection}" )
