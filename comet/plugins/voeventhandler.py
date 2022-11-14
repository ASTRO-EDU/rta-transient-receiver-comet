import voeventparse as vp
from comet.plugins.voeventsorting import VoeventSorting
from comet.plugins.databaseinterface import DatabaseInterface
from comet.utility.xml import xml_document
from comet.plugins.test.test_voevents import DUMMY_VOEVENT_GCN, DUMMY_VOEVENT_INTEGRAL, DUMMY_VOEVENT_CHIME, DUMMY_VOEVENT_LIGO, DUMMY_VOEVENT_LIGO_INITIAL, DUMMY_VOEVENT_LIGO_PRELIMINARY, DUMMY_VOEVENT_GCN_FERMI, DUMMY_VOEVENT_GCN_MAXI, DUMMY_VOEVENT_AGILE
from comet.plugins.emailnotifier import EmailNotifier

class VoeventHandler(object):
    
    def __init__(self):
        self.db = DatabaseInterface()
        self.voevent_sorter = VoeventSorting()
        self.email_notifier = EmailNotifier()

    def handleVoevent(self, voevent):
        voeventdata = self.voevent_sorter.sort(voevent)
        self.db.insert_voevent(voeventdata)
        result_row = self.db.meange_correlated_instruments(voeventdata)
        self.email_notifier.sendEmails(voeventdata, result_row)
    
    def printVoevent(self, voevent):
        voeventdata = self.voevent_sorter.sort(voevent)
        print(voeventdata)


class DummyEvent(object):
    """
    Class containing standard voevent from different networks
    """
    gcn = xml_document(DUMMY_VOEVENT_GCN)
    chime = xml_document(DUMMY_VOEVENT_CHIME)
    integral = xml_document(DUMMY_VOEVENT_INTEGRAL)
    fermi = xml_document(DUMMY_VOEVENT_GCN_FERMI) 
    ligo = xml_document(DUMMY_VOEVENT_LIGO)
    ligo2 = xml_document(DUMMY_VOEVENT_LIGO_PRELIMINARY)
    ligo_initial = xml_document(DUMMY_VOEVENT_LIGO_INITIAL)
    maxi = xml_document(DUMMY_VOEVENT_GCN_MAXI)
    agile = xml_document(DUMMY_VOEVENT_AGILE)

if __name__ == "__main__":
    dummyevents = DummyEvent()
    voe_chime = vp.loads(dummyevents.chime.raw_bytes) #tested
    voe_gcn = vp.loads(dummyevents.gcn.raw_bytes) #tested
    voe_integral = vp.loads(dummyevents.integral.raw_bytes) #tested
    voe_fermi = vp.loads(dummyevents.fermi.raw_bytes) #tested
    voe_ligo = vp.loads(dummyevents.ligo.raw_bytes) #tested
    voe_ligo_2 = vp.loads(dummyevents.ligo2.raw_bytes) #tested
    voe_ligo_init = vp.loads(dummyevents.ligo_initial.raw_bytes) #tested
    voe_maxi = vp.loads(dummyevents.maxi.raw_bytes) #tested
    voe_agile = vp.loads(dummyevents.agile.raw_bytes)  #tested

    voevent_handler = VoeventHandler()
    voevent_handler.handleVoevent(voe_chime)
    voevent_handler.handleVoevent(voe_gcn)
    voevent_handler.handleVoevent(voe_integral)
    voevent_handler.handleVoevent(voe_fermi)
    voevent_handler.handleVoevent(voe_ligo)
    voevent_handler.handleVoevent(voe_ligo_2)
    voevent_handler.handleVoevent(voe_ligo_init)
    voevent_handler.handleVoevent(voe_maxi)
    voevent_handler.handleVoevent(voe_agile)