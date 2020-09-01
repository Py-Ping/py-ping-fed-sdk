import os
import tarfile
import docker
from time import sleep
from helpers import get_auth_session
from docker_generate import Container

from pingfedsdk.models.license_agreement_info import LicenseAgreementInfo
from pingfedsdk.models.administrative_account import AdministrativeAccount
from pingfedsdk.models.idp_connection import IdpConnection
from pingfedsdk.exceptions import ValidationError
from pingfedsdk.apis.idp_adapters import IdpAdapters
from pingfedsdk.apis.idp_default_urls import IdpDefaultUrls
from pingfedsdk.apis.version import Version
from pingfedsdk.apis.license import License
from pingfedsdk.apis.administrative_accounts import AdministrativeAccounts
from pingfedsdk.apis.sp_idp_connections import SpIdpConnections
from pingfedsdk.apis.sp_adapters import SpAdapters
from pingfedsdk.apis.sp_target_url_mappings import SpTargetUrlMappings
from pingfedsdk.apis.sp_default_urls import SpDefaultUrls
from pingfedsdk.apis.idp_sp_connections import IdpSpConnections
from pingfedsdk.apis.idp_connectors import IdpConnectors
from pingfedsdk.apis.idp_to_sp_adapter_mapping import IdpToSpAdapterMapping
from pingfedsdk.apis.authentication_api import AuthenticationApi


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

    response = Version(endpoint, session).getVersion()
    print(response.version)
    license_obj = License(endpoint, session)
    agreement = LicenseAgreementInfo(
        **{
            "accepted": True,
            "licenseAgreementUrl": "https://localhost:9999/pf-admin-api/license-agreement"
        }
    )
    print(license_obj.updateLicenseAgreement(agreement))

    adp = IdpAdapters(endpoint, session).getIdpAdapters(1, 1, filter="OTIdPJava")
    from pprint import pprint
    pprint(adp.to_dict())

    try:
        pprint(IdpAdapters(endpoint, session).deleteIdpAdapter(id='OTIdPJava'))
    except ValidationError as ex:
        print(ex)

    pprint(IdpDefaultUrls(endpoint, session).getDefaultUrl().to_dict())
    idp_sp_conn = IdpSpConnections(endpoint, session).getConnections(entityId='OTIdPJava', page=1, numberPerPage=1, filter='').to_dict()
    pprint(IdpConnectors(endpoint, session).getIdpConnectorDescriptors().to_dict())

    sp_id_connections = SpIdpConnections(endpoint, session)
    response = sp_id_connections.getConnections(entityId='OTSPJava', page=1, numberPerPage=1, filter='OTSPJava')
    conn = response.items[0]
    pprint(conn)
    pprint(sp_id_connections.deleteConnection(conn.id))

    sleep(5)
    pprint(IdpConnection.from_dict(conn.to_dict()))
    idp_conn = sp_id_connections.createConnection(body=conn, XBypassExternalValidation=True)
    pprint(idp_conn.credentials.certs)

    pprint(SpAdapters(endpoint, session).getSpAdapterDescriptors().to_dict())
    pprint(SpAdapters(endpoint, session).getSpAdapters(page=1, numberPerPage=1, filter='').to_dict())

    try:
        SpAdapters(endpoint, session).deleteSpAdapter(id='OTSPJava')
    except ValidationError as ex:
        print(ex)

    pprint(IdpToSpAdapterMapping(endpoint, session).getIdpToSpAdapterMappings().to_dict())
    pprint(AuthenticationApi(endpoint, session).getAuthenticationApiSettings().to_dict())

    pprint(SpTargetUrlMappings(endpoint, session).getUrlMappings().to_dict())
    pprint(SpDefaultUrls(endpoint, session).getDefaultUrls().to_dict())

    admin_accounts = AdministrativeAccounts(endpoint, session)
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
