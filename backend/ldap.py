from ldap3 import Server, Connection, ALL, SUBTREE
from ldap3.core.exceptions import LDAPException, LDAPBindError


class LDAP:
    def __init__(self, server_addr, root_dn, test_user="admin", pw="admin"):
        self.root_dn = root_dn
        self.test_user = test_user
        self.test_user_pw = pw
        self.server = Server(server_addr, get_info=ALL)

    def health(self):
        return self.authenticate(f"cn={self.test_user}", self.test_user_pw)

    def authenticate(self, object, password):
        try:
            return True, Connection(
                self.server,
                user=f"{object},{self.root_dn}",
                password=password,
                auto_bind=True,
            )
        except (LDAPBindError) as e:
            return False, e

    def authenticate_user(self, user, password):
        ldap_object = f"cn={user},ou=users"
        return self.authenticate(ldap_object, password)
