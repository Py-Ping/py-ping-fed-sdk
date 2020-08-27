import os
import tarfile
import docker
from time import sleep
from helpers import get_auth_session, retry_with_backoff
from docker_generate import Container

from pingfedsdk.models.LicenseAgreementInfo import LicenseAgreementInfo
from pingfedsdk.models.AdministrativeAccount import AdministrativeAccount
from pingfedsdk.models.IdpConnection import IdpConnection
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.apis.idp_adapters import idp_adapters
from pingfedsdk.apis.idp_defaultUrls import idp_defaultUrls
from pingfedsdk.apis.version import version
from pingfedsdk.apis.license import license
from pingfedsdk.apis.administrativeAccounts import administrativeAccounts
from pingfedsdk.apis.sp_idpConnections import sp_idpConnections
from pingfedsdk.apis.sp_adapters import sp_adapters
from pingfedsdk.apis.sp_targetUrlMappings import sp_targetUrlMappings
from pingfedsdk.apis.sp_defaultUrls import sp_defaultUrls
from pingfedsdk.apis.idp_spConnections import idp_spConnections
from pingfedsdk.apis.idp_connectors import idp_connectors
from pingfedsdk.apis.idpToSpAdapterMapping import idpToSpAdapterMapping
from pingfedsdk.apis.authenticationApi import authenticationApi


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
	kit_path = f"/opt/{demo_package}/sample"
	exec(container, f"unzip /opt/{demo_package}.zip")
	sleep(20)
	exec(container, f"mv {kit_path}/data.zip {pf_path}/data/drop-in-deployer/")
	exec(container, f"mv {kit_path}/IdpSample.war {pf_path}/deploy/")
	exec(container, f"mv {kit_path}/SpSample.war {pf_path}/deploy/")

	container.stop()
	container.wait()
	container.start()

	sleep(45)
	response = version(endpoint, session).getVersion()
	print(response.version)
	license_obj = license(endpoint, session)
	agreement = LicenseAgreementInfo(
		**{
			"accepted": True,
			"licenseAgreementUrl": "https://localhost:9999/pf-admin-api/license-agreement"
		}
	)
	print(license_obj.updateLicenseAgreement(agreement))

	adp = idp_adapters(endpoint, session).getIdpAdapters(1, 1, filter="OTIdPJava")
	from pprint import pprint
	pprint(adp.to_dict())

	try:
		pprint(idp_adapters(endpoint, session).deleteIdpAdapter(id='OTIdPJava'))
	except ValidationError as ex:
		print(ex)

	pprint(idp_defaultUrls(endpoint, session).getDefaultUrl().to_dict())
	idp_sp_conn = idp_spConnections(endpoint, session).getConnections(entityId='OTIdPJava', page=1, numberPerPage=1, filter='').to_dict()
	pprint(idp_connectors(endpoint, session).getIdpConnectorDescriptors().to_dict())

	sp_id_connections = sp_idpConnections(endpoint, session)
	response = sp_id_connections.getConnections(entityId='OTSPJava', page=1, numberPerPage=1, filter='OTSPJava')
	conn = response.items[0]
	pprint(conn)
	pprint(sp_id_connections.deleteConnection(response.items[0]["id"]))

	pprint(IdpConnection.from_dict(conn))
	pprint(sp_id_connections.createConnection(body=IdpConnection(**conn), XBypassExternalValidation=True).to_dict())

	pprint(sp_adapters(endpoint, session).getSpAdapterDescriptors().to_dict())
	pprint(sp_adapters(endpoint, session).getSpAdapters(page=1, numberPerPage=1, filter='').to_dict())

	try:
		sp_adapters(endpoint, session).deleteSpAdapter(id='OTSPJava')
	except ValidationError as ex:
		print(ex)

	pprint(idpToSpAdapterMapping(endpoint, session).getIdpToSpAdapterMappings().to_dict())
	pprint(authenticationApi(endpoint, session).getAuthenticationApiSettings().to_dict())


	pprint(sp_targetUrlMappings(endpoint, session).getUrlMappings().to_dict())
	pprint(sp_defaultUrls(endpoint, session).getDefaultUrls().to_dict())

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

	pprint(admin_accounts.getAccounts().to_dict())
