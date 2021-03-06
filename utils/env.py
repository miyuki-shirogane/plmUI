import configparser
import os

root_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
configPath = os.path.join(root_path, "utils/env.ini")
cf = configparser.ConfigParser()
cf.read(configPath, encoding='UTF-8')

pick = cf.get("pick", "env")
environment = cf.get(pick, "env")
tenantCode = cf.get(pick, "tenantCode")
account = cf.get(pick, "account")
password = cf.get(pick, "password")

class Environment:
    def url(self, module: str):
        return "https://" + environment + ".teletraan.io/subapp/plm/base/" + module

    def adress(self, path="login"):
        return "https://" + environment + ".teletraan.io/" + path

    def tenant_code(self):
        return tenantCode

    def account(self):
        return account

    def password(self):
        return password


if __name__ == "__main__":
    env = Environment()
    print(env.url(module="flow"))
    print(account, password)
