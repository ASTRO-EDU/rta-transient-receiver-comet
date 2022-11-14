from gcn_kafka import Consumer

# Connect as a consumer.
# Warning: don't share the client secret with others.

config = {'group.id': '',
          'auto.offset.reset': 'earliest'}

"""
consumer = Consumer(config=config,
                    client_id='1bhh120087sgv8s9ctb5lvfpi8',
                    client_secret='d3m68h5mra18litkb1lkh6t93ic16ral36j7gr32kvna4hp5cqh',
                    domain='gcn.nasa.gov')
"""

consumer = Consumer(client_id='1bhh120087sgv8s9ctb5lvfpi8',
                    client_secret='d3m68h5mra18litkb1lkh6t93ic16ral36j7gr32kvna4hp5cqh')

agileset = ['gcn.classic.voevent.AGILE_MCAL_ALERT']
fermiset = ['gcn.classic.voevent.FERMI_GBM_FLT_POS',
            'gcn.classic.voevent.FERMI_LAT_MONITOR',
            'gcn.classic.voevent.FERMI_LAT_OFFLINE']
icecubeset =  ['gcn.classic.voevent.AMON_ICECUBE_EHE',
                'gcn.classic.voevent.AMON_ICECUBE_HESE',
                'gcn.classic.voevent.ICECUBE_ASTROTRACK_BRONZE',
                'gcn.classic.voevent.ICECUBE_ASTROTRACK_GOLD']
integralset = ['gcn.classic.voevent.INTEGRAL_OFFLINE',
                'gcn.classic.voevent.INTEGRAL_REFINED',
                'gcn.classic.voevent.INTEGRAL_WAKEUP']
lvcset = ['gcn.classic.voevent.LVC_EARLY_WARNING',
            'gcn.classic.voevent.LVC_INITIAL',
            'gcn.classic.voevent.LVC_PRELIMINARY',      
            'gcn.classic.voevent.LVC_UPDATE']
maxiset = ['gcn.classic.voevent.MAXI_KNOWN',
            'gcn.classic.voevent.MAXI_UNKNOWN']
swiftset = ['gcn.classic.voevent.SWIFT_BAT_QL_POS']
konusset = ['gcn.classic.voevent.KONUS_LC']

swiftsetcomplete = ['gcn.classic.voevent.SWIFT_ACTUAL_POINTDIR',
                    'gcn.classic.voevent.SWIFT_BAT_ALARM_LONG',
                    'gcn.classic.voevent.SWIFT_BAT_ALARM_SHORT',
                    'gcn.classic.voevent.SWIFT_BAT_GRB_ALERT',
                    'gcn.classic.voevent.SWIFT_BAT_GRB_LC',
                    'gcn.classic.voevent.SWIFT_BAT_GRB_LC_PROC',
                    'gcn.classic.voevent.SWIFT_BAT_GRB_POS_ACK',
                    'gcn.classic.voevent.SWIFT_BAT_GRB_POS_NACK',
                    'gcn.classic.voevent.SWIFT_BAT_GRB_POS_TEST',
                    'gcn.classic.voevent.SWIFT_BAT_KNOWN_SRC',
                    'gcn.classic.voevent.SWIFT_BAT_MONITOR',
                    'gcn.classic.voevent.SWIFT_BAT_QL_POS',
                    'gcn.classic.voevent.SWIFT_BAT_SCALEDMAP',
                    'gcn.classic.voevent.SWIFT_BAT_SLEW_POS',
                    'gcn.classic.voevent.SWIFT_BAT_SUB_THRESHOLD',
                    'gcn.classic.voevent.SWIFT_BAT_SUBSUB',
                    'gcn.classic.voevent.SWIFT_BAT_TRANS',
                    'gcn.classic.voevent.SWIFT_FOM_OBS',
                    'gcn.classic.voevent.SWIFT_FOM_PPT_ARG_ERR',
                    'gcn.classic.voevent.SWIFT_FOM_SAFE_POINT',
                    'gcn.classic.voevent.SWIFT_FOM_SLEW_ABORT',
                    'gcn.classic.voevent.SWIFT_POINTDIR',
                    'gcn.classic.voevent.SWIFT_SC_SLEW',
                    'gcn.classic.voevent.SWIFT_TOO_FOM',
                    'gcn.classic.voevent.SWIFT_TOO_SC_SLEW',
                    'gcn.classic.voevent.SWIFT_UVOT_DBURST',
                    'gcn.classic.voevent.SWIFT_UVOT_DBURST_PROC',
                    'gcn.classic.voevent.SWIFT_UVOT_EMERGENCY',
                    'gcn.classic.voevent.SWIFT_UVOT_FCHART',
                    'gcn.classic.voevent.SWIFT_UVOT_FCHART_PROC',
                    'gcn.classic.voevent.SWIFT_UVOT_POS',
                    'gcn.classic.voevent.SWIFT_UVOT_POS_NACK',
                    'gcn.classic.voevent.SWIFT_XRT_CENTROID',
                    'gcn.classic.voevent.SWIFT_XRT_EMERGENCY',
                    'gcn.classic.voevent.SWIFT_XRT_IMAGE',
                    'gcn.classic.voevent.SWIFT_XRT_IMAGE_PROC',
                    'gcn.classic.voevent.SWIFT_XRT_LC',
                    'gcn.classic.voevent.SWIFT_XRT_POSITION',
                    'gcn.classic.voevent.SWIFT_XRT_SPECTRUM',
                    'gcn.classic.voevent.SWIFT_XRT_SPECTRUM_PROC',
                    'gcn.classic.voevent.SWIFT_XRT_SPER',
                    'gcn.classic.voevent.SWIFT_XRT_SPER_PROC',
                    'gcn.classic.voevent.SWIFT_XRT_THRESHPIX',
                    'gcn.classic.voevent.SWIFT_XRT_THRESHPIX_PROC']


