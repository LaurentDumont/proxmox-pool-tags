from proxmoxer import ProxmoxAPI

PROXMOX_HOST = ''
PROXMOX_USER = ''
USER_PASSWORD = ''
VERIFY_SSL = False

PROXMOX_POOLS = {
'DH Lab Pool-1' : 'DH-LAB-1',
'DH Lab Pool-2' : 'DH-LAB-2',
'DH Lab Pool-3' : 'DH-LAB-3',
}

proxmox_api_session = ProxmoxAPI(PROXMOX_HOST, user=PROXMOX_USER, password=USER_PASSWORD, verify_ssl=VERIFY_SSL)
existing_pools = proxmox_api_session.pools.get()

for poolid in PROXMOX_POOLS.items():
    if len(existing_pools) == 0:
        print('creating the pools since the are none on the server')
        proxmox_api_session.pools.create(poolid=poolid[1], comment=poolid[0])
    else:
        
        poolid_existing_pools = []

        #Create a list of all the currents tags.
        for pool in existing_pools:
            poolid_existing_pools.append(pool['poolid'])
        
        #Check if tag is already present in the existing Proxmox pool tags.
        if poolid[1] in poolid_existing_pools:
            print('Pool ' + poolid[1] + 'already exists.')
        else:
            proxmox_api_session.pools.create(poolid=poolid[1], comment=poolid[0])
