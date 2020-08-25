import os
import tarfile
import docker
from time import sleep
from helpers import get_auth_session, retry_with_backoff
from docker_generate import Container


from pingfedsdk.models.LicenseAgreementInfo import LicenseAgreementInfo
from pingfedsdk.models.AdministrativeAccount import AdministrativeAccount
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.apis.idp_adapters import idp_adapters
from pingfedsdk.apis.idp_defaultUrls import idp_defaultUrls
from pingfedsdk.apis.version import version
from pingfedsdk.apis.license import license
from pingfedsdk.apis.administrativeAccounts import administrativeAccounts


home = os.environ["HOME"]
ping_user = os.environ["PING_IDENTITY_DEVOPS_USER"]
ping_key = os.environ["PING_IDENTITY_DEVOPS_KEY"]
endpoint = "https://localhost:9999/pf-admin-api/v1"
swagger_url = f"{endpoint}/api-docs"
session = get_auth_session()
session.verify = False


client = docker.from_env()


def copy_to(src, dst):
    name, dst = dst.split(':')
    container = client.containers.get(name)

    os.chdir(os.path.dirname(src))
    srcname = os.path.basename(src)
    tar = tarfile.open(src + '.tar', mode='w')
    try:
        tar.add(srcname)
    finally:
        tar.close()

    data = open(src + '.tar', 'rb').read()
    container.put_archive(os.path.dirname(dst), data)


def exec(container, cmd):
	return container.exec_run(f'/bin/sh -c "{cmd}"', stream=False, demux=False)


endpoint = "https://localhost:9999/pf-admin-api/v1"
session = get_auth_session()
session.verify = False

with Container(home, ping_user, ping_key) as container:
	demo_package = "pf-Java-integration-kit"
	print(f"Running container {container.id}")
	copy_to(f'./{demo_package}.zip', f'{container.id}:/opt/{demo_package}.zip')

	pf_path = "/opt/out/instance/server/default"

	exec(container, f"unzip /opt/{demo_package}.zip")
	sleep(20)
	exec(container, f"mv /opt/{demo_package}/sample/data.zip {pf_path}/data/drop-in-deployer/")
	exec(container, f"mv /opt/{demo_package}/sample/IdpSample.war {pf_path}/deploy/")
	exec(container, f"mv /opt/{demo_package}/sample/SpSample.war {pf_path}/deploy/")

	container.stop()
	container.wait()
	container.start()

	sleep(45)
	response = version(endpoint, session).getVersion()
	print(response.version)
	license_obj = license(endpoint, session)
	agreement = LicenseAgreementInfo(**{'accepted': True, 'licenseAgreementUrl': 'https://localhost:9999/pf-admin-api/license-agreement'})
	print(license_obj.updateLicenseAgreement(agreement))

	idp_adapters = idp_adapters(endpoint, session).getIdpAdapters(1, 1, filter="OTIdPJava")
	from pprint import pprint

	pprint(idp_adapters.to_dict())

	pprint(idp_defaultUrls(endpoint, session).getDefaultUrl().to_dict())
	
	admin_accounts = administrativeAccounts(endpoint, session)
	admin_account = AdministrativeAccount(
		username='penguin',
		password='2FederateM0re',
		active=True,
		description='Test account for a penguin.',
		auditor=False,
		phoneNumber='+61403111111',
		emailAddress='penguin@versent.com.au',
		department='Fish',
		roles={'ADMINISTRATOR', 'USER_ADMINISTRATOR'}
	)

	try:
		admin_accounts.addAccount(admin_account)
	except ValidationError:
		print("User already exists, skipping...")

	print(admin_accounts.getAccounts())

	input('wait...')