subscribeSet = ['gcn.classic.voevent.AGILE_MCAL_ALERT',
                    'gcn.classic.voevent.AMON_ICECUBE_EHE',
                    'gcn.classic.voevent.AMON_ICECUBE_HESE',
                    'gcn.classic.voevent.FERMI_GBM_FLT_POS',
                    'gcn.classic.voevent.FERMI_LAT_MONITOR',
                    'gcn.classic.voevent.FERMI_LAT_OFFLINE',
                    'gcn.classic.voevent.ICECUBE_ASTROTRACK_BRONZE',
                    'gcn.classic.voevent.ICECUBE_ASTROTRACK_GOLD',
                    'gcn.classic.voevent.INTEGRAL_OFFLINE',
                    'gcn.classic.voevent.INTEGRAL_REFINED',
                    'gcn.classic.voevent.INTEGRAL_WAKEUP',
                    'gcn.classic.voevent.LVC_EARLY_WARNING',
                    'gcn.classic.voevent.LVC_INITIAL',
                    'gcn.classic.voevent.LVC_PRELIMINARY',
                    'gcn.classic.voevent.LVC_UPDATE',
                    'gcn.classic.voevent.MAXI_KNOWN',
                    'gcn.classic.voevent.MAXI_UNKNOWN',
                    'gcn.classic.voevent.SWIFT_BAT_QL_POS',
                    'gcn.classic.voevent.KONUS_LC']

#not okey
#agile no
#fermi no
#'gcn.classic.voevent.ICECUBE_ASTROTRACK_BRONZE',
#'gcn.classic.voevent.ICECUBE_ASTROTRACK_GOLD'

#okey
#gcn.classic.voevent.AMON_ICECUBE_EHE
#gcn.classic.voevent.AMON_ICECUBE_HESE:

workingset = ['gcn.classic.voevent.AMON_ICECUBE_EHE',
                'gcn.classic.voevent.AMON_ICECUBE_HESE',
                'gcn.classic.voevent.LVC_EARLY_WARNING',
                'gcn.classic.voevent.LVC_UPDATE']


consumer.subscribe(swiftset)

# Subscribe to topics and receive alerts
#consumer.subscribe(['gcn.classic.voevent.AGILE_MCAL_ALERT'])
while True:
    for message in consumer.consume():
        value = message.value()
        print(value)
