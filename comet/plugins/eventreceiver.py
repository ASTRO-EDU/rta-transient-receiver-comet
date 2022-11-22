import voeventparse as vp
from comet.icomet import IHandler
from twisted.plugin import IPlugin
from zope.interface import implementer
from voeventhandler.voeventhandler import VoeventHandler
from voeventhandler.test.test_voevents import DUMMY_VOEVENT_GCN, DUMMY_VOEVENT_INTEGRAL, DUMMY_VOEVENT_CHIME, DUMMY_VOEVENT_LIGO, DUMMY_VOEVENT_LIGO_INITIAL, DUMMY_VOEVENT_LIGO_PRELIMINARY, DUMMY_VOEVENT_GCN_FERMI, DUMMY_VOEVENT_GCN_MAXI
from comet.utility.xml import xml_document
from pathlib import Path
import sys
#sys.path.append('rta-transient-receiver/voeventhandler')

# Event handlers must implement IPlugin and IHandler.
@implementer(IPlugin, IHandler)
class EventReceiver(object):
    
    name = "receive-event"
    print("receive event attivo")       

    # When the handler is called, it is passed an instance of
    # comet.utility.xml.xml_document.
    def __call__(self, event):
        
        #save a reference to the log file
        log_file = Path(__file__).parent / "log.txt"

        try:
            voevent_handler = VoeventHandler()
            voevent_handler.printVoevent(vp.loads(event.raw_bytes))
            voevent_handler.handleVoevent(vp.loads(event.raw_bytes))
            return True
        except Exception as e:
            error = 'Error: ' + str(e) + "\n"
            message = 'Message: ' + str(event.raw_bytes) + "\n"
            f = open(log_file, "a")
            f.write(error)
            f.write(message)
            f.write("----------------------- \n")
            f.close()
            print(message)
            print(error)
            return True

receive_event = EventReceiver()


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


if __name__ == "__main__":
    
    dummyevents = DummyEvent()

    voe_chime = dummyevents.chime
    voe_gcn = dummyevents.gcn
    voe_integral = dummyevents.integral
    voe_fermi = dummyevents.fermi
    voe_ligo = dummyevents.ligo
    voe_ligo_2 = dummyevents.ligo2
    voe_ligo_init = dummyevents.ligo_initial
    voe_maxi = dummyevents.maxi

    receive_event = EventReceiver()
    receive_event(voe_chime)
    receive_event(voe_gcn)
    receive_event(voe_integral)
    receive_event(voe_fermi)
    receive_event(voe_ligo)
    receive_event(voe_ligo_2)
    receive_event(voe_ligo_init)
    receive_event(voe_maxi)