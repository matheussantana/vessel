import boto3
import pprint as pp




def getInstanceList():
    inst_list = []
    for r in res:
        inst = r.get('Instances')
        inst_id = inst[0].get('InstanceId')
        tags = inst[0].get('Tags')
        state = inst[0].get('State')

        #print(r)
        if state.get('Code') == 16 or state.get('Code') == 80:
            #print(inst_id)
            #print(tags)
            serial=""
            namespace=""
            for t in tags:
            #    if t['Key'] == 'id':
            #        print t
            # print(state)**/
                if t['Key'] == 'serial':
                    serial = t['Value']

                if t['Key'] == "id":
                    uuid = t['Value']


            inst_list.append([inst_id, serial, uuid])


    return inst_list

def getImageID(name):
    vm_images_res = client.describe_images(
        Filters=[
            {
                'Name': 'name',
                'Values': [
                    name,
                ]
            },
        ]
    )
    # Sort on Creation date Desc
    #image_details = sorted(response['Images'], key=itemgetter('CreationDate'), reverse=True)
    #pp.pprint(vm_images['Images'][0]['ImageId'])
    pp.pprint(vm_images_res)
    vm_images = vm_images_res['Images']

    #print(vm_images)
    #exit(0)

    if len(vm_images) == 0:
        return False
    else:
        vm_image_name = vm_images[0]['Name']
        vm_image_state = vm_images[0]['State']

        print(vm_image_state)
        #input()
        if vm_image_state == "available":
            vm_image_id = vm_images[0]['ImageId']
            vm_image_snapshot = vm_images[0]['BlockDeviceMappings']
            snapshot_id_list = []
            for snap_list in vm_image_snapshot:
                snapshot_id_list.append(snap_list['Ebs']['SnapshotId'])

                #for snap in snap_list['Ebs']:

                    #snapshot_id_list.append(snap['SnapshotId'])

            #print snapshot_id_list
            #for
            #exit(0)

            return [vm_image_id, vm_image_state, snapshot_id_list, vm_image_name]
        elif vm_image_state == "pending":
            return vm_image_state

    #ami_id = image_details[0]['ImageId']



def copy_snapshot(vm_image_id, vm_image_name):
    import time
    ts = str(int(time.time()))
    copy_name = "cp_"+vm_image_name+"."+ts
    print("Copying snapshot %s %s: %s" % (copy_name, vm_image_id, vm_image_name))
    copy_image = client.copy_image(ClientToken=copy_name, Description="Copy from "+vm_image_id, Name=copy_name, SourceImageId=vm_image_id, SourceRegion=region)

    time.sleep(5)

    copy_vm_image = getImageID(copy_name)

    #print(copy_vm_image)
    #input()
    while copy_vm_image == "pending" or copy_vm_image == False:
        copy_vm_image = getImageID(copy_name)


    return copy_vm_image


def create_snapshot(inst_id, uuid):
    print("Creating Snapshot for %s with name %s" % (inst_id, uuid))
    vm_image = client.create_image(Description="VM_Image", DryRun=False, InstanceId=inst_id, Name=uuid, NoReboot=True)

def remove_snapshot(vm_image_id, vm_image_state, vm_snapshot_list):
    print("Removing VM Image and Snapshots with id %s" % vm_image_id)
    image = list(ec2.images.filter(ImageIds=[vm_image_id]).all())[0]
    image.deregister(DryRun=False)

    for snap in vm_snapshot_list:
        client.delete_snapshot(SnapshotId=snap)
        print("Deleting snapshot " + snap)


#region = "us-east-1"
region = "sa-east-1"

client = boto3.client('ec2', region_name=region)
ec2 = boto3.resource('ec2', region_name=region)



#_op="create"
#_op="delete"
import sys
if len(sys.argv) == 2:
    _op = sys.argv[1]

else:
    print "create | delete | reset"
    exit(0)


if _op == "create":

    custom_filter = [{
        'Name':'tag:Class',
        'Values': ['VM']}]

    response = client.describe_instances(Filters=custom_filter)
    res = response.get('Reservations')


    inst_list = getInstanceList()
    #print(inst_list)
    table_vm = {}

    for inst in inst_list:
        #table_vm
        #print(vm_image)
        #print(inst)
        inst_id = inst[0]

        serial = str(int(inst[1])+1)
        uuid = inst[2]+"-"+serial
        #if serial == "0":
            #print(inst[0])


        vm_image = getImageID(uuid)
            #print(vm_image)
            #exit(0)


        if vm_image == False:
            #getImageID("1")
            create_snapshot(inst_id, uuid)

        else:
            vm_image_id = vm_image[0]
            vm_image_name = vm_image[3]
            vm_image_state = vm_image[1]
            vm_snapshot_list = vm_image[2]

            copy_snapshot(vm_image_id, vm_image_name)
            remove_snapshot(vm_image_id, vm_image_state, vm_snapshot_list)
            create_snapshot(inst_id, uuid)


elif _op == "delete":


    vm_images_res = client.describe_images(
        Filters=[
            {
                'Name': 'name',
                'Values': [
                    "cp_*",
                ]
            },
        ]
    )
    # Sort on Creation date Desc
    #image_details = sorted(response['Images'], key=itemgetter('CreationDate'), reverse=True)
    #pp.pprint(vm_images['Images'][0]['ImageId'])
    #pp.pprint(vm_images_res)
    vm_images = vm_images_res['Images']
    #pp.pprint(vm_images)
    snap_id_lst = []
    for snap in vm_images:
        snap_id_lst.append(snap['Name'])

    print(snap_id_lst)
    for snap_id in snap_id_lst:
        vm_image = getImageID(snap_id)
        vm_image_id = vm_image[0]
        vm_image_name = vm_image[3]
        vm_image_state = vm_image[1]
        vm_snapshot_list = vm_image[2]
        remove_snapshot(vm_image_id, vm_image_state, vm_snapshot_list)

elif _op == "reset":


    custom_filter = [{
        'Name':'tag:Class',
        'Values': ['VM']}]

    response = client.describe_instances(Filters=custom_filter)
    res = response.get('Reservations')


    inst_list = getInstanceList()
    #print(inst_list)
    table_vm = {}

    for inst in inst_list:

        inst_id = inst[0]
        print(inst[1])
        exit
        serial = str(int(inst[1])+1)
        uuid = inst[2]+"-"+serial
        #if serial == "0":
            #print(inst[0])

        vm_image = getImageID(uuid)
            #print(vm_image)
            #exit(0)


        if vm_image == False:
            #getImageID("1")
           ##create_snapshot(inst_id, uuid)
            pass
        else:
            vm_image_id = vm_image[0]
            vm_image_name = vm_image[3]
            vm_image_state = vm_image[1]
            vm_snapshot_list = vm_image[2]

                #copy_snapshot(vm_image_id, vm_image_name)
            remove_snapshot(vm_image_id, vm_image_state, vm_snapshot_list)
                #create_snapshot(inst_id, uuid)

#inst = res.get('Instances')
#pp.pprint(response.keys)
#pp.pprint(res)

#state = response.get('')

#pp.pprint(response)

