import pypot.dynamixel
import pypot.robot

#print(pypot.dynamixel.get_available_ports())
#dxl_io = pypot.dynamixel.DxlIO('/dev/ttyUSB0')
#print(dxl_io.scan())

mot = ['m0', 'm1', 'm2', 'm3', 'm4', 'm5']
mot_i = {'m0':0, 'm1':1, 'm2':2, 'm3':3, 'm4':4, 'm5':5}


bras_config = {
    'controllers': {
        'my_dxl_controller': {
            'sync_read': False,
            'attached_motors': ['arm'],
            'port': '/dev/ttyUSB0' # 'auto'
        }
    },
    'motorgroups': {
        'arm': mot,
    },
    'motors': {
        'm0': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 22,
            'angle_limit': [-120.0, 120.0],
            'offset': 0.0
        },
        'm1': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 21,
            'angle_limit': [-120.0, 120.0],
            'offset': 0.0
        },
        'm2': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 23,
            'angle_limit': [-120.0, 120.0],
            'offset': 0.0
        },
        'm3': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 12,
            'angle_limit': [-120.0, 120.0],
            'offset': 0.0
        },
        'm4': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 11,
            'angle_limit': [-120.0, 120.0],
            'offset': 0.0
        },
        'm5': {
            'orientation': 'direct',
            'type': 'AX-12',
            'id': 13,
            'angle_limit': [-120.0, 120.0],
            'offset': 0.0
        },
    },
}

bras = pypot.robot.from_config(bras_config)

#for m in bras.motors:
#    m.compliant = False
#    m.goto_position(0, 2)

